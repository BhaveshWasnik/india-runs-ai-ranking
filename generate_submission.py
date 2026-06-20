import json
import csv

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

    if signals["open_to_work_flag"]:
        score += 10

    if signals["recruiter_response_rate"] > 0.5:
        score += 10

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

    if signals["github_activity_score"] > 70:
        score += 15
    elif signals["github_activity_score"] > 40:
        score += 10

    if signals["saved_by_recruiters_30d"] > 20:
        score += 15
    elif signals["saved_by_recruiters_30d"] > 5:
        score += 8

    if signals["avg_response_time_hours"] < 24:
        score += 10

    if signals["willing_to_relocate"]:
        score += 5

    if signals["notice_period_days"] > 90:
        score -= 10

    return score


def generate_reasoning(candidate):

    title = candidate["profile"]["current_title"]
    exp = candidate["profile"]["years_of_experience"]

    candidate_skills = [s["name"] for s in candidate["skills"]]

    important_skills = [
        "vector search",
        "recommendation systems",
        "information retrieval",
        "embeddings",
        "pinecone",
        "milvus",
        "faiss",
        "qdrant",
        "elasticsearch",
        "learning to rank",
        "fine-tuning llms",
        "lora",
        "rag",
        "nlp"
    ]

    matched_skills = []

    for skill in candidate_skills:
        if skill.lower() in [x.lower() for x in important_skills]:
            matched_skills.append(skill)

    top_skills = ", ".join(matched_skills[:3])

    signals = candidate["redrob_signals"]
    recruiter_saves = signals["saved_by_recruiters_30d"]
    notice_period = signals["notice_period_days"]

    reasoning = (
        f"{title} with {exp} years of experience. "
        f"Strong background in {top_skills}. "
    )

    if recruiter_saves >= 20:
        reasoning += (
            f"High recruiter interest ({recruiter_saves} saves in the last 30 days). "
        )

    if notice_period == 0:
        reasoning += "Immediate availability is an additional advantage."
    elif notice_period > 90:
        reasoning += f"Strong profile, though the {notice_period}-day notice period may slow hiring."

    return reasoning

candidates = []

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        score = calculate_score(candidate)

        candidates.append({
            "candidate_id": candidate["candidate_id"],
            "score": score,
            "candidate": candidate
        })

candidates.sort(key=lambda x: x["score"], reverse=True)

top_100 = candidates[:100]

with open("submission.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    for rank, item in enumerate(top_100, start=1):
        writer.writerow([
            item["candidate_id"],
            rank,
            item["score"],
            generate_reasoning(item["candidate"])
        ])

print("submission.csv generated successfully!")
print("Top 100 candidates exported.")