"""Per-route rate limiting decorator for Flask (sliding window + burst)."""
import functools

from flask import jsonify, request

from .store import hit


def limit(max_requests: int, window_seconds: int = 60, burst: int = 0):
    """Limit a route to max_requests (+burst) within a sliding window per IP."""
    ceiling = max_requests + max(burst, 0)

    def decorator(view):
        @functools.wraps(view)
        def wrapper(*args, **kwargs):
            key = f"{request.remote_addr}:{request.path}"
            count = hit(key, window_seconds)
            if count > ceiling:
                resp = jsonify({"error": "rate limit exceeded", "limit": ceiling})
                resp.status_code = 429
                resp.headers["Retry-After"] = str(window_seconds)
                return resp
            return view(*args, **kwargs)
        return wrapper
    return decorator
