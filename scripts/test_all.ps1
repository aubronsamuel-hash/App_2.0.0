# Run backend tests, frontend build and smoke tests
param()
pytest -q
pushd frontend
npm install
npm run build
popd
k6 run perf/smoke.js
