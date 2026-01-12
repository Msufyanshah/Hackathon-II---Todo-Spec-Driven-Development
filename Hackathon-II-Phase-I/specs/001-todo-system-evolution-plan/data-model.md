# Data Model: Todo System Evolution

## Entity: Task

### Attributes
- `id` (string, required): Unique identifier for the task
- `title` (string, required): Title of the task
- `description` (string, optional): Detailed description of the task
- `completed` (boolean): Completion status of the task
- `created_at` (datetime): Timestamp when the task was created
- `updated_at` (datetime): Timestamp when the task was last updated
- `owner_id` (string, required): ID of the user who owns the task
- `priority` (string, optional): Priority level (Phase V) - low, medium, high, urgent
- `tags` (array of strings, optional): Tags for categorization (Phase V)
- `due_date` (datetime, optional): Due date for the task (Phase V)
- `recurrence` (string, optional): Recurrence pattern (Phase V) - none, daily, weekly, monthly, yearly

### Validation Rules
- Title must be between 1 and 255 characters
- Description must be less than 1000 characters if provided
- Owner ID must reference an existing user
- Due date must be in the future if provided
- Priority must be one of the allowed values if provided

### State Transitions
- `created` → `active` (default upon creation)
- `active` → `completed` (when marked complete)
- `completed` → `active` (when marked incomplete)

## Entity: User

### Attributes
- `id` (string, required): Unique identifier for the user
- `username` (string, required): Unique username for the user
- `email` (string, required): Valid email address
- `password_hash` (string, required): Hashed password
- `created_at` (datetime): Timestamp when the user was created
- `updated_at` (datetime): Timestamp when the user was last updated
- `is_active` (boolean): Whether the account is active

### Validation Rules
- Username must be between 3 and 30 characters and unique
- Email must be a valid email format and unique
- Password must meet security requirements (to be defined)
- User must be active to perform operations

## Entity: Event

### Attributes
- `id` (string, required): Unique identifier for the event
- `type` (string, required): Type of event (task.created, task.updated, task.deleted, task.completed)
- `payload` (object, required): Event-specific data
- `timestamp` (datetime): When the event occurred
- `source` (string): System component that generated the event

### Validation Rules
- Type must be one of the predefined event types
- Payload must match the schema for the event type
- Timestamp must be current or past (not future)

## Entity: Conversation

### Attributes
- `id` (string, required): Unique identifier for the conversation
- `user_id` (string, required): ID of the user involved in the conversation
- `messages` (array of objects): List of messages in the conversation
- `created_at` (datetime): When the conversation started
- `updated_at` (datetime): When the conversation was last updated

### Validation Rules
- User ID must reference an existing user
- Messages must follow the required structure
- Conversation must be updated when new messages are added

## Relationships

### Task - User
- A Task belongs to one User (owner)
- A User can own many Tasks
- Relationship: One-to-Many (User → Task)

### Event - Task/User
- An Event may reference a Task or User
- Events are primarily informational and don't enforce strict relationships
- Relationship: Loose coupling for audit and processing purposes

### Conversation - User
- A Conversation belongs to one User
- A User can have one active Conversation at a time
- Relationship: One-to-One (User → Conversation) for active conversations