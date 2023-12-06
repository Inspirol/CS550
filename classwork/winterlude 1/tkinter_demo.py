from tkinter import *
from tkinter import ttk
root = Tk()

first_initial = {
'a':' stinky',
'b':' lumpy',
'c':' buttercup',
'd':' gidget',
'e':' crusty',
'f':' greasy',
'g':' fluffy',

'h':' cheeseball',
'i':' chim-chim',
'j':' poopsie',
'k':' flunky',
'l':' booger',
'm':' pinky',
'n':' zippy',

'o':' goober',
'p':' doofus',
'q':' slimy',
'r':' loopy',
's':' snotty',
't':' falafel',

'u':' dorkey',
'v':' squeezit',
'w':' oprah',
'x':' skipper',
'y':' dinky',
'z':' zsa-zsa',
}

last_first_initial = {
'a':' diaper',
'b':' toilet',
'c':' giggle',
'd':' bubble',
'e':' girdle',
'f':' barf',
'g':' lizard',
'h':' waffle',
'i':' cootie',
'j':' monkey',
'k':' potty',
'l':' liver',
'm':' banana',
'n':' rhino',
'o':' burger',
'p':' hamster',
'q':' toad',
'r':' gizzard',
's':' pizza',
't':' gerbil',
'u':' chicken',
'v':' pickle',
'w':' chuckle',
'x':' tofu',
'y':' gorilla',
'z':' stinker',
}

last_last_initial = {
'a':' head',
'b':' mouth',
'c':' face',
'd':' nose',
'e':' tush',
'f':' breath',
'g':' pants',
'h':' shorts',
'i':' lips',
'j':' honker',
'k':' butt',
'l':' brain',
'm':' tushie',
'n':' chunks',
'o':' hiney',
'p':' biscuits',
'q':' toes',
'r':' buns',
's':' fanny',
't':' sniffer',
'u':' sprinkles',
'v':' kisser',
'w':' squirt',
'x':' humperdinck',
'y':' brains',
'z':' juice',
}

root.title("Basic tkinter demo")
root.geometry("300x300")
root.resizable(False, False)

ttk.Label(root, text="first name").grid()

first_name = ttk.Entry(root)

first_name.grid()

ttk.Label(root, text="last name").grid()

last_name = ttk.Entry(root)

last_name.grid()



def name_thing():
    first = first_name.get()
    last = last_name.get()
    if first == "" or last == "":
        return
    first_initial_letter = first[0].lower()
    last_first_initial_letter = last[0].lower()
    last_last_initial_letter = last[-1].lower()
    new_name = first_initial[first_initial_letter] + last_first_initial[last_first_initial_letter] + last_last_initial[last_last_initial_letter]
    ttk.Label(root, text=new_name).grid()

ttk.Button(root, text="new name", command=name_thing).grid()

root.mainloop()

