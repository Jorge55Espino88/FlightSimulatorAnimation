# Airplane Race - Air Race Simulation

Simulation of 3 airplanes with different laws of motion `X = a * t^n` for analysis of distance and speed vs time.

![Race Demo](race.gif)
*Figure: Simulation capture - 3 planes at different altitudes*

### Model Physics

Every plane follows a power law:

- **Position:** `X(t) = a * t^n` [km]
- **Speed:** `V(t) = dX/dt = n * a * t^(n-1)` [km/hr]

Configured aircraft:
- **Plane 1 (Red):** `X = 800 * t^1` -> Uniform motion, constant V=800
- **Plane 2 (Blue):** `X = 1131 * t^0.5` -> Decelerated, V decreases as t^-0.5
- **Plane 3 (Green):** `X = 200 * t^3` -> Accelerated, V grows as t^2

> Original concept by Mark Misin Engineering. See LICENSE.

###Features

- Scalable OOP: adding a plane is 1 line in `configs`
- Animation with 3 synchronized subplots
- Optimized wake calculation with slicing
- Graphs of X(t) and V(t) in real time

### Installation

```bash
pip install numpy matplotlib