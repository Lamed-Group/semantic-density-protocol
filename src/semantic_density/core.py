"""Dependency-free reference calculations for protocol v0.1."""

from __future__ import annotations

from dataclasses import dataclass
from statistics import median, pstdev
from typing import Iterable


@dataclass(frozen=True, slots=True)
class Observation:
    """One measured observation under a declared interpretive lens."""

    nodes: int
    reading_seconds: float
    reflection_seconds: float
    dispersion: float

    def __post_init__(self) -> None:
        if isinstance(self.nodes, bool) or not isinstance(self.nodes, int):
            raise TypeError("nodes must be an integer")
        if self.nodes < 0:
            raise ValueError("nodes must be non-negative")
        if self.reading_seconds <= 0:
            raise ValueError("reading_seconds must be greater than zero")
        if self.reflection_seconds < 0:
            raise ValueError("reflection_seconds must be non-negative")
        if self.dispersion <= 0:
            raise ValueError("dispersion must be greater than zero")

    @property
    def E(self) -> float:
        """Reflection-to-reading time ratio."""

        return self.reflection_seconds / self.reading_seconds

    @property
    def P_observed(self) -> float:
        """Observed semantic density for this lens and context."""

        return self.nodes * self.E / self.dispersion

    def as_dict(self) -> dict[str, float | int]:
        return {
            "N": self.nodes,
            "reading_seconds": self.reading_seconds,
            "reflection_seconds": self.reflection_seconds,
            "E": self.E,
            "D": self.dispersion,
            "P_observed": self.P_observed,
        }


@dataclass(frozen=True, slots=True)
class Summary:
    """Robust descriptive summary across independent observations."""

    count: int
    minimum: float
    median: float
    maximum: float
    population_sd: float

    def as_dict(self) -> dict[str, float | int]:
        return {
            "count": self.count,
            "minimum": self.minimum,
            "median": self.median,
            "maximum": self.maximum,
            "population_sd": self.population_sd,
        }


def summarize(observations: Iterable[Observation]) -> Summary:
    """Summarize P_observed without hiding variation between lenses."""

    values = [item.P_observed for item in observations]
    if not values:
        raise ValueError("at least one observation is required")
    return Summary(
        count=len(values),
        minimum=min(values),
        median=median(values),
        maximum=max(values),
        population_sd=pstdev(values),
    )
