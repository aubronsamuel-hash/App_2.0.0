import { useEffect, useState } from 'react'
import { getMissions, Mission } from '../api/client'

export default function Missions() {
  const [missions, setMissions] = useState<Mission[]>([])
  useEffect(() => {
    const token = localStorage.getItem('token') || ''
    getMissions(token).then(setMissions)
  }, [])
  return (
    <div className="p-4">
      <h1 className="text-xl mb-2">Missions</h1>
      <ul>
        {missions.map(m => (
          <li key={m.id}>{m.title} {m.published && '(published)'}</li>
        ))}
      </ul>
    </div>
  )
}
