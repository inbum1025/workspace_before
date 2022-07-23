#! /usr/bin/env python3

# 우주궤도역학 과제3
# 위성 궤도 3차원 공간에서 표출하기

##############################################################

import math
import numpy as np
import matplotlib.pyplot as plt


def final():
    # 입력값; 궤도 요소 6가지
    a = float(input('장반경[DU] a:'))          # 장반경 semi-major axis
    e = float(input('이심률 e:'))                 # 이심률 eccentricity
    i = float(input('경사각 i:'))                 # 경사각 inclination
    Omg = float(input('적경각 \u03A9:'))          # 적경각 right ascension
    omg = float(input('근점편각 \u03C9:'))         # 근점편각 argument of  perigee
    nu = float(input('실제 비행각[deg] \u03BD:'))        # 실제 비행각 true anomaly
    nu = nu * math.pi / 180

    # 궤도 파라미터 계산
    p = a * (1 - e**2)                  # semi-latus rectum(side straight)
    b = math.sqrt(a**2 * (1 - e**2))    # semi-minor axis
    c = a * e                           # focus point
    rp = a * (1 - e)                    # periapsis

    # 인공위성 궤도
    nus = np.arange(0, 2*math.pi, 0.01)
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    for nu_i in nus:
        r = p / (1 + e * np.cos(nu_i))          # r
        x = r * math.cos(nu_i) + c              # x
        y = r * math.sin(nu_i)                  # y

        ax.scatter(x, y, c='k', s=0.5)

    # 지구
    ax.scatter(c, 0, 0, c='b', s=50)        # 지구 위치

    # 적도면
    X = np.arange(-a-2, a+2, 0.25)
    Y = np.arange(-b-2, b+2, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    #Z = np.zeros(X.shape)
    Z = X * math.atan(-i)
    ax.plot_surface(X, Y, Z, linewidth=0, antialiased=False, alpha=0.2)

    # 위성 위치
    r_sat = p / (1 + e * np.cos(nu))        # 위성 r
    x_sat = r_sat * math.cos(nu) + c        # 위성 x
    y_sat = r_sat * math.sin(nu)            # 위성 y
    ax.scatter(x_sat, y_sat, 0, marker='s', c='k', s=30)

    # ECI(지구중심관성좌표계, Earth-Centered Inertial Frame) 축
    ax.plot([0, 0], [-b-2, 0], [0, 0], lw=1,
            c='k')                         # ECI i1
    ax.plot([0, (a+2)], [0, 0], [0, (a+2)*math.atan(-i)],
            lw=1, c='k')      # ECI i2

    ax.set_xlim(-a-1, a+1)
    ax.set_ylim(-b-1, b+1)
    plt.show()
