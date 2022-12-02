import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hola yorvy")
# engine.runAndWait()

#  Vamos a trabajarlo de la siguiente manera 

book=open(r'texto.txt')
book_text=book.readlines()

engine = pyttsx3.init()  # Es para escuchar

for line in book_text:
	engine.say(line)
	engine.runAndWait() # Es el espera


