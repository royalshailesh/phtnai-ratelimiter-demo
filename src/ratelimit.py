"""Per-route rate limiting decorator for Flask."""
import functools

from flask import jsonify, request

from .store import hit


def limit(max_requests: int, window_seconds: int = 60):
    """Limit a route to max_requests within window_seconds per client IP."""
    def decorator(view):
        @functools.wraps(view)
        def wrapper(*args, **kwargs):
            key = f"{request.remote_addr}:{request.path}"
            count = hit(key, window_seconds)
            if count > max_requests:
                resp = jsonify({"error": "rate limit exceeded"})
                resp.status_code = 429
                resp.headers["Retry-After"] = str(window_seconds)
                return resp
            return view(*args, **kwargs)
        return wrapper
    return decorator
