Dans models.py et schemas.py, definis:
- User: id, username, hashed_password, role in {admin, intermittent}, prefs {email?, telegram?, telegram_chat_id?}, created_at, updated_at, deleted_at?
- Mission: id, title, start, end, location, call_time?, positions[] de Position{label, count>=1, skills: dict}, documents[]?, status in {draft, published}, created_by
- Assignment: id, mission_id, user_id?, role_label, status in {invited, confirmed, declined, removed}, channel?, responded_at?

Ajoute schemas d entree/sortie (In/Out) et contraintes: start < end, labels uniques dans positions, etc.
