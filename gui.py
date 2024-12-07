# gui.py

import tkinter as tk
from tkinter import messagebox
from game_logic import generar_cartas, comparar_resultados

class MathMemoryGame:
    def __init__(self, master, filas=4, columnas=4):
        self.master = master
        self.master.title("Juego de Memoria Matemática")

        self.filas = filas
        self.columnas = columnas
        self.total_cartas = filas * columnas
        self.cartas_info = generar_cartas(self.total_cartas // 2)  # (op, resultado)
        
        # Estado del juego
        self.botones = []
        self.reveladas = [False] * self.total_cartas
        self.primera_seleccion = None
        self.segunda_seleccion = None

        self.crear_tablero()

    def crear_tablero(self):
        frame = tk.Frame(self.master)
        frame.pack(padx=10, pady=10)

        for i in range(self.filas):
            for j in range(self.columnas):
                idx = i * self.columnas + j
                b = tk.Button(frame, text="?", width=8, height=4, 
                              command=lambda idx=idx: self.voltear_carta(idx))
                b.grid(row=i, column=j, padx=5, pady=5)
                self.botones.append(b)

    def voltear_carta(self, idx):
        if self.reveladas[idx]:
            # Ya está revelada, no hacemos nada
            return

        if self.primera_seleccion is None:
            # Primera carta a voltear
            self.primera_seleccion = idx
            self.botones[idx].config(text=self.cartas_info[idx][0], state="disabled")
        elif self.segunda_seleccion is None and idx != self.primera_seleccion:
            # Segunda carta a voltear
            self.segunda_seleccion = idx
            self.botones[idx].config(text=self.cartas_info[idx][0], state="disabled")
            self.master.after(1000, self.verificar_par)

    def verificar_par(self):
        i1 = self.primera_seleccion
        i2 = self.segunda_seleccion

        if comparar_resultados(self.cartas_info, i1, i2):
            # Es un par
            self.reveladas[i1] = True
            self.reveladas[i2] = True
        else:
            # No es un par, las volvemos a tapar
            self.botones[i1].config(text="?", state="normal")
            self.botones[i2].config(text="?", state="normal")

        # Reiniciamos selecciones
        self.primera_seleccion = None
        self.segunda_seleccion = None

        # Comprobamos si todas las cartas han sido reveladas
        if all(self.reveladas):
            messagebox.showinfo("¡Felicidades!", "¡Has encontrado todos los pares!")
            self.master.quit()

