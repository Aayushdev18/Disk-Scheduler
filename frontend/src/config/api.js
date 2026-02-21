// API Configuration
// Uses environment variables with fallback to localhost for development

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

export const API_ENDPOINTS = {
  SIMULATE: `${API_BASE_URL}/api/simulate/`,
  COMPARE: `${API_BASE_URL}/api/compare/`,
  ALGORITHMS: `${API_BASE_URL}/api/algorithms/`,
  ROOT: `${API_BASE_URL}/api/`,
};

export default API_BASE_URL;
