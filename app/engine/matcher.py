from app.models.event import Event


def match_event(event: Event, preferences: list[str]) -> bool:
    return event.category.lower() in [
        pref.lower() for pref in preferences
    ]