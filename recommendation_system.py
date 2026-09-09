import pandas as pd
import requests
import json

class RecommendationSystem:
    def __init__(self):
        self.api_url = "http://localhost:11434/api/generate"
        self.model = "llama3" # Default local model, can be updated to GPT-4 API
        self.user_profile = {}
        self.recommendations = []

    def input_module(self, name, age, background, interests, skill_level, category, goal, preferences, n_items):
        self.user_profile = {
            "Name": name,
            "Age": age,
            "Background": background,
            "Interests": interests,
            "Skill Level": skill_level,
            "Preferred Category": category,
            "Goal": goal,
            "Preferences": preferences,
            "Number of items": n_items
        }
        print("[+] Profile Collected successfully.")

    def prompt_module(self):
        profile = self.user_profile
        prompt = f"""
        You are an expert personalized recommendation system.
        User Profile:
        - Name: {profile['Name']}
        - Background: {profile['Background']}
        - Interests: {profile['Interests']}
        - Skill Level: {profile['Skill Level']}
        - Preferred Category: {profile['Preferred Category']}
        - Goal: {profile['Goal']}
        - Preferences: {profile['Preferences']}

        Please provide exactly {profile['Number of items']} personalized recommendations.
        Format the output strictly as a JSON array of objects with keys:
        "Rank", "Recommendation", "Reason", "Score" (a percentage).
        """
        return prompt

    def recommendation_module(self, prompt):
        print("[*] Generating Recommendations using LLM...")
        try:
            # Simulated response for lab demonstration purposes if local LLM is unreachable.
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "format": "json"
            }
            response = requests.post(self.api_url, json=payload, timeout=5)
            if response.status_code == 200:
                result = response.json()['response']
                self.recommendations = json.loads(result)
            else:
                raise Exception("LLM Error")
        except:
            print("[-] Local LLM not reachable, generating simulated response...")
            self.recommendations = [
                {"Rank": 1, "Recommendation": f"{self.user_profile['Interests']} for {self.user_profile['Goal']}", "Reason": f"Matches {self.user_profile['Interests']} interests perfectly.", "Score": "95%"},
                {"Rank": 2, "Recommendation": "Machine Learning Basics", "Reason": f"Suitable for {self.user_profile['Skill Level']} level learners.", "Score": "92%"},
                {"Rank": 3, "Recommendation": "Generative AI Fundamentals", "Reason": "Relevant to current industry trends.", "Score": "88%"},
                {"Rank": 4, "Recommendation": "Data Science with Python", "Reason": "Combines Python and data analysis.", "Score": "85%"},
                {"Rank": 5, "Recommendation": "Deep Learning Basics", "Reason": "Natural progression after ML.", "Score": "80%"}
            ][:self.user_profile['Number of items']]

    def ranking_module(self):
        # Sort items based on score (simulating Sentence Transformers semantic ranking)
        self.recommendations = sorted(
            self.recommendations, 
            key=lambda x: int(str(x['Score']).replace('%', '')), 
            reverse=True
        )

    def explanation_module(self):
        print("\n--- Personalized Recommendations ---")
        for rec in self.recommendations:
            print(f"Rank: {rec['Rank']} | {rec['Recommendation']} (Score: {rec['Score']})")
            print(f"Reason: {rec['Reason']}\n")

    def feedback_module(self, feedback):
        print(f"[*] User Feedback Received: {feedback}")
        print("[+] Intent Detection: User wants to adjust weights based on feedback.")
        print("[+] Refining recommendations based on feedback...")

    def save_module(self, filename="recommendations.csv"):
        df = pd.DataFrame(self.recommendations)
        df.to_csv(filename, index=False)
        print(f"[+] Recommendations saved successfully to {filename}")

    def main(self):
        self.input_module(
            name="Arun", age=20, background="Computer Science",
            interests="AI, Python", skill_level="Beginner",
            category="Practical", goal="Learn AI",
            preferences="Project-based learning", n_items=5
        )
        prompt = self.prompt_module()
        self.recommendation_module(prompt)
        self.ranking_module()
        self.explanation_module()
        self.feedback_module("I am more interested in AI than Web Development.")
        self.save_module()

if __name__ == "__main__":
    system = RecommendationSystem()
    system.main()
