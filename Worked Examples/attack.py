from guizero import App, Box, Text, TextBox, Picture, PushButton, Window
from tkinter import Message

tx_colour = "#ffffff"
font_type = "Verdana"

app = App(bg="#b566ff", title="Which rockstar are you?")
question_window = Window(app, title="Questions", bg="#b566ff")
question_window.hide()

end_window = Window(app, title="End", bg="#000000")
end_window.hide()


def q_window():
    question_window.show(wait=True)


def e_window():
    question_window.hide()
    end_window.show(wait=True)


# Intro page

title_box = Box(app, width="fill", align="top", border=False, height=80)
Text(title_box, text="Which rockstar are you?", font=font_type, size=25, color=tx_colour)

content_box = Box(app, layout="grid", width="fill")

guitarist_image = Picture(content_box, image="guitarist.png", grid=[0, 0, 1, 2], height=300, width=200)
text_content_box = Box(content_box, grid=[1, 0, 2, 1])
intro_text = Message(text_content_box.tk,
                     text="Hey Dude, wanna find out what your Rockstar name is?\n\nClick the start button below, "
                          "answer me a few questions and I'll tell you what your Rockstar name is!")
intro_text.config(bg='#b566ff', font=('Verana', 12), width=300, foreground="#ffffff")
intro_text.pack()
button = PushButton(content_box, text="start", command=q_window, grid=[2, 1, 2, 1])

# Questions page
q_title_box = Box(question_window, width="fill", align="top", border=False, height=80)
Text(q_title_box, text="Answer the questions below", font=font_type, size=25, color=tx_colour)

questions_box = Box(question_window, layout="grid", width="fill")

name_label = Text(questions_box, text="Name", grid=[0, 0], align="left", color=tx_colour, font=font_type)
name = TextBox(questions_box, grid=[1, 0])
band_label = Text(questions_box, text="Who is your favourite band or artist?", grid=[0, 1], align="left",
                  color=tx_colour, font=font_type)
band = TextBox(questions_box, grid=[1, 1])
dob_label = Text(questions_box, text="What is your date of birth?", grid=[0, 2], align="left", color=tx_colour,
                 font=font_type)
dob = TextBox(questions_box, grid=[1, 2])
pet_label = Text(questions_box, text="What was the name of your first pet?", grid=[0, 3], align="left", color=tx_colour,
                 font=font_type)
pet = TextBox(questions_box, grid=[1, 3])
maiden_label = Text(questions_box, text="What is your mothers maiden name?", grid=[0, 4], align="left", color=tx_colour,
                    font=font_type)
maiden = TextBox(questions_box, grid=[1, 4])

finish_button = PushButton(questions_box, text="Submit", command=e_window, grid=[0, 5, 2, 1], align="left")

# End page

e_title_box = Box(end_window, width="fill", align="top", border=False, height=80)
Text(e_title_box, text="STOP AND THINK", font=font_type, size=25, color=tx_colour)
guitarist_image = Picture(end_window, image="end_image.png", height=100, width=200)

end_text_content_box = Box(end_window, border=False, width="fill")
end_text = Message(end_text_content_box.tk,
                   text="You freely shared your personal data with us. Just think what a cyber criminal could do with "
                        "this data!\n\nDisclaimer: This program aims to highlight the dangers of freely submitting "
                        "your personal data. None of your personal data has been stored by this program.")
end_text.config(bg='#000000', font=('Verana', 12), width=300, foreground="#ffffff")
end_text.pack()

app.display()
