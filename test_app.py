"""
Simple test script to verify Flask application functionality
"""
import requests
import time
import subprocess
import sys

def test_flask_app():
    """Test the Flask application endpoints"""
    try:
        # Wait a moment for the server to start
        time.sleep(2)
        
        # Test the home page
        response = requests.get('http://localhost:5000/')
        if response.status_code == 200:
            print("✅ Home page loads successfully")
        else:
            print(f"❌ Home page failed with status: {response.status_code}")
            
        # Test contact form submission
        contact_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message'
        }
        
        response = requests.post('http://localhost:5000/contact', data=contact_data)
        if response.status_code == 302:  # Redirect after form submission
            print("✅ Contact form submission works")
        else:
            print(f"❌ Contact form failed with status: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Flask server. Make sure it's running on localhost:5000")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")

if __name__ == "__main__":
    print("Testing Flask Portfolio Application...")
    test_flask_app()
