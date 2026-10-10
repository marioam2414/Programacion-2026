"""Microreto: el portero del café."""

nombre = input ("como te llamas?: ").upper().strip()
energia = int(input("cuanta energia tienes de 0 a 100?:")) == 'si'

mensaje = ''

#si vengo con menos del 50% del cafe y no tengo cafe mandarme a descansar
if energia < 50 and not (trae_cafe): #trae_cafe == false
    mensaje = "Vete a descansar"
    
#si vengo con el 50% del cafe me da el acceso a la clase me va a dejar entrar a la clase
elif energia >= 50 or trae_cafe:
    mensaje = "Acceso permitido, puedes entrar a la clase."
    
#cualquier otro caso: portero confundido: revisar respuestas
else:
    mensaje = "Portero confundido, revisa las respuestas."
    
print(f"{nombre}: {mensaje}")