import PySimpleGUI as sg    # importing pysimplegui
sg.theme("green")
# Content to be displayed in the window
layout=[[sg.Text("Divisibility Checker\n\n",font=('blue',50),justification="Center",size=(22,1),text_color="Darkgreen")],
        [sg.Text("\n\nThis program is made to check the divisibility of a number",font=("",25),size=(250,5),auto_size_text=True,justification="center",text_color="black")],
        [sg.Text("\n\nEnter the number to be checked:  ",font=("",18),size=(40,5),auto_size_text=True,justification="right"),sg.Input(key="inp1",do_not_clear=False,focus=True),sg.Text(" "),sg.Button("Enter",image_filename="Button image.png",font=("",18),auto_size_button=True,key="k")],
        [sg.Text("\t\t\t\t"),sg.Checkbox("Check divisibility by 2",key="check",font=("",18),size=(40,5)),sg.Checkbox("Check divisibility by 3",key="check1",font=("",18),size=(40,5))],
        [sg.Text("\t\t\t\t"),sg.Checkbox("Check divisibility by 5",key="check2",font=("",18),size=(40,5)),sg.Checkbox("Display all factors of the number",key="check3",font=("",18),size=(40,5))]]
# Creating window
window=sg.Window('Divisibility',layout,size=(1300,800),return_keyboard_events=True)
while True:     # event loop
    e,v=window.read()
    if e is None:
        break
    if e=="k" or e=="\r":
        try:
            inp = int(v['inp1'])
        except:
            inp1 = "Unkown Text"
            window.FindElement('inp1').update(inp1)
            continue
        result2 = ""
        result1 = ""
        result = ""
        result3 = ""
        if v['check'] == True:
            if inp % 2 == 0:
                result = "Divisible by 2"
            else:
                result = "Not Divisible by 2"
        if v['check1'] == True:
            if inp % 3 == 0:
                result1 = "Divisible by 3"
            else:
                result1 = "Not Divisible by 3"
        if v['check2'] == True:
            if inp % 5 == 0:
                result2 = "Divisible by 5"
            else:
                result2 = "Not Divisible by 5"
        if v['check3'] == True:
            lst = []
            for i in range(2, inp//2):
                if inp % i == 0:
                    lst.append(i)
            result3 = ",".join([str(v) for v in lst])
            if result3 == "":
                result3="It is a prime number"
        sg.popup(result + "\n" + result1 + "\n" + result2 + "\n" + result3, font=("", 20),any_key_closes=True,title="Final result")
