# complementos-telematica
## Analizador de latencia y jitter de red

**Autora:** Carmen Lucía Espinar Sánchez

## Qué hace el script
El programa `latencia_red.py` analiza una lista de tiempos de respuesta (ping) en milisegundos (`[18, 22, 19, 145, 21, 20, 110, 17]`) y calcula la latencia mínima, máxima y media, el jitter medio entre muestras consecutivas y cuántas medidas superan un umbral de `100 ms`, mostrando además un aviso final si detecta picos de latencia altos.

## Cómo lo hice con GitHub Copilot
- **Prompt utilizado:** `"Crea un script sencillo en Python sin librerías externas que analice una lista de tiempos de ping en milisegundos, calcule la latencia mínima, máxima, media y el jitter medio entre valores consecutivos, y cuente cuántas muestras superan un umbral de 100 ms mostrando un mensaje por consola."`
- **Modificaciones realizadas:**
  - Sustituí los valores de ejemplo que me generó Copilot inicialmente (`[24.5, 31.2, 28.7, 105.3, 42.1]`) por una lista propia de tiempos de ping (`[18, 22, 19, 145, 21, 20, 110, 17]`) para probar distintos picos por encima del umbral.
  - Añadí manualmente al final del script un bloque condicional `if sobre_umbral > 0:` / `else:` para avisar por consola de que se han detectado picos de latencia altos cuando supera el umbral o indicar que la conexión es estable sin picos altos.

## Cómo se ejecuta
Asegúrate de tener Python 3 instalado, abre una terminal en la carpeta donde esté el archivo y ejecuta:

```bash
python latencia_red.py
