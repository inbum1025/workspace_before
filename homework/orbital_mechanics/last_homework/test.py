import tkinter as tk
from turtle import left
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import tkinter as tk
import math
import os


fig, ax = plt.subplots(figsize=(7, 4), subplot_kw={"projection": "3d"})

# GUI정의
root = tk.Tk()


# 위젯---------------------------------------------------------------------


def final(a, e, i, Omg, omg, nu):

    ax = fig.add_subplot(111, projection='3d')

    i = i * math.pi / 180
    Omg = Omg * math.pi / 180
    omg = omg * math.pi / 180
    nu = nu * math.pi / 180
    # --------------------------

    # 궤도 파라미터 계산
    p = a * (1 - e**2)                  # semi-latus rectum(side straight)
    b = math.sqrt(a**2 * (1 - e**2))    # semi-minor axis
    c = a * e                           # focus point
    rp = a * (1 - e)                    # periapsis

    # 인공위성 궤도
    nus = np.arange(0, 2*math.pi, 0.01)
    #fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    for nu_i in nus:
        r = p / (1 + e * np.cos(nu_i))          # r
        x = r * math.cos(nu_i) + c              # x
        y = r * math.sin(nu_i)                  # y

        ax.scatter(x, y, c='k', s=0.5)

    # 적도면
    X = np.arange(-a-2, a+2, 0.25)
    Y = np.arange(-b-2, b+2, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    #Z = np.zeros(X.shape)
    Z = X * math.atan(-i)
    ax.plot_surface(X, Y, Z, linewidth=0, antialiased=False, alpha=0.2)

    # 지구
    ax.scatter(c, 0, 0, c='b', s=50, label='Earth')        # 지구 위치

    # 위성 위치
    r_sat = p / (1 + e * np.cos(nu))        # 위성 r
    x_sat = r_sat * math.cos(nu) + c        # 위성 x
    y_sat = r_sat * math.sin(nu)            # 위성 y
    ax.scatter(x_sat, y_sat, 0, marker='s', c='k', s=30, label='satellite')

    # ECI(지구중심관성좌표계, Earth-Centered Inertial Frame) 축
    ax.plot([0, 0], [-b-2, 0], [0, 0], lw=1,
            c='k')                         # ECI i1
    ax.plot([0, (a+2)], [0, 0], [0, (a+2)*math.atan(-i)],
            lw=1, c='k')      # ECI i2
    ax.set_xlim(-a-2, a+2)
    ax.set_ylim(-b-2, b+2)

    plt.legend(frameon=False)
    plt.show()


def f(text):
    def click():
        # GUI를 통한 새로운 데이터 값들 입력
        a = int(txt.get())
        e = float(txt2.get())
        i = float(txt3.get())
        Omg = float(txt4.get())
        omg = float(txt5.get())
        nu = float(txt6.get())

        final(a, e, i, Omg, omg, nu)

    lbl = tk.Label(root, text=text, font=("Arial", 20))
    lbl_1 = tk.Label(root, width=50, height=5)
    lbl_txt = tk.Label(lbl_1, text="장반경[DU]")
    txt = tk.Entry(lbl_1, width=15)

    lbl_2 = tk.Label(root, width=50, height=5)
    lbl_txt2 = tk.Label(lbl_2, text="이심률")
    txt2 = tk.Entry(lbl_2, width=15)

    lbl_3 = tk.Label(root, width=50, height=5)
    lbl_txt3 = tk.Label(lbl_3, text="경사각[degree]")
    txt3 = tk.Entry(lbl_3, width=15)

    lbl_4 = tk.Label(root, width=50, height=5)
    lbl_txt4 = tk.Label(lbl_4, text="적경각[degree]")
    txt4 = tk.Entry(lbl_4, width=15)

    lbl_5 = tk.Label(root, width=50, height=5)
    lbl_txt5 = tk.Label(lbl_5, text="근점편각[degree]")
    txt5 = tk.Entry(lbl_5, width=15)

    lbl_6 = tk.Label(root, width=50, height=5)
    lbl_txt6 = tk.Label(lbl_6, text="실제비행각[degree]")
    txt6 = tk.Entry(lbl_6, width=15)

    btn = tk.Button(root, text="확인", width=5, command=click)

    lbl.pack()

    lbl_1.pack()
    lbl_txt.pack(side="left")
    txt.pack(side="left")

    lbl_2.pack()
    lbl_txt2.pack(side="left")
    txt2.pack()

    lbl_3.pack()
    lbl_txt3.pack(side="left")
    txt3.pack()

    lbl_4.pack()
    lbl_txt4.pack(side="left")
    txt4.pack()

    lbl_5.pack()
    lbl_txt5.pack(side="left")
    txt5.pack()

    lbl_6.pack()
    lbl_txt6.pack(side="left")
    txt6.pack()

    btn.pack()


f("궤도요소")

# GUI 로 옮기기------------------------------------------------------------------/  ///
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()
root.mainloop()


# plt.tight_layout()
# plt.show()
