// frontend/src/services/auth.ts
import api from './api';

interface LoginCredentials {
  username: string;
  password: string;
}

interface RegisterData {
  username: string;
  email: string;
  password: string;
}

interface User {
  id: string;
  username: string;
  email: string;
}

class AuthService {
  async login(credentials: LoginCredentials): Promise<{ user: User; accessToken: string }> {
    try {
      const response = await api.login(credentials.username, credentials.password);
      const { user, access_token } = response.data;

      // Store the token in localStorage
      localStorage.setItem('accessToken', access_token);

      return { user, accessToken: access_token };
    } catch (error) {
      throw new Error('Login failed. Please check your credentials.');
    }
  }

  async register(userData: RegisterData): Promise<User> {
    try {
      const response = await api.register(userData);
      return response.data;
    } catch (error) {
      throw new Error('Registration failed. Please try again.');
    }
  }

  logout(): void {
    // Remove the token from localStorage
    localStorage.removeItem('accessToken');
    
    // Redirect to login page
    window.location.href = '/login';
  }

  isAuthenticated(): boolean {
    // Check if token exists in localStorage
    const token = localStorage.getItem('accessToken');
    return !!token;
  }

  getCurrentUser(): User | null {
    // In a real implementation, you might decode the JWT to get user info
    // For now, we'll return null and let components handle user data separately
    return null;
  }

  getAccessToken(): string | null {
    return localStorage.getItem('accessToken');
  }
}

export default new AuthService();