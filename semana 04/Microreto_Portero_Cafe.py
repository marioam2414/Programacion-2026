"""Microreto: el portero del café."""

print("Bienvenido al café")

energia = int(input("¿Cuánta energía tienes del 0 al 100?: "))
cafe = input("¿Traes café? Escribe si o no: ").lower().strip()

if energia < 30 and cafe == "no":
    print("No puedes entrar, necesitas descansar o traer café.")

elif energia >= 30 or cafe == "si":
    print("Puedes entrar, ¡bienvenido!")

else:
    print("Respuesta no válida, intenta de nuevo.")
