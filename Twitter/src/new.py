import Tkinter
window = Tkinter.Tk()
window.configure(background="#a1dbcd")
window.title("Sentiment Predictor")
window.geometry("500x500")


def OnButtonClick():
    labelVariable.set("Button Clicked!")         
    entryLabel.focus_set()
    entryLabel.selection_range(0, Tkinter.END)

def OnPressEnter(event):
    labelVariable.set( "Enter Pressed!" )
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