import Tkinter
import svm
class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter Tweet: ")
        
        button = Tkinter.Button(self,text=u"Predict",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = Tkinter.StringVar()

        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue", width=200)
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Predicted Sentiment ! ")
        

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry("500x500")       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
            
    def OnButtonClick(self):
        def numbers_to_strings(argument):
            switcher = {
                4: "Positive",
                2: "Neutral",
                0: "Negative",
                }
            return switcher.get(argument, "nothing")
        self.labelVariable.set( numbers_to_strings(int(svm.predict(self.entryVariable.get(),svm.MODEL))) )         
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        def numbers_to_strings(argument):
            switcher = {
                4: "Positive",
                2: "Neutral",
                0: "Negative",
                }
            return switcher.get(argument, "nothing")
        self.labelVariable.set( numbers_to_strings(int(svm.predict(self.entryVariable.get(),svm.MODEL))) )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Sentiment Predictor')
    app.mainloop()
