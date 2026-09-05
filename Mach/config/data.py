import numpy as np
from config.constants import GAMMA, R, T0, L, ALTITUDES, T_MAX, DT

def temp_at_h(h):
    # ISA: T(h) = T0 - L*h
    # The higher the altitude, the colder
    return T0 - L * h

def speed_of_sound(h):
    # Physical formula: c = sqrt(gamma * R * T)
    # c depends only on temperature, and T depends on h
    # Therefore, at higher altitudes (colder) -> c is smaller
    T = temp_at_h(h)
    return np.sqrt(GAMMA * R * T)

def generate_flight_data(a=5.0, n=1.5):
    # Vectorized time
    t = np.arange(0, T_MAX, DT)

    # original physics equation X = a * t^n
    X = a * t**n

    # Derived velocity V = dX/dt = a*n*t^(n-1)
    # V[0]=0 to avoid inf at t=0
    V = a * n * t**(n-1)
    V[0] = 0

    results = {}
    for h in ALTITUDES:
        # c is constant per height (because h is fixed per plane)
        c = speed_of_sound(h)

        # Mach = V / c -> here is the magic
        # Same V, but different c for height = different Mach
        M = V / c

        results[h] = {'t': t, 'X': X, 'V': V, 'M': M, 'c': c}

    return results


data = generate_flight_data()
print(data[1000]['M'][-1]) #The aircraft's Mach number dropped at the end.
print(data[10000]['M'][-1]) # Mach of the high plane at the end -> it must be higher