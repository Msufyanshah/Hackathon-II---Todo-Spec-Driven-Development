---
id: 1
title: Update Project Constitution
stage: constitution
date_iso: 2026-01-12
surface: agent
model: Qwen
feature: none
branch: main
user: user
command: /sp.constitution
labels:
  - constitution
  - governance
  - principles
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
  - README.md
tests_yaml:
  - none
---

# Prompt History Record: Update Project Constitution

## Original Prompt

```
"""Core principles:

Spec-first development (no implementation without an approved specification)

Agentic workflow integrity (Write spec → Plan → Tasks → Claude Code execution)

Zero manual coding (all code generated via Claude Code + Spec-Kit Plus)

User data isolation and security (strict per-user task ownership)

Reproducibility and auditability (all steps, prompts, and iterations reviewable)

Key standards:

All features must be derived directly from Spec-Kit specifications

All backend and frontend changes must reference specs using @specs/...

REST API must follow documented endpoints and HTTP methods exactly

Authentication must use Better Auth with JWT, no alternative auth mechanisms

Database access must use SQLModel only, no raw SQL

Environment configuration must be handled via environment variables only

JWT verification must occur on every API request

Unauthorized requests must return 401 Unauthorized

Task access must always be filtered by authenticated user ID

Technology standards:

Frontend: Next.js 16+ (App Router), TypeScript, Tailwind CSS

Backend: Python FastAPI

ORM: SQLModel

Database: Neon Serverless PostgreSQL

Authentication: Better Auth (JWT enabled)

Spec System: GitHub Spec-Kit + Spec-Kit Plus

AI Implementation: Claude Code only

Architectural constraints:

Monorepo structure with clear separation:

/frontend for Next.js application

/backend for FastAPI application

/specs as the single source of truth

Each project phase exists as a top-level folder, not a sub-folder

GitHub submissions may appear as subdirectories, but internal structure must remain flat

Multiple CLAUDE.md files must be used:

Root CLAUDE.md for global rules

/frontend/CLAUDE.md for UI and client logic

/backend/CLAUDE.md for API and database logic

API behavior rules:

All endpoints must remain REST-compliant

Endpoints include:

GET /api/{user_id}/tasks

POST /api/{user_id}/tasks

GET /api/{user_id}/tasks/{id}

PUT /api/{user_id}/tasks/{id}

DELETE /api/{user_id}/tasks/{id}

PATCH /api/{user_id}/tasks/{id}/complete

JWT token must be passed via:

Authorization: Bearer <token>


Backend must:

Verify JWT signature

Extract authenticated user identity

Match token user with URL user

Filter database queries accordingly

Security principles:

Stateless authentication using JWT

No backend dependency on frontend session storage

JWT expiry enforced (e.g., 7 days)

Shared secret (BETTER_AUTH_SECRET) must be identical across frontend and backend

No cross-user data visibility under any condition

Documentation requirements:

Specs must be organized under:

/specs/features

/specs/api

/specs/database

/specs/ui

Specs must be written in structured markdown

Any requirement change must update the relevant spec first

Claude Code prompts must explicitly reference specs

Constraints:

Manual code edits are prohibited

No deviation from defined tech stack

No additional authentication libraries

No inline styles in frontend

No undocumented endpoints or database fields

No shared database sessions between users

Success criteria:

All Phase-II basic features implemented as a working web application

Full compliance with Spec-Kit structure and references

Secure, JWT-protected REST API

Persistent task storage in Neon PostgreSQL

Each user can only view and modify their own tasks

Frontend and backend fully functional under Claude Code execution

All phases, prompts, specs, and iterations are review-ready for hackathon evaluation

Definition of done:

Specs accurately reflect the implemented system

Application runs locally and in production environments

Authentication and authorization verified across all endpoints

No unauthorized access paths exist

Project passes hackathon Phase-II technical review without exceptions"""
```

## Response Summary

Updated the project constitution with the specified principles and standards. The new constitution includes:

- Core principles: Spec-first development, agentic workflow integrity, zero manual coding, user data isolation, and reproducibility
- Key standards: Feature derivation from specs, API compliance, authentication standards, database access rules
- Technology standards: Frontend (Next.js 16+), Backend (Python FastAPI), ORM (SQLModel), Database (Neon PostgreSQL)
- Architectural constraints: Monorepo structure, project organization, documentation files
- API behavior rules: REST compliance, defined endpoints, JWT handling
- Security principles: Stateless authentication, shared secrets
- Documentation requirements: Spec organization and format
- Constraints: Prohibited practices
- Success criteria: Implementation goals
- Definition of done: Completion requirements

Updated dependent templates to align with the new constitution, including:
- Plan template with constitution check items
- Spec template with functional requirements aligned to constitution
- Tasks template with constitution-compliant task definitions
- Created a new README file reflecting the constitutional principles

## Outcome

The project constitution has been successfully updated to version 1.1.0 with all specified principles. Dependent templates have been updated to align with the new constitution. The sync impact report indicates all required changes have been made.