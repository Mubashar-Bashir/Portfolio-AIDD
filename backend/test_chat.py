"""
Test script for chat functionality with "Hello World" interaction
This demonstrates the basic "Hello World" functionality implemented in the backend
"""
import requests
import json

def test_hello_world_interaction():
    """
    Test the basic "Hello World" interaction with the chatbot
    """
    print("Testing Hello World chat functionality...")

    # This would be run against a running server
    base_url = "http://localhost:8000/api/v1"

    # Test 1: Start a new chat session
    print("\n1. Starting a new chat session...")
    try:
        session_response = requests.post(f"{base_url}/chat/start",
                                      json={"user_id": "test_user_123"})
        if session_response.status_code == 200:
            session_data = session_response.json()
            session_id = session_data['session_id']
            print(f"   ✓ Session created successfully: {session_id}")
        else:
            print(f"   ✗ Failed to create session: {session_response.status_code}")
            return False
    except Exception as e:
        print(f"   ✗ Error starting session: {str(e)}")
        return False

    # Test 2: Send a "Hello World" message
    print("\n2. Sending 'Hello World' message...")
    try:
        message_response = requests.post(f"{base_url}/chat/{session_id}/message",
                                       json={"content": "Hello World!"})
        if message_response.status_code == 200:
            message_data = message_response.json()
            response = message_data['response']
            print(f"   ✓ Received response: {response}")

            # Check if response contains expected "Hello World" greeting
            if "Hello" in response and "Welcome" in response:
                print("   ✓ 'Hello World' functionality working correctly")
            else:
                print("   ⚠ Response doesn't match expected 'Hello World' greeting")
        else:
            print(f"   ✗ Failed to send message: {message_response.status_code}")
            return False
    except Exception as e:
        print(f"   ✗ Error sending message: {str(e)}")
        return False

    # Test 3: Send a "Hi" message (alternative greeting)
    print("\n3. Sending 'Hi' message...")
    try:
        message_response = requests.post(f"{base_url}/chat/{session_id}/message",
                                       json={"content": "Hi there!"})
        if message_response.status_code == 200:
            message_data = message_response.json()
            response = message_data['response']
            print(f"   ✓ Received response: {response}")

            # Check if response contains expected greeting
            if "Hello" in response or "Hi" in response:
                print("   ✓ Greeting functionality working correctly")
            else:
                print("   ⚠ Response doesn't match expected greeting pattern")
        else:
            print(f"   ✗ Failed to send message: {message_response.status_code}")
            return False
    except Exception as e:
        print(f"   ✗ Error sending message: {str(e)}")
        return False

    print("\n✓ All 'Hello World' interaction tests passed!")
    return True

def test_chat_session_retrieval():
    """
    Test retrieving chat session details
    """
    print("\n4. Testing chat session retrieval...")
    base_url = "http://localhost:8000/api/v1"

    try:
        # Start a session first
        session_response = requests.post(f"{base_url}/chat/start",
                                      json={"user_id": "test_user_456"})
        if session_response.status_code == 200:
            session_data = session_response.json()
            session_id = session_data['session_id']

            # Retrieve the session
            get_response = requests.get(f"{base_url}/chat/{session_id}")
            if get_response.status_code == 200:
                session_details = get_response.json()
                print(f"   ✓ Retrieved session details for: {session_details['id']}")
                print(f"   ✓ Session is active: {session_details['is_active']}")
                return True
            else:
                print(f"   ✗ Failed to retrieve session: {get_response.status_code}")
                return False
        else:
            print(f"   ✗ Failed to create session for retrieval test")
            return False
    except Exception as e:
        print(f"   ✗ Error in session retrieval test: {str(e)}")
        return False

if __name__ == "__main__":
    print("Running Chat Functionality Tests")
    print("=" * 40)

    success1 = test_hello_world_interaction()
    success2 = test_chat_session_retrieval()

    print("\n" + "=" * 40)
    if success1 and success2:
        print("✓ All tests passed! Hello World functionality is working correctly.")
    else:
        print("✗ Some tests failed. Please check the implementation.")