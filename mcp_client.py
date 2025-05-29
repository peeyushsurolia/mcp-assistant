from mcp import MCPClient, mcptool
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

class CalculatorClient(MCPClient):
    def __init__(self, server_url):
        super().__init__("calculator-client", server_url)
        self.register_tools()

    def register_tools(self):
        @mcptool("add")
        async def add(a: float, b: float) -> float:
            return await self.call_tool("add", {"a": a, "b": b})

        @mcptool("subtract")
        async def subtract(a: float, b: float) -> float:
            return await self.call_tool("subtract", {"a": a, "b": b})

        @mcptool("multiply")
        async def multiply(a: float, b: float) -> float:
            return await self.call_tool("multiply", {"a": a, "b": b})

        @mcptool("divide")
        async def divide(a: float, b: float) -> float:
            return await self.call_tool("divide", {"a": a, "b": b})

calculator_client = CalculatorClient("http://localhost:5000")

@app.route('/calculate', methods=['POST'])
async def calculate():
    try:
        data = request.json
        if not data or 'operation' not in data or 'a' not in data or 'b' not in data:
            return jsonify({'error': 'Invalid request format'}), 400

        operation = data['operation']
        a = float(data['a'])
        b = float(data['b'])

        if operation == 'add':
            result = await calculator_client.add(a, b)
        elif operation == 'subtract':
            result = await calculator_client.subtract(a, b)
        elif operation == 'multiply':
            result = await calculator_client.multiply(a, b)
        elif operation == 'divide':
            result = await calculator_client.divide(a, b)
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001) 