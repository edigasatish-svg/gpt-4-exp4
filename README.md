# Personalized Recommendation System

This project is an intelligent, personalized recommendation system designed to analyze user preferences (interests, skill level, background) and generate tailored recommendations. 

## Features
* **User Profile Collection**: Takes inputs such as age, goals, and preferred learning styles.
* **LLM Integration**: Connects dynamically to local LLMs (like Ollama) or uses a simulated fallback to generate logical recommendations.
* **Ranking & Explanation**: Ranks items based on relevance and provides a clear explanation for why an item was recommended.
* **Feedback Loop**: Processes user feedback to refine and adjust future intents.
* **CSV Export**: Automatically saves the ranked recommendations to a `recommendations.csv` file.

## Requirements
* Python 3.10+
* Pandas
* Requests
* *Optional: [Ollama](https://ollama.com/) running locally for live LLM inference.*

## How to Run

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the main script:
   ```bash
   python recommendation_system.py
   ```

## Output
The script will output the recommendations directly into the console and generate a `recommendations.csv` file with the results.
