---
name: harness-backend
description: Design and implement secure, evolvable backend APIs with explicit contracts, authorization, persistence boundaries, and failure semantics. Use for endpoints, services, or schema changes.
---

# Backend contracts before machinery

Inspect the existing API style, authentication, persistence, and deployment
constraints. Define each changed operation's caller, authorization, input schema,
output schema, status codes, error shape, and side effects. Reuse the established
OpenAPI/schema system if present; keep runtime validation and docs aligned.

Design for change with clear boundaries rather than extra infrastructure:
- Separate transport validation, domain decisions, and persistence when the
  existing architecture supports it. Keep modules cohesive; avoid a microservice
  split or generic repository abstraction without a concrete need.
- Prefer backward-compatible additions. For breaking changes, describe migration
  and compatibility explicitly. Do not add version prefixes merely by habit.
- Bound collection queries; use pagination with stable ordering. Define filter
  and sort semantics. Consider indexes and N+1 queries using actual access paths.
- Specify transaction boundaries and consistency guarantees. Use idempotency or
  concurrency control for operations where retries or races can corrupt state.
  Do not add those mechanisms to read-only paths without evidence.
- Treat external services as fallible: timeouts, bounded retries for safe
  operations, and explicit failure responses. Add queues/caches only for a
  demonstrated workload, with invalidation and failure behavior explained.

Apply security at the server boundary, scaled to the actual exposure:
- Authentication is not authorization. Check object ownership, role/function
  access, and allowed fields for each affected operation. Test cross-user access.
- Allow-list writable fields and validate size, type, range, and format. Use
  parameterized queries. Do not return internal stack traces or secret fields.
- Keep credentials server-side. Use established password/session libraries if
  authentication is required; do not roll custom cryptography.
- Consider CSRF for cookie authentication, restrictive CORS, safe uploads, SSRF
  for user-supplied URLs, and resource/rate bounds where relevant.
- Keep useful request/error context without logging credentials or private data.
  Development fixtures must not become real authorization decisions.

Test normal and invalid requests, unauthenticated/forbidden requests, missing
objects, and material retry/conflict cases. Include integration tests against the
real persistence mechanism or an appropriate isolated equivalent; mocks alone
cannot verify transactions, constraints, or query behavior.

Explain an extension scenario the API can accommodate and the point where more
infrastructure would become justified. Do not claim scalability from structure
alone: label throughput expectations as unmeasured unless tested.

Reference for relevant risk classes:
[OWASP API Security](https://owasp.org/API-Security/editions/2023/en/0x11-t10/).
