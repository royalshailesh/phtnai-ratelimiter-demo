# phtnai-ratelimiter-demo

A small Flask service demonstrating a **per-route rate limiter** exposed as a
`@limit` decorator. Used as a reference target for the PHTN.AI
Requirements -> Design -> Tests and PR Regression Impact pipelines.

## Architecture

- `src/app.py` - Flask application factory, wires routes to the limiter.
- `src/ratelimit.py` - the `@limit(max_requests, window_seconds)` decorator.
- `src/store.py` - in-memory sliding-window hit counter.
- `tests/` - pytest suite for the limiter and the app.

## Features

- **Rate limiting**: cap requests per client IP per route within a time window.
- **429 responses**: return HTTP 429 with a `Retry-After` header when exceeded.
- **Health check**: unthrottled `/health` endpoint.
