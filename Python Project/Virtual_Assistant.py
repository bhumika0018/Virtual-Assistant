#Importing Libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import random
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
#from Final_gui import *



listener = sr.Recognizer()
reader = pyttsx3.init()


#maleandfemalevoice
voices = reader.getProperty('voices')
reader.setProperty('voice',voices[1].id)

reader.say('Hello!! I am  Sophia')
reader.say('How may I help you')
reader.say('Please Login to proceed')
reader.runAndWait()

#to repeat text like a parrot
def parrot(text):
    reader.say(text)
    reader.runAndWait()

#to listen and to record audio
def order():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            #print(f'You said {command}')
            return command
            #parrot(command)
    except:
        pass
    return command

#calculator
def calculator():        
    def add(a,b):
        return a + b

    def sub(a,b):
      return a - b

    def multi(a,b):
      return a * b

    def div(a,b):
      return a / b
    def calcs():
        dictionary={"+":add,"-":sub,"*":multi,"/":div}
        num1=float(input("Enter first number\n"))
        num2=float(input("Enter second number\n"))
        for signs in dictionary:
            print(signs)
        turn = False
        while not turn:    
            enterr=input("Enter the sign you want to perform\n")
            
            dinn=dictionary[enterr]
            first_ans=dinn(num1,num2)
            print(f"Sum of the given two numbers is {first_ans}")
            last_in=input("type 'y' to continue and 'n' to start a fresh calculation and  exit to exit from calculator\n").lower()
            
            if last_in=="n":
                turn = True
                calcs()
            elif last_in== "y":
                num3=float(input("Enter a number\n"))
                num1=first_ans
                num2=num3
                turn = False
            elif last_in == "exit":
                turn = True
                running_mode()
                
                
    calcs()
#password generator
def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    yo_li=[]
    for i in range(0,nr_letters+1):
        ranu= random.choice(letters)
        yo_li+=ranu
    for i in range(0,nr_symbols+1):
        sym = random.choice(symbols)
        yo_li+=sym
    for i in range(0,nr_numbers+1):
        num = random.choice(numbers)
        yo_li+=num
    random.shuffle(yo_li)
    yo = ""
    for i in yo_li:
        yo+=i
    return yo


#activites performed by sofia
def running_mode():
    try:
        command = order()
        #print(command)
        if 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M %p')
            print(f'Time is {time}')
            parrot('Time is' + time)

        elif 'day' in command:
            day = datetime.datetime.today().weekday() + 1
            days_dictionary = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thusday',5:'Friday',6:'Saturday',7:'Sunday'}
            if day in days_dictionary.keys():
                week = days_dictionary[day]
                print(week)
                parrot('The day is'+ week)
        elif 'hello'in command:
            parrot('HELLO! Welcome')
            print('HELLO! Welcome')

        elif 'who is' in command:
            person = command.replace('who is','')
            info = wikipedia.summary(person,3)
            print(info)
            parrot(info)

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            parrot(joke)

        elif 'play ' in command:
            song = command
            parrot('Playing...' + song)
            print('Playing')
            pywhatkit.playonyt(song)

        elif 'python' in command:
            print('Opening Python')
            parrot('Opening python')
            webbrowser.open('www.python.org')

        elif 'quora' in command:
            print('Opening Quora')
            parrot('Opening Quora')
            webbrowser.open('www.quora.com')

        elif 'stack' in command:
            print('Opening stackoverflow')
            parrot('Opening stackoverflow')
            webbrowser.open('www.stackoverflow.com')

        elif 'mail' in command:
            print('Opening gmail')
            parrot('Opening gmail')
            webbrowser.open('www.gmail.com')    

        elif 'are you' in command:
            print("Hi,Its good to hear from you. I hope you and your loved ones are staying safe and healthy during this difficult time")
            parrot("Hi,Its good to hear from you. I hope you and your loved ones are staying safe and healthy during this difficult time")

        elif 'sing a song' in command:
            print(" I need a one dance Got a Hennessy in my hand One more time 'fore I go Higher powers taking a hold on me")
            parrot(" I need a one dance Got a Hennessy in my hand One more time 'fore I go Higher powers taking a hold on me")

        elif 'name' in command:
            print("My name is Sophia")
            parrot("My name is Sophia")

        elif 'hobbies' in command:
            print('My hobbies include , listening to you,')
            parrot('My hobbies include , listening to you,')

        elif 'online game' in command:
            parrot('I like all kind of games.')
            webbrowser.open('www.arkadium.com')
        elif 'calculator' in command:
            parrot('Opening Calculator')
            calculator()

        elif 'password' in command:
            parrot('Opening password generator')
            passwd = password()
            print(f'Here is your secured password {passwd}')
            parrot('Here is your secured password')
        elif 'exit' in command:
            parrot('Sorry to see you go,will meet soon byebye')
            print('Sorry to see you go,will meet soon byebye')
        else:
            parrot('Sorry I did not understand,please repeat it again ')
    except:
        print("We can't reach you at this time!! TRY AGAIN")


