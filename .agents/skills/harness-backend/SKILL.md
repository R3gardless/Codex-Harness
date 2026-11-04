---
name: harness-backend
description: Implement backend APIs with separate API, DTO, service, infrastructure, and DB responsibilities, explicit contracts, authorization, and failure semantics. Use for endpoints, services, or schema changes.
---

# Backend contracts before machinery

Inspect the existing API style, authentication, persistence, and deployment
constraints. Define each changed operation's caller, authorization, input schema,
output schema, status codes, error shape, and side effects. Reuse the established
OpenAPI/schema system if present; keep runtime validation and docs aligned.

Before implementation, map the operation to distinct responsibilities. Use the
host project's equivalent names and module layout; for new code a useful shape
is `api/`, `dto/`, `services/`, `infra/`, with DB code in `infra/db/`. These are
code boundaries, not a requirement for separate deployments or microservices.

| Layer | Owns | Must not own |
| --- | --- | --- |
| `api` | Routes/controllers, authentication context, DTO validation, service calls, HTTP response/error mapping | Business decisions, direct SQL/ORM access |
| `dto` | Explicit request/response schemas, allowed fields, serialization contracts | I/O, business orchestration, exposing ORM entities as public responses |
| `services` | Use cases, business rules, object/tenant authorization, transaction intent | HTTP request/response objects, framework handlers, concrete DB/client setup |
| `infra` | External clients, configuration, timeouts, adapter implementations | Product rules or dependencies on API handlers |
| `infra/db` | Connections/pools, persistence mappings, queries/repositories, migrations, constraints, transaction mechanics | HTTP contracts or transport error mapping |

The request flow is API + DTO validation → service → persistence/external
adapter → response DTO. Inject infrastructure dependencies at the composition
root using the existing framework. Services describe required operations through
small contracts or existing interfaces; concrete adapters satisfy them. DTOs
stay independent of handlers and ORM models. Services decide transaction scope;
DB adapters execute it without hidden per-call commits that break atomicity.
Use explicit response mapping so internal fields cannot leak.

Preserve existing public interfaces. For legacy code, apply boundaries to the
changed flow and explain remaining coupling; do not force a whole-project rewrite
or create empty layers. When infrastructure or persistence setup is needed, use
[harness-infra](../harness-infra/SKILL.md) for the working DB/configuration slice.

Design for compatible change and bounded resource use:

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
objects, and material retry/conflict cases. Cover API/DTO contracts, service rules
and authorization independently, then an end-to-end request through the adapters.
Include DB integration tests for migrations, constraints, rollback, and relevant
concurrency using the real persistence mechanism or an isolated equivalent that
preserves those semantics; mocks alone cannot verify them. Run existing import
or architecture checks for dependency direction when available.

Explain an extension scenario the API can accommodate and the point where more
infrastructure would become justified. Do not claim scalability from structure
alone: label throughput expectations as unmeasured unless tested.

Reference for relevant risk classes:
[OWASP API Security](https://owasp.org/API-Security/editions/2023/en/0x11-t10/).
