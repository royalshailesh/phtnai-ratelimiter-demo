"""In-memory sliding-window request counters keyed by client + route."""
import time
from collections import defaultdict

_BUCKETS: dict[str, list[float]] = defaultdict(list)


def hit(key: str, window_seconds: int) -> int:
    """Record a hit for key, drop entries older than the window, return count."""
    now = time.time()
    cutoff = now - window_seconds
    bucket = [t for t in _BUCKETS[key] if t >= cutoff]
    bucket.append(now)
    _BUCKETS[key] = bucket
    return len(bucket)


def reset(key: str) -> None:
    _BUCKETS.pop(key, None)
