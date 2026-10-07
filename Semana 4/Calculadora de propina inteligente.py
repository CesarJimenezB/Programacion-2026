# Calculadora de propina inteligente

total_cuenta = float(input("Ingrese el total de la cuenta: $"))
porcentaje_propina = float(input("Ingrese el porcentaje de propina (%): "))

propina = total_cuenta * (porcentaje_propina / 100)
total_final = total_cuenta + propina

print(f"\nTotal de la cuenta: ${total_cuenta:.2f}")
print(f"Propina ({porcentaje_propina}%): ${propina:.2f}")
print(f"Total a pagar: ${total_final:.2f}")
