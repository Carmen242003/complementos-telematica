# complementos-telematica
## Analizador de latencia y jitter de red

**Autora:** Carmen Lucía Espinar Sánchez

## Cómo lo hice con GitHub Copilot
**Prompt utilizado:** `"Crea un script sencillo en Python sin librerías externas que analice una lista de tiempos de ping en milisegundos, calcule la latencia mínima, máxima, media y el jitter medio entre valores consecutivos, y cuente cuántas muestras superan un umbral de 100 ms mostrando un mensaje por consola."` (indicándole después la lista `[18, 22, 19, 145, 21, 20, 110, 17]`). 

**Modificaciones realizadas:** Añadí al final del script un bloque condicional `if sobre_umbral > 0:` / `else:` para avisar por consola de que se han detectado picos de latencia altos cuando supera el umbral o indicar que la conexión es estable sin picos altos.

## Cómo se ejecuta
Asegúrate de tener Python 3 instalado, abre una terminal en la carpeta donde esté el archivo y ejecuta:

```bash
python latencia_red.py
```
