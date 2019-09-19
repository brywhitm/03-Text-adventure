from tkinter import *       #Imports tkinter items----text needed this to work in a gui
import tkinter              #imports tkinter----tkinter is the main gui modual I am useing
import json                 #imports json----allows the code to use .json files
import time                 #imports time----allows use of time (didnt use was use in a test then keep just because)

root = Tk()                 #creates the window for tkinter which is now set to root
root.configure(background='gray')               #the root window is configured to have a gray background color
text = Text(root, wrap=WORD, cursor="arrow")    #sets the text variable to a text box created in the root window and makes the cursor look like and arrow when hovering over

root.title('Text Adventure')                    #sets the root windows title to Text Adventure
root.geometry("1000x700")                       #created a pixle grid for the root window
root.resizable(0, 0)                            #disables the ability to change the root window size because a lot of the stuff is set to points not to grid size

canvas = Canvas(root, width=700, height=700)    #creates a canvas in the root window allowing me to import shapes,colors,and images into it. set the canvas size in root window
canvas.pack(side="left")                        #sets the canvas to the left side. I dont 100% know what pack is but it is needed for all tkinter items you will see all for the  buttons and text has it as well
MapIm=PhotoImage(file='TownMap.png')            #sets the image for the map to a variable so it can be called latter
canvas.create_image(1,1,image=MapIm, anchor=NW) #Latter IS NOW! the canvas creates the image over it starting from the point (1,1) the pixel grid starts in the top left corner. this also anchors the image to the northwest of the box/canvas

MyOval = canvas.create_oval(450,450,475,475, fill='red')    #this is just the oval that is created on the map to show starting point I did plan on makeing it move but didnt have the time

current=''      #makes a global variable for current because for my loop I need it to change and it cant change if it is in the def that redefinds it each time
count=0         #makes a global variable for count. this is used 2 time for the first text and setting current for the first time as stated above if I didnt it would be reset each time allowing you to go no where
if count ==0:   #first count is used here if you can read basic logic you can read it IF COUNT is equal to 0 then do the following. if you dont know how it works then welp I cant help you
    text.insert(INSERT,"\n\nDirections: Click a direction then click continue. If your location repeats it means you can not go in the direction you have chosen. Scroll to read text. Main goal is to just explore the town. There is no automatic end so you can leave by closing the window or clicking on quit.\n\n")
    text.insert(INSERT,"\n\nYou are at Your House\n")       #
    text.insert(INSERT,"This is your house.")               # This is just the first text displayed in the text window. its logicly read as well
    text.insert(INSERT,'\nWhere would you like to go? ')    # in text(the variable defind above)insert the string ....
def check_input(event):                                     # and here it is the game loop this is where the magic happens. were the event is used for making a loop(latter a button is used to call to this)
    gameFile = 'game.json'                                  #this just sets the .json file to a variable
    SB.place(bordermode=OUTSIDE, height=90, width=150, x=775, y=550)        #this make the continue button an puts it on the screen
    B1.place(bordermode=OUTSIDE, height=30, width=50, x=40000, y=40000)     #
    B2.place(bordermode=OUTSIDE, height=30, width=50, x=40000, y=40060)     #These are button that are defined latter
    B3.place(bordermode=OUTSIDE, height=30, width=50, x=35000, y=40030)     #I didnt want to remove button and replace button each time so I put this here
    B4.place(bordermode=OUTSIDE, height=30, width=50, x=45000, y=43000)     #It sends the buttons to timbuktu based on cord
    game = {}                               #creates the game dictionary used a lot
    with open(gameFile) as json_file:       #this opens the json file I think I just took it from the first code because it did what I needed
        game = json.load(json_file)         #this sets game the the .json file and tells it to load it
    global current                          #calls the global variable current
    global count                            #calls the global variable count
    if count ==0:               #this is why count was made first just to set current then not allow it to be reset
        current = 'Your House'  #sets current
        count=count+1           #adds one to count so all programs using count will stop basicly for a one use item
    
    r = game['rooms']   #explaned below because I got tired of typing up here so I started at bottom
    c = r[current]      #^^^^^^^^^^^
    verbs=game['verbs'] #sets the variable verbs to the game dict verbs for easy calling

    toReturn = event.widget['text']        #gets the input event and sets it to a variable and change to a string
    
    for v in verbs:             #checks to see if inputed item is a verb and does stuff again I took this from first code because I needed it for this to work
        if toReturn == v['v']:  #^^^^^^^
            toReturn=v['map']   #^^^^^

    for e in game['rooms'][current]['exits']:                   #modified from first code so that current works. removed all of that selection crap and made it simple with current and the input
        if toReturn == e['verb'] and e['target'] != 'NoExit':   #logicly read and explaned a little^^^
            current=e['target']     #sets current to the target which is in the .json file based on the verb from the input


    
    return current      #returns current to global variable after changing

    #if current=='Your House':
    #    MyOval = canvas.create_oval(450,450,475,475, fill='red')   
    #elif current=='the dirt road':
    #    MyOval = canvas.create_oval(500,420,525,445, fill='red')
    #elif current=="Faendal's House":
    #    MyOval = canvas.create_oval(0,0,0,0, fill='red')
    #elif current=='the center of town':
    #    MyOval = canvas.create_oval(0,0,0,0, fill='red') 
    #elif current=='the local inn':
    #    MyOval = canvas.create_oval(0,0,0,0, fill='red') 
    #elif current=="the town's shopping district":
    #    MyOval = canvas.create_oval(0,0,0,0, fill='red') 
    #elif current=="Sven and Hilde's House":
    #    MyOval = canvas.create_oval(0,0,0,0, fill='red') 
    #elif current=="the town's southern wall":
    #    MyOval = canvas.create_oval(0,0,0,0, fill='red') 
    #elif current=="the archery range":
    #    MyOval = canvas.create_oval(0,0,0,0, fill='red') 
    #elif current=="the town's lumber mill":
    #    MyOval = canvas.create_oval(0,0,0,0, fill='red') 
    #elif current=="the lumber yard":
    #    MyOval = canvas.create_oval(0,0,0,0, fill='red') 
    #elif current=="the town's northern wall":
    #    MyOval = canvas.create_oval(0,0,0,0, fill='red') 
    #elif current=="the town's eastern wall":
    #    MyOval = canvas.create_oval(0,0,0,0, fill='red')       #all a test that was not done made to show the player where they are at but not done ran out of time

