import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json: { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, json = Input_json, header = Headers)

    res = json.loads(response.text)

    if response.status_code == 200:
        return res
    elif response.status_code == 400:
        res = {'anger': None,'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    return res


