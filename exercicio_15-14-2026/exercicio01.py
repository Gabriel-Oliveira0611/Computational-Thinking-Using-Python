maca = int(input("Insira quantas maças foram vendidas: "))
bananas = int(input("Insira quantas bananas foram vendidas: "))

if maca > bananas: {

print(f"""
-> O número de maçãs vendidas foi de: {maca}.
-> O número de bananas vendidas foi de: {bananas}.
--> Logo, foram vendidas mais maças do que bananas.
      """)
}
elif maca < bananas: {

    print(f"""
-> O número de maçãs vendidas foi de: {maca}.
-> O número de bananas vendidas foi de: {bananas}.
--> Logo, foram vendidas mais bananas do que maçãs.
      """)
}
else :{
    
    print("Houve um empate.")
}