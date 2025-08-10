from fastmcp import FastMCP

mcp = FastMCP("mcp-context", stateless_http=True)
userTestInfo = {
        "name": "John Doe",
        "age": 20,
        "email": "john.doe@example.com", 
        "current_project": "AI powered productivity browser extension",
    }


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
    

    # just return the test information
    return f"Name: {userTestInfo['name']}, Age: {userTestInfo['age']}, Email: {userTestInfo['email']}, Current Project: {userTestInfo['current_project']}"

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