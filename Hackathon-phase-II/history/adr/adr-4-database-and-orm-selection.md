# ADR-4: Database and ORM Selection

## Status
Accepted

## Date
2026-01-12

## Context
We need to select a database solution and ORM for the multi-user todo application that meets constitutional requirements for Neon Serverless PostgreSQL and SQLModel, while supporting proper data isolation and efficient querying.

## Decision
We will use Neon Serverless PostgreSQL as the database with SQLModel as the ORM. This combination provides serverless PostgreSQL with smart caching, automated branching, and great performance, while SQLModel combines the power of SQLAlchemy and Pydantic for type validation and easy serialization.

The complete data layer includes:
- Database: Neon Serverless PostgreSQL
- ORM: SQLModel
- Migration Tool: Alembic (via SQLModel)
- Connection Pooling: Built into Neon

## Alternatives Considered
- SQLite: Not suitable for multi-user application with concurrent access
- MongoDB: Would deviate from the specified SQL requirement
- Raw SQL: Prohibited by constitution (FR-003)
- Traditional PostgreSQL without Neon: Would miss serverless benefits
- SQLAlchemy Core without SQLModel: Would require more boilerplate code
- Prisma: Would require Node.js backend, conflicting with Python requirement

## Consequences
Positive:
- Serverless benefits: automatic scaling, branching, and reduced costs
- Combines SQLAlchemy's power with Pydantic's type validation
- Seamless integration with FastAPI's Pydantic models
- Built-in connection pooling and smart caching
- Automated backup and point-in-time recovery

Negative:
- Learning curve for SQLModel if team is more familiar with traditional ORMs
- Potential vendor lock-in to Neon's specific features
- Serverless database might have cold start latency considerations
- Less mature ecosystem compared to traditional PostgreSQL ORMs

## References
- plan.md: Technical Context section
- research.md: Database: Neon Serverless PostgreSQL with SQLModel section
- spec.md: Functional Requirements FR-003, FR-007