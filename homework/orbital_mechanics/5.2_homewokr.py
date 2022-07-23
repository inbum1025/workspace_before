import math

u = 3.98*10**5


def caculate_result(r1, r2, rb):
    a1 = (r1 + rb)/2
    a2 = (rb + r2)/2
    et1 = -u/(2*a1)
    et2 = -u/(2*a2)
    v1 = math.sqrt(2*((u/r1) + et1)) - math.sqrt(u/r1)
    v2 = math.sqrt(2*((u/rb) + et2)) - math.sqrt(2*((u/rb) + et1))
    v3 = math.sqrt(u/r2) - math.sqrt(2*((u/r2) + et2))
    v_total = abs(v1) + abs(v2) + abs(v3)
    time_trans = math.pi*math.sqrt(a1**3/u) + math.pi*math.sqrt(a2**3/u)

    print("속도 변화량:", round(v_total, 4), "km/s")
    print("궤도변경 시간:", round(time_trans, 1), "sec")


# 예제 2번 (r1,r2,rb 값들을 대입하면 결과값이 출력된다.)
caculate_result(6678.137, 42164.137, 106378.137)
