"""Demo Flask app showcasing the @limit rate limiter."""
from flask import Flask, jsonify

from .ratelimit import limit


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/ping")
    @limit(max_requests=5, window_seconds=60)
    def ping():
        return jsonify({"pong": True})

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    return app


app = create_app()
