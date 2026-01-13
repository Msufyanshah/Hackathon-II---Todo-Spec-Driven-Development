# Hackathon-phase-II

This project follows the principles outlined in our constitution for spec-driven development.

## Core Principles

### Spec-first Development
All implementation must originate from an approved specification; no coding without a corresponding spec document.

### Agentic Workflow Integrity
Follow the prescribed workflow sequence: Write spec → Plan → Tasks → Claude Code execution; maintain integrity of each phase.

### Zero Manual Coding
All code generation must occur through Claude Code + Spec-Kit Plus; manual code edits are prohibited.

### User Data Isolation and Security
Implement strict per-user task ownership with no cross-user data visibility under any condition.

### Reproducibility and Auditability
Maintain comprehensive records of all steps, prompts, and iterations to ensure reviewability.

## Technology Stack

- **Frontend**: Next.js 16+ (App Router), TypeScript, Tailwind CSS
- **Backend**: Python FastAPI
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth (JWT enabled)
- **Spec System**: GitHub Spec-Kit + Spec-Kit Plus
- **AI Implementation**: Claude Code only

## Project Structure

The project follows a monorepo structure with clear separation:
- `/frontend` for Next.js application
- `/backend` for FastAPI application
- `/specs` as the single source of truth

## API Endpoints

The application implements the following REST-compliant endpoints:
- GET /api/{user_id}/tasks
- POST /api/{user_id}/tasks
- GET /api/{user_id}/tasks/{id}
- PUT /api/{user_id}/tasks/{id}
- DELETE /api/{user_id}/tasks/{id}
- PATCH /api/{user_id}/tasks/{id}/complete

## Security

- Stateless authentication using JWT
- JWT verification occurs on every API request
- Task access is filtered by authenticated user ID
- Shared secret (BETTER_AUTH_SECRET) is identical across frontend and backend

## Code Quality Standards

- All code changes require approval from at least one other team member
- Code reviews verify compliance with all constitutional requirements
- Test coverage must be 80% or higher for all new features
- Code must pass all linting and formatting checks before merging

## Source Verification

- All external dependencies must be verified against known security databases
- Dependencies must be pinned to specific versions in package managers
- Any dependency with known vulnerabilities (CVSS score > 7.0) must be updated or justified
- All code from external sources must be properly attributed

## Getting Started

1. Ensure you have the required technology stack installed
2. Follow the agentic workflow: Write spec → Plan → Tasks → Claude Code execution
3. All features must be derived directly from Spec-Kit specifications
4. Reference specs using @specs/... notation

## Contributing

All contributions must comply with the project constitution. Manual code edits are prohibited. All code must be generated through Claude Code + Spec-Kit Plus following the spec-first development approach.