def TextBlock(event):           #the def used for text and updating the current correctly so the program isnt behind
    global current              #explaned
    gameFile = 'game.json'      #explaned
    canvas.delete(MyOval)       #deletes the starting oval made for finding start
    game = {}       #explaned
    with open(gameFile) as json_file:   #explaned
        game = json.load(json_file)     #explaned above just reused to make this one undersand the variable
    r = game['rooms']       #sets the rooms from the json file to a variable to make it easier for calling
    c = r[current]          #current stuff
    text.insert(INSERT,'\n\nYou are at '+ current +"\n")    #
    text.insert(INSERT,c['desc'])                           #inserts text into the root window text box
    text.insert(INSERT,'\nWhere would you like to go? ')    #
    SB.place(bordermode=OUTSIDE, height=90, width=150, x=50000, y=40000)            #sends continue button to timbuktu
    B1.place(bordermode=OUTSIDE, height=30, width=50, x=825, y=430)         #
    B2.place(bordermode=OUTSIDE, height=30, width=50, x=825, y=490)         #calls buttons back from timbuktu
    B3.place(bordermode=OUTSIDE, height=30, width=50, x=775, y=460)         #
    B4.place(bordermode=OUTSIDE, height=30, width=50, x=875, y=460)         #


def Quit(event):        #the quit button calls here and ends the program
    root.destroy()      #closes the root window

B1 = tkinter.Button(root, text ="NORTH")                            #
B2 = tkinter.Button(root, text ="SOUTH")                            #button names the setting them the the root window
B3 = tkinter.Button(root, text ="WEST")                             #
B4 = tkinter.Button(root, text ="EAST")                             #
SB=tkinter.Button(root, text='Continue')                            #

text.pack()                                                         #
Quitb=tkinter.Button(root, text = "Quit")                           #
Quitb.bind('<Button-1>', Quit)                                      #
Quitb.pack()                                                        #button placement and size as well as event handlers
Quitb.place(bordermode=OUTSIDE, height=30, width=50, x=950, y=5)    #
SB.bind('<Button-1>', TextBlock)                                    #
SB.pack()                                                           #
SB.place(bordermode=OUTSIDE, height=90, width=150, x=775, y=550)    #
B1.bind('<Button-1>', check_input)                                  #
B1.pack()                                                           #buttons just buttons
B1.place(bordermode=OUTSIDE, height=30, width=50, x=825, y=430)     #at this point after days of making this code and testing like crazy
B2.bind('<Button-1>', check_input)                                  #and now commenting on everything
B2.pack()                                                           #all i have to say is this is all the buttons and there event inputs
B2.place(bordermode=OUTSIDE, height=30, width=50, x=825, y=490)     #still dont know what pack is
B3.bind('<Button-1>', check_input)                                  #this is all kinda logical you can basicly read it
B3.pack()                                                           #
B3.place(bordermode=OUTSIDE, height=30, width=50, x=775, y=460)     #
B4.bind('<Button-1>', check_input)                                  #
B4.pack()                                                           #
B4.place(bordermode=OUTSIDE, height=30, width=50, x=875, y=460)     #
root.mainloop()     #the loop that allows the buttons to be presses without ending right after basicly keeps everything loaded on the root window
#I made all of this code other then the 10 lines I used from the first code given dont think I just coppied crap and said I made it I know what it all does took we a week just to make in free time