from fastmcp import FastMCP

from database import DatabaseManger

db_manager = DatabaseManger("mcp-context-users", "users")
print("Connecting to the database...")
db_manager.connect()

mcp = FastMCP("mcp-context", stateless_http=True)


@mcp.tool()
def get_user_information(query:str):
    '''
    Retrieves a wide range of information about the current user from the database. 
    This tool should be used to answer any question that requires details about the user. 
    The query argument should be a direct, natural language question about the user.
    Args:
        query (str): Natural language query to get user information.
    Returns:
        str: Requested User information if available, otherwise an message indicating that the information is not available.
    '''

    print("Received query: ", query)

    # fetch user information from the database
    userInfo = db_manager.get_user_information("test_user_1")
    print("User information fetched: ", userInfo)
    if userInfo:
        return userInfo
    else:
        return "User information not found."

@mcp.tool()
def update_user_information(field:str, value:str):
    '''
    Updates a specific field in the user's information in the database. 
    This tool should be used to modify any user details.
    Args:
        field (str): The field to update (e.g., "name", "age", "email", "current_project").
        value (str): The new value for the specified field.
    Returns:
        str: Confirmation message indicating whether the update was successful or if the field does not exist.
    '''

    print(f"Updating field: {field} with value: {value}")

    if field in userTestInfo:
        userTestInfo[field] = value
        print(userTestInfo)
        return f"User information updated successfully: {field} is now {value}."
    else:
        return f"Field '{field}' does not exist in user information."

if __name__ == "__main__":
    mcp.run()
