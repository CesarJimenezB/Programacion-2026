energia = int(input("¿Cuánta energía tienes de 0-100?: "))
trae_cafe = input("¿Traes café? (si/no): ").lower().strip() == "si"

mensaje = "Completa las reglas del portero."

# Menos de 30 de energía y no trae café
if energia < 30 and not trae_cafe:
    mensaje = "❌ No puedes pasar: tienes poca energía y no traes café."

# Energía suficiente o trae café
elif energia >= 30 or trae_cafe:
    mensaje = "✅ Puedes pasar. Bienvenido."

print(mensaje)
