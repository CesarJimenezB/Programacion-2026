# Validador de compra con descuento

cliente = input("Ingrese el nombre del cliente: ")

try:
    monto = float(input("Ingrese el monto de la compra: ₡"))
    
    frecuente = input("¿Es cliente frecuente? (si/no): ").lower()

    # Reglas de descuento:
    # 15% si es cliente frecuente y compra >= 100
    # 5% si cumple solo una de las condiciones
    # 0% en los demás casos

    if frecuente == "si" and monto >= 100:
        descuento_pct = 15
    elif frecuente == "si" or monto >= 100:
        descuento_pct = 5
    else:
        descuento_pct = 0

    descuento = monto * (descuento_pct / 100)
    total_pagar = monto - descuento

    print(f"\nCliente: {cliente}")
    print(f"Monto de compra: ₡{monto:.2f}")
    print(f"Descuento aplicado: {descuento_pct}%")
    print(f"Descuento: ₡{descuento:.2f}")
    print(f"Total a pagar: ₡{total_pagar:.2f}")

except ValueError:
    print("Error: Debe ingresar un número válido para el monto.")