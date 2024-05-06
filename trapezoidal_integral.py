from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------


a= 0
b= 1
N= 100

h = ( b - a ) / N

daikei_s = 0

for k in range(1, N):
    x_l = a+(k-1)*h
    x_r = a+k*h
    y_l = sin(x_l)
    y_r = sin(x_r)
    daikei_s += (y_l + y_r) / 2


sekibun = h * daikei_s



print("台形積分の近似値",sekibun)
