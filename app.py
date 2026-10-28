from flask import Flask, request, jsonify

# Create the Flask application.
app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    """Return a personalized greeting, or a default greeting."""
    name = request.args.get('name', '').strip()
    if name:
        message = f'Hello, {name}!'
    else:
        message = 'Hello, World!'
    return jsonify({'message': message}), 200


@app.route('/sum', methods=['POST'])
def calculate_sum():
    """Validate a JSON list of numbers and return its sum."""
    if not request.is_json:
        return jsonify({'error': 'Request must contain JSON data.'}), 400
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({'error': 'Invalid JSON object.'}), 400
    if 'numbers' not in data:
        return jsonify({'error': "Missing 'numbers' field."}), 400
    numbers = data['numbers']
    if not isinstance(numbers, list):
        return jsonify({'error': "'numbers' must be a list."}), 400
    if not numbers:
        return jsonify({'error': 'The numbers list cannot be empty.'}), 400
    if not all(isinstance(num, (int, float)) and not isinstance(num, bool) for num in numbers):
        return jsonify({'error': 'All values must be numbers.'}), 400
    return jsonify({'numbers': numbers, 'sum': sum(numbers)}), 200


if __name__ == '__main__':
    # Local development server on the required port.
    app.run(port=5000, debug=True)
