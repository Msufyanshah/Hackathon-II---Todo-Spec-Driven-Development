// frontend/src/components/TaskList.tsx
import React, { useState, useEffect } from 'react';
import TaskItem from './TaskItem';
import { Task } from '../types/task';
import api from '../services/api';
import auth from '../services/auth';

interface TaskListProps {
  userId: string;
  onTaskUpdate?: () => void;
}

const TaskList: React.FC<TaskListProps> = ({ userId, onTaskUpdate }) => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchTasks();
  }, [userId]);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const response = await api.getTasks(userId);
      setTasks(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to load tasks. Please try again later.');
      console.error('Error fetching tasks:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleTaskToggle = async (taskId: string) => {
    try {
      await api.toggleTaskCompletion(userId, taskId);
      // Refresh the task list
      fetchTasks();
      if (onTaskUpdate) onTaskUpdate();
    } catch (err) {
      setError('Failed to update task. Please try again.');
      console.error('Error toggling task:', err);
    }
  };

  const handleTaskDelete = async (taskId: string) => {
    try {
      await api.deleteTask(userId, taskId);
      // Refresh the task list
      fetchTasks();
      if (onTaskUpdate) onTaskUpdate();
    } catch (err) {
      setError('Failed to delete task. Please try again.');
      console.error('Error deleting task:', err);
    }
  };

  if (!auth.isAuthenticated()) {
    return <div>Please log in to view your tasks.</div>;
  }

  if (loading) {
    return <div className="text-center py-4">Loading tasks...</div>;
  }

  if (error) {
    return <div className="text-red-500 text-center py-4">{error}</div>;
  }

  return (
    <div className="bg-white shadow-md rounded-lg p-6">
      <h2 className="text-xl font-bold mb-4">Your Tasks</h2>
      {tasks.length === 0 ? (
        <p className="text-gray-500 text-center">No tasks found. Create your first task!</p>
      ) : (
        <ul className="space-y-3">
          {tasks.map((task) => (
            <TaskItem
              key={task.id}
              task={task}
              onToggle={() => handleTaskToggle(task.id)}
              onDelete={() => handleTaskDelete(task.id)}
            />
          ))}
        </ul>
      )}
    </div>
  );
};

export default TaskList;