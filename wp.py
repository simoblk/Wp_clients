import requests
from datetime import datetime

# Define your API key and Search Engine ID
API_KEY = "YOUR_API_KEY"  # Replace with your Google API key
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"  # Replace with your Search Engine ID

# Define the dorks
DORKS = [
    'inurl:/wp-admin/ intitle:"WordPress" intext:"Just another WordPress site"',
    'inurl:/wp-login.php intitle:"WordPress" intext:"Powered by WordPress"',
    'inurl:/wp-content/uploads/ intitle:"WordPress" intext:"Site is under construction"',
    'inurl:/wp-includes/ intitle:"WordPress" intext:"Proudly powered by WordPress"',
    'inurl:/wp-json/ intitle:"WordPress" intext:"Version 6.0"'
]

def display_dorks():
    """Display available dorks for selection."""
    print("Choose one of the following dorks:")
    for i, dork in enumerate(DORKS, start=1):
        print(f"{i}. {dork}")

def get_user_choice():
    """Get user's choice of dork."""
    while True:
        try:
            choice = int(input("Enter the number of the dork you want to use (1-5): "))
            if 1 <= choice <= 5:
                return DORKS[choice - 1]
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def perform_search(dork, num_results=10):
    """Perform a Google search using the selected dork."""
    try:
        print(f"Searching for new WordPress websites using dork: {dork}")
        
        # Google Custom Search API endpoint
        url = f"https://www.googleapis.com/customsearch/v1"
        
        # Parameters for the API request
        params = {
            "key": API_KEY,
            "cx": SEARCH_ENGINE_ID,
            "q": dork,
            "num": num_results  # Number of results to return
        }
        
        # Send a GET request to the API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the JSON response
        data = response.json()
        
        # Extract search results
        results = []
        if "items" in data:
            for item in data["items"]:
                results.append(item["link"])
        
        return results
    except Exception as e:
        print(f"An error occurred during the search: {e}")
        return []

def save_results(results, filename="wordpress_sites.txt"):
    """Save the search results to a text file."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a") as file:
            file.write(f"Search Results - {timestamp}\n")
            file.write("\n".join(results) + "\n\n")
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the results: {e}")

def main():
    """Main function to execute the script."""
    display_dorks()
    selected_dork = get_user_choice()
    search_results = perform_search(selected_dork)
    
    if search_results:
        save_results(search_results)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()