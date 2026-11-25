tiempos_ping_ms = [18, 22, 19, 145, 21, 20, 110, 17]
umbral_ms = 100

minimo = min(tiempos_ping_ms)
maximo = max(tiempos_ping_ms)
media = sum(tiempos_ping_ms) / len(tiempos_ping_ms)

diferencias = [
    abs(tiempos_ping_ms[i] - tiempos_ping_ms[i - 1])
    for i in range(1, len(tiempos_ping_ms))
]
jitter_medio = sum(diferencias) / len(diferencias)
sobre_umbral = sum(1 for tiempo in tiempos_ping_ms if tiempo > umbral_ms)

print(f"Latencia mínima: {minimo:.2f} ms")
print(f"Latencia máxima: {maximo:.2f} ms")
print(f"Latencia media: {media:.2f} ms")
print(f"Jitter medio: {jitter_medio:.2f} ms")
print(f"Muestras superiores a {umbral_ms} ms: {sobre_umbral}")

if sobre_umbral > 0:
    print("Aviso: se detectaron picos de latencia altos.")
else:
    print("Conexión estable sin picos altos.")