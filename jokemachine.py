from guizero import App, Text, ButtonGroup, PushButton

def jokes():
    if joke_choice.value == "Stick":
        display_joke.value = "What is brown and sticky? A stick"
    elif joke_choice.value == "Fluff":
        display_joke.value = "What is pink and fluffy? Pink Fluff"
    elif joke_choice.value == "Chicken":
        display_joke.value = "Why did the chicken cross the road? To buy some toilet paper"
    elif joke_choice.value == "Frog":
        display_joke.value = "What happens to a frog's car when it breaks down? it gets toad away"

app = App()

instruction = Text(app, text="Please choose a joke from the list below")
joke_choice = ButtonGroup(app, options=["Stick", "Fluff", "Chicken", "Frog"], selected="Stick")
joke_button = PushButton(app, command=jokes, text="Show Joke")
display_joke = Text(app, text="... waiting for joke")

app.display()

