Tu es mon agent full-stack. Genere les dossiers et fichiers suivants (sans accents, ASCII only):

root/
  backend/
    app/
      __init__.py
      main.py
      models.py
      schemas.py
      storage.py
      security.py
      deps.py
      routers/
        __init__.py
        auth.py
        missions.py
        assignments.py
        admin.py
        utils.py
      tests/
        __init__.py
        test_auth.py
        test_missions.py
        test_admin.py
        test_utils.py
    scripts/
      seed_plus.py
      demo_calls.ps1
    pyproject.toml
    requirements.txt
    Dockerfile
    .env.example
    README.md

  frontend/
    src/
      main.tsx
      App.tsx
      lib/api.ts
      lib/hooks.ts
      pages/
        Login.tsx
        Missions.tsx
        Planning.tsx
        UsersAdmin.tsx
      components/
        Topbar.tsx
        MissionForm.tsx
        AssignTable.tsx
    index.html
    package.json
    tsconfig.json
    vite.config.ts
    postcss.config.js
    tailwind.config.js
    .env.example
    README.md

  deploy/
    compose.yaml
    .env.example
    grafana/ (optionnel plus tard)

  .github/workflows/deploy.yml
  README.md

Ajoute des README clairs pour lancer dev et prod. Ne mets pas de code placeholder inutile: cree de vrais squelettes pret a coder.
