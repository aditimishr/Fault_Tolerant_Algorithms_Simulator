import random
import math

# def poisson(lambda_value, t_dash):
#     t = 0
#     k = 0
#     while(t<=t_dash):
#         k = k+1
#         u = random.uniform(0, 1)
#         # t = random.uniform(0, t_dash)
#         t = t + (-(((math.log(u))/lambda_value)))
#
#     return k-1
#
#
# x = poisson(5, 10000)
# print(x)
#
# def poisson(lambda_value, t_dash):
#     t = 0
#     k = 0
#     L = (-(lambda_value*t_dash))
#     u1 = 1.0
#     while(t>=L):
#         k = k+1
#         u = random.uniform(0, 1)
#         # t = random.uniform(0, t_dash)
#         # t = t + (-(((math.log(u))/lambda_value)))
#         u1 = u1*u
#         t = math.log(u1)
#
#     return k-1
#
#
# x = poisson(5, 100)
# print(x)

def poisson(lambda_number,area):
    L = math.exp(-(lambda_number*area))
    p = 1.0
    k = 0

    while(p>L):
        k = k+1
        p = p * random.uniform(0, 1)

    return k-1

x = poisson(5,10000)
print(x)

# def poisson(lambda_number,area):
#     L = math.exp(-(lambda_number))
#     p = 1.0
#     k = 0
#
#     while(p>L):
#         k = k+1
#         p = p * random.uniform(0, 1)
#
#     return k-1
#
# x = poisson(5,1000000)
# print(x)