from typing import NamedTuple


class Limits(NamedTuple):
    max_intensity: float
    min_theta: float | None
    max_theta: float | None
