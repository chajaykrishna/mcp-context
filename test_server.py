import json
import os
import tempfile
import shutil

def get_user_information_logic(query: str):
    """Extract the core logic from server.py for testing"""
    current_path = os.path.dirname(os.path.abspath(__file__))
    context_file_path = os.path.join(current_path, "context.json")
    
    print("Received query: ", query)
    
    try:
        with open(context_file_path, 'r') as f:
            userInfo = f.read()
    except FileNotFoundError:
        print("context.json file not found.")
        return "User information not found."
    except Exception as e:
        print("Error occurred while fetching user information: ", e)
        return f"User information not found, error: {e}"
    
    print("User information fetched: ", userInfo)
    if userInfo:
        return userInfo
    else:
        return "User information not found."

def update_user_information_logic(updates: dict):
    """Extract the core logic from server.py for testing"""
    current_path = os.path.dirname(os.path.abspath(__file__))
    context_file_path = os.path.join(current_path, "context.json")
    
    try:
        with open(context_file_path, 'r') as f:
            data = json.load(f)
        
        for field, value in updates.items():
            data[field] = value
        
        with open(context_file_path, 'w') as f:
            json.dump(data, f, indent=4)
        
        return "User information updated successfully."
    
    except FileNotFoundError:
        return "Error: context.json not found."
    except json.JSONDecodeError:
        return "Error: context.json is not a valid JSON file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def test_get_user_information():
    """Test the get_user_information function"""
    print("Testing get_user_information...")
    
    # Test with the actual context.json file
    result = get_user_information_logic("What is the user's name?")
    print("Result:", result)
    
    # Parse the JSON result to verify structure
    try:
        user_data = json.loads(result)
        if 'name' in user_data:
            print(f"✓ User found: name={user_data.get('name')}")
            print(f"✓ Current project: {user_data.get('current_project', 'Not specified')}")
        else:
            print("✗ Name field not found in user data")
    except json.JSONDecodeError:
        print("✗ Result is not valid JSON:", result)

def test_update_user_information():
    """Test the update_user_information function"""
    print("\nTesting update_user_information...")
    
    # Create a backup of the original context.json
    context_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "context.json")
    backup_file = context_file + ".backup"
    
    try:
        # Create backup
        shutil.copy2(context_file, backup_file)
        
        # Test update
        updates = {"test_field": "test_value", "last_test_run": "2024"}
        result = update_user_information_logic(updates)
        print("Update result:", result)
        
        # Verify the update worked
        verification_result = get_user_information_logic("What is the test_field value?")
        try:
            user_data = json.loads(verification_result)
            if user_data.get("test_field") == "test_value":
                print("✓ Update verification successful")
            else:
                print("✗ Update verification failed")
        except json.JSONDecodeError:
            print("✗ Verification failed - invalid JSON")
        
    finally:
        # Restore backup
        if os.path.exists(backup_file):
            shutil.move(backup_file, context_file)
            print("✓ Context file restored from backup")

def test_edge_cases():
    """Test edge cases and error handling"""
    print("\nTesting edge cases...")
    
    # Test with empty query
    result = get_user_information_logic("")
    print("Empty query result:", result)
    
    # Test with very specific query
    result = get_user_information_logic("What phone does the user have?")
    print("Phone query result:", result)

if __name__ == "__main__":
    test_get_user_information()
    test_update_user_information()
    test_edge_cases()
    print("\n✓ All tests completed!")
