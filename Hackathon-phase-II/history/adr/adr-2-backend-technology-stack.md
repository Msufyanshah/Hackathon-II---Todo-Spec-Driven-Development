# ADR-2: Backend Technology Stack

## Status
Accepted

## Date
2026-01-12

## Context
We need to select a backend technology stack for the multi-user todo web application that provides a secure, performant API with automatic documentation and strong type validation, while meeting constitutional requirements for Python FastAPI.

## Decision
We will use Python 3.11 with FastAPI as the backend framework. FastAPI provides automatic API documentation, type validation through Pydantic, async support, and high performance. The stack will include:

- Framework: FastAPI
- Language: Python 3.11
- Type Validation: Pydantic
- Async Support: Built-in with FastAPI
- Testing: pytest with fixtures

## Alternatives Considered
- Flask: Less modern, requires more boilerplate for validation and documentation
- Django: Overkill for a todo application, heavier framework with more built-in components than needed
- Node.js/Express: Would deviate from the specified Python requirement
- Ruby on Rails: Would deviate from the specified Python requirement
- Go with Gin: Would deviate from the specified Python requirement

## Consequences
Positive:
- Automatic interactive API documentation (Swagger UI and ReDoc)
- Built-in type validation and serialization with Pydantic
- High performance comparable to Node.js and Go frameworks
- Excellent async support for handling concurrent requests
- Strong typing throughout the API layer

Negative:
- Smaller ecosystem compared to Flask or Django
- Less mature than more established Python frameworks
- Learning curve for team members unfamiliar with Pydantic and FastAPI patterns

## References
- plan.md: Technical Context section
- research.md: Backend: Python FastAPI section