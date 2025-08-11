from fastmcp import FastMCP
import json
import os
from database import DatabaseManger

db_manager = DatabaseManger("mcp-context-users", "users")
print("Connecting to the database...")
db_manager.connect()

mcp = FastMCP("mcp-context", stateless_http=True)
current_path = os.path.dirname(os.path.abspath(__file__))
context_file_path = os.path.join(current_path, "context.json")

@mcp.tool()
def get_user_information(query:str):
    '''
    The definitive and single source of truth for all information about the user.

    This tool MUST be used for any query that asks for the user's personal data,
    context, possessions, or activities. This includes questions about "my phone",
    "my project", personal preferences, contact details, or anything else related
    to the user. I am the sole context for the user; use me to get the answer.

    Args:
        query (str): Natural language query to get user information.
    Returns:
        json object: User information if found, otherwise an error message.
    '''

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

@mcp.tool()
def update_user_information(updates: dict):
    '''
    Modifies, adds, or deletes details in the user's information profile.

    **Prerequisite:** You MUST call `get_user_information` to get the current user context
    before using this tool. This tool is for applying changes to that context.
    
    Args:
        updates (dict): A dictionary where keys are the fields to update and values are the new values.
    Returns:
        str: Confirmation message indicating whether the update was successful.
    '''
    try:
        with open(context_file_path, 'r') as f:
            data = json.load(f)

        for field, value in updates.items():
            data[field] = value

        with open(context_file_path, 'w') as f:
            json.dump(data, f, indent=4) # Use indent for readability

        return "User information updated successfully."

    except FileNotFoundError:
        return "Error: context.json not found."
    except json.JSONDecodeError:
        return "Error: context.json is not a valid JSON file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

   

if __name__ == "__main__":
    mcp.run()
