from collections import defaultdict

def detect_threats(events):

    alerts = []

    failed_logins = defaultdict(int)
    success_logins = 0
    total_events = len(events)

    for event in events:

        event_type = event.get("event") or "UNKNOWN"
        user = event.get("user") or "unknown_user"

        # SUCCESS LOGIN
        if event_type == "LOGIN_SUCCESS":
            success_logins += 1

        # FAILED LOGIN
        elif event_type == "LOGIN_FAILED":
            failed_logins[user] += 1

            # MEDIUM ALERT
            if failed_logins[user] == 3:
                alerts.append({
                    "type": "Suspicious Login Activity",
                    "severity": "MEDIUM",
                    "description": f"Repeated failed logins for user '{user}'"
                })

            # HIGH ALERT (Brute force)
            elif failed_logins[user] == 5:
                alerts.append({
                    "type": "Brute Force Attack",
                    "severity": "HIGH",
                    "description": f"Multiple failed login attempts detected for user '{user}'"
                })

        # UNKNOWN EVENT
        else:
            alerts.append({
                "type": "Unknown Event",
                "severity": "LOW",
                "description": f"Unknown event type detected: {event_type}"
            })

    return {
        "alerts": alerts,
        "total_events": total_events,
        "success_logins": success_logins,
        "failed_logins": sum(failed_logins.values())
    }