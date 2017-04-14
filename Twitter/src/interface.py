import Tkinter
import svm
window = Tkinter.Tk()
window.configure(background="#a1dbcd")
window.title("Sentiment Predictor")
window.geometry("400x400")


def OnButtonClick():
    def numbers_to_strings(argument):
        switcher = {
            4: "Positive",
            2: "Neutral",
            0: "Negative",
            }
        return switcher.get(argument, "nothing")
    str = entryVariable.get()
    if not str:
        labelVariable.set("Cannot Predict Sentiment Of Blank Spaces. Please Enter Text")
    else:
        labelVariable.set( numbers_to_strings(int(svm.predict(str,svm.MODEL))) )         
    entryLabel.focus_set()
    entryLabel.selection_range(0, Tkinter.END)

def OnPressEnter(event):
    def numbers_to_strings(argument):
        switcher = {
            4: "Positive",
            2: "Neutral",
            0: "Negative",
            }
        return switcher.get(argument, "nothing")
    str = entryVariable.get()
    if not str:
        labelVariable.set("Cannot Predict Sentiment Of Blank Spaces. Please Enter Text")
    else:
        labelVariable.set( numbers_to_strings(int(svm.predict(str,svm.MODEL))) )    
    entryLabel.focus_set()
    entryLabel.selection_range(0, Tkinter.END)
    

label = Tkinter.Label(window, text = "Enter Tweet to predicts its Sentiment: ", fg = "#383a39", bg = "#a1dbcd")
label.pack(pady = 10)

entryVariable = Tkinter.StringVar()
entryLabel = Tkinter.Entry(window, textvariable= entryVariable)
entryLabel.bind("<Return>", OnPressEnter)
entryLabel.pack(pady = 10, ipadx= 100, ipady =20)

btn = Tkinter.Button(window, text="Predict", fg = "#383a39", bg = "green", command= OnButtonClick)
btn.pack(pady = 10)

labelVariable = Tkinter.StringVar()
label2 = Tkinter.Label(window, text = "Sentiment : ", fg = "#383a39", bg = "#a1dbcd", textvariable=labelVariable)
label2.pack(pady = 10)

window.mainloop()