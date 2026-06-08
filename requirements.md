---
# Rate Limiter - Requirements

**Feature ID:** FEAT-001
**Version:** 1.0.0
**Status:** Approved
**Priority:** P1
**Domain:** Web / API Infrastructure
---

## Overview

Provide a per-route rate limiter for the Flask service, exposed as a `@limit`
decorator, to protect endpoints from abuse and accidental overload.

## Functional Requirements

- **FR-1**: A route annotated with `@limit(max_requests, window_seconds)` MUST
  reject requests beyond `max_requests` within any rolling `window_seconds`.
- **FR-2**: When the limit is exceeded the service MUST return HTTP `429` with a
  `Retry-After` header set to the window length in seconds.
- **FR-3**: Limits MUST be tracked per client IP and per route path independently.
- **FR-4**: The `/health` endpoint MUST never be rate limited.

## Non-Functional Requirements

- **NFR-1**: Limit checks MUST add < 5ms overhead per request.
- **NFR-2**: Counter storage MUST be pluggable (in-memory default).
