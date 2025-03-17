# Neon API & Azure AI Agent Integration

This project integrates the **[Neon Management API](https://api-docs.neon.tech/reference/getting-started-with-neon-api?refcode=44WD03UH)** in Python using [Neon SDK](https://pypi.org/project/neon-api/) with **[Azure AI Agent Service](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)** to create, manage, and interact with Neon projects, databases, branches, and more using AI-driven commands.

## Features
- Create and manage Neon projects, databases, branches, roles, and endpoints.
- Accept user commands from the console to trigger Neon API operations.

## Demo

![Neon API & Azure AI Agent Integration](/assets/Neon%20Azure%20AI%20Agent%20Demo.gif)

## Supported Tools
The following tools are supported through Neon API:
- **Project Management**
  - Create, update, list, delete projects

### Coming soon

- **Branch Management**
  - Create, update, delete branches
  - Set a branch as primary
- **Database Management**
  - Create, update, delete databases
  - Retrieve database details
- **Endpoint Management**
  - Create, update, delete endpoints
  - Start and suspend endpoints
- **Role Management**
  - Create, delete roles
  - Reveal and reset role passwords
- **SQL Execution**
  - Run queries on Neon databases
- **API Key Management**
  - Create, list, and delete API keys
- **Operations Monitoring**
  - List and track project operations
- **Consumption Metrics**
  - Retrieve usage and consumption data

## Prerequisites
Before running the project, ensure you have:
- Python 3.8+
- An **[Azure AI Agent](https://learn.microsoft.com/en-us/azure/ai-services/agents/quickstart?pivots=ai-foundry-portal)** setup
- A **[Neon API Key](https://neon.tech/docs/manage/api-keys#creating-api-keys?refcode=44WD03UH)**

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/neondatabase-labs/neon-azure-ai-agent-demo.git
   cd neon-azure-ai-agent-demo
   ```
2. Create a new virtual environment:
   ```bash
   python -m venv venv && source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables by creating a `.env` file:
   ```ini
   PROJECT_CONNECTION_STRING=your_azure_project_connection_string
   AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=your_deployment_name
   NEON_API_KEY=your_neon_api_key
   ```

## Usage
### Running the AI Agent
Start the AI agent and interact with Neon API:
```bash
python ai-gent.py
```

### Example Commands
After running the script, you can enter commands in the console:
- **Create a project**:
  ```text
  Create a project called My Neon Project
  ```
- **List Projects**:
  ```text
  List existing projects
  ```

## Project Structure
```
neon-azure-ai/
│── ai-agent.py           # Main AI Agent application entry point
│── neon_functions.py     # Neon API interaction functions
│── .env                  # Environment variables (not committed)
│── requirements.txt      # Required dependencies
│── README.md             # Project documentation
```

## Contributing
Contributions are welcome! Feel free to submit a pull request with improvements.