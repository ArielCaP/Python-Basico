# Juego: Adivina el Número 🎲

El programa genera un número secreto al azar entre 1 y 100, y el usuario debe adivinarlo. Después de cada intento, se le indica si el número fue muy alto o muy bajo, hasta que acierte.

## 🎯 ¿Qué hace?

1. Genera un número aleatorio entre 1 y 100
2. El usuario intenta adivinarlo
3. Le indica si su intento fue "muy alto" o "muy bajo"
4. Al acertar, muestra cuántos intentos usó

## 📚 Lo que aprendí

- Módulo `random` para generar números al azar
- Bucles `while` para repetir código
- La instrucción `break` para detener un bucle
- Contadores (variables que van sumando)

## 🎲 Sobre la librería `random`

`random` es un módulo que viene incluido en Python (no hay que instalarlo aparte) y sirve para generar valores al azar, simulando el "azar" dentro de un programa.

### ¿Para qué se usa normalmente?

- **Juegos** 🎮 — tirar un dado, barajar cartas, generar eventos al azar
- **Simulaciones y pruebas** 🧪 — generar datos de prueba falsos, simular situaciones del mundo real
- **Sorteos y decisiones** 🎁 — elegir un ganador al azar, mezclar el orden de una lista
- **Arte y música generativa** 🎨 — crear patrones o sonidos que varían cada ejecución

### Funciones útiles del módulo

| Función | Qué hace |
|---|---|
| `random.randint(1, 100)` | Número entero al azar entre 1 y 100 |
| `random.choice(["rojo", "azul", "verde"])` | Elige un elemento al azar de una lista |
| `random.shuffle(mi_lista)` | Revuelve el orden de una lista (como barajar cartas) |
| `random.random()` | Número decimal al azar entre 0 y 1 |

## 🚀 Cómo ejecutarlo

```
python adivina_numero.py
```
