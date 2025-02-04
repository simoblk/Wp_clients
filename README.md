Wp-clients is a Python script designed to search for new WordPress websites using Google dorks for new release websites. 
It allows you to choose from a list of predefined dorks, performs a search using the Google Custom Search JSON API, and saves the results to a text file. 
The script is reliable, efficient, and avoids issues like Google blocking or HTML parsing errors by leveraging Google's official API.

Step 1: Set Up Google Custom Search API
Go to the Google Cloud Console.

Create a new project.

Enable the Custom Search API for your project.

Generate an API key.

Create a Custom Search Engine:

Go to the Custom Search Engine page.

Create a new search engine and configure it to search the entire web.

Note down the Search Engine ID.


Step 2: Install Required Libraries
Install the requests library:
pip install requests


How It Works:
The script uses the Google Custom Search API to perform the search.

It extracts the URLs of the search results from the JSON response.

The results are saved to a text file (wordpress_sites.txt).

API Quotas:

The Google Custom Search API has a free tier with a limited number of requests per day. If you exceed the quota, you’ll need to upgrade to a paid plan.

Search Engine Configuration:

Ensure your Custom Search Engine is configured to search the entire web.

Legal Compliance:

Using the Google Custom Search API complies with Google’s terms of service.
