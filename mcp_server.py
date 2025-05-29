from mcp import MCPServer, mcptool, Parameter
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class CalculatorServer(MCPServer):
    def __init__(self):
        super().__init__("calculator-server")
        self.register_tools()

    def register_tools(self):
        @mcptool("add")
        @Parameter("a", float, "First number")
        @Parameter("b", float, "Second number")
        def add(a: float, b: float) -> float:
            return a + b

        @mcptool("subtract")
        @Parameter("a", float, "First number")
        @Parameter("b", float, "Second number")
        def subtract(a: float, b: float) -> float:
            return a - b

        @mcptool("multiply")
        @Parameter("a", float, "First number")
        @Parameter("b", float, "Second number")
        def multiply(a: float, b: float) -> float:
            return a * b

        @mcptool("divide")
        @Parameter("a", float, "First number")
        @Parameter("b", float, "Second number")
        def divide(a: float, b: float) -> float:
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b

if __name__ == '__main__':
    server = CalculatorServer()
    server.run(host='0.0.0.0', port=5000) 