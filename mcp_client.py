from mcp.client.fastMCP import FastMCP
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import httpx

load_dotenv()

app = Flask(__name__)
CORS(app)

mcp = FastMCP("http://localhost:5000")

@mcp.tool(name="add")
async def add(a: float, b: float) -> float:
    response = await mcp.call_tool("add", {"a": a, "b": b})
    return response

@mcp.tool(name="subtract")
async def subtract(a: float, b: float) -> float:
    response = await mcp.call_tool("subtract", {"a": a, "b": b})
    return response

@mcp.tool(name="multiply")
async def multiply(a: float, b: float) -> float:
    response = await mcp.call_tool("multiply", {"a": a, "b": b})
    return response

@mcp.tool(name="divide")
async def divide(a: float, b: float) -> float:
    response = await mcp.call_tool("divide", {"a": a, "b": b})
    return response

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
            result = await add(a, b)
        elif operation == 'subtract':
            result = await subtract(a, b)
        elif operation == 'multiply':
            result = await multiply(a, b)
        elif operation == 'divide':
            result = await divide(a, b)
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001) 
