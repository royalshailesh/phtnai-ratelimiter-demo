# Rate Limiter - Design

**Requirements:** requirements.md
**Version:** 1.0.0

## Architecture Overview

The limiter is a decorator factory `limit(max_requests, window_seconds)` that
wraps a Flask view. On each call it derives a key of `"{client_ip}:{path}"`,
records a hit in a sliding-window store, and compares the rolling count to the
ceiling.

```
graph TD
  A[Request] --> B[limit decorator]
  B --> C[store.hit key,window]
  C --> D{count > ceiling?}
  D -- yes --> E[429 + Retry-After]
  D -- no --> F[run view]
```

## Components

- **store.hit(key, window_seconds)**: append now(), drop entries older than the
  window, return current count.
- **limit(...)**: compares count to ceiling, short-circuits with 429 when over.

## Error Handling

Exceeding the limit yields a JSON body `{"error": "rate limit exceeded"}` with
status 429 and `Retry-After`.
