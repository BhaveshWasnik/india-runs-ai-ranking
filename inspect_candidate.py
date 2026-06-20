import json

TARGET_ID = "CAND_0086022"

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        if candidate["candidate_id"] == TARGET_ID:

            print("\nTITLE:")
            print(candidate["profile"]["current_title"])

            print("\nSUMMARY:")
            print(candidate["profile"]["summary"])

            print("\nEXPERIENCE:")
            print(candidate["profile"]["years_of_experience"])

            print("\nCAREER HISTORY:")
            for job in candidate["career_history"]:
                print(job["title"])
                print(job["description"])
                print("-" * 50)

            print("\nSKILLS:")
            for skill in candidate["skills"]:
                print(skill["name"])

            print("\nSIGNALS:")
            print(candidate["redrob_signals"])

            break