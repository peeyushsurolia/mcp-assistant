# AI Assistant with Calculator

This project implements an AI assistant with a calculator functionality using OpenAI's GPT model and a custom MCP (Message Control Protocol) client-server architecture.

## Features

- OpenAI-powered chatbot
- Calculator functionality (add, subtract, multiply, divide)
- Modern web-based UI
- MCP client-server architecture
- REST API endpoints

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the Application

1. Start the MCP Server:
   ```bash
   python server/mcp_server.py
   ```

2. Start the MCP Client:
   ```bash
   python client/mcp_client.py
   ```

3. Start the Main Application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5002`

## Usage

- The chatbot can handle both general conversations and calculations
- For calculations, use natural language like:
  - "add 5 and 3"
  - "multiply 4 by 2"
  - "subtract 10 from 15"
  - "divide 20 by 4"

## Architecture

- MCP Server (Port 5000): Handles calculator operations
- MCP Client (Port 5001): Acts as a service and handles REST calls
- Main Application (Port 5002): Integrates OpenAI and serves the web UI

## API Endpoints

- `POST /chat`: Send messages to the AI assistant
- `POST /calculate`: Perform calculations through the MCP client
- `POST /mcp`: Direct calculator operations on the MCP server 