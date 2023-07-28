
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":

    print("welcome to RoboSpeaker 1.1 created by shilpa ")
    while True:
       text_to_speak = input("Enter the text you want the RoboSpeaker to say: ")
       if text_to_speak == "stop":
           break

       speak(text_to_speak)

