"""
Example client for WordSalad API
Demonstrates how to interact with the API programmatically
"""

import requests
import json


class WordSaladClient:
    """Client for interacting with WordSalad API"""
    
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
    
    def health_check(self):
        """Check if the API is healthy"""
        try:
            response = requests.get(f"{self.base_url}/health")
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def get_api_info(self):
        """Get API information"""
        try:
            response = requests.get(f"{self.base_url}/")
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def generate_paragraph(self, input_str):
        """
        Generate a paragraph
        
        Args:
            input_str: Format "topic+wordcount" (e.g., "moon30")
        
        Returns:
            dict: API response with generated paragraph
        """
        try:
            response = requests.post(
                f"{self.base_url}/generate",
                json={"input": input_str},
                headers={"Content-Type": "application/json"}
            )
            return response.json(), response.status_code
        except Exception as e:
            return {"error": str(e)}, 500


def main():
    """Example usage of WordSalad client"""
    
    print("=" * 70)
    print("WordSalad API Client - Example Usage")
    print("=" * 70)
    print()
    
    # Initialize client
    client = WordSaladClient()
    
    # Health check
    print("1. Health Check:")
    health = client.health_check()
    print(f"   {json.dumps(health, indent=2)}")
    print()
    
    # Get API info
    print("2. API Information:")
    info = client.get_api_info()
    if 'error' not in info:
        print(f"   Service: {info.get('service')}")
        print(f"   Version: {info.get('version')}")
    else:
        print(f"   Error: {info.get('error')}")
    print()
    
    # Example paragraph generations
    print("3. Generate Paragraphs:")
    examples = [
        "moon30",
        "python50",
        "artificial intelligence100"
    ]
    
    for example in examples:
        print(f"\n   Input: '{example}'")
        result, status_code = client.generate_paragraph(example)
        
        if status_code == 200 and result.get('success'):
            print(f"   ✓ Generated {result.get('word_count')} words about {result.get('topic')}")
            print(f"   Wikipedia used: {result.get('used_wikipedia')}")
            print(f"   Paragraph: {result.get('paragraph')[:100]}...")
        else:
            print(f"   ✗ Error: {result.get('error', 'Unknown error')}")
    
    print()
    print("=" * 70)


if __name__ == "__main__":
    # Note: This requires the Flask app to be running
    # Run it with: python app.py
    # Then in another terminal: python example_client.py
    
    print("Note: Make sure the Flask API is running before using this client.")
    print("Run: python app.py")
    print()
    
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure the API is running at http://localhost:5000")
