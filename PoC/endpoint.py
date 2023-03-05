from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def store_data():
    data = request.data
    with open("stored_data.json", "a") as file:
        file.write(data.decode("utf-8") + "\n")
    return "Data stored successfully"

if __name__ == '__main__':
    app.run(port=8000, debug=True)
