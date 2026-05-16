from app.engine.decider import decide_match, DecisionType
from app.engine.matcher import match_event
from app.services.notifier import send_notifications


def process_event(event, user_preferences):
    decision = decide_match(event, user_preferences)

    if decision == DecisionType.HIGH_PRIORITY:
        send_notifications(
                f"Match FOUND!\n"
                f"{event.title} in {event.city} ({event.category})"
            )
    elif decision == DecisionType.LOW_PRIORITY:
        send_notifications("Maybe later")
    else:
        pass

    return {
        "event": event,
        "decision": decision.value
    }