
import requests


class BitcoinPriceAgent:
    """
    An AI agent that autonomously fetches and displays Bitcoin price information.
    
    This agent demonstrates the fundamental components of an AI agent:
    - Abilities: API communication and data processing
    - Goals: Retrieve and display current Bitcoin price
    - Prior Knowledge: Understanding of API structure and data format
    """
    
    def __init__(self, api_url):
        """
        Initialize the Bitcoin price agent with the API endpoint.
        
        Args:
            api_url (str): URL of the CoinDesk API endpoint for Bitcoin price data
        """
        self.api_url = api_url

    def fetch_bitcoin_price(self):
        """
        Fetch the current Bitcoin price in USD from the CoinDesk API.
        
        This method demonstrates the core agent behavior:
        1. Perceives the environment by making an API request
        2. Processes the response to extract relevant information
        3. Acts by displaying the price to the user
        
        Handles various error conditions including network failures,
        API errors, and data parsing issues.
        """
        try:
            # Perceive: Make a GET request to the CoinDesk API
            response = requests.get(self.api_url)
            
            # Decide: Check if the API request was successful
            if response.status_code == 200:
                # Process the JSON response from the API
                data = response.json()
                
                # Extract the Bitcoin price in USD from the nested JSON structure
                bitcoin_price = data["bpi"]["USD"]["rate_float"]
                
                # Act: Display the current Bitcoin price to the user
                print(f"Current Bitcoin Price (USD): ${bitcoin_price}")
            else:
                # Handle API errors (e.g., rate limiting, server errors)
                print(f"API request failed with status code: {response.status_code}")
                print("Failed to fetch Bitcoin price. Please check the API.")
        except requests.exceptions.RequestException as e:
            # Handle network-related errors (connection, timeout, etc.)
            print(f"Network error occurred: {e}")
        except KeyError as e:
            # Handle data structure errors (missing expected fields)
            print(f"Data parsing error: Expected field not found - {e}")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")


def main():
    """
    Main execution function that creates and runs the Bitcoin price agent.
    
    This demonstrates the complete agent lifecycle from initialization
    to task execution.
    """
    # Define the API endpoint for the CoinDesk Bitcoin Price Index
    api_url = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"
    
    # Create an instance of the BitcoinPriceAgent
    agent = BitcoinPriceAgent(api_url)
    
    # Execute the agent's primary task
    agent.fetch_bitcoin_price()


if __name__ == "__main__":
    main()