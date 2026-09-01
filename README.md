
## Architecture

### POO/ - Basic OOP Refactor
Refactor of original script into classes. Keeps coupled physics + rendering as original did.
- `POO/models/airplane_race.py`: Artist + physics `X=a*t^n` together (optimized with `t_safe` and vectorized SHAPE)
- `POO/config/airplane_config.py`: Defines 3 airplanes

### Mach/ - Advanced OOP + Mach Extension
Decoupled architecture using Manager pattern + ISA atmosphere model.
- `Mach/models/airplane_speed.py`: Pure renderer, no physics. Uses `OFFSETS` dict.
- `Mach/config/data.py`: Physics source `X(t)`, `V(t)`, `M(t) = V(t)/c(h)` with ISA `c(h)=sqrt(gamma*R*T(h))`
- `Mach/managers/`: 5 managers (air, building, graph, text, trail)
- `Mach/plots/animator.py`: Composition root

## No Duplication
Two airplane models are intentional:
- POO version: coupled for simplicity (v1)
- Mach version: decoupled for scalability (v2)

## Run

```bash
python -m POO.models.airplane_race
python -m Mach.speed`
```

Roadmap to Mach
POO refactor
Manager architecture
ISA model c(h) in data.py
Mach number plot + text