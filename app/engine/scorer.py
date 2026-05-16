def score_event(event, user_preferences):
    event_category = event.category.lower()
    normalized = [p.lower() for p in user_preferences]

    if event_category in normalized:
        return 100
    elif any(pref in event_category for pref in normalized):
        return 50
    else:
        return 0