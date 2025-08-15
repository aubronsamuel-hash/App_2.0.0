import { ButtonHTMLAttributes } from 'react'

export default function Button(props: ButtonHTMLAttributes<HTMLButtonElement>) {
  return <button className="bg-blue-500 text-white px-4 py-2" {...props} />
}
