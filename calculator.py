import math
import tkinter
from tkinter import ttk
import customtkinter 
from PIL import ImageTk, Image

equation_text = ''

def maincalculator():
 def clicked(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)
    
 def operation(sign):
    global equation_text
    equation_text = equation_text + str(sign)
    equation_label.set(equation_text)

 def exponents(exp):
    global equation_text
    powered = equation_text**exp
    equation_label.set(powered)
    equation_text = ''
    equation_text = equation_text + str(powered)
 
 def equal():
    newequation = ''
    global equation_text
    equationsaved
    
    for letter in equation_text:
        if letter == '÷':
            newequation += '/'
        elif letter == '×':
            newequation += '*'
        elif letter == 'log':
            newequation += 'math.log'
        else:
            newequation += letter
    requation = ''
    result = eval(newequation)
    for letter in newequation:
        if letter == '/':
            requation += '%'
        else:
            requation += letter
    remainder = eval(requation)
    if remainder == 0:
        
        result = f'{result:.0f}'
    equation_label.set(result)
    equationsaved.append(equation_text + ' = ' + str(result))
    equation_text = ''
    equation_text += equation_text + str(result)
    


 def equals(event):
    global equation_text
    newequation = ''
    for letter in equation_text:
        if letter == '÷':
            newequation += '/'
        elif letter == '×':
            newequation += '*'
        else:
            newequation += letter
    requation = ''
    result = eval(newequation)
    for letter in newequation:
        if letter == '/':
            requation += '%'
        else:
            requation += letter
    remainder = eval(requation)
    if remainder == 0:
        
        result = f'{result:.0f}' 
    equation_label.set(result)
    equation_text = ''
    equation_text += equation_text + str(result)  
      
 def clear():
    global equation_text
    equation_text = ''
    equation_label.set(equation_text)

 def constants(con):
    global equation_text
    if con == 'e':
     con = math.e
    elif con == '𝝅' or 'p':
     con = math.pi
    equation_text = equation_text + str(con)
    equation_label.set(equation_text)

 def ln():
    global equation_text
    nequation_text = eval(equation_text)
    natural = math.log(nequation_text)
    equation_label.set(natural)
    equation_text = ''
    equation_text += equation_text + str(natural)

 def log():
    global equation_text
    number = eval(equation_text)
    logged = math.log(number, 10)
    equation_label.set(logged)
    equation_text = ''
    equation_text += equation_text + str(logged)

 def sqrt():
    global equation_text
    equation_text = eval(equation_text)
    sqrted = math.sqrt(equation_text)
    sqrted = str(sqrted)
    split = sqrted.split('.')
    for letter in split:
        if len(split[1]) == 1 and letter == '0':
            sqrted = float(sqrted)
            sqrted = f'{sqrted:.0f}'
        else:
            sqrted
    equation_label.set(sqrted)
    equation_text = ''
    equation_text += equation_text + str(sqrted) 
    
 def keyboard(event):
    if event.char.isdigit():
        clicked(int(event.char))
    elif event.char in '+-*/.':
        operation(event.char)
    elif event.char in '=':
        equal()
    elif event.char in 'c' or 'C':
        clear()
    elif event.char in 'p':
        constants('p')

 def squared():
    global equation_text
    squared = eval(equation_text)**2
    equation_label.set(squared)
    equation_text = ''
    equation_text += equation_text + str(squared)  

 def enter(event):
    equals(event)

 def backed(okay):
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 windowsize = window.geometry('325x450')
 window.title('Calculator')
 window.configure(bg = '#333333')
 window.bind('<Key>', keyboard)
 window.bind('<Return>', enter)
 window.bind('<BackSpace>', backed)

 menuframe = tkinter.Frame(window, bg = '#333333')
 menuframe.pack(side = 'top', fill = tkinter.X)
 menubutton = tkinter.Button(menuframe, text = '≡', font = 5, fg = 'white', bg = '#333333', bd = 0, command = lambda: togglemenu())
 menubutton.pack(side = 'left')

 equation_label = tkinter.StringVar()
 
 textdisplay = tkinter.Label(window, bg = '#333333', fg = 'white', width = 40, height = 6, textvariable=equation_label, font = ('ArialRoundedMT Bold', 16), anchor = 'se')
 textdisplay.pack()

 style = ttk.Style()
 style.configure('CustomSeparator.TSeparator', background = 'dodger blue')
 line = ttk.Separator(window, style = 'CustomSeparator.TSeparator' )
 line.pack(padx = 1, pady = 1, fill = tkinter.X, expand = True)

 frames = tkinter.Frame(window, bg = '#333333') 
 frames.pack()
 frames.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)
 frames.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)


 button1 = customtkinter.CTkButton(frames, text = 1, width = 60, height = 35, font = ('Avant Garde Medium', 16),fg_color = 'dodger blue', command = lambda: clicked(1))
 button1.grid(row = 6, column = 1, padx = 1, pady = 1, sticky = 'nsew')

 button2 = customtkinter.CTkButton(frames, text = 2, width = 60,height = 35, font = ('Avant Garde Medium', 16),fg_color = 'dodger blue', command = lambda: clicked(2))
 button2.grid(row = 6, column = 2, padx = 1, pady = 1, sticky = 'nsew')

 button3 = customtkinter.CTkButton(frames, text = 3, width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dodger blue',  command = lambda: clicked(3))
 button3.grid(row = 6, column = 3, padx = 1, pady = 1, sticky = 'nsew')

 button4 = customtkinter.CTkButton(frames, text = 4, width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dodger blue', command = lambda: clicked(4))
 button4.grid(row = 5, column = 1, padx = 1, pady = 1, sticky = 'nsew')

 button5 = customtkinter.CTkButton(frames, text = 5, width = 60,height = 35,font = ('Avant Garde Medium', 16), fg_color = 'dodger blue', command = lambda: clicked(5))
 button5.grid(row = 5, column = 2, padx = 1, pady = 1, sticky = 'nsew')

 button6 = customtkinter.CTkButton(frames, text = 6, width = 60,height = 35, font = ('Avant Garde Medium', 16),fg_color = 'dodger blue',command = lambda: clicked(6))
 button6.grid(row = 5, column = 3, padx = 1, pady = 1, sticky = 'nsew')

 button7 = customtkinter.CTkButton(frames, text = 7, width = 60, height = 35, font = ('Avant Garde Medium', 16),fg_color = 'dodger blue',command = lambda: clicked(7))
 button7.grid(row = 4, column = 1, padx = 1, pady = 1, sticky = 'nsew')

 button8 = customtkinter.CTkButton(frames, text = 8, width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dodger blue',  command = lambda: clicked(8))
 button8.grid(row = 4, column = 2, padx = 1, pady = 1, sticky = 'nsew')

 button9 = customtkinter.CTkButton(frames, text = 9, width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dodger blue', command = lambda: clicked(9))
 button9.grid(row = 4, column = 3, padx = 1, pady = 1, sticky = 'nsew')

 buttonc = customtkinter.CTkButton(frames, text = 'c', width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dark orange',command = lambda: clear())
 buttonc.grid(row = 2, column = 3, padx = 1, pady = 1, sticky = 'nsew')

 buttonback = customtkinter.CTkButton(frames, text = 'del', width = 60,height = 35,font = ('Avant Garde Medium', 13),fg_color = 'dark orange', command = lambda: clear())
 buttonback.grid(row = 2, column = 4, padx = 1, pady = 1, sticky = 'nsew')

 button0 = customtkinter.CTkButton(frames, text = 0, width = 120,height = 35, font = ('Avant Garde Medium', 16),fg_color = 'dodger blue',command = lambda: clicked(0))
 button0.grid(row = 7, column = 1, columnspan = 2, padx = 1, pady = 1, sticky = 'nsew')

 buttonPeriod = customtkinter.CTkButton(frames, text = '.', width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dodger blue',  command = lambda: clicked('.'))
 buttonPeriod.grid(row = 7, column = 3, padx = 1, pady = 1, sticky = 'nsew')

 buttonadd = customtkinter.CTkButton(frames, text = '+', width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dark orange', command = lambda: operation('+'))
 buttonadd.grid(row = 6, column = 4, padx = 1, pady = 1, sticky = 'nsew')

 buttonsub = customtkinter.CTkButton(frames, text = '-', width = 60,height = 35,font = ('Avant Garde Medium', 16), fg_color = 'dark orange', command = lambda: operation('-'))
 buttonsub.grid(row = 5, column = 4, padx = 1, pady = 1, sticky = 'nsew')

 buttone = customtkinter.CTkButton(frames, text = '=', width = 60,height = 35, font = ('Avant Garde Medium', 16), fg_color = 'dark orange', command = lambda: equal())
 buttone.grid(row = 7, column = 4, padx = 1, pady = 1, sticky = 'nsew')

 buttond = customtkinter.CTkButton(frames, text = '÷', width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dark orange',  command = lambda: operation('÷'))
 buttond.grid(row = 4, column = 4, padx = 1, pady = 1, sticky = 'nsew')

 buttonm = customtkinter.CTkButton(frames, text = '×', width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dark orange', command = lambda: operation('×'))
 buttonm.grid(row = 3, column = 4, padx = 1, pady = 1, sticky = 'nsew')

 buttonRParenthesis = customtkinter.CTkButton(frames, text = ')', width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dodger blue', command = lambda: clicked(')'))
 buttonRParenthesis.grid(row = 3, column = 3, padx = 1, pady = 1, sticky = 'nsew')

 buttonLParenthesis = customtkinter.CTkButton(frames, text = '(', width =60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dodger blue',command = lambda: clicked('('))
 buttonLParenthesis.grid(row = 3, column = 2, padx = 1, pady = 1, sticky = 'nsew')

 buttonEx = customtkinter.CTkButton(frames, text = 'xʸ', width = 60,height = 35,font = ('Avant Garde Medium', 13), fg_color = 'dodger blue', command = lambda: operation('**'))
 buttonEx.grid(row = 3, column = 1, padx = 1, pady = 1, sticky = 'nsew')

 buttonBIGE = customtkinter.CTkButton(frames, text = 'e', width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dark orange',  command = lambda: constants('e'))
 buttonBIGE.grid(row = 2, column = 1, padx = 1, pady = 1, sticky = 'nsew')

 buttonPI = customtkinter.CTkButton(frames, text = '𝝅', width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dark orange',  command = lambda: constants('𝝅'))
 buttonPI.grid(row = 2, column = 2, padx = 1, pady = 1, sticky = 'nsew')

 buttonSEC = customtkinter.CTkButton(frames, text = '2nd', width = 60,height = 35,font = ('Avant Garde Medium', 13),fg_color = 'dark orange',  command = lambda: operation('×'))
 buttonSEC.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = 'nsew')

 buttonSQRT = customtkinter.CTkButton(frames, text = '√', width = 60,height = 35,font = ('Avant Garde Medium', 16),fg_color = 'dodger blue', command = lambda: sqrt())
 buttonSQRT.grid(row = 3, column = 0, padx = 1, pady = 1, sticky = 'nsew')

 buttonTENX = customtkinter.CTkButton(frames, text = '10ˣ', width = 60,height = 35,font = ('Avant Garde Medium', 13),fg_color = 'dodger blue', command = lambda: operation('×'))
 buttonTENX.grid(row = 4, column = 0, padx = 1, pady = 1, sticky = 'nsew')

 buttonLOG = customtkinter.CTkButton(frames, text = 'log', width = 60, height = 35,font = ('Avant Garde Medium', 13),fg_color = 'dodger blue', command = lambda: log())
 buttonLOG.grid(row = 5, column = 0, padx = 1, pady = 1, sticky = 'nsew')

 buttonLN = customtkinter.CTkButton(frames, text = 'ln', width = 60, height = 35, font = ('Avant Garde Medium', 13),fg_color = 'dodger blue',command = lambda: ln())
 buttonLN.grid(row = 6, column = 0, padx = 1, pady = 1, sticky = 'nsew')

 buttonSQUARED = customtkinter.CTkButton(frames, text = 'x²', width = 60, height = 35,font = ('Avant Garde Medium', 13),fg_color = 'dodger blue',  command = lambda: squared())
 buttonSQUARED.grid(row = 7, column = 0, padx = 1, pady = 1, sticky = 'nsew')
#----------------------------------------------------------------------------------------------------------------------------------
equationsaved = []

def togglemenu():
  def middleman():
     for widget in window.winfo_children():
        widget.destroy()
     maincalculator()
  def close():
    toggle.destroy()
  def historywindow():
      def close2():
          toggle.destroy()
      
      for widget in window.winfo_children():
        widget.destroy()
      global equationsaved
      toggle = tkinter.Frame(window, bg = 'white')
      menuheight = window.winfo_height()
      toggle.place(x=0,y=0, height = menuheight, width = 200)
      exitmenu = tkinter.Button(toggle, text = 'x', font = 1, bd = 0, bg = '#333333', fg = 'white', command = lambda: close2())
      exitmenu.place(x = 0, y = 0)
      history = tkinter.Button(toggle, text = 'history', font = ('ArialRoundedMT Bold', 12), bg = '#333333', bd = 0, fg = 'white', command = lambda: historywindow())
      history.place(x = 10, y = 50)
      calculator = tkinter.Button(toggle, text = 'calculator', font = ('ArialRoundedMT Bold', 12), bg = '#333333', bd = 0, fg = 'white', command = lambda: maincalculator())
      menuframe = tkinter.Frame(window, bg = '#333333')
      menuframe.pack(side = 'top', fill = tkinter.X)
     #   menuimage = ImageTk.PhotoImage(file='downloads/menu.png')
      menubutton = tkinter.Button(menuframe, text = '≡', font = 5, fg = 'white', bg = '#333333', bd = 0, command = lambda: togglemenu())
      menubutton.pack(side = 'left')
      calculator.place(x = 10, y = 80)
      equation_label = tkinter.StringVar()
      
      equation_label.set('\n'.join(reversed(equationsaved)))
      labelheight = window.winfo_height()
      labelwidth = window.winfo_width()
      textdisplay = tkinter.Label(window,bg = '#333333', fg = 'white', textvariable=equation_label, height = labelheight, width = labelwidth, anchor = 'ne', font = 10)
      textdisplay.pack()
      toggle.lift(textdisplay)
      
  
  toggle = tkinter.Frame(window, bg = 'white')
  menuheight = window.winfo_height()
  toggle.place(x=0,y=0, height = menuheight, width = 200)
  exitmenu = tkinter.Button(toggle, text = 'x', font = 1, bd = 0, bg = 'white', fg = 'black', command = lambda: close())
  exitmenu.place(x = 0, y = 0)
  history = tkinter.Button(toggle, text = 'history', font = ('ArialRoundedMT Bold', 12), bg = 'white', bd = 0, fg = 'black', command = lambda: historywindow())
  history.place(x = 10, y = 50)
  calculator = tkinter.Button(toggle, text = 'calculator', font = ('ArialRoundedMT Bold', 12), bg = 'white', bd = 0, fg = 'black', command = lambda: middleman())
  calculator.place(x = 10, y = 80)

window = tkinter.Tk()
Image = tkinter.PhotoImage(file = 'projects/items/calculatoricon.png')
window.iconphoto(False, Image) 
#comma Image
maincalculator()
window.mainloop()

#icon:  https://icons8.com/icons/set/calculator
