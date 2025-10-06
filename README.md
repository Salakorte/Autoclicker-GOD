# 🖱️ AutoClicker Avanzado con Interfaz Gráfica (Python)

Un **autoclicker y autopulsador de teclas** totalmente configurable, creado en **Python** con interfaz **Tkinter**, pensado para ser ligero, intuitivo y compatible con juegos o aplicaciones en segundo plano.

---

## 🚀 Características principales

* 🖱️ **Clics automáticos** (izquierdo o derecho)
* ⌨️ **Pulsación automática de teclas configurable**
* ⏱️ **Control de velocidad por intervalo o CPS (clics por segundo)**
* 🔁 **Dos modos de activación:**

  * Activar/Desactivar con una tecla (toggle)
  * Mientras mantienes la tecla presionada (hold)
* 🎯 **Hotkey global personalizable** (funciona aunque la ventana esté minimizada)
* 🧩 **Interfaz limpia y ligera**, sin dependencias externas complejas
* 🪟 **Ejecutable independiente (.exe)** creado con PyInstaller

---

## 🧠 Tecnologías utilizadas

* **Python 3.10+**
* **Tkinter** → interfaz gráfica
* **pynput** → control del teclado y ratón
* **threading** → ejecución paralela sin bloquear la interfaz

---

## ⚙️ Instalación y ejecución

### Opción 1 — Ejecutar desde código fuente

```bash
git clone https://github.com/Salakorte/Autoclicker-GOD.git
cd Autoclicker-GOD
pip install pynput
python autoclicker.py
```

### Opción 2 — Ejecutar versión compilada

Si usas Windows, simplemente abre el archivo:

```
AutoClicker.exe
```

No requiere instalación ni Python.

---

## 🧩 Compilar a ejecutable (.exe)

Para crear tu propio `.exe` sin consola visible:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile autoclicker.py
```

El ejecutable aparecerá en la carpeta `dist/`.

---

## 🖼️ Interfaz

* Selección de acción (clic o tecla)
* Campo para elegir la tecla a pulsar
* Ajuste del intervalo o CPS
* Selector de modo de activación
* Campo para configurar la hotkey
* Botones para iniciar/detener manualmente
* Estado visual de ejecución (“Activo” / “Inactivo”)

---

## 🛡️ Seguridad

Incluye control por hotkey global y soporte para detener manualmente desde la interfaz.

---

## 🧑‍💻 Desarrollado por

**Salakorte  //  Salakolte**
📦 [GitHub](https://github.com/Salakorte)
