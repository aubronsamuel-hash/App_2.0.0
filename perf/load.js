import http from 'k6/http'
import { check, sleep } from 'k6'
import { htmlReport } from 'https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js'

export const options = {
  stages: [
    { duration: '10s', target: 20 },
    { duration: '20s', target: 20 },
    { duration: '10s', target: 0 },
  ],
}

export default function () {
  const res = http.get('http://localhost:8001/missions')
  check(res, { 'status is 200': r => r.status === 200 })
  sleep(1)
}

export function handleSummary(data) {
  return {
    'perf/reports/load.html': htmlReport(data),
  }
}
