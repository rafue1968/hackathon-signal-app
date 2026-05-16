from enum import Enum

class DecisionType(Enum):
    NOT_MATCHED = "not_matched"
    LOW_PRIORITY = "low_priority"
    HIGH_PRIORITY = "high_priority"


def decide_match(event, user_preferences):

    event_category = event.category.lower()
    normalized = [p.lower() for p in user_preferences]


    if event_category in normalized:
        return DecisionType.HIGH_PRIORITY
    elif event_category in normalized:
        return DecisionType.LOW_PRIORITY

    return DecisionType.NOT_MATCHED
    