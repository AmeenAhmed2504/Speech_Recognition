import speech_recognition as sr
from deep_translator import GoogleTranslator

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)

    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio)
        print("\nYou said: " + text)

        # Language selection menu
        languages = {"hi": "Hindi", "kn": "Kannada", "ur": "Urdu"}
        print("\nSelect a language for translation:")
        for key, value in languages.items():
            print(f"{key} - {value}")

        selected_lang = input("\nEnter language code (hi/kn/ur): ").strip().lower()

        if selected_lang in languages:
            translated_text = GoogleTranslator(source="auto", target=selected_lang).translate(text)
            print(f"\nTranslated to {languages[selected_lang]}: {translated_text}")
        else:
            print("\nInvalid selection. Please enter a valid language code (hi/kn/ur).")

    except sr.UnknownValueError:
        print("\nCould not understand audio.")
    except sr.RequestError:
        print("\nCould not request results from Google Speech Recognition service.")

if __name__ == "__main__":
    recognize_speech()
