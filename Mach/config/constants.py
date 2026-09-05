# Physical constants of air - ISA (International Standard Atmosphere)
GAMMA = 1.4 # Ratio of specific heats of air (cp/cv)
R = 287.05 # Gas constant for air [J/(kg*K)]
T0 = 288.15 # Temperature at sea level [K] -> 15 C
L = 0.0065 # Thermal gradient [K/m] -> every 1000m drops 6.5 C
G = 9.81 # Gravity [m/s²]

# Simulation
T_MAX = 100 # Max simulation time [s]
DT = 0.1 # Time step [s]
ALTITUDES = [1000, 5000, 10000] # 3 planes at different altitudes = different Mach numbers