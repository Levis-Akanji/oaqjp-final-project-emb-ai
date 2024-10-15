import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Define the input data (JSON)
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send the POST request
    response = requests.post(url, json=myobj, headers=headers)

    # Debug: Print the raw response text
    print("Raw Response Text:", response.text)  # For debugging
    
    # Convert the response text into a dictionary
    try:
        response_dict = json.loads(response.text)
    except json.JSONDecodeError:
        print("Failed to decode JSON from response.")
        return {}

    # Debug: Print the parsed response dictionary
    print("Parsed Response Dictionary:", response_dict)  # For debugging

    # Extract the required emotions
    emotions = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None
    }
    
    # Accessing the emotion predictions
    emotion_predictions = response_dict.get('emotionPredictions', [])

    # Check if any predictions exist
    if not emotion_predictions:
        print("No emotion predictions found.")
        return emotions

    # Extract emotions from the first prediction
    for emotion_data in emotion_predictions:
        # Directly access the emotion scores
        emotion_scores = emotion_data['emotion']  # Access the 'emotion' key directly
        
        # Update emotions dictionary with scores
        for emotion_name in emotions.keys():
            emotions[emotion_name] = emotion_scores.get(emotion_name)  # Correctly assign scores

    # Debug: Print the extracted emotions
    print("Extracted Emotions:", emotions)  # For debugging
    
    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=lambda k: emotions[k] if emotions[k] is not None else -1)
    
    # Create the final output dictionary
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return result

# Test the function with a specific input
if __name__ == "__main__":
    response = emotion_detector("I am so happy I am doing this")
    print(response)
