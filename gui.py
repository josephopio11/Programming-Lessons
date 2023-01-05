from guizero import App, Text, TextBox, PushButton

def addition():
    num1 = int(enter_num1.value)
    num2 = int(enter_num2.value)
    ans = num1 + num2
    answer.value = ans

def subtraction():
    num1 = int(enter_num1.value)
    num2 = int(enter_num2.value)
    ans = num1 - num2
    answer.value = ans

def multiplication():
    num1 = int(enter_num1.value)
    num2 = int(enter_num2.value)
    ans = num1 * num2
    answer.value = ans

def division():
    num1 = int(enter_num1.value)
    num2 = int(enter_num2.value)
    ans = num1 / num2
    answer.value = ans


app = App(title="My Calculator")
instruction = Text(app, "Enter your first number")
enter_num1 = TextBox(app)
instruction2 = Text(app, "Enter your second number")
enter_num2 = TextBox(app)

answer = Text(app, "Answer")

display_number = PushButton(app,command=addition, text="Add")
display_number = PushButton(app,command=subtraction, text="Subtract")
display_number = PushButton(app,command=multiplication, text="Multiply")
display_number = PushButton(app,command=division, text="Divide")

app.display()