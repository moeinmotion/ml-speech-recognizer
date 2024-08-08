from dotenv import load_dotenv
import os
from openai import OpenAI
import speech_recognition as sr
from gtts import gTTS

load_dotenv()
# Load environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
# Set your OpenAI API key
OpenAI.api_key = openai_api_key
# Initialize speech recognizer
r = sr.Recognizer()

def process_voice_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def jarvis_response(user_input):
    # Query ChatGPT for response
    response = client.completions.create(engine="text-davinci-003",
    prompt=user_input,
    max_tokens=150)
    return response.choices[0].text.strip()

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

if __name__ == "__main__":
    while True:
        command = process_voice_command().lower()

        if 'jarvis' in command:
            user_input = command.replace('jarvis', '').strip()
            if user_input:
                response = jarvis_response(user_input)
                print(f"Jarvis: {response}")
                speak(response)
            else:
                print("Yes, sir?")

        elif 'exit' in command:
            print("Exiting...")
            break