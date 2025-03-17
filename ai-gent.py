import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import FunctionTool, ToolSet
from datetime import datetime
from dotenv import load_dotenv
from typing import Any, Callable, Set
from neon_api import NeonAPI
from neon_functions import (
    get_current_user,
    list_api_keys,
    create_api_key,
    delete_api_key,
    list_projects,
    get_project,
    create_project,
    update_project,
    delete_project,
    get_project_permissions,
    grant_project_permissions,
    revoke_project_permissions,
    get_connection_uri,
    list_branches,
    get_branch,
    create_branch,
    update_branch,
    delete_branch,
    set_primary_branch,
    list_databases,
    get_database,
    create_database,
    update_database,
    delete_database,
    list_endpoints,
    create_endpoint,
    update_endpoint,
    delete_endpoint,
    start_endpoint,
    suspend_endpoint,
    list_roles,
    get_role,
    create_role,
    delete_role,
    reveal_role_password,
    reset_role_password,
    list_operations,
    get_operation,
    get_consumption,
)


load_dotenv()

# Initialize Azure AI Client
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

user_functions: Set[Callable[..., Any]] = {
    # get_current_user,
    # list_api_keys,
    # create_api_key,
    # delete_api_key,
    # list_projects,
    # get_project,
    create_project,
    # update_project,
    # delete_project,
    # get_project_permissions,
    # grant_project_permissions,
    # revoke_project_permissions,
    # get_connection_uri,
    # list_branches,
    # get_branch,
    # create_branch,
    # update_branch,
    # delete_branch,
    # set_primary_branch,
    # list_databases,
    # get_database,
    # create_database,
    # update_database,
    # delete_database,
    # list_endpoints,
    # create_endpoint,
    # update_endpoint,
    # delete_endpoint,
    # start_endpoint,
    # suspend_endpoint,
    # list_roles,
    # get_role,
    # create_role,
    # delete_role,
    # reveal_role_password,
    # reset_role_password,
    # list_operations,
    # get_operation,
    # get_consumption,
}
functions = FunctionTool(user_functions)
toolset = ToolSet()
toolset.add(functions)

# Create AI Agent
agent = project_client.agents.create_agent(
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
    name=f"neon-db-agent-{datetime.now().strftime('%Y%m%d%H%M')}",
    description="AI Agent for managing Neon databases and running SQL queries.",
    instructions=f"""
    You are an AI assistant that helps users create and manage Neon projects, databases, 
    branches. Use the provided functions to perform actions.
    The current date is {datetime.now().strftime("%Y-%m-%d")}.
    """,
    toolset=toolset,
)
print(f"✅ Created agent, ID: {agent.id}")


# Create a thread for agent interactions
thread = project_client.agents.create_thread()
print(f"✅ Created thread, ID: {thread.id}")


def process_command(command: str):
    """Processes a user command and interacts with the AI agent."""
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content=command,
    )
    print(f"✅ Created message, ID: {message.id}")

    run = project_client.agents.create_and_process_run(
        thread_id=thread.id, agent_id=agent.id
    )
    print(f"✅ Run finished with status: {run.status}")

    if run.status == "failed":
        print(f"❌ Run failed: {run.last_error}")
    else:
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"📜 Messages: {messages['data'][0]['content'][0]['text']['value']}")


# Accept user commands from the console
def main():
    while True:
        command = input("Enter a command (or 'exit' to quit): ")
        if command.lower() == "exit":
            break
        try:
            process_command(command)
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
