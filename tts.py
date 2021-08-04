import tkinter as tk
import  pyttsx3

engine=pyttsx3.init()

root = tk.Tk()
root.title('Test-To-Speech')
root.configure(background="blue")
label = tk.Label(root,text="Type here something",font="arial 25 bold" ,bg="blue" ,fg="red")
label.pack()
textbox=tk.Entry(root,width=30,font="arial 20")
textbox.pack()

def speak(text):
    engine.say(text)
    engine.runAndWait()

button = tk.Button(root,text="Speak",font="arial 25 bold" ,bg="pink" ,fg="red",command=lambda:speak(textbox.get()))
button.pack()
root.mainloop()