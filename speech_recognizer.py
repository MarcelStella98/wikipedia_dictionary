import speech_recognition as sr
import wikipediaapi

# utwórz obiekt recognizer i mikrofon
r = sr.Recognizer()
mic = sr.Microphone()


def get_wiki_definition(word):
    wiki = wikipediaapi.Wikipedia('pl')
    page = wiki.page(word)
    if page.exists():
        return page.summary
    else:
        return "Sorry, I couldn't find a definition for that word."


# function
def listen():
    with mic as source:
        r.adjust_for_ambient_noise(source) # adjust the noise level
        print("Mów teraz!")
        audio = r.listen(source) # listening
        try:
            text = r.recognize_google(audio, language='pl-PL') # 
          #  print("Zrozumiałem: " + text)
        except sr.UnknownValueError:
            print("Nie zrozumiałem, spróbuj ponownie.")
    return text 





      

word = listen() # słowo, dla którego chcesz uzyskać definicję
definition = get_wiki_definition(word)
print(definition)