nombre = input("Nombre: ").strip()
autorizado = input("¿Está autorizado? (si/no): ").strip().lower()

try:
    cantidad = int(input("Cantidad de kits: "))
    dias = int(input("Cantidad de días: "))
except ValueError:
    cantidad = dias = -1

if not nombre or cantidad < 0 or dias < 0:
    print("❌ Rechazo: nombre vacío o datos numéricos inválidos.")
elif autorizado == "si" and cantidad <= 3 and dias <= 7:
    print("✅ Aprobación.")
elif cantidad > 3 or dias > 7:
    print("⚠️ Enviar a revisión.")
else:
    print("❌ Rechazo.")