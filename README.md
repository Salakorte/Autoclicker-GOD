🖱️ AutoClicker Avanzado con Interfaz Gráfica (Python)
🇪🇸 Español

Un autoclicker y autopulsador de teclas totalmente configurable, creado en Python con interfaz Tkinter, pensado para ser ligero, intuitivo y compatible con juegos o aplicaciones en segundo plano.

🚀 Características principales

🖱️ Clics automáticos (izquierdo o derecho)

⌨️ Pulsación automática de teclas configurable

⏱️ Control de velocidad por intervalo o CPS (clics por segundo)

🔁 Dos modos de activación:

Activar/Desactivar con una tecla (toggle)

Mientras mantienes la tecla presionada (hold)

🎯 Hotkey global personalizable (funciona aunque la ventana esté minimizada)

🧩 Interfaz limpia y ligera, sin dependencias externas complejas

🪟 Ejecutable independiente (.exe) creado con PyInstaller

🧠 Tecnologías utilizadas

Python 3.10+

Tkinter → interfaz gráfica

pynput → control del teclado y ratón

threading → ejecución paralela sin bloquear la interfaz

⚙️ Instalación y ejecución
Opción 1 — Ejecutar desde código fuente
git clone https://github.com/tuusuario/autoclicker-avanzado.git
cd autoclicker-avanzado
pip install pynput
python autoclicker.py

Opción 2 — Ejecutar versión compilada

Si usas Windows, simplemente abre el archivo:

AutoClicker.exe


No requiere instalación ni Python.

🧩 Compilar a ejecutable (.exe)

Para crear tu propio .exe sin consola visible:

pip install pyinstaller
pyinstaller --noconsole --onefile autoclicker.py


El ejecutable aparecerá en la carpeta dist/.

🖼️ Interfaz

Selección de acción (clic o tecla)

Campo para elegir la tecla a pulsar

Ajuste del intervalo o CPS

Selector de modo de activación

Campo para configurar la hotkey

Botones para iniciar/detener manualmente

Estado visual de ejecución (“Activo” / “Inactivo”)

🛡️ Seguridad

Incluye control por hotkey global y soporte para detener manualmente desde la interfaz.

🧑‍💻 Desarrollado por

Alex Villen
📦 GitHub

🇬🇧 English

A fully configurable autoclicker and auto key presser, built in Python with a Tkinter GUI, designed to be lightweight, intuitive, and compatible with games or background applications.

🚀 Main Features

🖱️ Automatic mouse clicks (left or right)

⌨️ Configurable automatic key pressing

⏱️ Speed control by interval or CPS (clicks per second)

🔁 Two activation modes:

Activate/Deactivate with a key (toggle)

While holding the key (hold)

🎯 Customizable global hotkey (works even if the window is minimized)

🧩 Clean and lightweight interface, no complex external dependencies

🪟 Standalone executable (.exe) created with PyInstaller

🧠 Technologies Used

Python 3.10+

Tkinter → GUI

pynput → keyboard & mouse control

threading → parallel execution without blocking GUI

⚙️ Installation & Usage
Option 1 — Run from source
git clone https://github.com/tuusuario/autoclicker-avanzado.git
cd autoclicker-avanzado
pip install pynput
python autoclicker.py

Option 2 — Run compiled version

If you are on Windows, just open the file:

AutoClicker.exe


No installation or Python required.

🧩 Compile to executable (.exe)

To create your own .exe without a console:

pip install pyinstaller
pyinstaller --noconsole --onefile autoclicker.py


The executable will appear in the dist/ folder.

🖼️ Interface

Action selection (click or key)

Field to choose key to press

Adjust interval or CPS

Activation mode selector

Field to set hotkey

Buttons to start/stop manually

Execution status (“Active” / “Inactive”)

🛡️ Safety

Includes global hotkey control and manual stop support via GUI.

🧑‍💻 Developed by Alex Villen


