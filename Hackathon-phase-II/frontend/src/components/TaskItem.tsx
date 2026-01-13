// frontend/src/components/TaskItem.tsx
import React from 'react';
import { Task } from '../types/task';

interface TaskItemProps {
  task: Task;
  onToggle: () => void;
  onDelete: () => void;
}

const TaskItem: React.FC<TaskItemProps> = ({ task, onToggle, onDelete }) => {
  const formatDate = (dateString: string) => {
    const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };

  return (
    <li className={`border rounded-lg p-4 flex items-start space-x-3 ${task.status === 'completed' ? 'bg-green-50' : ''}`}>
      <input
        type="checkbox"
        checked={task.status === 'completed'}
        onChange={onToggle}
        className="mt-1 h-5 w-5 rounded border-gray-300 text-blue-600 focus:ring-blue-500"
      />
      <div className="flex-1 min-w-0">
        <div className="flex items-baseline justify-between">
          <h3 className={`text-lg font-medium truncate ${task.status === 'completed' ? 'line-through text-gray-500' : 'text-gray-900'}`}>
            {task.title}
          </h3>
          <span className={`ml-2 px-2 py-1 text-xs rounded-full ${
            task.priority === 'high' ? 'bg-red-100 text-red-800' :
            task.priority === 'medium' ? 'bg-yellow-100 text-yellow-800' :
            'bg-green-100 text-green-800'
          }`}>
            {task.priority}
          </span>
        </div>
        {task.description && (
          <p className="text-sm text-gray-500 mt-1 truncate">{task.description}</p>
        )}
        <div className="mt-2 flex items-center text-xs text-gray-500">
          {task.due_date && (
            <span className="mr-3">Due: {formatDate(task.due_date)}</span>
          )}
          <span>Status: {task.status}</span>
          {task.category && (
            <span className="ml-3 bg-gray-100 px-2 py-1 rounded">#{task.category}</span>
          )}
        </div>
      </div>
      <button
        onClick={onDelete}
        className="ml-2 text-red-500 hover:text-red-700 focus:outline-none"
        aria-label="Delete task"
      >
        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path
            fillRule="evenodd"
            d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
            clipRule="evenodd"
          />
        </svg>
      </button>
    </li>
  );
};

export default TaskItem;