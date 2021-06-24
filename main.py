from tkinter import *
from tkinter import ttk
from random import randint
import time
from threading import Timer

# stime = time.time()
# print(input())
# endtime = time.time()
# print("{:.2f}".format(endtime - stime));

cuvinte = ['masina', 'copil', 'caine', 'dictionar', 'ac', 'astronaut', 'calculator', 'scoala', 'automobil', 'cascador', 'cameleon', 'caracatita', 'papagal',
           'xerox', 'zebra', 'kimono', 'kilogram', 'student', 'restanta', 'profesor', 'instragram', 'masa', 'casa', 'televizor', 'aspirator', 'gunoi', 'geografie',
           'cunoastere', 'biblioteca', 'drum', 'bormasina', 'cal', 'apartament', 'excvator', 'frumusete', 'frumos', 'petrol', 'avion', 'combustibil', 'tabla',
           'numaratoare', 'fractie', 'kiwi', 'mango', 'mamut', 'tigru', 'maimuta', 'misiune','soldat', 'antrenament', 'sport', 'aspirator', 'baschet', 'fotbal',
           'handbal', 'golf', 'spatiu', 'pamant', 'viitor', 'trecut', 'prezent', 'iubire', 'ura', 'paine', 'sarmale']

class Application(Frame):
    def __init__(self, master=None, Frame=None):
        Frame.__init__(self, master)
        super(Application, self).__init__()
        self.grid(column=0, row=0)
        self.createMenuWidgets()

    def actionPlayButton(self):
        self.destroy()
        super(Application, self).__init__()
        self.grid(column=0, row=0)
        self.createPlayWidgets()

    def actionBackButton(self):
        self.destroy()
        super(Application, self).__init__()
        self.grid(column=0, row=0)
        self.createMenuWidgets()

    def actionInfoButton(self):
        self.destroy()
        super(Application, self).__init__()
        self.grid(column=0, row=0)
        self.createInfoWidgets()

    def actionEasyButton(self):
        self.destroy()
        super(Application, self).__init__()
        self.grid(column=0, row=0)
        self.createEasyWidgets()

    def actionMediumButton(self):
        self.destroy()
        super(Application, self).__init__()
        self.grid(column=0, row=0)
        self.createMediumWidgets()

    def actionHardButton(self):
        self.destroy()
        super(Application, self).__init__()
        self.grid(column=0, row=0)
        self.createHardWidgets()

    def actionExitButton(self):
        self.quit()

    def actionEnterEasy(self, event):
        # self.after_cancel(self.easyid)
        self.easyTime = 6
        self.total = self.total+1
        if self.easyEntry.get() == self.copy_cuvinte[self.n]:
            self.score = self.score+1
        if self.total == 10:
            self.destroy()
            super(Application, self).__init__()
            self.grid(column=0, row=0)
            self.createFinalWidgets()
        else:
            self.destroy()
            super(Application, self).__init__()
            self.grid(column=0, row=0)
            self.createEasyWidgets()

    def actionEnterMedium(self, event):
        self.after_cancel(self.mediumid)
        self.mediumTime = 4
        self.total = self.total + 1
        if self.mediumEntry.get() == self.copy_cuvinte[self.n]:
            self.score = self.score + 1
        if self.total == 15:
            self.destroy()
            super(Application, self).__init__()
            self.grid(column=0, row=0)
            self.createFinalWidgets()
        else:
            self.destroy()
            super(Application, self).__init__()
            self.grid(column=0, row=0)
            self.createMediumWidgets()

    def actionEnterHard(self, event):
        self.after_cancel(self.hardmid)
        self.hardTime = 4
        self.total = self.total + 1
        if self.hardEntry.get() == self.copy_cuvinte[self.n]:
            self.score = self.score + 1
        if self.total == 20:
            self.destroy()
            super(Application, self).__init__()
            self.grid(column=0, row=0)
            self.createFinalWidgets()
        else:
            self.destroy()
            super(Application, self).__init__()
            self.grid(column=0, row=0)
            self.createHardWidgets()

    def actionAfterTimeEasy(self):
        if self.easyTime == 0:
            self.easyTimeLabel.config(text="Time left: " + str(self.easyTime))
            self.easyTime = 6
            self.total += 1
            if self.easyEntry.get() == self.copy_cuvinte[self.n]:
                self.score += 1
            if self.total == 10:
                self.destroy()
                super(Application, self).__init__()
                self.grid(column=0, row=0)
                self.createFinalWidgets()
            else:
                self.createEasyWidgets()
        else:
            self.easyTime -= 1
            self.easyTimeLabel.config(text="Time left: "+str(self.easyTime))
            self.id = self.after(1000, self.actionAfterTimeEasy)

    def actionAfterTimeMedium(self):
        if self.mediumTime == 0:
            self.mediumTimeLabel.config(text="Time left: " + str(self.mediumTime))
            self.mediumTime = 4
            self.total += 1
            if self.mediumEntry.get() == self.copy_cuvinte[self.n]:
                self.score += 1
            if self.total == 15:
                self.destroy()
                super(Application, self).__init__()
                self.grid(column=0, row=0)
                self.createFinalWidgets()
            else:
                self.createMediumWidgets()
        else:
            self.mediumTime -= 1
            self.mediumTimeLabel.config(text="Time left: "+str(self.mediumTime))
            self.id = self.after(1000, self.actionAfterTimeMedium)

    def actionAfterTimeHard(self):
        if self.hardTime == 0:
            self.hardTimeLabel.config(text="Time left: " + str(self.hardTime))
            self.hardTime = 2
            self.total += 1
            if self.hardEntry.get() == self.copy_cuvinte[self.n]:
                self.score += 1
            if self.total == 20:
                self.destroy()
                super(Application, self).__init__()
                self.grid(column=0, row=0)
                self.createFinalWidgets()
            else:
                self.createHardWidgets()
        else:
            self.hardTime -= 1
            self.hardTimeLabel.config(text="Time left: "+str(self.hardTime))
            self.id = self.after(1000, self.actionAfterTimeHard)


    def createMenuWidgets(self):
        self.easyTime = 6
        self.mediumTime = 4
        self.hardTime = 2

        self.score = 0
        self.total = 0

        self.copy_cuvinte = cuvinte
        self.random_numbers = []

        #impartirea in pagina
        self.topframe = Frame(self)
        self.topframe.grid(row=0, column=0)

        self.midframe1 = Frame(self)
        self.midframe1.grid(row=1, column=0)

        self.midframe2 = Frame(self)
        self.midframe2.grid(row=2, column=0)

        self.bottomframe = Frame(self)
        self.bottomframe.grid(row=3, column=1)

        #titlu+butoane
        self.titlu = Label(self.topframe, text='Type Practice', height=1, width=10)
        self.titlu.pack(pady=20, padx=(100, 90))

        self.playButton = Button(self.midframe1, text='Play', height=2, width=10, command=self.actionPlayButton)
        self.playButton.pack(pady=20, padx=(100, 90))

        self.exitButton = Button(self.midframe2, text='Exit', height=2, width=10, command=self.actionExitButton)
        self.exitButton.pack(padx=(100, 90))

        self.infoButton = Button(self.bottomframe, text='?', command=self.actionInfoButton)
        self.infoButton.pack(side=RIGHT)

    def createPlayWidgets(self):
        #impartirea in pagina
        self.playTopFrame = Frame(self)
        self.playTopFrame.grid(row=0, column=0)

        self.playMidFrame1 = Frame(self)
        self.playMidFrame1.grid(row=1, column=0)

        self.playMidFrame2 = Frame(self)
        self.playMidFrame2.grid(row=2, column=0)

        self.playMidFrame3 = Frame(self)
        self.playMidFrame3.grid(row=3, column=0)

        self.playBottomFrame = Frame(self)
        self.playBottomFrame.grid(row=4, column=0)

        #text+butoane
        self.playText = Label(self.playTopFrame, text='Choose difficulty', height=1, width=20)
        self.playText.pack(pady=20, padx=100)

        self.playEasyButton = Button(self.playMidFrame1, text='Easy', height=2, width=10, command=self.actionEasyButton)
        self.playEasyButton.pack(pady=20, padx=100)

        self.playMediumButton = Button(self.playMidFrame2, text='Medium', height=2, width=10, command=self.actionMediumButton)
        self.playMediumButton.pack(padx=100)

        self.playHardButton = Button(self.playMidFrame3, text='Hard', height=2, width=10, command=self.actionHardButton)
        self.playHardButton.pack(pady=20, padx=100)

        self.playBackButton = Button(self.playBottomFrame, text='Back', height=2, width=10, command=self.actionBackButton)
        self.playBackButton.pack(pady=20, padx=100)

    def createInfoWidgets(self):
        #impartirea in pagina
        self.infoLabelFrame = Frame(self)
        self.infoLabelFrame.grid(row=0, column=0)

        self.infoButtonFrame = Frame(self)
        self.infoButtonFrame.grid(row=1, column=0)

        #text-butoane
        self.infoLabel = Label(self.infoLabelFrame, text=
                               'Pas 1: Dati "Play"\n'
                               'Pas 2: Alegeti Dificultatea\n'
                               '\n'
                               'Trebuie sa scrieti cuvantul care apare pe ecran in timpul pe care il aveti la dispozitie\n'
                               '\n'
                               'Easy -> 10 cuvinte si 7 sec/cuvant\n'
                               'Medium -> 15 cuvinte si 5 sec/cuvant\n'
                               'Hard -> 20 cuvinte si 3 sec/cuvant'
                               )
        self.infoLabel.pack(padx=100, pady=20)

        self.infoBackButton = Button(self.infoButtonFrame, text='Back', height=2, width=10, command=self.actionBackButton)
        self.infoBackButton.pack(padx=100, pady=20)

    def createEasyWidgets(self):
        self.n = randint(0, len(self.copy_cuvinte) - 1)
        found_n = 1
        while found_n == 1:
            if self.n in self.random_numbers:
                self.n = randint(0, len(self.copy_cuvinte) - 1)
            else:
                found_n = 0
        self.random_numbers.insert(len(self.random_numbers), self.n)

        #timer
        # Timer(5.0, self.actionEnterEasy).start()
        self.easyid = self.after(1000, self.actionAfterTimeEasy)

        #impartirea in pagina
        self.pack(padx=20,pady=50)
        self.easyLabelFrame = Frame(self)
        self.easyLabelFrame.grid(row=0, column=1)

        self.easyEntryFrame = Frame(self)
        self.easyEntryFrame.grid(row=1, column=1)

        self.easyScoreFrame = Frame(self)
        self.easyScoreFrame.grid(row=2, column=0)

        self.easyTimeFrame = Frame(self)
        self.easyTimeFrame.grid(row=2, column=2)

        #label+entry
        self.easyLabel = Label(self.easyLabelFrame, text=self.copy_cuvinte[self.n])
        self.easyLabel.pack(padx=10, pady=20)

        self.easyEntry = Entry(self.easyEntryFrame)
        self.easyEntry.bind('<Return>', self.actionEnterEasy)
        self.easyEntry.pack(padx=10, pady=20)
        self.easyEntry.focus_set()

        self.easyScoreLabel = Label(self.easyScoreFrame, text="Score: "+str(self.score)+"/"+str(self.total))
        self.easyScoreLabel.pack(pady=20, side='right')

        self.easyTimeLabel = Label(self.easyTimeFrame, text="Time left: "+str(self.easyTime))
        self.easyTimeLabel.pack(pady=20, side=LEFT)

    def createMediumWidgets(self):
        self.n = randint(0, len(self.copy_cuvinte) - 1)
        found_n = 1
        while found_n == 1:
            if self.n in self.random_numbers:
                self.n = randint(0, len(self.copy_cuvinte) - 1)
            else:
                found_n = 0
        self.random_numbers.insert(len(self.random_numbers), self.n)

        # timer
        # Timer(5.0, self.actionEnterEasy).start()
        self.mediumid = self.after(1000, self.actionAfterTimeMedium)

        # impartirea in pagina
        self.pack(padx=20, pady=50)
        self.mediumLabelFrame = Frame(self)
        self.mediumLabelFrame.grid(row=0, column=1)

        self.mediumEntryFrame = Frame(self)
        self.mediumEntryFrame.grid(row=1, column=1)

        self.mediumScoreFrame = Frame(self)
        self.mediumScoreFrame.grid(row=2, column=0)

        self.mediumTimeFrame = Frame(self)
        self.mediumTimeFrame.grid(row=2, column=2)

        # label+entry
        self.mediumLabel = Label(self.mediumLabelFrame, text=self.copy_cuvinte[self.n])
        self.mediumLabel.pack(padx=10, pady=20)

        self.mediumEntry = Entry(self.mediumEntryFrame)
        self.mediumEntry.bind('<Return>', self.actionEnterMedium)
        self.mediumEntry.pack(padx=10, pady=20)
        self.mediumEntry.focus_set()

        self.mediumScoreLabel = Label(self.mediumScoreFrame, text="Score: " + str(self.score) + "/" + str(self.total))
        self.mediumScoreLabel.pack(pady=20, side='right')

        self.mediumTimeLabel = Label(self.mediumTimeFrame, text="Time left: " + str(self.mediumTime))
        self.mediumTimeLabel.pack(pady=20, side=LEFT)

    def createHardWidgets(self):
        self.n = randint(0, len(self.copy_cuvinte) - 1)
        found_n = 1
        while found_n == 1:
            if self.n in self.random_numbers:
                self.n = randint(0, len(self.copy_cuvinte) - 1)
            else:
                found_n = 0
        self.random_numbers.insert(len(self.random_numbers), self.n)

        # timer
        # Timer(5.0, self.actionEnterEasy).start()
        self.hardmid = self.after(1000, self.actionAfterTimeHard)

        # impartirea in pagina
        self.pack(padx=20, pady=50)
        self.hardLabelFrame = Frame(self)
        self.hardLabelFrame.grid(row=0, column=1)

        self.hardEntryFrame = Frame(self)
        self.hardEntryFrame.grid(row=1, column=1)

        self.hardScoreFrame = Frame(self)
        self.hardScoreFrame.grid(row=2, column=0)

        self.hardTimeFrame = Frame(self)
        self.hardTimeFrame.grid(row=2, column=2)

        # label+entry
        self.hardLabel = Label(self.hardLabelFrame, text=self.copy_cuvinte[self.n])
        self.hardLabel.pack(padx=10, pady=20)

        self.hardEntry = Entry(self.hardEntryFrame)
        self.hardEntry.bind('<Return>', self.actionEnterHard)
        self.hardEntry.pack(padx=10, pady=20)
        self.hardEntry.focus_set()

        self.hardScoreLabel = Label(self.hardScoreFrame, text="Score: " + str(self.score) + "/" + str(self.total))
        self.hardScoreLabel.pack(pady=20, side='right')

        self.hardTimeLabel = Label(self.hardTimeFrame, text="Time left: " + str(self.hardTime))
        self.hardTimeLabel.pack(pady=20, side=LEFT)

    def createFinalWidgets(self):
        self.pack(padx=100, pady=50)

        self.finalTopFrame = Frame(self)
        self.finalTopFrame.grid(row=0, column=0)

        self.finalMiddleFrame = Frame(self)
        self.finalMiddleFrame.grid(row=1, column=0)

        self.finalBottomFrame = Frame(self)
        self.finalBottomFrame.grid(row=2, column=0)

        self.finalLabel = Label(self.finalTopFrame, text='Final score')
        self.finalLabel.pack(padx=20, pady=20)

        self.finalScoreLabel = Label(self.finalMiddleFrame, text=str(self.score)+"/"+str(self.total))
        self.finalScoreLabel.pack(padx=20, pady=20)

        self.finalButton = Button(self.finalBottomFrame, text="Back", command=self.actionBackButton)
        self.finalButton.pack(padx=20, pady=20)


app = Application()
app.master.title('Typing Practice')
app.master.resizable(False, False)
app.mainloop()