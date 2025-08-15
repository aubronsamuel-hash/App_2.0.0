import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { login } from '../api/client'

export default function Login() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  const handle = async (e: React.FormEvent) => {
    e.preventDefault()
    const res = await login(username, password)
    localStorage.setItem('token', res.access_token)
    navigate('/dashboard')
  }

  return (
    <form className="p-4 max-w-sm mx-auto" onSubmit={handle}>
      <h1 className="text-xl mb-2">Login</h1>
      <input className="border p-2 mb-2 w-full" value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" className="border p-2 mb-2 w-full" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
      <button className="bg-blue-500 text-white px-4 py-2" type="submit">Login</button>
    </form>
  )
}
