import tkinter as tk
from tkinter import ttk
import threading
import time
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Listener

mouse = MouseController()
keyboard = KeyboardController()

running = False
hold_mode = False
current_hotkey = "f6"
key_pressed = set()

def click_loop(action, key_to_press, delay):
    global running
    while running:
        if action == "Click izquierdo":
            mouse.click(Button.left)
        elif action == "Click derecho":
            mouse.click(Button.right)
        elif action == "Pulsar tecla":
            keyboard.press(key_to_press)
            keyboard.release(key_to_press)
        time.sleep(delay)

def start_action():
    global running
    if running:
        return
    running = True
    status_label.config(text="Activo", foreground="green")
    try:
        val = float(interval_entry.get())
    except ValueError:
        val = 0.1
    interval_type = interval_type_var.get()
    delay = 1 / val if interval_type == "CPS" and val > 0 else val
    action = action_var.get()
    key_to_press = key_entry.get()
    threading.Thread(target=click_loop, args=(action, key_to_press, delay), daemon=True).start()

def stop_action():
    global running
    running = False
    status_label.config(text="Inactivo", foreground="red")

def on_press(key):
    global running
    try:
        k = key.char
    except AttributeError:
        k = str(key).replace("Key.", "")
    if k == current_hotkey:
        if hold_mode:
            key_pressed.add(k)
            start_action()
        else:
            if running:
                stop_action()
            else:
                start_action()

def on_release(key):
    global running
    try:
        k = key.char
    except AttributeError:
        k = str(key).replace("Key.", "")
    if k == current_hotkey and hold_mode:
        key_pressed.discard(k)
        if not key_pressed:
            stop_action()

def set_hotkey():
    global current_hotkey
    current_hotkey = hotkey_entry.get().lower()
    hotkey_label.config(text=f"Hotkey configurada: {current_hotkey}")

def toggle_mode():
    global hold_mode
    hold_mode = not hold_mode
    mode_label.config(text=f"Modo: {'Mientras mantienes' if hold_mode else 'Activar/Desactivar'}")

# --- GUI ---
root = tk.Tk()
root.title("Autoclicker DEL DIAVLO")
root.geometry("320x460")
root.resizable(False, False)

ttk.Label(root, text="Acción:").pack(pady=5)
action_var = tk.StringVar(value="Click izquierdo")
ttk.Combobox(root, textvariable=action_var, values=["Click izquierdo", "Click derecho", "Pulsar tecla"]).pack()

ttk.Label(root, text="Tecla (si aplica):").pack(pady=5)
key_entry = ttk.Entry(root)
key_entry.insert(0, "e")
key_entry.pack()

ttk.Label(root, text="Intervalo:").pack(pady=5)
interval_entry = ttk.Entry(root)
interval_entry.insert(0, "0.1")
interval_entry.pack()

interval_type_var = tk.StringVar(value="Segundos")
ttk.Combobox(root, textvariable=interval_type_var, values=["Segundos", "CPS"]).pack()

ttk.Label(root, text="Tecla de activación:").pack(pady=5)
hotkey_entry = ttk.Entry(root)
hotkey_entry.insert(0, "f6")
hotkey_entry.pack()

ttk.Button(root, text="Configurar hotkey", command=set_hotkey).pack(pady=5)
hotkey_label = ttk.Label(root, text="Hotkey configurada: f6")
hotkey_label.pack(pady=5)

ttk.Button(root, text="Cambiar modo (Hold / Toggle)", command=toggle_mode).pack(pady=5)
mode_label = ttk.Label(root, text="Modo: Activar/Desactivar")
mode_label.pack(pady=5)

status_label = ttk.Label(root, text="Inactivo", foreground="red")
status_label.pack(pady=10)

ttk.Button(root, text="Iniciar manualmente", command=start_action).pack(pady=5)
ttk.Button(root, text="Detener manualmente", command=stop_action).pack(pady=5)

# --- Listener ---
listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

root.mainloop()
