from datetime import datetime
import os


def today():
	oggi = str(datetime.today()).split(" ")[0]
	y,m,d = oggi.split("-")
	return f"{d}/{m}/{y}"

def write(file, text):
	print(os.getcwd())
	with open(file, "a") as f:
		print(text, file=f)
	os.startfile(file)

if __name__ == "__main__":
	todo = input("Add to todo> ")
	write("todo.txt", today() + " " + todo)