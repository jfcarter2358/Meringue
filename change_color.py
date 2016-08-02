import sys
try:
    from Tkinter import *
    import Tkinter as tk
    import ttk
except:
    from tkinter import *
    import tkinter as tk
    import tkinter.ttk as ttk
from subprocess import PIPE, Popen



class change_color:

    def change(self):
        try:
            string = str(self.var1.get())
            index = self.function_list.index(string)

            args = ['java', 'Color_Picker']
            p = Popen(args, stdin=PIPE, stdout=PIPE, shell=False)
            p.wait()
            out = p.stdout.read().split('\n')
            print(out)

            r = out[0]
            g = out[1]
            b = out[2]

            self.read_config()
            line = self.lines[index][:self.lines[index].find('=')]
            hex = '#%02x%02x%02x' % (int(r), int(g), int(b))
            line = line + '=' + hex
            self.lines[index] = line
            self.write_config()
            self.parent_obj.read_config()
            self.parent_obj.change_ed_colors()
            self.top.destroy()
        except:
            self.top.destroy()

    def write_config(self):
        with open(self.parent_obj.merengue_path+'config.ini', 'w') as f_out:
            for line in self.lines:
                f_out.write(line + '\n')
            f_out.flush()

    def read_config(self):
        with open(self.parent_obj.merengue_path+'config.ini', 'r') as f_in:
            self.lines = f_in.read().split('\n')
            self.highlight_foreground = self.lines[0].split('=')[1]
            self.highlight_background = self.lines[1].split('=')[1]
            self.highlight_keyword = self.lines[2].split('=')[1]
            self.highlight_function_name = self.lines[3].split('=')[1]
            self.highlight_function = self.lines[4].split('=')[1]
            self.highlight_boolean = self.lines[5].split('=')[1]
            self.highlight_string = self.lines[6].split('=')[1]
            self.highlight_number = self.lines[7].split('=')[1]
            self.highlight_operator = self.lines[8].split('=')[1]
            #self.highlight_normal = self.lines[9].split('=')[1]
            self.highlight_comment = self.lines[9].split('=')[1]
            self.foreground = self.lines[10].split('=')[1]
            self.background = self.lines[11].split('=')[1]
            self.file_color = self.lines[12].split('=')[1]
            self.dir_color = self.lines[13].split('=')[1]
            self.line_num_color = self.lines[14].split('=')[1]
            self.line_num_background_color = self.lines[15].split('=')[1]
            self.file_bar_color = self.lines[16].split('=')[1]
            self.file_bar_text_color = self.lines[17].split('=')[1]
            self.notebook_background = self.lines[18].split('=')[1]
            self.folder = self.lines[19].split('=')[1]

    def end(self):
        #self.parent_obj.reset_counters()
        #self.find_string = '!!END!!'
        self.top.destroy()

    def __init__(self, parent, parent_obj):

        top = self.top = Toplevel(parent)

        self.parent_obj = parent_obj

        self.function_list = ['highlight_foreground','highlight_background','highlight_keyword','highlight_function_name','highlight_function','highlight_boolean','highlight_string','highlight_number','highlight_operator','highlight_comment','foreground','background','file_color','dir_color','line_num_color','line_num_background_color','file_bar_color','file_bar_text_color','notebook_background']

        #index = self.parent_obj.n.tabs().index(self.parent_obj.n.select())
        #ed = self.parent_obj.eds[index]

        #ed.return_function_names(self)

        self.textFrame = Frame(top)

        lst1 = self.function_list
        self.var1 = StringVar()
        self.var1.set('highlight_foreground')
        self.dropdown = OptionMenu(self.textFrame, self.var1, *lst1)
        self.dropdown.pack()

        self.textFrame.pack()

        self.button = Button(top, text="Select Color", command=self.change)
        self.button.pack()

        self.button4 = Button(top, text="Cancel", command=self.end)
        self.button4.pack()

        self.parent_obj = parent_obj