import io

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def run_quickstart():

    client = speech.SpeechClient()
    file_name = 'brooklyn.flac'

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))


if __name__ == '__main__':
    run_quickstart()
