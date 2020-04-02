import tkinter as tk
from project_file import Engsci_Press


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.press = None
        self.children_dict = {}
        self.wm_title("EngSci Press")
        self.set_author_window()
        self.st_greetings = tk.Label(self, text="Welcome to EngSci Press!\n"
                                                "This is an amazing interactive dictionary!\n"
                                                "How can we help you today?\n")
        self.st_choice = tk.Label(self, text="Please choose one of the following options by pressing on a button:")
        self.st_greetings.pack()
        self.st_choice.pack()

        self.load_file_btn = tk.Button(self, text="Load a file to the dictionary",
                                       command=self.load_file_window)
        self.load_file_btn.pack(padx=50, pady=20)

        self.get_def_btn = tk.Button(self, text="Get word's definition",
                                     command=self.get_def_window)
        self.get_def_btn.pack(padx=50, pady=20)

        self.new_word_btn = tk.Button(self, text="Add a new word and its definition",
                                      command=self.new_word_window)
        self.new_word_btn.pack(padx=50, pady=20)

        self.word_del_btn = tk.Button(self, text="Delete a word from the dictionary",
                                      command=self.word_del_window)
        self.word_del_btn.pack(padx=50, pady=20)

        self.scroll_btn = tk.Button(self, text="Scroll the dictionary from a given word",
                                    command=self.scroll_window)
        self.scroll_btn.pack(padx=50, pady=20)

        self.ref_word_btn = tk.Button(self, text="Find a subset for a reference word",
                                      command=self.ref_word_window)
        self.ref_word_btn.pack(padx=50, pady=20)

        self.sev_let_btn = tk.Button(self, text="Find a word from beginning letters",
                                     command=self.sev_let_window)
        self.sev_let_btn.pack(padx=50, pady=20)

        self.clos_pos_btn = tk.Button(self, text="Find the closest word to a reference word",
                                      command=self.clos_pos_window)
        self.clos_pos_btn.pack(padx=50, pady=20)

        self.size_btn = tk.Button(self, text="Tell size of dictionary",
                                      command=self.size_window)
        self.size_btn.pack(padx=50, pady=20)

        self.save_btn = tk.Button(self, text="Save current dictionary to a file",
                                      command=self.save_window)
        self.save_btn.pack(padx=50, pady=20)

        self.dull_btn = tk.Button(self, text="I forgot who's the author...",
                                      command=self.dull_window)
        self.dull_btn.pack(padx=50, pady=20)

    def set_author_window(self):
        load = tk.Toplevel()
        load.wm_title("Log In")

        load.itemLabel = tk.Label(load, text="Enter your name, my grace: ")
        load.itemVar = tk.StringVar()
        load.itemEntry = tk.Entry(load, textvariable=load.itemVar)
        load.itemEntry.focus_set()
        self.children_dict[load] = load.itemVar
        #
        load.itemLabel.grid(row=0, column=0)
        load.itemEntry.grid(row=0, column=1)

        load.okButton = tk.Button(load,text="Ok", command=lambda: self.set_author(load))

        load.okButton.grid(row=1, column=0)

    def set_author(self, per):
        name = self.children_dict[per].get()
        self.press = Engsci_Press(name)
        #self.user = name
        temp = tk.Toplevel()
        temp.wm_title("Success")
        temp.itemLabel = tk.Label(temp, text="Done!\n"
                                             "Welcome to EngSci Press, {}!\n"
                                             "Your personal dictionary has been initialized.".format(name))
        temp.itemLabel.pack()


    def load_file_window(self):
        load = tk.Toplevel()
        load.wm_title("Load a file")

        load.itemLabel = tk.Label(load, text="Enter the file name: ")
        load.itemVar = tk.StringVar()
        load.itemEntry = tk.Entry(load,
                                  textvariable=load.itemVar)
        load.itemEntry.focus_set()
        self.children_dict[load] = load.itemVar
        load.itemLabel.grid(row=0, column=0)
        load.itemEntry.grid(row=0, column=1)

        load.okButton = tk.Button(load,
                                  text="Ok",
                                  command=lambda: self.load_file(load))

        load.okButton.grid(row=1, column=0)

    def load_file(self, load):
        # value = self.children_dict[load].get()
        # self.press.process_dictionary(value)#get more details
        # print('Success!')
        self.press.collate_bsts()
        temp = tk.Toplevel()
        temp.wm_title("Success")
        temp.itemLabel = tk.Label(temp, text="Done!")
        temp.itemLabel.pack()

    def get_def_window(self):
        defs = tk.Toplevel()
        defs.wm_title("Word's definition")

        defs.itemLabel = tk.Label(defs, text="Enter the word: ")
        defs.itemVar = tk.StringVar()
        defs.itemEntry = tk.Entry(defs, textvariable=defs.itemVar)
        defs.itemEntry.focus_set()
        self.children_dict[defs] = defs.itemVar
        defs.itemLabel.grid(row=0, column=0)
        defs.itemEntry.grid(row=0, column=1)

        defs.submitButton = tk.Button(defs,
                                      text="Ok",
                                      command=lambda: self.get_def(defs))

        defs.submitButton.grid(row=1, column=0)

    def get_def(self, defs):
        value = self.children_dict[defs].get()
        definition = self.press.output_definition(value)  # get more details
        temp = tk.Toplevel()
        temp.wm_title("Word's definition")
        temp.itemLabel = tk.Label(temp, text=definition)
        temp.itemLabel.pack()

    def new_word_window(self):
        new = tk.Toplevel()
        new.wm_title("Add a word with its definiton")

        # word input
        new.wordLabel = tk.Label(new, text="Enter the word: ")
        new.wordVar = tk.StringVar()
        new.wordEntry = tk.Entry(new,
                                 textvariable=new.wordVar)
        new.wordEntry.focus_set()

        new.wordLabel.grid(row=0, column=0)
        new.wordEntry.grid(row=0, column=1)

        # definition input
        new.defLabel = tk.Label(new, text="Enter the definition: ")
        new.defVar = tk.StringVar()
        new.defEntry = tk.Entry(new,
                                textvariable=new.defVar)

        new.defLabel.grid(row=1, column=0)
        new.defEntry.grid(row=1, column=1)

        self.children_dict[new] = (new.wordVar, new.defVar)

        new.okButton = tk.Button(new,
                                 text="Ok",
                                 command=lambda: self.new_word(new))
        new.okButton.grid(row=2, column=0)

    def new_word(self, new):
        value = self.children_dict[new]
        word = value[0].get()
        definition = value[1].get()
        self.press.add_word(word, definition)
        temp = tk.Toplevel()
        temp.wm_title("Success")
        temp.itemLabel = tk.Label(temp, text="Done!")
        temp.itemLabel.pack()

    def word_del_window(self):
        dels = tk.Toplevel()
        dels.wm_title("Word's deletion")

        dels.itemLabel = tk.Label(dels, text="Enter the word: ")
        dels.itemVar = tk.StringVar()
        dels.itemEntry = tk.Entry(dels, textvariable=dels.itemVar)
        dels.itemEntry.focus_set()
        self.children_dict[dels] = dels.itemVar
        dels.itemLabel.grid(row=0, column=0)
        dels.itemEntry.grid(row=0, column=1)

        dels.submitButton = tk.Button(dels,
                                      text="Ok",
                                      command=lambda: self.word_del(dels))

        dels.submitButton.grid(row=1, column=0)

    def word_del(self, dels):
        value = self.children_dict[dels].get()
        #self.press.delete_word(value)
        temp = tk.Toplevel()
        temp.wm_title("Success")
        temp.itemLabel = tk.Label(temp, text="Done!")
        temp.itemLabel.pack()

    def scroll_window(self):
        scr = tk.Toplevel()
        scr.wm_title("Scrolling")

        scr.itemLabel = tk.Label(scr, text="Enter the word: ")
        scr.itemVar = tk.StringVar()
        scr.itemEntry = tk.Entry(scr, textvariable=scr.itemVar)
        scr.itemEntry.focus_set()
        self.children_dict[scr] = scr.itemVar
        scr.itemLabel.pack()
        scr.itemEntry.pack()

        scr.submitButton = tk.Button(scr,
                                     text="Ok",
                                     command=self.scroll(scr))

        scr.submitButton.pack()

    def scroll(self, scr):
        temp = tk.Toplevel()
        temp.wm_title("Scrolling")
        temp.itemLabel = tk.Label(temp, text="Choose which direction to scroll\n"
                                             "'<' means to letter A\n"
                                             "'>' means to letter Z\n")
        temp.itemLabel.grid(column=1, row=0)
        temp.A_btn = tk.Button(temp, text="<", command=self.A_click(scr))
        temp.Z_btn = tk.Button(temp, text=">", command=self.Z_click(scr))
        temp.A_btn.grid(column=0, row=1)
        temp.Z_btn.grid(column=2, row=1)
        temp.lbl = tk.Label(temp)
        temp.lbl.grid(column=1, row=2)
        '''
        scr.lbl = tk.Label(scr, text="Choose which direction to scroll\n"
                                     "'<' means to letter A\n"
                                     "'>' means to letter Z\n")
        scr.lbl.grid(column=1, row=1)
        scr.A_btn = tk.Button(scr, text="<", command=self.A_click(scr))
        scr.Z_btn = tk.Button(scr, text=">", command=self.Z_click(scr))
        scr.A_btn.grid(column=0, row=2)
        scr.Z_btn.grid(column=2, row=2)
        '''

    def A_click(self, scr):
        value = self.children_dict[scr].get()
        ff = tk.Toplevel()
        ff.wm_title("Result")
        ff.itemLabel = tk.Label(scr)
        word = self.press.scroll(value, 0)
        text = "The previous word is {}\n".format(word) if word else "Sorry that was the end of the dictionary!\n"
        ff.lbl.config(text=text)

    def Z_click(self, scr):
        value = self.children_dict[scr].get()
        word = self.press.scroll(value, 1)
        ff = tk.Toplevel()
        ff.wm_title("Result")
        ff.itemLabel = tk.Label(ff)
        text = "The previous word is {}\n".format(word) if word else "Sorry that was the end of the dictionary!\n"
        ff.lbl.config(text=text)

    def ref_word_window(self):
        ref = tk.Toplevel()
        ref.wm_title("Searching for words")

        ref.itemLabel = tk.Label(ref, text="Enter the word: ")
        ref.itemVar = tk.StringVar()
        ref.itemEntry = tk.Entry(ref, textvariable=ref.itemVar)
        ref.itemEntry.focus_set()
        self.children_dict[ref] = ref.itemVar
        ref.itemLabel.grid(row=0, column=0)
        ref.itemEntry.grid(row=0, column=1)

        ref.submitButton = tk.Button(ref, text="Ok", command=lambda: self.ref_word(ref))

        ref.submitButton.grid(row=1, column=0)

    def ref_word(self, ref):
        value = self.children_dict[ref].get()
        mass = self.press.subset_words(value)
        temp = tk.Toplevel()
        temp.wm_title("Success")
        text = ''
        for i in mass:
            text = text + i + '\n'
        temp.itemLabel = tk.Label(temp, text=text)
        temp.itemLabel.pack()

    def sev_let_window(self):
        sev = tk.Toplevel()
        sev.wm_title("Searching for words")

        sev.itemLabel = tk.Label(sev, text="Enter the word: ")
        sev.itemVar = tk.StringVar()
        sev.itemEntry = tk.Entry(sev, textvariable=sev.itemVar)
        sev.itemEntry.focus_set()

        sev.numLabel = tk.Label(sev, text="Enter the threshold: ")
        sev.numVar = tk.IntVar()
        sev.numEntry = tk.Entry(sev, textvariable=sev.numVar)

        self.children_dict[sev] = (sev.itemVar, sev.numVar)
        sev.itemLabel.grid(row=0, column=0)
        sev.itemEntry.grid(row=0, column=1)
        sev.numLabel.grid(row=1, column=0)
        sev.numEntry.grid(row=1, column=1)

        sev.submitButton = tk.Button(sev, text="Ok", command=lambda: self.sev_let(sev))

        sev.submitButton.grid(row=2, column=0)

    def sev_let(self, sev):
        value = self.children_dict[sev]
        mass = self.press.reference_word(value[0].get(), value[1].get())
        temp = tk.Toplevel()
        temp.wm_title("Success")
        temp.itemLabel = tk.Label(temp, text=mass)
        temp.itemLabel.pack()

    def clos_pos_window(self):
        sev = tk.Toplevel()
        sev.wm_title("Searching for words")

        sev.itemLabel = tk.Label(sev, text="Enter the word: ")
        sev.itemVar = tk.StringVar()
        sev.itemEntry = tk.Entry(sev, textvariable=sev.itemVar)
        sev.itemEntry.focus_set()

        sev.numLabel = tk.Label(sev, text="Enter the threshold: ")
        sev.numVar = tk.IntVar()
        sev.numEntry = tk.Entry(sev, textvariable=sev.numVar)

        self.children_dict[sev] = (sev.itemVar, sev.numVar)
        sev.itemLabel.grid(row=0, column=0)
        sev.itemEntry.grid(row=0, column=1)
        sev.numLabel.grid(row=1, column=0)
        sev.numEntry.grid(row=1, column=1)

        sev.submitButton = tk.Button(sev, text="Ok", command=lambda: self.clos_pos(sev))

        sev.submitButton.grid(row=2, column=0)

    def clos_pos(self, sev):
        value = self.children_dict[sev]
        mass = self.press.suggest_word(value[0].get(), value[1].get())
        temp = tk.Toplevel()
        temp.wm_title("Success")
        temp.itemLabel = tk.Label(temp, text=mass)
        temp.itemLabel.pack()

    def size_window(self):
        sev = tk.Toplevel()
        sev.wm_title("The number for words")
        sev.itemLabel = tk.Label(sev, text=str(self.press.size()) + " words")#doesn't catch zero size
        sev.itemLabel.pack()

    def save_window(self):
        sev = tk.Toplevel()
        sev.wm_title("Searching for anfile")

        sev.itemLabel = tk.Label(sev, text="Enter the name of file (ex: 'filename.txt'): ")
        sev.itemVar = tk.StringVar()
        sev.itemEntry = tk.Entry(sev, textvariable=sev.itemVar)
        sev.itemEntry.focus_set()

        self.children_dict[sev] = sev.itemVar
        sev.itemLabel.grid(row=0, column=0)
        sev.itemEntry.grid(row=0, column=1)
        sev.submitButton = tk.Button(sev, text="Ok", command=lambda: self.save(sev))
        sev.submitButton.grid(row=2, column=0)

    def save(self, sev):
        self.press.push_tofile(self.children_dict[sev].get())
        temp = tk.Toplevel()
        temp.wm_title("Success")
        temp.itemLabel = tk.Label(temp, text="Done!")
        temp.itemLabel.pack()

    def dull_window(self):
        sev = tk.Toplevel()
        sev.wm_title("It'S YoU")
        sev.itemLabel = tk.Label(sev, text="Your Majesty, is everything ok?\n"
                                               "How could you forget your name?\n"
                                               "People of your kingdom grieve for you, {}".format(self.press.author))
        sev.itemLabel.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
