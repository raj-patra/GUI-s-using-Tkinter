"""

Simple on-screen keyboard using tkinter

Author : Raj Patra

Version 5.0

"""

from tkinter import *
import tkinter.messagebox
import tkinter.filedialog


on_screen = Tk()

buttons = [

    'ESC', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', '[', ']', '{', '}',
    '~', '!', '@', '#', '$', '%', '^', '&', '(', ')', '|', '"', '<<', 'CLEAR', '_', '=', '+',
    'TAB', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'ENTER', '7', '8', '9', '-',
    'CAPS', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '<', 'SHIFT', '4', '5', '6', '*',
    'CTRL', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', '>', 'CTRL', '1', '2', '3', '/',
    ' Space ',

]
buttons_cap = [

    'ESC', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', '[', ']', '{', '}',
    '~', '!', '@', '#', '$', '%', '^', '&', '(', ')', '|', '"', '<<', 'CLEAR', '_', '=', '+',
    'TAB', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'ENTER', '7', '8', '9', '-',
    'CAPS', 'A', 'S', 'D', 'f', 'G', 'H', 'J', 'K', 'L', ';', '<', 'SHIFT', '4', '5', '6', '*',
    'CTRL', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '?', '>', 'CTRL', '1', '2', '3', '/',
    ' Space ',

]

counter = 0  # counter variable for Caps_Lock event
counter_ = 0 # counter variable for deleting the boot message


