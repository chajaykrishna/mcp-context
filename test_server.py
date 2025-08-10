from database import DatabaseManger

def test_get_user_information():
    db_manager = DatabaseManger("mcp-context-users", "users")
    db_manager.connect()
    print("Testing get_user_information for user_id 'test_user_1'")
    user_info = db_manager.get_user_information("test_user_1")
    print("Result from DB:", user_info)
    if user_info:
        print(f"User found: id={user_info.get('_id')}, name={user_info.get('name')}, age={user_info.get('Age')}")
    else:
        print("User information not found.")

if __name__ == "__main__":
    test_get_user_information()
