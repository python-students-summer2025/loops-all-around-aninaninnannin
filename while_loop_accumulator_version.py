def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
            print("Please enter a number ≥1")
        except ValueError:
            print("Please enter a valid number")

def sing(bottles):
    current = bottles
    while current > 0:
        if current > 1:
            print(f"{current} bottles of beer on the wall, {current} bottles of beer.")
            if current-1 > 1:
                print(f"Take one down, pass it around, {current-1} bottles of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, 1 bottle of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        current -= 1