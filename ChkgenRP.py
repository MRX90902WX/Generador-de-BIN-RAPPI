from os import system
system("clear")

print("\033[1;35m    ____  _____   __      ___    ____  ______")
print("   / __ )/  _/ | / /     /   |  / __ \/ ____/")
print("  / __  |/ //  |/ /_____/ /| | / /_/ / / __")
print(" / /_/ // // /|  /_____/ ___ |/ _, _/ /_/ /")
print("/_____/___/_/ |_/     /_/  |_/_/ |_|\____/")
print("")
print("\033[1;33m :D     :D     :D     :D     :D     :D")
print("")
print(" #1. CHecK (°1)")
print(" #2. CHecK (°2)")
print("") 
main = input(" \033[1;32m----> ")
print("")

if main == "1":
   system("python chk1.py")
elif main == "2":
   system("python chk2.py")
else:
   print("\033[1;34m[X]\033[1;31mOPCIÓN INCORRECTA")

