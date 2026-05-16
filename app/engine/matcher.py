from app.models.event import Event


def match_event(event: Event, user_preferences: list[str]) -> bool:
    event_category = event.category.lower()

    normalized_prefs = [p.lower() for p in user_preferences]
    
    return event_category in normalized_prefs