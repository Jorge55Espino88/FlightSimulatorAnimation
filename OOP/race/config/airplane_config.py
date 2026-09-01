from dataclasses import dataclass

@dataclass
class AirplaneConfig:
    """Configuración física de cada avión"""
    a: float # coeficiente
    n: float # exponente: X = a * t^n
    altitude: float
    color: str
    label: str