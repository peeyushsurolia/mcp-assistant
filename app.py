from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv
import aiohttp
import asyncio

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

MCP_CLIENT_URL = "http://localhost:5001/calculate"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
async def chat():
    try:
        data = request.json
        user_message = data.get('message', '')

        # Check if the message is a calculation request
        if any(op in user_message.lower() for op in ['add', 'subtract', 'multiply', 'divide']):
            # Extract numbers and operation from the message
            words = user_message.lower().split()
            try:
                operation = next(op for op in ['add', 'subtract', 'multiply', 'divide'] if op in words)
                numbers = [float(word) for word in words if word.replace('.', '').isdigit()]
                if len(numbers) >= 2:
                    async with aiohttp.ClientSession() as session:
                        async with session.post(
                            MCP_CLIENT_URL,
                            json={
                                'operation': operation,
                                'a': numbers[0],
                                'b': numbers[1]
                            }
                        ) as response:
                            result = await response.json()
                            if 'result' in result:
                                return jsonify({'response': f"The result is: {result['result']}"})
            except Exception as e:
                pass

        # If not a calculation or calculation failed, use OpenAI
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that can also perform calculations. For calculations, use the format: 'add 5 and 3' or 'multiply 4 by 2'."},
                {"role": "user", "content": user_message}
            ]
        )
        
        return jsonify({'response': response.choices[0].message.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002) 