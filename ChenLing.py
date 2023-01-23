import math

code = True
n = True
repeat = True
h = True
w = True
walls = 0
count = 0
height = 0
width = 0
area = 0
ta = 0
price = 0
des = ""

print("Tile Description & Price per Box:")
print("001 | Small Black Granite      $19.50")
print("002 | Small Grey Marble        $25.95")
print("003 | Small Powder Blue        $35.75")
print("004 | Medium Sunset Yellow     $13.50")
print("005 | Medium Berry Red         $11.00")
print("006 | Medium Glitter Purple    $52.95")
print("007 | Large Oak Wood Effect    $65.00")
print("008 | Large Black Granite      $58.98")
print("009 | Large Bamboo Effect      $85.00")
print("010 | Extra-Large White Marble $62.75")

tile = input("\nEnter the code for the tile: ")

while code:
    if tile == "001" or tile == "002" or tile == "003" or tile == "004" or tile == "005" or tile == "006" or tile == "007" or tile == "008" or tile == "009" or tile == "010":
        code = False
        if tile == "001":
            des = "Small Black Granite"
            price = 19.5
        elif tile == "002":
            des = "Small Grey Marble"
            price = 25.95
        elif tile == "003":
            des = "Small Powder Blue"
            price = 35.75
        elif tile == "004":
            des = "Medium Sunset Yellow"
            price = 12.5
        elif tile == "005":
            des = "Medium Berry Red"
            price = 11
        elif tile == "006":
            des = "Medium Glitter Purple"
            price = 52.95
        elif tile == "007":
            des = "Large Oak Wood Effect"
            price = 65
        elif tile == "008":
            des = "Large Black Granite"
            price = 58.98
        elif tile == "009":
            des = "Large Bamboo Effect"
            price = 85
        else:
            des = "Extra-Large White Marble"
            price = 62.75
    else:
        tile = input("ERROR\nEnter the code for the tile: ")

print("")

while n:
    try:
        walls = int(input("Enter the number of walls to be tiled: "))
        n = False
    except ValueError:
        print("ERROR")

print("")

while repeat:
    while h:
        try:
            height = float(input("Enter the height of the wall (m): "))
            h = False
        except ValueError:
            print("ERROR")
    while w:
        try:
            width = float(input("Enter the width of the wall (m): "))
            w = False
            count = count + 1
            area = height * width
            ta = round(ta + area, 5)
            print("")
        except ValueError:
            print("ERROR")
    if count == walls:
        repeat = False
    else:
        h = True
        w = True

waste = int(input("Enter the percentage of estimated wastage: "))

taw = round((ta * waste / 100) + ta, 5)
box = math.ceil(taw)
cost = round(price * box, 6)

print("\nTile description:", des)
print("Total area to be tiled:", ta)
print("+ Estimated wastage:", taw)
print("Number of boxes of tiles required:", box)
print(f"Total cost: ${cost}")
