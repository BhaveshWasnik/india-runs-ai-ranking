import json

def calculate_score(candidate):
    score = 0

    exp = candidate["profile"]["years_of_experience"]

    if 5 <= exp <= 9:
        score += 20

    skills = [s["name"].lower() for s in candidate["skills"]]

    important_skills = [
        "nlp",
        "fine-tuning llms",
        "lora",
        "milvus",
        "python"
    ]

    for skill in important_skills:
        if skill in skills:
            score += 10

    signals = candidate["redrob_signals"]

    # Basic signals
    if signals["open_to_work_flag"]:
        score += 10

    if signals["recruiter_response_rate"] > 0.5:
        score += 10

    # Career analysis
    career_text = ""

    for job in candidate["career_history"]:
        career_text += job["description"].lower() + " "

    career_keywords = [
        "ranking",
        "retrieval",
        "recommendation",
        "embeddings",
        "rag",
        "vector",
        "search",
        "evaluation",
        "a/b testing",
        "production"
    ]

    for keyword in career_keywords:
        if keyword in career_text:
            score += 8

    # GitHub Activity Bonus
    if signals["github_activity_score"] > 70:
        score += 15
    elif signals["github_activity_score"] > 40:
        score += 10

    # Recruiter Interest Bonus
    if signals["saved_by_recruiters_30d"] > 20:
        score += 15
    elif signals["saved_by_recruiters_30d"] > 5:
        score += 8

    # Fast Response Bonus
    if signals["avg_response_time_hours"] < 24:
        score += 10

    # Relocation Bonus
    if signals["willing_to_relocate"]:
        score += 5

    # Notice Period Penalty
    if signals["notice_period_days"] > 90:
        score -= 10

    return score

candidates = []

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        score = calculate_score(candidate)

        candidates.append({
            "id": candidate["candidate_id"],
            "score": score,
            "title": candidate["profile"]["current_title"]
        })

candidates.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\nTop 20 Candidates:\n")

for c in candidates[:20]:
    print(c)