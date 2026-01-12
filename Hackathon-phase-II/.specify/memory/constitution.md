<!-- SYNC IMPACT REPORT
Version change: 1.1.0 → 1.2.0
Modified principles: Documentation Requirements section updated with testable standards
Added sections: Code Quality Standards, Source Verification
Removed sections: None
Templates requiring updates:
- ✅ .specify/templates/plan-template.md - Updated
- ✅ .specify/templates/spec-template.md - Updated
- ✅ .specify/templates/tasks-template.md - Updated
- ⚠️  .specify/templates/commands/*.md - Review for principle alignment
- ⚠️  README.md - Review for principle alignment
Follow-up TODOs: None
-->

# Hackathon-phase-II Constitution

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

## Key Standards

### Feature Development
All features must be derived directly from Spec-Kit specifications; all backend and frontend changes must reference specs using @specs/...

### API Compliance
REST API must follow documented endpoints and HTTP methods exactly; all endpoints must remain REST-compliant.

### Authentication Standard
Authentication must use Better Auth with JWT; no alternative auth mechanisms are permitted.

### Database Access
Database access must use SQLModel only; no raw SQL is allowed.

### Configuration Management
Environment configuration must be handled via environment variables only.

### Security Verification
JWT verification must occur on every API request; unauthorized requests must return 401 Unauthorized.

### Task Access Control
Task access must always be filtered by authenticated user ID.

## Technology Standards

### Frontend Stack
Next.js 16+ (App Router), TypeScript, Tailwind CSS

### Backend Stack
Python FastAPI

### ORM
SQLModel

### Database
Neon Serverless PostgreSQL

### Authentication
Better Auth (JWT enabled)

### Spec System
GitHub Spec-Kit + Spec-Kit Plus

### AI Implementation
Claude Code only

## Architectural Constraints

### Monorepo Structure
Maintain clear separation: /frontend for Next.js application, /backend for FastAPI application, /specs as the single source of truth.

### Project Organization
Each project phase exists as a top-level folder, not a sub-folder; GitHub submissions may appear as subdirectories, but internal structure must remain flat.

### Documentation Files
Multiple CLAUDE.md files must be used: Root CLAUDE.md for global rules, /frontend/CLAUDE.md for UI and client logic, /backend/CLAUDE.md for API and database logic.

## API Behavior Rules

### Defined Endpoints
Include: GET /api/{user_id}/tasks, POST /api/{user_id}/tasks, GET /api/{user_id}/tasks/{id}, PUT /api/{user_id}/tasks/{id}, DELETE /api/{user_id}/tasks/{id}, PATCH /api/{user_id}/tasks/{id}/complete

### JWT Token Handling
JWT token must be passed via: Authorization: Bearer <token>

### Backend Requirements
Verify JWT signature, extract authenticated user identity, match token user with URL user, filter database queries accordingly.

## Security Principles

### Stateless Authentication
Use JWT without backend dependency on frontend session storage; enforce JWT expiry (e.g., 7 days).

### Shared Secrets
Shared secret (BETTER_AUTH_SECRET) must be identical across frontend and backend.

## Documentation Requirements

### Spec Organization
Organize specs under: /specs/features, /specs/api, /specs/database, /specs/ui.

### Spec Format
Specs must be written in structured markdown with the following requirements:
- Each functional requirement must have a unique identifier (FR-###)
- All requirements must have acceptance criteria that are objectively testable
- Requirement changes must be tracked with before/after documentation
- All external dependencies must be cited with version numbers and source URLs

### Claude Code Prompts
Claude Code prompts must explicitly reference specs.

## Code Quality Standards

### Code Review Process
- All code changes require approval from at least one other team member
- Code reviews must verify compliance with all constitutional requirements
- Reviewers must validate that new code has corresponding tests

### Code Quality Metrics
- Test coverage must be 80% or higher for all new features
- Code must pass all linting and formatting checks before merging
- No new technical debt may be introduced without explicit approval and tracking

## Source Verification

### Dependency Management
- All external dependencies must be verified against known security databases
- Dependencies must be pinned to specific versions in package managers
- Any dependency with known vulnerabilities (CVSS score > 7.0) must be updated or justified

### Code Attribution
- All code from external sources must be properly attributed
- Third-party code must be reviewed for license compatibility
- No code from unverified sources may be integrated into the codebase

## Constraints

### Prohibited Practices
Manual code edits are prohibited; no deviation from defined tech stack; no additional authentication libraries; no inline styles in frontend; no undocumented endpoints or database fields; no shared database sessions between users.

## Success Criteria

### Implementation Goals
All Phase-II basic features implemented as a working web application; full compliance with Spec-Kit structure and references; secure, JWT-protected REST API; persistent task storage in Neon PostgreSQL; each user can only view and modify their own tasks; frontend and backend fully functional under Claude Code execution; all phases, prompts, specs, and iterations are review-ready for hackathon evaluation.

## Definition of Done

### Completion Requirements
Specs accurately reflect the implemented system; application runs locally and in production environments; authentication and authorization verified across all endpoints; no unauthorized access paths exist; project passes hackathon Phase-II technical review without exceptions.

## Governance

All development practices must comply with this constitution; amendments require formal documentation and approval process; all team members must verify compliance during reviews; complexity must be justified with clear benefits.

**Version**: 1.2.0 | **Ratified**: 2025-06-13 | **Last Amended**: 2026-01-12