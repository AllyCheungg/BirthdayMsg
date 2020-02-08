from tkinter import *

top = Tk()
top.title("Max's Birthday 2020")
plane = Frame(top)
plane.pack(fill=BOTH, expand=True, padx=20)
top.maxsize(900, 1000)

# items
sb = Scrollbar(top)
sb.pack(side=RIGHT, fill=Y)

item = Listbox(top, yscrollcommand=sb.set)
item.pack(side=RIGHT, fill=BOTH)

# menu bar
menubar = Menu(top)
# file
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)
# name
namemenu = Menu(menubar, tearoff=0)
namemenu.add_command(label="Knock on George's door")
namemenu.add_command(label="Yell 'Alabama' three times")
namemenu.add_command(label="Debug the code")
menubar.add_cascade(label="Help", menu=namemenu)

top.config(menu=menubar)


def message():
    pointer = name.get()
    seb = "Hey Max, I know u love long paragraphs so " \
          "Ill keep this message short.  " \
          "I just wanted to wish you happy birthday, " \
          "wish you the best and thank you for dealing with us " \
          "and helping us with coding, mse, etc. Happy Birthday " \
          "Sebastian Arroyo-Altenburg"
    abn = "Happy Birthday Max! " \
          "It’s been great having many random conversations with you, " \
          "from talking about cults to Australian marsupials, " \
          "and you’re always a knowledgeable and fun person to talk to."
    ame = "Happy birthday Max! " \
          "I really enjoy all the dinner talk with you. " \
          "Thank you for all your help this year! " \
          "Without your matlab help, " \
          "I might be taking python right now, " \
          "and might be a cool non-ece engineer lol. " \
          "I’ll try not to be that surprised when I see you on campus. " \
          "Running in the rain with juicy dumplings was a fun time haha."
    ish = "Happy Birthday Max! " \
          "Thank you for always understanding all of my US references " \
          "and for making everyone laugh with your wonderful ideas! " \
          "I’m grateful for having met you this year and " \
          "I look forward to playing more card games with you in the years to come."
    be = "happy birthday max, " \
         "please continue to flex on us with ur coding knowledge. " \
         "Also feel free to write my programs for me sometime :D"
    emm = "Happy birthday Max! " \
          "Thanks for talking about all the fun facts and " \
          "interesting stories during dinner XD. " \
          "Exploding kittens is super fun with you and " \
          "I would like a temporary alliance at some point haha. " \
          "Have a good birthday!! Enjoy your cookies too~"
    dic = {'Ally': "Ally: HBD",
           'Selena': "Selena: Dear Max, happy birth of day",
           'Eric': "Eric: print('Happy Birthday Max!!!!')",
           'Abnash': "Abnash: " + abn,
           'Sebastian': "Sebastian: " + seb,
           'George': "George: Happy Birthday Max",
           'Amelie': "Amelie: " + ame,
           'Shiqi': "Shiqi: happy being old Max",
           'Isha': "Isha: " + ish,
           'Ben': "Ben: " + be,
           'Emma': "Emma: " + emm,
           'Albert': "Albert: Happy Birthday Max"
           }

    if pointer in dic.keys():
        result = Label(item, text=dic[pointer], wraplength=500)
        result.pack(padx=30, pady=10)

    else:
        wrong = Label(item, text="brain.exe has stopped working")
        wrong.pack(padx=30, pady=10)


# instruction
opening = Label(plane, text="Enter a name \n (Please capitalize the first letter)")
opening.pack(side=TOP, padx=30, pady=5)

# return
inst = Label(top, text="Our birthday message(s):")
inst.pack(side=LEFT)
name = StringVar()

# input
entry = Entry(plane, bd=5, textvariable=name)
entry.pack()

# button
button = Button(plane, text="Enter", padx=10, command=message)
button.pack()

top.mainloop()