def Tkinter():
    box=Tk()
    box.geometry('1200x630')
    #box.configure(bg='cyan')
    box.title('Login Page')

    #BG Image
    my_bg=ImageTk.PhotoImage(Image.open("D:\LPU\Semester 3\INT213\Python Report\Project/Assistant.png"))
    my_label = Label(image=my_bg)

    my_label.pack()
    my_label.place(x=0,y=0)

    #LoginFrame
    login_frame = Frame(bg='white')
    login_frame.place(x=50,y=210,height=340,width=490)

    title=Label(login_frame,text='Login Here',font=('Goudy old style',25,"bold"),fg='#000080',bg='white')
    title.place(x=165,y=30)

    lb1_user=Label(login_frame,text='UserName',font=('Goudy old style',20,"bold"),fg='grey',bg='white')
    lb1_user.place(x=40,y=83)

    e1=Entry(login_frame,font=('times new roman',15),bg='lightgray')
    e1.place(x=45,y=130,width=350,height=25)

    lb2_pass=Label(login_frame,text='Password',font=('Goudy old style',20,"bold"),fg='grey',bg='white')
    lb2_pass.place(x=40,y=180)

    e2=Entry(login_frame,font=('times new roman',15),show='*',bg='lightgray')
    e2.place(x=45,y=230,width=350,height=25)

    

   
    def myf():
        if e1.get()=='Priya' and e2.get()=='PRIYA':
            def sofia():
                
                img=ImageTk.PhotoImage(Image.open("D:\LPU\Semester 3\INT213\Python Report\Project/Sofia.png"))
                my_label = Label(image=img)

                my_label.pack(side='left')
                my_label.place(x=-50,y=0)

                imga=ImageTk.PhotoImage(Image.open("D:\LPU\Semester 3\INT213\Python Report\Project/Black.png"))
                my_label1 = Label(image=imga)
                my_label1.pack(side='right')
                my_label1.place(x=900,y=0)

                b1=Button(text='Speak',font=("bold"),fg='white',bg='#000080',cursor='hand2',command=running_mode)
                b1.place(x=0,y=600,width=902,height=40)

                f1=Button(text='Close',cursor='hand2',font=("bold"),fg='black',bg='yellow',command=box.destroy)
                f1.place(x=902,y=600,width=300,height=40)

                

                #print('How can i help you?')
                mainloop()
            sofia()
            #messagebox.showinfo('Welcome','You are successfully logged in')
        elif e1.get()=='Priya' and e2.get()=='12345':
            messagebox.showerror('Error','Your password is wrong Try again')
        elif e1.get()=='Priya' and e2.get()=='':
            messagebox.showerror('Error','Do enter your password to proceed')    
        else:
            messagebox.showerror('Error','All Fields are required')
    b1=Button(login_frame,text='Login', fg='white',bg='#000080',cursor='hand2',command=myf)
    b1.place(x=350,y=290,width=110,height=30)
    f1=Button(login_frame,text='Forgot password?',cursor='hand2',fg='#000080',bg='white')
    f1.place(x=45,y=270)
    mainloop()

Tkinter()
#while True:
 # running_mode()

          
        
