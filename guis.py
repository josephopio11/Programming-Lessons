from guizero import App, Text, TextBox, PushButton

def add():
    num1 = int(enter_num1.value)
    num2 = int(enter_num2.value)
    answer = num1 + num2
    display_answer.value = answer


def subtract():
    num1 = int(enter_num1.value)
    num2 = int(enter_num2.value)
    answer = num1 - num2
    display_answer.value = answer

def multiply():
    num1 = int(enter_num1.value)
    num2 = int(enter_num2.value)
    answer = num1 * num2
    display_answer.value = answer

def divide():
    num1 = int(enter_num1.value)
    num2 = int(enter_num2.value)
    answer = num1 / num2
    display_answer.value = answer


app = App(title="Add two numbers")

instruction = Text(app, "Enter a number")
enter_num1 = TextBox(app)

instruction2 = Text(app, "Enter another number")
enter_num2 = TextBox(app)

display_answer = Text(app, "Answer")

display_number = PushButton(app,command=add, text="Add")
display_number = PushButton(app,command=subtract, text="Subtract")
display_number = PushButton(app,command=multiply, text="Multiply")
display_number = PushButton(app,command=divide, text="Divide")
app.display()