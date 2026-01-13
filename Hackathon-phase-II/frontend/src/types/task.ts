// frontend/src/types/task.ts
export interface Task {
  id: string;
  title: string;
  description?: string;
  status: 'to-do' | 'in-progress' | 'completed';
  priority: 'low' | 'medium' | 'high';
  due_date?: string; // ISO date string
  created_at: string; // ISO date string
  updated_at: string; // ISO date string
  completed_at?: string; // ISO date string
  category?: string;
  user_id: string;
}