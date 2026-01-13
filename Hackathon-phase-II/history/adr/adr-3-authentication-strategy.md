# ADR-3: Authentication Strategy

## Status
Accepted

## Date
2026-01-12

## Context
We need to implement secure authentication for the multi-user todo application that enforces JWT-based authentication with strict user-level data isolation, as required by the constitutional requirements.

## Decision
We will implement Better Auth for authentication with JWT tokens. This solution provides a complete authentication system with JWT support, social logins, and security best practices out of the box. The implementation will include:

- Authentication Provider: Better Auth
- Token Type: JWT (JSON Web Tokens)
- Token Storage: httpOnly cookies to prevent XSS attacks
- Security: CSRF protection
- Session Management: Stateless JWT tokens with proper expiration

## Alternatives Considered
- Auth0: More complex setup and potential cost considerations
- Custom JWT implementation: Would require more development time and potential security vulnerabilities
- Session-based authentication: Would not meet the stateless JWT requirement
- Next-Auth: Alternative auth solution but Better Auth has better FastAPI integration
- Simple username/password without JWT: Would not meet constitutional requirements

## Consequences
Positive:
- Complete authentication solution with minimal setup
- Built-in security best practices
- Good integration with both Next.js frontend and FastAPI backend
- Support for social logins if needed in the future
- Automatic token refresh mechanisms

Negative:
- Additional dependency with potential vendor lock-in
- Less control over authentication flow compared to custom implementation
- Potential cost implications for production deployment
- Reliance on external service for authentication logic

## References
- plan.md: Constitution Check section
- research.md: Authentication: Better Auth with JWT section
- spec.md: Functional Requirements FR-002, FR-005, FR-015, FR-016