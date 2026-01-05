class Distance:
    def __init__(self, meters: float) -> None:
        self.meters = float(meters)

    def __str__(self) -> str:
        return f"{self.meters} m"

    def __repr__(self) -> str:
        return f"Distance({self.meters})"

    # Operações aritméticas
    def __add__(self, other: "Distance") -> "Distance":
        if not isinstance(other, Distance):
            return NotImplemented
        return Distance(self.meters + other.meters)

    def __iadd__(self, other: "Distance") -> "Distance":
        if not isinstance(other, Distance):
            return NotImplemented
        self.meters += other.meters
        return self

    def __mul__(self, value: float) -> "Distance":
        if not isinstance(value, (int, float)):
            return NotImplemented
        return Distance(self.meters * value)

    def __truediv__(self, value: float) -> "Distance":
        if not isinstance(value, (int, float)):
            return NotImplemented
        return Distance(self.meters / value)

    # Comparações
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            return False
        return self.meters == other.meters

    def __lt__(self, other: "Distance") -> bool:
        return self.meters < other.meters

    def __le__(self, other: "Distance") -> bool:
        return self.meters <= other.meters

    def __gt__(self, other: "Distance") -> bool:
        return self.meters > other.meters

    def __ge__(self, other: "Distance") -> bool:
        return self.meters >= other.meters
