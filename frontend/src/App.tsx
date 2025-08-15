import { Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import Missions from './pages/Missions'
import Planning from './pages/Planning'
import AdminUsers from './pages/AdminUsers'
import Settings from './pages/Settings'

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/missions" element={<Missions />} />
      <Route path="/planning" element={<Planning />} />
      <Route path="/admin/users" element={<AdminUsers />} />
      <Route path="/settings" element={<Settings />} />
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  )
}
