# app to sing the song "99 bottles of beer on the wall"

b = 99

while b > 1:
    print(f"{b} bottles of beer on the wall, {b} bottles of beer")
    print("take one down and pass it around")
    b -= 1
    print(f"{b} bottles of beer on the wall")
if b == 1:
    print(f"{b} bottle of beer on the wall, {b} bottle of beer")
    print("take it down and pass it around")
    print("No more bottles of beer on the wall!")
else:
    print("No more beer")
