

nombre = input("Nombre: ").upper().strip()
kit = input("Tipo de kit: ").lower().strip()
autorizacion = input("¿Tiene autorización (si/no)?: ").lower().strip() == 'si'
try:
    cantidad = int(input("¿Cantidad de kits?: "))
    print("Cantidad registrada:", cantidad)
except ValueError:
    print("Error: escribe la cantidad con números, por ejemplo 3.")
    cantidad = -1
    
try:
    dias = int(input("¿Cantidad de dias?: "))
except ValueError:
    print("Error: escribe la cantidad con números, por ejemplo 3.")
    cantidad = -1
    
if not nombre or not kit or cantidad < 1:
    resultado = "registro rechazado: revise!"
elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = "solucitud aprobada para {nombre}: {cantidad} kit(s) de"
else:
    resultado = "resultado enviada a revision"
print("-" * 50,'\n')
print(resultado)


