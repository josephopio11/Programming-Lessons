from guizero import App, PushButton, ButtonGroup, Text, TextBox, Window
import math

def result():
    if tile2.value == "001 | Small Black Granite           $19.50":
        price = 19.5
    elif tile2.value == "002 | Small Grey Marble             $25.95":
        price = 25.95
    elif tile2.value == "003 | Small Powder Blue             $35.75":
        price = 35.75
    elif tile2.value == "004 | Medium Sunset Yellow     $13.50":
        price = 13.5
    elif tile2.value == "005 | Medium Berry Red             $11.00":
        price = 11
    elif tile2.value == "006 | Medium Glitter Purple       $52.95":
        price = 52.95
    elif tile2.value == "007 | Large Oak Wood Effect     $65.00":
        price = 65
    elif tile2.value == "008 | Large Black Granite            $58.98":
        price = 58.98
    elif tile2.value == "009 | Large Bamboo Effect         $85.00":
        price = 85
    else:
        price = 62.75
    window.show()
    display2.value = tile2.value
    display4.value = round(float(height2.value) * float(width2.value), 2)
    display6.value = round((float(waste2.value) * float(display4.value) / 100) + float(display4.value), 2)
    display8.value = math.ceil(float(display6.value))
    display10.value = round(price * float(display8.value), 6)

app = App(title="Tile Price Calculator")
window = Window(app, title="Result")
window.hide()
tile1 = Text(app, text="Tile Description & Price per Box:")
tile2 = ButtonGroup(app, options=["001 | Small Black Granite           $19.50", "002 | Small Grey Marble             $25.95", "003 | Small Powder Blue             $35.75", "004 | Medium Sunset Yellow     $13.50", "005 | Medium Berry Red             $11.00", "006 | Medium Glitter Purple       $52.95", "007 | Large Oak Wood Effect     $65.00", "008 | Large Black Granite            $58.98", "009 | Large Bamboo Effect         $85.00", "010 | Extra-Large White Marble $62.75"], selected="001 | Small Black Granite           $19.50")
height1 = Text(app, text="\nEnter the height of the wall (m):")
height2 = TextBox(app)
width1 = Text(app, text="\nEnter the width of the wall (m):")
width2 = TextBox(app)
waste1 = Text(app, text="\nEnter the percentage of estimated wastage:")
waste2 = TextBox(app)
space = Text(app)
show = PushButton(app, command=result, text="Calculate")
display1 = Text(window, text="\nTile description:")
display2 = Text(window)
display3 = Text(window, text="\nTotal area to be tiled (m3):")
display4 = Text(window)
display5 = Text(window, text="\n+ Estimated wastage (m3):")
display6 = Text(window)
display7 = Text(window, text="\nNumber of boxes of tiles required:")
display8 = Text(window)
display9 = Text(window, text="\nTotal cost ($):")
display10 = Text(window)
app.display()