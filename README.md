# Intelligent Candidate Discovery & Ranking System

## Problem Statement

Traditional hiring systems rely heavily on keyword matching and often fail to identify the best candidates. This project builds an AI-assisted ranking system that evaluates candidates using skills, experience, career history, and behavioral signals.

## Approach

The system processes candidate profiles and ranks the top 100 candidates for a given job description.

## Features Used

* Years of Experience
* Technical Skills
* Career History Analysis
* Open To Work Status
* Recruiter Response Rate
* GitHub Activity Score
* Recruiter Saves
* Response Time
* Relocation Preference
* Notice Period

## Scoring Logic

Candidates are scored based on:

* Relevant AI/ML Skills
* Retrieval and Ranking Experience
* Career History Keywords
* Behavioral Signals
* Experience Match

## Behavioral Signals

The following Redrob signals are used:

* open_to_work_flag
* recruiter_response_rate
* github_activity_score
* saved_by_recruiters_30d
* avg_response_time_hours
* willing_to_relocate
* notice_period_days

## Output Format

The system generates a CSV file containing:

* candidate_id
* rank
* score
* reasoning

## How to Run

```bash
python generate_submission.py
```

## Technologies Used

* Python
* JSON
* CSV

## Future Improvements

* Semantic Search
* Embedding-Based Retrieval
* Learning-to-Rank Models
* LLM-Based Candidate Matching

## Demo Sandbox

Google Colab Demo:

https://colab.research.google.com/drive/1_E_cYnj_FeNqOGTl1WbaMH6x-A3R-DI7?usp=sharing