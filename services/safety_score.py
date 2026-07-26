def calculate_safety_score(distance, travel_time, police_count, hospital_count):
    """
    Returns a safety score out of 100.
    """

    score = 100

    # Night travel penalty
    if travel_time.lower() == "night":
        score -= 20

    # Long routes
    if distance > 20:
        score -= 10
    elif distance > 10:
        score -= 5

    # Nearby police
    if police_count == 0:
        score -= 10
    elif police_count >= 3:
        score += 5

    # Nearby hospitals
    if hospital_count == 0:
        score -= 10
    elif hospital_count >= 3:
        score += 5

    # Clamp score
    score = max(0, min(score, 100))

    return score


def get_risk_level(score):
    if score >= 80:
        return "🟢 Low Risk"
    elif score >= 60:
        return "🟡 Medium Risk"
    else:
        return "🔴 High Risk"


if __name__ == "__main__":

    score = calculate_safety_score(
        distance=12,
        travel_time="Night",
        police_count=2,
        hospital_count=1
    )

    print("Safety Score:", score)
    print("Risk Level:", get_risk_level(score))