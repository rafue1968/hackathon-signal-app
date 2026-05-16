def get_user_preferences(user_id: str):
    fake_db = {
        "user_1": ["ai", "hackathon", "tech"],
        "user_2": ["design", "video"]
    }

    return fake_db.get(user_id, [])