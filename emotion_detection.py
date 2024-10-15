import requests

def emotion_detector(text_to_analyze):
    # Define the URL for the Watson NLP Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define the headers for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Define the input data (JSON) for the request
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send a POST request to the Watson NLP API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Return the response text
    return response.text
