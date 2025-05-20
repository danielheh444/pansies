import requests


API_KEY = "AQVNw4OzQPk_Gcm3Y8jru-tc35RcLOfWlMPYNrVv"
folder_id = "b1ggclmibj9ido60f67j"

def translate_text_yandex(text, target_language):
    body = {
        "sourceLanguageCode" : "ru",
        "targetLanguageCode": target_language,
        "texts": text,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key {0}".format(API_KEY),
    }

    response = requests.post(
        "https://translate.api.cloud.yandex.net/translate/v2/translate",
        json=body,
        headers=headers,
    )

    if response.status_code == 200:
        return response.json()['translations'][0]['text']
    else:
        raise Exception(f"Yandex API error: {response.text}")