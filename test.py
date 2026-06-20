import json

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    first_candidate = json.loads(f.readline())

print(first_candidate["candidate_id"])
print(first_candidate["profile"]["current_title"])
print(first_candidate["profile"]["years_of_experience"])

print("\nSkills:")
for skill in first_candidate["skills"]:
    print("-", skill["name"])