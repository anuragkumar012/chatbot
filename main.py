from openai import OpenAI
import json

# ✅ Use Together.ai key and base URL
client = OpenAI(
    api_key="73b5b87acba1aa64df2403d70bb6fc33ab9b6a8acc025195dfa3dd7ac1239292",
    base_url="https://api.together.xyz/v1"
)

# 🧠 Chat memory (system prompt + history)
chat_history = [
    {
        "role": "system",
        "content": "You are a friendly AI companion named Buddy. You respond with empathy, curiosity, and human-like friendliness."
    }
]

# 🧠 Chat function
def chat_with_bot(user_input):
    chat_history.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=chat_history,
        temperature=0.7,
        max_tokens=700,
    )
    
    reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": reply})
    return reply

# 📝 Feedback simulation (like RLHF collection)
def get_feedback(user_input, bot_reply, rating="positive"):
    feedback_data = {
        "user_input": user_input,
        "bot_reply": bot_reply,
        "feedback": rating
    }
    with open("feedback_log.jsonl", "a") as f:
        f.write(json.dumps(feedback_data) + "\n")

# 💬 Chat loop
if __name__ == "__main__":
    print("🤖 Replika AI Companion (Together.ai)\nType 'exit' to stop\n")
    while True:
        user = input("You: ")
        if user.lower() in ["exit", "quit"]:
            break
        reply = chat_with_bot(user)
        print("Bot:", reply)
        get_feedback(user, reply)  # default = "positive"

