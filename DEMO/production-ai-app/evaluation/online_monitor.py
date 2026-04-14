"""Simple online monitoring utilities."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class OnlineMonitor:
    latencies_ms: list[float] = field(default_factory=list)
    successes: int = 0
    failures: int = 0

    def record(self, latency_ms: float, success: bool) -> None:
        self.latencies_ms.append(latency_ms)
        if success:
            self.successes += 1
        else:
            self.failures += 1

    def snapshot(self) -> dict[str, float]:
        average_latency = sum(self.latencies_ms) / max(len(self.latencies_ms), 1)
        return {
            "requests": float(len(self.latencies_ms)),
            "successes": float(self.successes),
            "failures": float(self.failures),
            "avg_latency_ms": round(average_latency, 2),
        }


if __name__ == "__main__":
    monitor = OnlineMonitor()
    monitor.record(latency_ms=42.0, success=True)
    monitor.record(latency_ms=57.0, success=True)
    monitor.record(latency_ms=80.0, success=False)
    print(monitor.snapshot())
