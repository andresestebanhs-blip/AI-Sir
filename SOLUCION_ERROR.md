# 🛑 ERROR DETECTADO: Python no instalado o no configurado

El error que ves (`'pip' no se reconoce...`) ocurre porque tu computadora no sabe dónde está instalado Python. Aunque tengas archivos `.py`, el sistema "global" no tiene acceso al comando `python` ni `pip`.

## ✅ SOLUCIÓN RÁPIDA

1.  **Descargar Python**:
    Ve a [python.org/downloads](https://www.python.org/downloads/) y descarga la última versión.

2.  **INSTALACIÓN (¡MUY IMPORTANTE!)**:
    Al ejecutar el instalador, verás una casilla abajo que dice:
    **[X] Add python.exe to PATH**
    **TIENES QUE MARCARLA.** Si no la marcas, seguirá fallando.

3.  **Finalizar**:
    Dale a "Install Now" y espera a que termine.

4.  **REINICIAR TERMINAL**:
    Cierra esa ventana negra de comandos (CMD) y abre una nueva.

5.  **Verificar**:
    Escribe `python --version`. Si sale algo como `Python 3.12.x`, ¡ya funciona!

## 🚀 Poner en marcha la IA

Una vez arreglado lo anterior, ejecuta estos comandos en orden en tu nueva terminal:

1.  **Instalar librerías**:
    ```cmd
    pip install Flask torch
    ```

2.  **Entrenar el cerebro (con los nuevos datos expertos)**:
    ```cmd
    python train.py
    ```

3.  **Iniciar la Web**:
    ```cmd
    python app.py
    ```
