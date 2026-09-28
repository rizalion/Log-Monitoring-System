def calculate_risk(alerts):
    score = 0

    for alert in alerts:
        if alert["severity"] == "HIGH":
            score += 30
        elif alert["severity"] == "MEDIUM":
            score += 15
        elif alert["severity"] == "LOW":
            score += 5

    if score >= 60:
        level = "HIGH"
    elif score >= 30:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level