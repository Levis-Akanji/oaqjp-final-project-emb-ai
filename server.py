from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_endpoint():
    """Analyzes the emotion of the provided text and returns the emotions and dominant emotion."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Call the emotion_detector function
    emotions = emotion_detector(text_to_analyze)

    # Prepare the response format
    output = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} "
        f"and 'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."
    )

    # Return the output in JSON format (if needed) or as plain text
    return output  # or return jsonify(output) for JSON response

@app.route('/')
def index():
    """Renders the index page."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the server
