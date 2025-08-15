import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8001',
})

export interface Mission {
  id: number
  title: string
  description?: string
  published: boolean
}

export async function login(username: string, password: string) {
  const res = await api.post('/auth/login', { username, password })
  return res.data as { access_token: string }
}

export async function getMissions(token: string) {
  const res = await api.get<Mission[]>('/missions', {
    headers: { Authorization: `Bearer ${token}` },
  })
  return res.data
}

export default api
