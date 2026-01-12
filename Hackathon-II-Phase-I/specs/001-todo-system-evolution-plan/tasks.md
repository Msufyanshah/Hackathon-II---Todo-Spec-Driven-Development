# sp.tasks.phase1.impl

## Purpose

This document defines **Phase I–only implementation tasks** for the Todo application.

These tasks:

* Apply **exclusively to Phase I**
* Are **console-only** and **in-memory only**
* Contain **no frontend, backend, API, database, auth, AI, or network concepts**
* Are written for **Spec-Kit Plus + Claude Code execution**

Phase I tasks are intentionally small, explicit, and sequential to support deterministic agent execution and clear judge review.

---

## Phase I Scope (Locked)

Phase I delivers a **single-user Python console Todo application** with:

* In-memory task storage
* No persistence
* No authentication
* No networking
* No external services

Only **Basic Level features** are permitted:

1. Add Task
2. View Task List
3. Update Task
4. Delete Task
5. Mark Task Complete / Incomplete

---

## Execution Rules

* Tasks MUST be executed **in numeric order**
* Each task is executed via **one Claude Code run**
* No task may introduce concepts outside Phase I scope
* No manual coding is allowed

---

## Phase I — Implementation Tasks

### TASK-P1-001: Initialize Phase I Project Structure

**Objective**: Create the Phase I–only directory and baseline structure.

**Actions**:

* Create `phase-1-console/` directory
* Initialize Python project using UV
* Create `src/` folder and base files

**Acceptance Criteria**:

* Project runs a placeholder Python entry point
* No unused folders or future-phase artifacts exist

**Status**: [X] Completed

---

### TASK-P1-002: Define Task Data Model

**Objective**: Define the in-memory representation of a task.

**Actions**:

* Define Task attributes: id, title, description, completed
* Define data types for each field

**Acceptance Criteria**:

* Task model is explicit and minimal
* No persistence or timestamps required

**Status**: [X] Completed

---

### TASK-P1-003: Define In-Memory Storage Mechanism

**Objective**: Decide how tasks are stored during runtime.

**Actions**:

* Select data structure (list or dictionary)
* Define add, read, update, delete access patterns

**Acceptance Criteria**:

* All task operations work in-memory only
* Data resets on application restart

**Status**: [X] Completed

---

### TASK-P1-004: Define CLI Command Set

**Objective**: Specify all user commands.

**Commands**:

* add
* list
* update
* delete
* complete
* exit

**Acceptance Criteria**:

* Each command maps to exactly one operation
* No ambiguous or overloaded commands

**Status**: [X] Completed

---

### TASK-P1-005: Implement Add Task Flow

**Objective**: Allow user to create a task via CLI.

**Actions**:

* Prompt for title and description
* Generate unique task ID
* Store task in memory

**Acceptance Criteria**:

* Task appears in task list immediately
* Empty titles are rejected

**Status**: [X] Completed

---

### TASK-P1-006: Implement View Task List Flow

**Objective**: Display all tasks.

**Actions**:

* Print task ID, title, and completion status

**Acceptance Criteria**:

* Completed and incomplete tasks are distinguishable
* Empty list handled gracefully

**Status**: [X] Completed

---

### TASK-P1-007: Implement Update Task Flow

**Objective**: Modify existing task data.

**Actions**:

* Select task by ID
* Update title and/or description

**Acceptance Criteria**:

* Invalid IDs handled safely
* Updates reflected immediately

**Status**: [X] Completed

---

### TASK-P1-008: Implement Delete Task Flow

**Objective**: Remove a task.

**Actions**:

* Select task by ID
* Remove from in-memory storage

**Acceptance Criteria**:

* Deleted task no longer appears
* Invalid IDs do not crash app

**Status**: [X] Completed

---

### TASK-P1-009: Implement Mark Complete / Incomplete Flow

**Objective**: Toggle task completion state.

**Actions**:

* Select task by ID
* Toggle completed flag

**Acceptance Criteria**:

* Status updates correctly
* Toggle is reversible

**Status**: [X] Completed

---

### TASK-P1-010: Implement CLI Application Loop

**Objective**: Control program execution.

**Actions**:

* Start application
* Display command menu
* Loop until exit command

**Acceptance Criteria**:

* Application does not terminate unexpectedly
* User can perform multiple operations per run

**Status**: [X] Completed

---

### TASK-P1-011: Implement Input Validation & Error Handling

**Objective**: Prevent crashes and invalid state.

**Actions**:

* Validate command input
* Handle invalid IDs and empty input

**Acceptance Criteria**:

* No unhandled exceptions
* Clear error messages

**Status**: [X] Completed

---

### TASK-P1-012: Phase I Verification

**Objective**: Verify Phase I completeness.

**Checks**:

* All 5 Basic Level features work
* Application runs from CLI
* No out-of-scope features exist

**Acceptance Criteria**:

* Phase I passes all acceptance checks

**Status**: [X] Completed

---

## Phase I Exit Criteria

Phase I is complete when:

* Console app runs correctly
* All CRUD operations function
* State is in-memory only
* No Phase II+ concepts exist

Only after this may Phase II planning begin.