Cree app/main.py avec FastAPI, Uvicorn config, CORS (origins depuis env), TrustedHost (hosts depuis env), et router include pour: auth, missions, assignments, admin, utils. Ajoute /healthz GET qui renvoie { "ok": true }.
Cree deps.py avec get_storage() et get_current_user() qui utilise security.py (token bearer en memoire/JSON) et roles.
Cree security.py: hashage bcrypt, generation token serveur (pas JWT pour l instant), verif role admin.
Cree storage.py: lecture/ecriture atomique d un data.json (fichier auto-cree dans /data), avec locks pour threads. Fournis fonctions CRUD pour users, missions, assignments, soft delete via deleted_at.
Expose une config timezone UTC+04:00 pour serialisation ISO 8601.
