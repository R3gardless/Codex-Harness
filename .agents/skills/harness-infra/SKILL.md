---
name: harness-infra
description: Build separate infrastructure adapters and database support with reproducible configuration, migrations, persistence checks, and recovery. Use for DB setup, external adapters, deployment configuration, or operational changes; not for API-only edits.
---

# Build the infrastructure and DB boundary

Inspect the actual runtime, deployment files, DB engine/version, migration tool,
configuration loading, and existing adapters. Identify the required persistence
or integration path, target environment, data sensitivity, and operating limits.
Reuse the existing stack. A DB layer can use an embedded database; separation
does not imply a new cloud service, container platform, or repository framework.

Keep infrastructure in a separate module such as `infra/`, with DB-specific code
in `infra/db/`, or the host's equivalent. Define the small interface required by
services and inject the adapter at the composition root. Keep connection/client
construction and provider configuration out of API handlers, DTOs, and business
rules. Business transaction intent belongs to services; DB code implements it.

Build one reproducible path from configuration to connection, migration,
read/write, and shutdown before adding optional components:

- Configuration: documented required variables, non-secret example values,
  startup validation, and separate development/test/production targets. Keep
  credentials in the established secret mechanism; exclude them from logs and
  generated artifacts.
- DB: schema, keys, foreign keys, uniqueness, nullability, and indexes tied to
  real queries. Use parameterized access and bounded reads. Define pool limits,
  connection/query timeouts, lifecycle cleanup, and transaction rollback where
  applicable. Count connections across replicas/workers, not just one process.
- Migrations: use the existing migration tool and versioned files. Check a fresh
  DB and upgrade from the supported previous schema with representative fixtures.
  For existing data, consider lock duration, backfill size, and compatibility
  during rollout. State whether rollback or a forward repair is supported;
  destructive changes need a data-preserving recovery plan before execution.
- External adapters: use explicit timeouts, bounded safe retries, and error
  translation. Consider retry multiplication across layers and duplicate effects.
  Add cache/queue/storage adapters only when required, including invalidation,
  delivery/replay, and failure behavior for the components actually used.
- Runtime: supply the required local startup/teardown commands and health checks.
  Separate readiness from process liveness when the platform supports both so a
  dependency outage does not cause needless restart loops. Use existing deployment
  or IaC tooling only when deployment work is in scope.

For a deployed persistence path, identify the relevant recovery and observability
needs: backup/restore, migration failure, capacity exhaustion, dependency outage,
and useful logs/metrics. Tie each risk to the actual configuration and a trigger,
impact, detection signal, and mitigation. Mark missing operational evidence as
unknown; do not claim backups are recoverable without a restore check. Avoid a
provider-wide checklist for components the application does not use.

Verify against an isolated DB with matching relevant engine semantics: clean
startup, migration, CRUD path, constraints, atomic rollback, and persistence after
restart when promised. Cover upgrade behavior and relevant timeout/unavailable
dependency cases. Use safe fixtures; never reset a shared or production database
as a test. Mocks or a different DB engine cannot establish engine-specific query,
locking, migration, or consistency behavior. Mark unavailable checks unverified.

Deliver the adapter/configuration/migration files, exact setup and verification
commands, and remaining operational risks. Preparing these files does not itself
authorize provisioning resources, applying shared-environment migrations, or
changing live data; use the task's existing authorization and environment rules.
