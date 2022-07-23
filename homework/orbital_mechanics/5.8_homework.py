import math

mu = 3.98*10**5


def calculate_result(pi_initial, r1, r2):
    a = (r1 + r2)/2
    t_trans = math.pi*math.sqrt(a**3/mu)
    ni = math.sqrt(mu/r1**3)
    nt = math.sqrt(mu/r2**3)
    alpha = nt*t_trans
    pi_final = math.pi - alpha
    for k in range(0, 3):
        t_wait = (pi_initial - pi_final + 2*math.pi*k)/(ni - nt)
        print("대기시간(k = {}:)".format(k), round(t_wait, 2), "sec")
    # t_wait_0 = (pi_initial - pi_final + 2*math.pi*0)/(ni - nt)
    # t_wait_1 = (pi_initial - pi_final + 2*math.pi*1)/(ni - nt)
    v_a = math.sqrt(2*mu/r1 - mu/a) - math.sqrt(mu/r1)
    v_b = math.sqrt(mu/r2) - math.sqrt(2*mu/r2 - mu/a)
    v_total = abs(v_a) + abs(v_b)

    print("궤도변경 시간:", round(t_trans, 2), "sec")
    print("속도변화량(v_a):", round(v_a, 4), "km/sec")
    print("속도변화량(v_b):", round(v_b, 4), "km/sec")
    print("속도변화량(v_total):", round(v_total, 4), "km/sec")


# 예제 8번 (초기값, r1,r2 값들을 대입하면 결과값이 출력된다.)
calculate_result(math.pi/6, 6678.137, 42164.137)
