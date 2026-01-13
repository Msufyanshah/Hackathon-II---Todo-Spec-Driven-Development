// frontend/src/services/api.ts
import axios, { AxiosInstance, AxiosResponse } from 'axios';

interface ApiResponse<T> {
  data: T;
  message?: string;
}

class ApiService {
  private api: AxiosInstance;

  constructor(baseURL: string = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000') {
    this.api = axios.create({
      baseURL,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Add request interceptor to include JWT token
    this.api.interceptors.request.use(
      (config) => {
        const token = localStorage.getItem('accessToken');
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    // Add response interceptor to handle token expiration
    this.api.interceptors.response.use(
      (response) => response,
      (error) => {
        if (error.response?.status === 401) {
          // Token might be expired, redirect to login
          localStorage.removeItem('accessToken');
          window.location.href = '/login';
        }
        return Promise.reject(error);
      }
    );
  }

  // Authentication endpoints
  async login(username: string, password: string): Promise<AxiosResponse<ApiResponse<any>>> {
    return this.api.post('/auth/login', { username, password });
  }

  async register(userData: any): Promise<AxiosResponse<ApiResponse<any>>> {
    return this.api.post('/auth/register', userData);
  }

  // Task endpoints
  async getTasks(userId: string): Promise<AxiosResponse<ApiResponse<any>>> {
    return this.api.get(`/${userId}/tasks`);
  }

  async createTask(userId: string, taskData: any): Promise<AxiosResponse<ApiResponse<any>>> {
    return this.api.post(`/${userId}/tasks`, taskData);
  }

  async getTask(userId: string, taskId: string): Promise<AxiosResponse<ApiResponse<any>>> {
    return this.api.get(`/${userId}/tasks/${taskId}`);
  }

  async updateTask(userId: string, taskId: string, taskData: any): Promise<AxiosResponse<ApiResponse<any>>> {
    return this.api.put(`/${userId}/tasks/${taskId}`, taskData);
  }

  async deleteTask(userId: string, taskId: string): Promise<AxiosResponse<void>> {
    return this.api.delete(`/${userId}/tasks/${taskId}`);
  }

  async toggleTaskCompletion(userId: string, taskId: string): Promise<AxiosResponse<ApiResponse<any>>> {
    return this.api.patch(`/${userId}/tasks/${taskId}/complete`);
  }
}

export default new ApiService();