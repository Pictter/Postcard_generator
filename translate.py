from google.cloud import translate_v2 as translate

# Google Cloud Translation API를 설정합니다.
def translate_text(text, target_language='ko'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']