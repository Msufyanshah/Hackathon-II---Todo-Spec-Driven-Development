// frontend/src/pages/Dashboard.tsx
import React, { useState, useEffect } from 'react';
import TaskList from '../components/TaskList';
import TaskForm from '../components/TaskForm';
import { useNavigate } from 'react-router-dom';
import auth from '../services/auth';

const Dashboard: React.FC = () => {
  const navigate = useNavigate();
  const [userId, setUserId] = useState<string | null>(null);

  useEffect(() => {
    // Get user info from auth service
    // In a real implementation, you might decode the JWT to get user info
    const token = auth.getAccessToken();
    if (!token) {
      navigate('/login');
      return;
    }

    // For this example, we'll use a mock user ID
    // In a real app, you would extract this from the JWT
    setUserId('mock-user-id-123');
  }, [navigate]);

  if (!userId) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800">Todo Dashboard</h1>
        <p className="text-gray-600">Manage your tasks efficiently</p>
      </header>

      <main>
        <TaskForm userId={userId} onTaskCreated={() => {}} />
        <TaskList userId={userId} onTaskUpdate={() => {}} />
      </main>

      <footer className="mt-12 text-center text-gray-500 text-sm">
        <p>© {new Date().getFullYear()} Todo App. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Dashboard;