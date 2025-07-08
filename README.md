
 ## 🤖 AI Companion (Buddy)

A simple AI chatbot using Together.ai's API and the Mixtral-8x7B model. This project simulates a friendly, empathetic AI companion named **Buddy** who engages in human-like conversations. It also includes a basic feedback logging system for reinforcement learning simulations.

 🚀 Features

- 💬 Conversational chatbot with memory (`chat_history`)
- 🤗 Friendly AI personality named "Buddy"
- 🔁 Feedback logging (`feedback_log.jsonl`)
- ⚙️ Uses Together.ai for LLM completions



 🛠️ Setup Instructions
1. Clone the repository

```bash
git clone https://github.com/your-username/replika-buddy.git
cd replika-buddy
```

2. Install requirements

```bash
pip install openai
```

3. Configure API
 ```bash
from openai import OpenAI

client = OpenAI(
    api_key="your_together_api_key",
    base_url="https://api.together.xyz/v1"
)
```
🧠 Personality & Prompt

The system prompt defines the bot's personality:
"You are a friendly AI companion named Buddy. You respond with empathy, curiosity, and human-like friendliness."
How Feedback Works
Each user input and bot reply is stored in a JSONL file with feedback metadata. Example:
```bash

{
  "user_input": "How are you?",
  "bot_reply": "I'm just a bot, but I'm happy to talk to you!",
  "feedback": "positive"
}
#You can later use this data for fine-tuning or reward modeling.
```
🧪 Run the Chatbot
```bash
python main.py
```
