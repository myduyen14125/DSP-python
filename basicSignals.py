import numpy as np
import matplotlib.pyplot as plt

# function to generate unit step u[n-a]
def unit_step(a, n):
  unit = []
  for sample in n:
    if sample >= a:
      unit.append(1)
    else:
      unit.append(0)
  return (unit)

# function to plot impulse signal d(a)
def unit_impulse(a, n):
  delta = []
  for sample in n: 
    if sample == a:
      delta.append(1)
    else:
      delta.append(0)
  return delta

# function to generate unit ramp signal r(n), r(n) = n if n >= 0, r(n) = 0 otherwise
def unit_ramp(n):
  ramp = []
  for sample in n:
    if sample < 0:
      ramp.append(0)
    else:
      ramp.append(sample)
  return ramp

# function to generate exponential signal e^at
def exponential(a, n):
  expo = []
  for sample in n:
    expo.append(np.exp(a * sample))
  return expo

a = 2
UL = 10
LL = -10
n = np.arange(LL, UL, 1)

# plot unit step function u[n-a]
# unit = unit_step(a, n)
# plt.stem(n, unit)
# plt.xlabel('n')
# plt.xticks(np.arange(LL, UL, 1))
# plt.ylabel('u[n]')
# plt.yticks([0,1])
# plt.title('Unit Step u[n-a]')
# plt.show()

# d = unit_impulse(a, n)
# plt.stem(n, d)
# plt.xlabel('n')
# plt.xticks(np.arange(LL, UL, 1))
# plt.ylabel('d[n]')
# plt.yticks([0, 1])
# plt.title('Unit impulse d[2]')
# plt.show()

# r = unit_ramp(n)
# plt.stem(n, r)
# plt.xlabel('n')
# plt.xticks(n)
# plt.ylabel('r[n]')
# plt.yticks([0, UL, 1])
# plt.title('Unit ramp r[n]')
# plt.show()

UL = 1
LL = -1
n = np.arange(LL, UL, 0.1)
x = exponential(a, n)
plt.stem(n, x)
plt.xlabel('n')
plt.xticks(n)
plt.ylabel('x[n]')
plt.title('Exponential sequence signal e^(an)')
plt.savefig("Exponential.png")
plt.show()

