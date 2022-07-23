import math


# 태양중심
def planet_travel(alpha_initial, r_e, r_p, r_e_radius, r_p_radius):
    alpha_initial = alpha_initial * math.pi / 180
    mu_sun = 1.3 * 10**11  # km/s
    mu_planet = 4.3*10**4
    mu_earth = 4*10**5  # km/s
    r_e_park = r_e_radius + 300
    r_p_park = r_p_radius + 200

    a = (r_e + r_p)/2

    e_trans = -(mu_sun/(2*a))

    v_e = math.sqrt(mu_sun/r_e)
    v_p = math.sqrt(mu_sun/r_p)

    v_e_delta = math.sqrt(2*(mu_sun/r_e + e_trans)) - v_e
    v_p_delta = v_p - math.sqrt(2*(mu_sun/r_p + e_trans))

    # 지구중심

    e_hyper_e = (v_e_delta)**2 / 2
    v_e_burn = math.sqrt(2*(mu_earth/r_e_park + e_hyper_e)
                         ) - math.sqrt(mu_earth/r_e_park)

    # 행성중심

    e_hyper_p = (v_p_delta)**2 / 2

    v_p_burn = math.sqrt(mu_planet/r_p_park) - \
        math.sqrt(2*(mu_planet/r_p_park + e_hyper_p))

    # 종합

    t_flight = math.pi * math.sqrt(a**3/mu_sun)  # 비행시간

    n_earth = math.sqrt(mu_sun/r_e**3)  # 지구의 공전 각속도
    n_planet = math.sqrt(mu_sun/r_p**3)  # 행성의 공전 각속도

    alpha_lead = n_planet * t_flight  # 리드각
    alpha_final = math.pi - alpha_lead  # 위상각

    for k in range(0, 3):
        global t_wait
        t_wait = (alpha_initial - alpha_final +
                  2*math.pi*k)/(n_earth - n_planet)
        print("대기시간:", t_wait, "sec")

    v_mission = abs(v_e_burn) + abs(v_p_burn)

    print("비행시간", t_flight, "sec")
    print("지구궤도이탈 속도변화량", v_e_burn, "km/s")
    print("행성진입 속도변화량", v_p_burn, "km/s")
    print("총속도변화량", v_mission, "km/s")


# alpha_initial, r_e, r_p, r_e_radius, r_p_radius
planet_travel(60, 1.5*10**8, 2.2*10**8, 6300, 3400)
