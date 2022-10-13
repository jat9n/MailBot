
import smtplib # simple mail transfer protocol
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine= pyttsx3.init() #Speaking engine


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    # create a server| 587 is a port no.
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # TLS is transport Layer Security
    server.starttls()

    server.login('swamijatin1999@gmail.com', '*****') #enter password in place of ***** before running this code
    email = EmailMessage()
    email['From'] = 'swamijatin1999@gmail.com'
    email['TO'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'max' : 'jatinswami1999@gmail.com',
    'sam' : 'rdswami2005@gmail.com'
}


def get_email_info():
    talk('who you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('what is the subject of email?')
    subject = get_info()
    talk('start speaking')
    message = get_info()

    send_email(receiver, subject, message)
    talk('email is successfully sent')
    talk('do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()