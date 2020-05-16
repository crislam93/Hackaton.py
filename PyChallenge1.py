import random                               
options = ["piedra", "papel", "tijera"]     
play_again = "s"
user_choice = ""

while play_again == "s":
    computer_choice = random.choice(options) #elección automática de la computadora 
    user_input = str(input("Elige ==> Piedra[r], Papel[p], Tijera[t]: ")).lower()
    
    #Piedra[r]  <=== por rock
    #asocia el input a la opción que corresponda [piedra, papel o tijera]
    if user_input == "r" or user_input == "piedra":
        user_choice = options[0]
    elif user_input == "p" or user_input == "papel":
        user_choice = options[1]
    elif user_input == "t" or user_input == "tijera":
        user_choice = options[2]
    else: 
        user_input = False
        print("Opción inválida...")
      
    while user_input != False:
        #Compara tu elección vs la de la computadora
        if user_choice == computer_choice:
            print("Elegiste: {} vs Computadora: {} || Empate!!".format(user_choice,computer_choice))
        elif user_choice == options[0] and computer_choice == options[2]:
            print("Elegiste: {} vs Computadora: {} || Ganaste!!".format(user_choice, computer_choice))
        elif user_choice == options[1] and computer_choice == options[0]:
            print("Elegiste: {} vs Computadora: {} || Ganaste!!".format(user_choice, computer_choice))
        elif user_choice == options[2] and computer_choice == options[1]:
            print("Elegiste: {} vs Computadora: {} || Ganaste!!".format(user_choice, computer_choice))
        else: print("Elegiste: {} vs Computadora: {} || Perdiste!!".format(user_choice, computer_choice))
        break
     
    #Pregunta si quieres jugar de nuevo
    play_again = input("Quieres jugar de nuevo: s/n ").lower()
    if play_again != "s":
        print("Bye!")
        break