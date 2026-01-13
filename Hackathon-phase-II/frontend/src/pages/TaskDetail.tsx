// frontend/src/pages/TaskDetail.tsx
import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Task } from '../types/task';
import api from '../services/api';

const TaskDetail: React.FC = () => {
  const { taskId, userId } = useParams<{ taskId: string; userId: string }>();
  const navigate = useNavigate();
  const [task, setTask] = useState<Task | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!taskId || !userId) {
      setError('Missing task or user ID');
      setLoading(false);
      return;
    }

    const fetchTask = async () => {
      try {
        setLoading(true);
        const response = await api.getTask(userId, taskId);
        setTask(response.data);
        setError(null);
      } catch (err) {
        setError('Failed to load task details. Please try again later.');
        console.error('Error fetching task:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchTask();
  }, [taskId, userId]);

  const handleToggleCompletion = async () => {
    if (!task) return;

    try {
      const response = await api.toggleTaskCompletion(userId, task.id);
      setTask(response.data);
    } catch (err) {
      setError('Failed to update task. Please try again.');
      console.error('Error toggling task:', err);
    }
  };

  const handleDelete = async () => {
    if (!task) return;

    if (window.confirm('Are you sure you want to delete this task?')) {
      try {
        await api.deleteTask(userId, task.id);
        navigate(`/dashboard/${userId}`);
      } catch (err) {
        setError('Failed to delete task. Please try again.');
        console.error('Error deleting task:', err);
      }
    }
  };

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="text-center py-4">Loading task details...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="text-red-500 text-center py-4">{error}</div>
        <div className="text-center">
          <button
            onClick={() => navigate(-1)}
            className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
          >
            Go Back
          </button>
        </div>
      </div>
    );
  }

  if (!task) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="text-center py-4">Task not found</div>
        <div className="text-center">
          <button
            onClick={() => navigate(-1)}
            className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
          >
            Go Back
          </button>
        </div>
      </div>
    );
  }

  const formatDate = (dateString: string) => {
    const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-white shadow-md rounded-lg p-6">
        <div className="flex justify-between items-start">
          <div>
            <h1 className="text-2xl font-bold text-gray-800 mb-2">{task.title}</h1>
            <div className="flex items-center space-x-4 mb-4">
              <span className={`px-2 py-1 text-xs rounded-full ${
                task.priority === 'high' ? 'bg-red-100 text-red-800' :
                task.priority === 'medium' ? 'bg-yellow-100 text-yellow-800' :
                'bg-green-100 text-green-800'
              }`}>
                {task.priority} priority
              </span>
              <span className={`px-2 py-1 text-xs rounded-full ${
                task.status === 'completed' ? 'bg-green-100 text-green-800' :
                task.status === 'in-progress' ? 'bg-blue-100 text-blue-800' :
                'bg-gray-100 text-gray-800'
              }`}>
                {task.status.replace('-', ' ')}
              </span>
            </div>
          </div>
          <div className="flex space-x-2">
            <button
              onClick={handleToggleCompletion}
              className={`px-3 py-1 rounded-md text-sm ${
                task.status === 'completed' 
                  ? 'bg-yellow-500 text-white hover:bg-yellow-600' 
                  : 'bg-green-500 text-white hover:bg-green-600'
              }`}
            >
              {task.status === 'completed' ? 'Mark In Progress' : 'Mark Complete'}
            </button>
            <button
              onClick={handleDelete}
              className="px-3 py-1 bg-red-500 text-white rounded-md text-sm hover:bg-red-600"
            >
              Delete
            </button>
          </div>
        </div>

        {task.description && (
          <div className="mt-4">
            <h2 className="text-lg font-semibold text-gray-700 mb-2">Description</h2>
            <p className="text-gray-600">{task.description}</p>
          </div>
        )}

        <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <h3 className="text-sm font-medium text-gray-500">Created</h3>
            <p className="text-gray-900">{formatDate(task.created_at)}</p>
          </div>
          <div>
            <h3 className="text-sm font-medium text-gray-500">Updated</h3>
            <p className="text-gray-900">{formatDate(task.updated_at)}</p>
          </div>
          {task.completed_at && (
            <div>
              <h3 className="text-sm font-medium text-gray-500">Completed</h3>
              <p className="text-gray-900">{formatDate(task.completed_at)}</p>
            </div>
          )}
          {task.due_date && (
            <div>
              <h3 className="text-sm font-medium text-gray-500">Due Date</h3>
              <p className="text-gray-900">{formatDate(task.due_date)}</p>
            </div>
          )}
        </div>

        {task.category && (
          <div className="mt-4">
            <h3 className="text-sm font-medium text-gray-500">Category</h3>
            <p className="text-gray-900">#{task.category}</p>
          </div>
        )}

        <div className="mt-6">
          <button
            onClick={() => navigate(-1)}
            className="px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300"
          >
            Back to Tasks
          </button>
        </div>
      </div>
    </div>
  );
};

export default TaskDetail;