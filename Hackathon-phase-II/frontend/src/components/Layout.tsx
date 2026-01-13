// frontend/src/components/Layout.tsx
import React, { ReactNode } from 'react';
import { Outlet } from 'react-router-dom';
import ProtectedRoute from './ProtectedRoute';

interface LayoutProps {
  children?: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex">
              <div className="flex-shrink-0 flex items-center">
                <h1 className="text-xl font-bold text-gray-900">Todo App</h1>
              </div>
              <nav className="ml-6 flex space-x-8">
                <a
                  href="/dashboard"
                  className="border-transparent text-gray-500 hover:bg-gray-50 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
                >
                  Dashboard
                </a>
                <a
                  href="/profile"
                  className="border-transparent text-gray-500 hover:bg-gray-50 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
                >
                  Profile
                </a>
              </nav>
            </div>
            <div className="flex items-center">
              <button
                type="button"
                className="bg-white p-1 rounded-full text-gray-400 hover:text-gray-500 focus:outline-none"
              >
                <span className="sr-only">View notifications</span>
                <svg
                  className="h-6 w-6"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  aria-hidden="true"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
                  />
                </svg>
              </button>

              <div className="ml-3 relative">
                <div>
                  <button
                    type="button"
                    className="bg-gray-200 flex text-sm rounded-full focus:outline-none"
                    id="user-menu-button"
                  >
                    <span className="sr-only">Open user menu</span>
                    <div className="h-8 w-8 rounded-full bg-blue-500 flex items-center justify-center text-white font-bold">
                      U
                    </div>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main content */}
      <main>
        {children || <Outlet />}
      </main>

      {/* Footer */}
      <footer className="bg-white">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 md:flex md:items-center md:justify-between lg:px-8">
          <div className="mt-4 md:mt-0 md:order-1">
            <p className="text-center text-sm text-gray-500">
              &copy; {new Date().getFullYear()} Todo App. All rights reserved.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
};

// Wrapper that protects the layout with authentication
const ProtectedLayout: React.FC = () => {
  return (
    <ProtectedRoute>
      <Layout />
    </ProtectedRoute>
  );
};

export { Layout, ProtectedLayout };