class Keyboard:
    def __init__(self, master):
        global text, color_schemes, theme_choice
        self.master = master
        master.title("On-Screen Keyboard")

        master.resizable(0, 0)
        master.config(bg='#0C090A')

        menu = Menu(on_screen)
        on_screen.config(menu=menu)
        file_menu = Menu(menu)
        menu.add_cascade(label="Themes", menu=file_menu)
        menu.add_cascade(label="Save", accelerator='Ctrl+S', command=self.save)

        self.label1 = Label(on_screen, bg='#0C090A').grid(row=0, columnspan=25)

        boot_text = '\n\n'+'\t\t\t\t\t'+'          Pick a Theme...'
        text = Text(master, width=100, height=5, bg='black', fg='#f0f0f0',
                    font=('Comic sans MS', 15), relief='flat')
        text.grid(row=1, columnspan=18)
        text.insert(CURRENT, boot_text)

        self.label2 = Label(on_screen, bg='#0C090A', fg='#32CD32', ).grid(row=2, columnspan=25)

        color_schemes = {

            '1. Midnight Black': 'FFFFFF.0C090A',

            '2. Blood Red': 'F62217.0C090A',

            '3. Halloween Orange': 'F87217.0C090A',

            '4. Star Yellow': 'FFD801.0C090A',

            '5. Matrix Green': '32CD32.0C090A',

            '6. Meth Blue': '38ACEC.0C090A',

            '7. Sage Purple': 'E238EC.0C090A',

        }

        # Choosing and assigning the themes start # text.get("1.0", "end-1c")

        theme_choice = StringVar()
        theme_choice.set('1. Default White')
        for k in sorted(color_schemes):
            file_menu.add_radiobutton(label=k, variable=theme_choice, command=self.theme)

        text.bind('<Control-S>', self.save)
        text.bind('<Control-s>', self.save)

    def save(self, event=None):
        global filename
        try:
            f = open(filename, 'w')
            letter = text.get("1.0", "end-1c")
            f.write(letter)
            f.close()
        except:
            self.save_as()

    def save_as(self, event=None):
        try:
            f = tkinter.filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                                     filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            fh = open(f, 'w')
            global filename
            filename = f
            textoutput = text.get("1.0", "end-1c")
            fh.write(textoutput)
            fh.close()
        except:
            pass

    def theme(self):

        global bgc, fgc, a_fgc, a_bgc, counter_
        val = theme_choice.get()
        color = color_schemes.get(val)
        fgc, bgc = color.split('.')
        fgc, bgc = '#' + fgc, '#' + bgc
        a_bgc, a_fgc = color.split('.')
        a_bgc, a_fgc = '#' + a_bgc, '#' + a_fgc
        on_screen.config(bg=bgc)
        text.config(fg=fgc, relief='groove')
        if counter_ == 0:
            text.delete('1.0', END)
            counter_ += 1

        self.click(buttons)

    def special_keys(self, value):

        if value == '<<':
            tex = len(text.get("1.0", "end-1c")) - 1
            text.delete('1.' + str(tex), END)

        elif value == ' Space ':
            text.insert(END, ' ')

        elif value == 'TAB':
            text.insert(END, '   ')

        elif value == 'CAPS':

            global counter
            counter += 1
            if counter % 2 == 0:
                self.click(buttons)
            else:
                self.click(buttons_cap)
            if counter > 2:
                counter = 1

        elif value == 'ESC':
            if tkinter.messagebox.showinfo('WARNING', 'The application will be terminated...!'):
                on_screen.destroy()

        elif value == 'ENTER':
            text.insert(END, '\n')
            # text.get("1.0", "end-1c")
            # this command prints out all the contents of the text widgets

        elif value == 'CLEAR':
            text.delete('1.0', END)
            # this command deletes out all the contents of the text widgets

        else:
            text.insert(END, value)

    def click(self, buttons):

        key_row = 3
        key_column = 0

        # ----------------------------------Making of the Scrollbar------------------------------------

        scroll = Scrollbar(on_screen)
        scroll.grid(row=1, column=17, sticky=N + S + W)
        # the sticky=N+S+W command makes the scrollbar as long as the text widget
        scroll.config(command=text.yview, bg='black')
        text.config(yscrollcommand=scroll.set)

        # -----------------------------------Making of the buttons--------------------------------------

        for button in buttons:

            command = lambda x=button: self.special_keys(x)

            if button == ' Space ':
                self.b1 = Button(self.master, bg='#0C090A', fg='white', text=button, width=60
                                 , activebackground="#25383C", activeforeground='black'
                                 , relief=FLAT, padx=8, pady=8, bd=4, command=command, font=('Comic sans MS', 15))
                self.b1.grid(row=8, columnspan=17)
                self.b1.config(bg=bgc, fg=fgc, activebackground=a_bgc, activeforeground=a_fgc,
                               overrelief='groove')
                # b1.bind("<ENTER>", b1.config(bg=fgc, fg=bgc))

            elif button == 'ENTER':
                self.b2 = Button(self.master, text=button, bg='#0C090A', fg='white', width=11
                                 , activebackground="#25383C", activeforeground='black'
                                 , relief=FLAT, padx=4, pady=4, bd=2, command=command, font=('Comic sans MS', 15))
                self.b2.grid(row=key_row, column=key_column, columnspan=2)
                self.b2.config(bg=bgc, fg=fgc, activebackground=a_bgc, activeforeground=a_fgc,
                               overrelief='groove')

                key_column += 1

            elif button == 'F1' or button == 'F2' or button == 'F3' or button == 'F4' \
                    or button == 'F5' or button == 'F6' or button == 'F7' or button == 'F8' \
                    or button == 'F9' or button == 'F10' or button == 'F11' or button == 'F12' \
                    or button == 'CTRL' or button == 'SHIFT':

                self.b4 = Button(self.master, text=button, bg='#0C090A', fg='white', width=5
                                 , activebackground="#25383C", activeforeground='black'
                                 , relief='flat', padx=4, pady=4, bd=2, font=('Comic sans MS', 15))
                self.b4.grid(row=key_row, column=key_column)
                self.b4.config(bg=bgc, fg=fgc, activebackground=a_bgc, activeforeground=a_fgc,
                               overrelief='groove')


            else:
                self.b3 = Button(self.master, text=button, bg='#0C090A', fg='white', width=5
                                 , activebackground="#25383C", activeforeground='black'
                                 , relief=FLAT, padx=4, pady=4, bd=2, command=command, font=('Comic sans MS', 15))
                self.b3.grid(row=key_row, column=key_column)
                self.b3.config(bg=bgc, fg=fgc, activebackground=a_bgc, activeforeground=a_fgc,
                               overrelief='groove')

            key_column += 1

            # -----------------------------------Arrangement of the buttons--------------------------------------

            if key_column > 16 and key_row == 3:
                key_column = 0
                key_row += 1

            if key_column > 16 and key_row == 4:
                key_column = 0
                key_row += 1

            if key_column > 16 and key_row == 5:
                key_column = 0
                key_row += 1

            if key_column > 16 and key_row == 6:
                key_column = 0
                key_row += 1


my_board = Keyboard(on_screen)
on_screen.protocol("WM_DELETE_WINDOW", on_screen.destroy)

on_screen.mainloop()