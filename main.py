import tkinter as tk
import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time
import speech_recognition as sr
from gtts import gTTS
import playsound
from playsound import playsound

class GUIConBotones:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI con Botones")

        # Variable para rastrear el estado global (On/Off)
        self.estado_global = tk.BooleanVar(value=False)

        # Botón global de On/Off a la izquierda
        self.boton_global = tk.Button(root, text="On" if self.estado_global.get() else "Off", command=self.toggle_estado_global)
        self.boton_global.pack(side=tk.LEFT, padx=10)

        # Crear botón 1
        self.boton_1 = tk.Button(root, text="Gestos Básicos", command=self.accion_boton_1)
        self.boton_1.pack(side=tk.LEFT, pady=10)

        # Crear botón 2
        self.boton_2 = tk.Button(root, text="Asis. Voz", command=self.accion_boton_2)
        self.boton_2.pack(side=tk.LEFT, pady=10)

        # Crear botón 3
        self.boton_3 = tk.Button(root, text="Braille", command=self.accion_boton_3)
        self.boton_3.pack(side=tk.LEFT, pady=10)

        # Crear botón 4
        self.boton_4 = tk.Button(root, text="Funciones Gestos", command=self.accion_boton_4)
        self.boton_4.pack(side=tk.LEFT, pady=10)

    def mostrar_texto(self, texto):
        # Función para mostrar el texto del botón presionado
        print(f"Texto del botón presionado: {texto}")

    def toggle_estado_global(self):
        # Función para alternar el estado global (On/Off)
        self.estado_global.set(not self.estado_global.get())
        self.boton_global.config(text="On" if self.estado_global.get() else "Off")

    def accion_boton_1(self):
        # Función para el botón 1
        print("Acción del Botón 1")
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles # from pose.py hands.py
        mp_pose = mp.solutions.pose
        mp_hands = mp.solutions.hands

        px = np.zeros(33)
        py = np.zeros(33)
        hx = np.zeros(21)
        hy = np.zeros(21)

        def calculate_distance(x1, y1, x2, y2):
            p1 = np.array([x1, y1])
            p2 = np.array([x2, y2])
            return np.linalg.norm(p1 - p2)


        #funciones para cada palabra
        def detect_word_si(hand_landmarks):
            word_si = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para la palabra "si"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h1 = int(hand_landmarks.landmark[1].x * width) #posicion en x de hand 1(muñeca)
            y_h1 = int(hand_landmarks.landmark[1].y * height) #posicion en y de hand 1(muñeca)
            x_h2 = int(hand_landmarks.landmark[2].x * width) #posicion en x de hand 2(muñeca)
            y_h2 = int(hand_landmarks.landmark[2].y * height) #posicion en y de hand 2(muñeca)
            x_h3 = int(hand_landmarks.landmark[3].x * width) #posicion en x de hand 3(muñeca)
            y_h3 = int(hand_landmarks.landmark[3].y * height) #posicion en y de hand 3(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 4
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h6 = int(hand_landmarks.landmark[6].x * width) #posicion en x de hand 6
            y_h6 = int(hand_landmarks.landmark[6].y * height) #posicion en y de hand 6
            x_h7 = int(hand_landmarks.landmark[7].x * width) #posicion en x de hand 7
            y_h7 = int(hand_landmarks.landmark[7].y * height) #posicion en y de hand 7
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h9 = int(hand_landmarks.landmark[9].x * width) #posicion en x de hand 9(punta del indice) 
            y_h9 = int(hand_landmarks.landmark[9].y * height) #posicion en y de hand 9(punta del indice)
            x_h10 = int(hand_landmarks.landmark[10].x * width) #posicion en x de hand 10(punta del indice) 
            y_h10 = int(hand_landmarks.landmark[10].y * height) #posicion en y de hand 10(punta del indice)
            x_h11 = int(hand_landmarks.landmark[11].x * width) #posicion en x de hand 11(punta del indice) 
            y_h11 = int(hand_landmarks.landmark[11].y * height) #posicion en y de hand 11(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h13 = int(hand_landmarks.landmark[13].x * width) #posicion en x de hand 13(punta del dedo del medio)
            y_h13 = int(hand_landmarks.landmark[13].y * height) #posicion en y de hand 13(punta del dedo del medio)
            x_h14 = int(hand_landmarks.landmark[14].x * width) #posicion en x de hand 14(punta del dedo del medio)
            y_h14 = int(hand_landmarks.landmark[14].y * height) #posicion en y de hand 14(punta del dedo del medio)
            x_h15 = int(hand_landmarks.landmark[15].x * width) #posicion en x de hand 15(punta del dedo del medio)
            y_h15 = int(hand_landmarks.landmark[15].y * height) #posicion en y de hand 15(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h17 = int(hand_landmarks.landmark[17].x * width) #posicion en x de hand 17(punta del dedo del medio)
            y_h17 = int(hand_landmarks.landmark[17].y * height) #posicion en y de hand 17(punta del dedo del medio)
            x_h18 = int(hand_landmarks.landmark[18].x * width) #posicion en x de hand 18(punta del dedo del medio)
            y_h18 = int(hand_landmarks.landmark[18].y * height) #posicion en y de hand 18(punta del dedo del medio)
            x_h19 = int(hand_landmarks.landmark[19].x * width) #posicion en x de hand 19(punta del dedo del medio)
            y_h19 = int(hand_landmarks.landmark[19].y * height) #posicion en y de hand 19(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h6 = calculate_distance(x_h0, y_h0, x_h6, y_h6) #distancia de 0 a 6 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 8 (mano)
            d_base_h9 = calculate_distance(x_h0, y_h0, x_h9, y_h9) #distancia de 0 a 9 (mano)
            d_base_h10 = calculate_distance(x_h0, y_h0, x_h10, y_h10) #distancia de 0 a 9 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 12 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 16 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 20 (mano)
            if d_base_h8 < d_base_h9 and d_base_h12 < d_base_h9 and d_base_h16 < d_base_h9 and d_base_h20 < d_base_h9:
                word_si = True
            return word_si

        def detect_word_no(hand_landmarks):
            word_no = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para la palabra "no"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h1 = int(hand_landmarks.landmark[1].x * width) #posicion en x de hand 1(muñeca)
            y_h1 = int(hand_landmarks.landmark[1].y * height) #posicion en y de hand 1(muñeca)
            x_h2 = int(hand_landmarks.landmark[2].x * width) #posicion en x de hand 2(muñeca)
            y_h2 = int(hand_landmarks.landmark[2].y * height) #posicion en y de hand 2(muñeca)
            x_h3 = int(hand_landmarks.landmark[3].x * width) #posicion en x de hand 3(muñeca)
            y_h3 = int(hand_landmarks.landmark[3].y * height) #posicion en y de hand 3(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 4
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h6 = int(hand_landmarks.landmark[6].x * width) #posicion en x de hand 6
            y_h6 = int(hand_landmarks.landmark[6].y * height) #posicion en y de hand 6
            x_h7 = int(hand_landmarks.landmark[7].x * width) #posicion en x de hand 7
            y_h7 = int(hand_landmarks.landmark[7].y * height) #posicion en y de hand 7
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h9 = int(hand_landmarks.landmark[9].x * width) #posicion en x de hand 9(punta del indice) 
            y_h9 = int(hand_landmarks.landmark[9].y * height) #posicion en y de hand 9(punta del indice)
            x_h10 = int(hand_landmarks.landmark[10].x * width) #posicion en x de hand 10(punta del indice) 
            y_h10 = int(hand_landmarks.landmark[10].y * height) #posicion en y de hand 10(punta del indice)
            x_h11 = int(hand_landmarks.landmark[11].x * width) #posicion en x de hand 11(punta del indice) 
            y_h11 = int(hand_landmarks.landmark[11].y * height) #posicion en y de hand 11(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h13 = int(hand_landmarks.landmark[13].x * width) #posicion en x de hand 13(punta del dedo del medio)
            y_h13 = int(hand_landmarks.landmark[13].y * height) #posicion en y de hand 13(punta del dedo del medio)
            x_h14 = int(hand_landmarks.landmark[14].x * width) #posicion en x de hand 14(punta del dedo del medio)
            y_h14 = int(hand_landmarks.landmark[14].y * height) #posicion en y de hand 14(punta del dedo del medio)
            x_h15 = int(hand_landmarks.landmark[15].x * width) #posicion en x de hand 15(punta del dedo del medio)
            y_h15 = int(hand_landmarks.landmark[15].y * height) #posicion en y de hand 15(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h17 = int(hand_landmarks.landmark[17].x * width) #posicion en x de hand 17(punta del dedo del medio)
            y_h17 = int(hand_landmarks.landmark[17].y * height) #posicion en y de hand 17(punta del dedo del medio)
            x_h18 = int(hand_landmarks.landmark[18].x * width) #posicion en x de hand 18(punta del dedo del medio)
            y_h18 = int(hand_landmarks.landmark[18].y * height) #posicion en y de hand 18(punta del dedo del medio)
            x_h19 = int(hand_landmarks.landmark[19].x * width) #posicion en x de hand 19(punta del dedo del medio)
            y_h19 = int(hand_landmarks.landmark[19].y * height) #posicion en y de hand 19(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h6 = calculate_distance(x_h0, y_h0, x_h6, y_h6) #distancia de 0 a 6 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 8 (mano)
            d_base_h9 = calculate_distance(x_h0, y_h0, x_h9, y_h9) #distancia de 0 a 9 (mano)
            d_base_h10 = calculate_distance(x_h0, y_h0, x_h10, y_h10) #distancia de 0 a 9 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 12 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 16 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 20 (mano)
            if d_base_h5 < d_base_h4 and d_base_h8 < d_base_h6 and d_base_h12 > d_base_h9:
                word_no = True
            return word_no
        def detect_num_uno(hand_landmarks):
            word_uno = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 > d_base_h12 and d_base_h5 > d_base_h16 and d_base_h5 > d_base_h20 and d_base_h5 < d_base_h8:
                word_uno = True
            return word_uno

        def detect_num_dos(hand_landmarks):
            word_dos = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 < d_base_h12 and d_base_h5 > d_base_h16 and d_base_h5 > d_base_h20 and d_base_h5 < d_base_h8:
                word_dos = True
            return word_dos

        def detect_num_tres(hand_landmarks):
            word_tres = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 < d_base_h4 and d_base_h5 < d_base_h8 and d_base_h5 < d_base_h12 and d_base_h5 > d_base_h16 and d_base_h5 > d_base_h20:
                word_tres = True
            return word_tres

        def detect_num_cuatro(hand_landmarks):
            word_cuatro = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 < d_base_h12 and d_base_h5 < d_base_h16 and d_base_h5 < d_base_h20 and d_base_h5 < d_base_h8:
                word_cuatro = True
            return word_cuatro

        def detect_num_cinco(hand_landmarks):
            word_cinco = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 < d_base_h4 and d_base_h5 < d_base_h12 and d_base_h5 < d_base_h16 and d_base_h5 < d_base_h20 and d_base_h5 < d_base_h8:
                word_cinco = True
            return word_cinco

        def detect_num_seis(hand_landmarks):
            word_seis = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 < d_base_h12 and d_base_h5 < d_base_h16 and d_base_h5 > d_base_h20 and d_base_h5 < d_base_h8:
                word_seis = True
            return word_seis

        def detect_num_siete(hand_landmarks):
            word_siete = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 < d_base_h12 and d_base_h5 > d_base_h16 and d_base_h5 < d_base_h20 and d_base_h5 < d_base_h8:
                word_siete = True
            return word_siete

        def detect_num_ocho(hand_landmarks):
            word_ocho = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 > d_base_h12 and d_base_h5 < d_base_h16 and d_base_h5 < d_base_h20 and d_base_h5 < d_base_h8:
                word_ocho = True
            return word_ocho

        def detect_num_nueve(hand_landmarks):
            word_nueve = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 < d_base_h12 and d_base_h5 < d_base_h16 and d_base_h5 < d_base_h20 and d_base_h5 > d_base_h8:
                word_nueve = True
            return word_nueve



        def coordi(hand_landmarks, resp, px, py):
            for ids,lm in enumerate(hand_landmarks.landmark):
                hx[ids], hy[ids] = lm.x * width, lm.y * height
            if resp.pose_landmarks != None:
                for idp, lmp in enumerate(resp.pose_landmarks.landmark):
                    px[idp], py[idp] = lmp.x * width, lmp.y * height
            #print(px,py,hx,hy)


        cap = cv2.VideoCapture(0)
        hands = mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)
        pose = mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)
        while cap.isOpened():
            ret, img = cap.read()
            height, width, _ = img.shape

            # Pose
            img.flags.writeable = False
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            resp = pose.process(img)

            # Hands
            resh = hands.process(img)

            # Draw both
            if resh.multi_hand_landmarks:
                for hand_landmarks in resh.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style()
                    )
                    coordi(hand_landmarks, resp, px, py)
                    if detect_word_si(hand_landmarks):
                        time.sleep(0.05)
                        print("si")
                        #pyautogui.click()
                    
                    elif detect_word_no(hand_landmarks):
                        time.sleep(0.05)
                        print("no")
                        #pyautogui.click()
                    elif detect_num_uno(hand_landmarks):
                        time.sleep(0.05)
                        print("uno")
                        #pyautogui.click()
                    elif detect_num_dos(hand_landmarks):
                        time.sleep(0.05)
                        print("dos")
                        #pyautogui.click()
                    elif detect_num_tres(hand_landmarks):
                        time.sleep(0.05)
                        print("tres")
                        #pyautogui.click()
                    elif detect_num_cuatro(hand_landmarks):
                        time.sleep(0.05)
                        print("cuatro")
                        #pyautogui.click()
                    elif detect_num_cinco(hand_landmarks):
                        time.sleep(0.05)
                        print("cinco")
                        #pyautogui.click()
                    elif detect_num_seis(hand_landmarks):
                        time.sleep(0.05)
                        print("seis")
                        #pyautogui.click()
                    elif detect_num_siete(hand_landmarks):
                        time.sleep(0.05)
                        print("siete")
                        #pyautogui.click()
                    elif detect_num_ocho(hand_landmarks):
                        time.sleep(0.05)
                        print("ocho")
                        #pyautogui.click()
                    elif detect_num_nueve(hand_landmarks):
                        time.sleep(0.05)
                        print("nueve")
                        #pyautogui.click()
            #if resp.pose_landmarks
            mp_drawing.draw_landmarks(
                img, resp.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec = mp_drawing_styles.get_default_pose_landmarks_style()
            )
            
            cv2.imshow("MPipe v2",cv2.flip(img,1))
            if cv2.waitKey(5)  & 0xFF == 27:
                break


        cap.release()

    def accion_boton_2(self):
        # Función para el botón 2
        print("Acción del Botón 2")
        r = sr.Recognizer()

        def voiceover(text):
            if (text == "necesito ayuda"):
                mytext = "Llamando a los servicios de emergencia"
                audio = gTTS(text=mytext, lang="es", slow=False)
                audio.save("tmp.mp3")
                playsound('tmp.mp3')
                #panicfnc()
            if (text == "tengo cita médica"):
                mytext = "De acuerdo, revisaremos la agenda, espere por favor..."
                audio = gTTS(text=mytext, lang="es", slow=False)
                audio.save("tmp.mp3")
                playsound('tmp.mp3')
                #citamedfnc()
            if (text == "me siento mal"):
                mytext = "Nos comunicaremos con el personal médico adecuado, espere por favor"
                audio = gTTS(text=mytext, lang="es", slow=False)
                audio.save("tmp.mp3")
                playsound('tmp.mp3')
                #feelbadfnc()

        with sr.Microphone() as source:
            # read the audio data from the default microphone
            audio_data = r.record(source, duration=3)
            print("Recognizing...")
            # convert speech to text
            #text = r.recognize_google(audio_data)
            text = r.recognize_google(audio_data, language="es-ES",show_all=True)
            if text != []:
                print(text)
                print(type(text))
            else:
                while text == []:
                    print("Repita nuevamente...")
                    audio_data = r.record(source, duration=3)
                    text = r.recognize_google(audio_data, language="es-ES",show_all=True)
                    print(text)
                    print(type(text))
        print(text['alternative'][0]['transcript'].lower())
        voiceover(text['alternative'][0]['transcript'].lower())

    def accion_boton_3(self):
        # Función para el botón 3
        print("Acción del Botón 3")
        def txt2br(text):
            code_table = {
            'a': [1,0,0,0,0,0],
            'b': [1,1,0,0,0,0],
            'c': [1,0,0,1,0,0],
            'd': [1,0,0,1,1,0],
            'e': [1,0,0,0,1,0],
            'f': [1,1,0,1,0,0],
            'g': [1,1,0,1,1,0],
            'h': [1,1,0,0,1,0],
            'i': [0,1,0,1,0,0],
            'j': [0,1,0,1,1,0],
            'k': [1,0,1,0,0,0],
            'l': [1,1,1,0,0,0],
            'm': [1,0,1,1,0,0],
            'n': [1,0,1,1,1,0],
            'o': [1,0,1,0,1,0],
            'p': [1,1,1,1,0,0],
            'q': [1,1,1,1,1,0],
            'r': [1,1,1,0,1,0],
            's': [0,1,1,1,0,0],
            't': [0,1,1,1,1,0],
            'u': [1,0,1,0,0,1],
            'v': [1,1,1,0,0,1],
            'w': [0,1,0,1,1,1],
            'x': [1,0,1,1,0,1],
            'y': [1,0,1,1,1,1],
            'z': [1,0,1,0,1,1],
            '#': [0,0,1,1,1,1],
            '1': [1,0,0,0,0,0],
            '2': [1,1,0,0,0,0],
            '3': [1,0,0,1,0,0],
            '4': [1,0,0,1,1,0],
            '5': [1,0,0,0,1,0],
            '6': [1,1,0,1,0,0],
            '7': [1,1,0,1,1,0],
            '8': [1,1,0,0,1,0],
            '9': [0,1,0,1,0,0],
            '0': [0,1,0,1,1,0],
            ' ': [0,0,0,0,0,0]}
            txt = text.lower()
            braille = code_table[txt]
            return braille


        txt = input()
        print("Solved")
        audio = gTTS(text=txt, lang="es", slow=False)
        audio.save("tmp.mp3")
        playsound('tmp.mp3', block=False)
        for letra in txt:
            braille_matrix = [txt2br(letra)[0], txt2br(letra)[1], txt2br(letra)[2]]
            print(letra, end='', flush=True)  # Imprime la letra sin salto de línea y forza el vaciado del búfer
            print(txt2br(letra))
            time.sleep(1)  # Espera 2 segundos antes de mostrar la siguiente letra

    def accion_boton_4(self):
        # Función para el botón 4
        print("Acción del Botón 4")
        #texto1="¿Hay algun personal del hospital que hable lenguaje de señas?"
        #tts=gTTS(text=texto1, lang='es', slow=False)
        #tts.save("c:/Users/rocas/iCloudDrive/Hackaton/Jars/sonido1.mp3")

        #texto2="¡Ayuda!, socorro a victima de violencia sexual y/o género"
        #tts=gTTS(text=texto2, lang='es', slow=False)
        #tts.save("c:/Users/rocas/iCloudDrive/Hackaton/Jars/sonido2.mp3")

        #texto3="Emergencia, mujer cerca del alumbramiento"
        #tts=gTTS(text=texto3, lang='es', slow=False)
        #tts.save("c:/Users/rocas/iCloudDrive/Hackaton/Jars/sonido3.mp3")

        #texto4="¿Podria visitar a mi familiar enfermo en este horario?"
        #tts=gTTS(text=texto4, lang='es', slow=False)
        #tts.save("c:/Users/rocas/iCloudDrive/Hackaton/Jars/sonido4.mp3")

        #texto5="¿Donde se encuentra el lugar de informaciones?"
        #tts=gTTS(text=texto5, lang='es', slow=False)
        #tts.save("c:/Users/rocas/iCloudDrive/Hackaton/Jars/sonido5.mp3")

        #texto6="¿En que horarios se puede sacar una cita y que requiero para una?"
        #tts=gTTS(text=texto6, lang='es', slow=False)
        #tts.save("c:/Users/rocas/iCloudDrive/Hackaton/Jars/sonido6.mp3")

        #texto7="¿Podria llamar a la enfermera?"
        #tts=gTTS(text=texto7, lang='es', slow=False)
        #tts.save("c:/Users/rocas/iCloudDrive/Hackaton/Jars/sonido7.mp3")

        #texto8="Tengo una cita medica a esta hora"
        #tts=gTTS(text=texto8, lang='es', slow=False)
        #tts.save("c:/Users/rocas/iCloudDrive/Hackaton/Jars/sonido8.mp3")

        #texto9="No me siento bien, ¿donde queda emergencias?"
        #tts=gTTS(text=texto9, lang='es', slow=False)
        #tts.save("c:/Users/rocas/iCloudDrive/Hackaton/Jars/sonido9.mp3")

        #textosi="Si"
        #tts=gTTS(text=textosi, lang='es', slow=False)
        #tts.save("c:/Users/rocas/iCloudDrive/Hackaton/Jars/sonidosi.mp3")

        #textono="No"
        #tts=gTTS(text=textono, lang='es', slow=False)
        #tts.save("c:/Users/rocas/iCloudDrive/Hackaton/Jars/sonidono.mp3")

        mp_drawing = mp.solutions.drawing_utils
        mp_holistic = mp.solutions.holistic


        mp_hands = mp.solutions.hands

        color_mouse_pointer = (255, 0, 255)
        #cap = cv2.VideoCapture("video_0001.mp4")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        #puntos en x,y de todos los puntos de la mano





        #funciones para cada palabra
        def detect_word_si(hand_landmarks):
            word_si = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para la palabra "si"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h1 = int(hand_landmarks.landmark[1].x * width) #posicion en x de hand 1(muñeca)
            y_h1 = int(hand_landmarks.landmark[1].y * height) #posicion en y de hand 1(muñeca)
            x_h2 = int(hand_landmarks.landmark[2].x * width) #posicion en x de hand 2(muñeca)
            y_h2 = int(hand_landmarks.landmark[2].y * height) #posicion en y de hand 2(muñeca)
            x_h3 = int(hand_landmarks.landmark[3].x * width) #posicion en x de hand 3(muñeca)
            y_h3 = int(hand_landmarks.landmark[3].y * height) #posicion en y de hand 3(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 4
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h6 = int(hand_landmarks.landmark[6].x * width) #posicion en x de hand 6
            y_h6 = int(hand_landmarks.landmark[6].y * height) #posicion en y de hand 6
            x_h7 = int(hand_landmarks.landmark[7].x * width) #posicion en x de hand 7
            y_h7 = int(hand_landmarks.landmark[7].y * height) #posicion en y de hand 7
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h9 = int(hand_landmarks.landmark[9].x * width) #posicion en x de hand 9(punta del indice) 
            y_h9 = int(hand_landmarks.landmark[9].y * height) #posicion en y de hand 9(punta del indice)
            x_h10 = int(hand_landmarks.landmark[10].x * width) #posicion en x de hand 10(punta del indice) 
            y_h10 = int(hand_landmarks.landmark[10].y * height) #posicion en y de hand 10(punta del indice)
            x_h11 = int(hand_landmarks.landmark[11].x * width) #posicion en x de hand 11(punta del indice) 
            y_h11 = int(hand_landmarks.landmark[11].y * height) #posicion en y de hand 11(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h13 = int(hand_landmarks.landmark[13].x * width) #posicion en x de hand 13(punta del dedo del medio)
            y_h13 = int(hand_landmarks.landmark[13].y * height) #posicion en y de hand 13(punta del dedo del medio)
            x_h14 = int(hand_landmarks.landmark[14].x * width) #posicion en x de hand 14(punta del dedo del medio)
            y_h14 = int(hand_landmarks.landmark[14].y * height) #posicion en y de hand 14(punta del dedo del medio)
            x_h15 = int(hand_landmarks.landmark[15].x * width) #posicion en x de hand 15(punta del dedo del medio)
            y_h15 = int(hand_landmarks.landmark[15].y * height) #posicion en y de hand 15(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h17 = int(hand_landmarks.landmark[17].x * width) #posicion en x de hand 17(punta del dedo del medio)
            y_h17 = int(hand_landmarks.landmark[17].y * height) #posicion en y de hand 17(punta del dedo del medio)
            x_h18 = int(hand_landmarks.landmark[18].x * width) #posicion en x de hand 18(punta del dedo del medio)
            y_h18 = int(hand_landmarks.landmark[18].y * height) #posicion en y de hand 18(punta del dedo del medio)
            x_h19 = int(hand_landmarks.landmark[19].x * width) #posicion en x de hand 19(punta del dedo del medio)
            y_h19 = int(hand_landmarks.landmark[19].y * height) #posicion en y de hand 19(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h6 = calculate_distance(x_h0, y_h0, x_h6, y_h6) #distancia de 0 a 6 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 8 (mano)
            d_base_h9 = calculate_distance(x_h0, y_h0, x_h9, y_h9) #distancia de 0 a 9 (mano)
            d_base_h10 = calculate_distance(x_h0, y_h0, x_h10, y_h10) #distancia de 0 a 9 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 12 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 16 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 20 (mano)
            if d_base_h8 < d_base_h9 and d_base_h12 < d_base_h9 and d_base_h16 < d_base_h9 and d_base_h20 < d_base_h9:
                word_si = True
                color_base = (255, 0, 255)
                color_h8 = (255, 0, 255)
            cv2.circle(output, (x_h0, y_h0), 5, color_base, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.line(output, (x_h0, y_h0), (x_h9, y_h9), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            return word_si

        def detect_word_no(hand_landmarks):
            word_no = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para la palabra "no"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h1 = int(hand_landmarks.landmark[1].x * width) #posicion en x de hand 1(muñeca)
            y_h1 = int(hand_landmarks.landmark[1].y * height) #posicion en y de hand 1(muñeca)
            x_h2 = int(hand_landmarks.landmark[2].x * width) #posicion en x de hand 2(muñeca)
            y_h2 = int(hand_landmarks.landmark[2].y * height) #posicion en y de hand 2(muñeca)
            x_h3 = int(hand_landmarks.landmark[3].x * width) #posicion en x de hand 3(muñeca)
            y_h3 = int(hand_landmarks.landmark[3].y * height) #posicion en y de hand 3(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 4
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h6 = int(hand_landmarks.landmark[6].x * width) #posicion en x de hand 6
            y_h6 = int(hand_landmarks.landmark[6].y * height) #posicion en y de hand 6
            x_h7 = int(hand_landmarks.landmark[7].x * width) #posicion en x de hand 7
            y_h7 = int(hand_landmarks.landmark[7].y * height) #posicion en y de hand 7
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h9 = int(hand_landmarks.landmark[9].x * width) #posicion en x de hand 9(punta del indice) 
            y_h9 = int(hand_landmarks.landmark[9].y * height) #posicion en y de hand 9(punta del indice)
            x_h10 = int(hand_landmarks.landmark[10].x * width) #posicion en x de hand 10(punta del indice) 
            y_h10 = int(hand_landmarks.landmark[10].y * height) #posicion en y de hand 10(punta del indice)
            x_h11 = int(hand_landmarks.landmark[11].x * width) #posicion en x de hand 11(punta del indice) 
            y_h11 = int(hand_landmarks.landmark[11].y * height) #posicion en y de hand 11(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h13 = int(hand_landmarks.landmark[13].x * width) #posicion en x de hand 13(punta del dedo del medio)
            y_h13 = int(hand_landmarks.landmark[13].y * height) #posicion en y de hand 13(punta del dedo del medio)
            x_h14 = int(hand_landmarks.landmark[14].x * width) #posicion en x de hand 14(punta del dedo del medio)
            y_h14 = int(hand_landmarks.landmark[14].y * height) #posicion en y de hand 14(punta del dedo del medio)
            x_h15 = int(hand_landmarks.landmark[15].x * width) #posicion en x de hand 15(punta del dedo del medio)
            y_h15 = int(hand_landmarks.landmark[15].y * height) #posicion en y de hand 15(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h17 = int(hand_landmarks.landmark[17].x * width) #posicion en x de hand 17(punta del dedo del medio)
            y_h17 = int(hand_landmarks.landmark[17].y * height) #posicion en y de hand 17(punta del dedo del medio)
            x_h18 = int(hand_landmarks.landmark[18].x * width) #posicion en x de hand 18(punta del dedo del medio)
            y_h18 = int(hand_landmarks.landmark[18].y * height) #posicion en y de hand 18(punta del dedo del medio)
            x_h19 = int(hand_landmarks.landmark[19].x * width) #posicion en x de hand 19(punta del dedo del medio)
            y_h19 = int(hand_landmarks.landmark[19].y * height) #posicion en y de hand 19(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h6 = calculate_distance(x_h0, y_h0, x_h6, y_h6) #distancia de 0 a 6 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 8 (mano)
            d_base_h9 = calculate_distance(x_h0, y_h0, x_h9, y_h9) #distancia de 0 a 9 (mano)
            d_base_h10 = calculate_distance(x_h0, y_h0, x_h10, y_h10) #distancia de 0 a 9 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 12 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 16 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 20 (mano)
            if d_base_h5 < d_base_h4 and d_base_h8 < d_base_h6 and d_base_h12 > d_base_h9:
                word_no = True
                color_base = (255, 0, 255)
                color_h8 = (255, 0, 255)
            cv2.circle(output, (x_h0, y_h0), 5, color_base, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h4, y_h4), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h6), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h5), 5, color_h8, 2)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            return word_no
        def detect_num_uno(hand_landmarks):
            word_uno = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 > d_base_h12 and d_base_h5 > d_base_h16 and d_base_h5 > d_base_h20 and d_base_h5 < d_base_h8:
                word_uno = True
                color_base = (255, 0, 255)
                color_h8 = (255, 0, 255)
            cv2.circle(output, (x_h0, y_h0), 5, color_base, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h4, y_h4), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h5), 5, color_h8, 2)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            return word_uno

        def detect_num_dos(hand_landmarks):
            word_dos = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 < d_base_h12 and d_base_h5 > d_base_h16 and d_base_h5 > d_base_h20 and d_base_h5 < d_base_h8:
                word_dos = True
                color_base = (255, 0, 255)
                color_h8 = (255, 0, 255)
            cv2.circle(output, (x_h0, y_h0), 5, color_base, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h4, y_h4), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h5), 5, color_h8, 2)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            return word_dos

        def detect_num_tres(hand_landmarks):
            word_tres = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 < d_base_h4 and d_base_h5 < d_base_h8 and d_base_h5 < d_base_h12 and d_base_h5 > d_base_h16 and d_base_h5 > d_base_h20:
                word_tres = True
                color_base = (255, 0, 255)
                color_h8 = (255, 0, 255)
            cv2.circle(output, (x_h0, y_h0), 5, color_base, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h4, y_h4), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h5), 5, color_h8, 2)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            return word_tres

        def detect_num_cuatro(hand_landmarks):
            word_cuatro = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 < d_base_h12 and d_base_h5 < d_base_h16 and d_base_h5 < d_base_h20 and d_base_h5 < d_base_h8:
                word_cuatro = True
                color_base = (255, 0, 255)
                color_h8 = (255, 0, 255)
            cv2.circle(output, (x_h0, y_h0), 5, color_base, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h4, y_h4), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h5), 5, color_h8, 2)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            return word_cuatro

        def detect_num_cinco(hand_landmarks):
            word_cinco = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 < d_base_h4 and d_base_h5 < d_base_h12 and d_base_h5 < d_base_h16 and d_base_h5 < d_base_h20 and d_base_h5 < d_base_h8:
                word_cinco = True
                color_base = (255, 0, 255)
                color_h8 = (255, 0, 255)
            cv2.circle(output, (x_h0, y_h0), 5, color_base, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h4, y_h4), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h5), 5, color_h8, 2)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            return word_cinco

        def detect_num_seis(hand_landmarks):
            word_seis = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 < d_base_h12 and d_base_h5 < d_base_h16 and d_base_h5 > d_base_h20 and d_base_h5 < d_base_h8:
                word_seis = True
                color_base = (255, 0, 255)
                color_h8 = (255, 0, 255)
            cv2.circle(output, (x_h0, y_h0), 5, color_base, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h4, y_h4), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h5), 5, color_h8, 2)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            return word_seis

        def detect_num_siete(hand_landmarks):
            word_siete = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 < d_base_h12 and d_base_h5 > d_base_h16 and d_base_h5 < d_base_h20 and d_base_h5 < d_base_h8:
                word_siete = True
                color_base = (255, 0, 255)
                color_h8 = (255, 0, 255)
            cv2.circle(output, (x_h0, y_h0), 5, color_base, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h4, y_h4), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h5), 5, color_h8, 2)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            return word_siete

        def detect_num_ocho(hand_landmarks):
            word_ocho = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 > d_base_h12 and d_base_h5 < d_base_h16 and d_base_h5 < d_base_h20 and d_base_h5 < d_base_h8:
                word_ocho = True
                color_base = (255, 0, 255)
                color_h8 = (255, 0, 255)
            cv2.circle(output, (x_h0, y_h0), 5, color_base, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h4, y_h4), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h5), 5, color_h8, 2)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            return word_ocho

        def detect_num_nueve(hand_landmarks):
            word_nueve = False
            color_base = (255, 0, 112)
            color_h8 = (255, 198, 82)
            #comando para el numero "uno"
            x_h0 = int(hand_landmarks.landmark[0].x * width) #posicion en x de hand 0(muñeca)
            y_h0 = int(hand_landmarks.landmark[0].y * height) #posicion en y de hand 0(muñeca)
            x_h4 = int(hand_landmarks.landmark[4].x * width) #posicion en x de hand 4
            y_h4 = int(hand_landmarks.landmark[4].y * height) #posicion en y de hand 
            x_h5 = int(hand_landmarks.landmark[5].x * width) #posicion en x de hand 5
            y_h5 = int(hand_landmarks.landmark[5].y * height) #posicion en y de hand 5
            x_h8 = int(hand_landmarks.landmark[8].x * width) #posicion en x de hand 8(punta del indice) 
            y_h8 = int(hand_landmarks.landmark[8].y * height) #posicion en y de hand 8(punta del indice)
            x_h12 = int(hand_landmarks.landmark[12].x * width) #posicion en x de hand 12(punta del dedo del medio)
            y_h12 = int(hand_landmarks.landmark[12].y * height) #posicion en y de hand 12(punta del dedo del medio)
            x_h16 = int(hand_landmarks.landmark[16].x * width) #posicion en x de hand 16(punta del dedo del medio)
            y_h16 = int(hand_landmarks.landmark[16].y * height) #posicion en y de hand 16(punta del dedo del medio)
            x_h20 = int(hand_landmarks.landmark[20].x * width) #posicion en x de hand 20(punta del dedo del medio)
            y_h20 = int(hand_landmarks.landmark[20].y * height) #posicion en y de hand 20(punta del dedo del medio)
            #distancias de la muñeca a puntos de la mano
            d_base_h4 = calculate_distance(x_h0, y_h0, x_h4, y_h4) #distancia de 0 a 4 (mano)
            d_base_h8 = calculate_distance(x_h0, y_h0, x_h8, y_h8) #distancia de 0 a 5 (mano)
            d_base_h5 = calculate_distance(x_h0, y_h0, x_h5, y_h5) #distancia de 0 a 5 (mano)
            d_base_h12 = calculate_distance(x_h0, y_h0, x_h12, y_h12) #distancia de 0 a 6 (mano)
            d_base_h16 = calculate_distance(x_h0, y_h0, x_h16, y_h16) #distancia de 0 a 8 (mano)
            d_base_h20 = calculate_distance(x_h0, y_h0, x_h20, y_h20) #distancia de 0 a 9 (mano)
            if d_base_h5 > d_base_h4 and d_base_h5 < d_base_h12 and d_base_h5 < d_base_h16 and d_base_h5 < d_base_h20 and d_base_h5 > d_base_h8:
                word_nueve = True
                color_base = (255, 0, 255)
                color_h8 = (255, 0, 255)
            cv2.circle(output, (x_h0, y_h0), 5, color_base, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h4, y_h4), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h8), 5, color_h8, 2)
            cv2.circle(output, (x_h8, y_h5), 5, color_h8, 2)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            cv2.line(output, (x_h0, y_h0), (x_h5, y_h5), color_base, 3)
            cv2.line(output, (x_h0, y_h0), (x_h8, y_h8), color_h8, 3)
            return word_nueve


        with mp_holistic.Holistic(
            static_image_mode=False,
            model_complexity=1) as holistic:
            while True:
                ret, frame = cap.read()
                if ret == False:
                    break
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = holistic.process(frame_rgb)
                # rostro
                #mp_drawing.draw_landmarks(
                #    frame, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION,
                    #   mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1),
                    #  mp_drawing.DrawingSpec(color=(0, 128, 255), thickness=2))
                
                # Mano izquieda (azul)
                mp_drawing.draw_landmarks(
                    frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2, circle_radius=1),
                    mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2))
                
                # Mano derecha (verde)
                mp_drawing.draw_landmarks(
                    frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=1),
                    mp_drawing.DrawingSpec(color=(57, 143, 0), thickness=2))
                
                # Postura
                mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(128, 0, 255), thickness=2, circle_radius=1),
                    mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))
                frame = cv2.flip(frame, 1)

                cv2.imshow("Frame", frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    break

        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands
        cap = cv2.VideoCapture(0)
        color_mouse_pointer = (255, 0, 255)
        # Puntos de la pantalla-juego
        SCREEN_GAME_X_INI = 150
        SCREEN_GAME_Y_INI = 160
        SCREEN_GAME_X_FIN = 150 + 780
        SCREEN_GAME_Y_FIN = 160 + 450
        aspect_ratio_screen = (SCREEN_GAME_X_FIN - SCREEN_GAME_X_INI) / (SCREEN_GAME_Y_FIN - SCREEN_GAME_Y_INI)
        print("aspect_ratio_screen:", aspect_ratio_screen)
        X_Y_INI = 100
        def calculate_distance(x1, y1, x2, y2):
            p1 = np.array([x1, y1])
            p2 = np.array([x2, y2])
            return np.linalg.norm(p1 - p2)

        with mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5) as hands:
            while True:
                ret, frame = cap.read()
                if ret == False:
                    break
                height, width, _ = frame.shape
                frame = cv2.flip(frame, 1)
                # Dibujando un área proporcional a la del juego
                area_width = width - X_Y_INI * 2
                area_height = int(area_width / aspect_ratio_screen)
                aux_image = np.zeros(frame.shape, np.uint8)
                aux_image = cv2.rectangle(aux_image, (X_Y_INI, X_Y_INI), (X_Y_INI + area_width, X_Y_INI +area_height), (255, 0, 0), -1)
                output = cv2.addWeighted(frame, 1, aux_image, 0.7, 0)
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = hands.process(frame_rgb)
                
                if results.multi_hand_landmarks is not None:
                    for hand_landmarks in results.multi_hand_landmarks:
                        x = int(hand_landmarks.landmark[9].x * width)
                        y = int(hand_landmarks.landmark[9].y * height)
                        xm = np.interp(x, (X_Y_INI, X_Y_INI + area_width), (SCREEN_GAME_X_INI, SCREEN_GAME_X_FIN))
                        ym = np.interp(y, (X_Y_INI, X_Y_INI + area_height), (SCREEN_GAME_Y_INI, SCREEN_GAME_Y_FIN))
                        pyautogui.moveTo(int(xm), int(ym))
                        
                        if detect_word_si(hand_landmarks):
                            playsound("/home/alejandro_jm/Documentos/hackaton_tinku/sonidosi.mp3", True)
                            print("si")
                            #pyautogui.click()
                            cv2.circle(output, (x, y), 10, color_mouse_pointer, 3)
                            cv2.circle(output, (x, y), 5, color_mouse_pointer, -1)
                        
                        if detect_word_no(hand_landmarks):
                            playsound("/home/alejandro_jm/Documentos/hackaton_tinku/sonidono.mp3", True)
                            print("no")
                            #pyautogui.click()
                            cv2.circle(output, (x, y), 10, color_mouse_pointer, 3)
                            cv2.circle(output, (x, y), 5, color_mouse_pointer, -1)
                        if detect_num_uno(hand_landmarks):
                            playsound("/home/alejandro_jm/Documentos/hackaton_tinku/sonido1.mp3", True)
                            print("uno")
                            #pyautogui.click()
                            cv2.circle(output, (x, y), 10, color_mouse_pointer, 3)
                            cv2.circle(output, (x, y), 5, color_mouse_pointer, -1)
                        if detect_num_dos(hand_landmarks):
                            playsound("/home/alejandro_jm/Documentos/hackaton_tinku/sonido2.mp3", True)
                            print("dos")
                            #pyautogui.click()
                            cv2.circle(output, (x, y), 10, color_mouse_pointer, 3)
                            cv2.circle(output, (x, y), 5, color_mouse_pointer, -1)
                        if detect_num_tres(hand_landmarks):
                            playsound("/home/alejandro_jm/Documentos/hackaton_tinku/sonido3.mp3", True)
                            print("tres")
                            #pyautogui.click()
                            cv2.circle(output, (x, y), 10, color_mouse_pointer, 3)
                            cv2.circle(output, (x, y), 5, color_mouse_pointer, -1)
                        if detect_num_cuatro(hand_landmarks):
                            playsound("/home/alejandro_jm/Documentos/hackaton_tinku/sonido4.mp3", True)
                            print("cuatro")
                            #pyautogui.click()
                            cv2.circle(output, (x, y), 10, color_mouse_pointer, 3)
                            cv2.circle(output, (x, y), 5, color_mouse_pointer, -1)
                        if detect_num_cinco(hand_landmarks):
                            time.sleep(0.05)
                            print("cinco")

                            #pyautogui.click()
                            cv2.circle(output, (x, y), 10, color_mouse_pointer, 3)
                            cv2.circle(output, (x, y), 5, color_mouse_pointer, -1)
                        if detect_num_seis(hand_landmarks):
                            playsound("/home/alejandro_jm/Documentos/hackaton_tinku/sonido6.mp3", True)
                            print("seis")
                            #pyautogui.click()
                            cv2.circle(output, (x, y), 10, color_mouse_pointer, 3)
                            cv2.circle(output, (x, y), 5, color_mouse_pointer, -1)
                        if detect_num_siete(hand_landmarks):
                            playsound("/home/alejandro_jm/Documentos/hackaton_tinku/sonido7.mp3", True)
                            print("siete")
                            #pyautogui.click()
                            cv2.circle(output, (x, y), 10, color_mouse_pointer, 3)
                            cv2.circle(output, (x, y), 5, color_mouse_pointer, -1)
                        if detect_num_ocho(hand_landmarks):
                            playsound("/home/alejandro_jm/Documentos/hackaton_tinku/sonido8.mp3", True)
                            print("ocho")
                            #pyautogui.click()
                            cv2.circle(output, (x, y), 10, color_mouse_pointer, 3)
                            cv2.circle(output, (x, y), 5, color_mouse_pointer, -1)
                        if detect_num_nueve(hand_landmarks):
                            playsound("/home/alejandro_jm/Documentos/hackaton_tinku/sonido9.mp3", True)
                            print("nueve")
                            #pyautogui.click()
                            cv2.circle(output, (x, y), 10, color_mouse_pointer, 3)
                            cv2.circle(output, (x, y), 5, color_mouse_pointer, -1)
                #cv2.imshow('Frame', frame)
                cv2.imshow('output', output)
                if cv2.waitKey(1) & 0xFF == 27:
                    break

        cap.release()
        cv2.destroyAllWindows()

# Crear la ventana principal
root = tk.Tk()

# Crear una instancia de la clase GUIConBotones
gui_con_botones = GUIConBotones(root)

# Ejecutar la aplicación
root.mainloop()
