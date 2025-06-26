# Judgey Bot 😤

Judgey Bot is an interactive Streamlit app that acts as your AI "disappointed parent." It asks probing, judgmental questions about your habits and life choices, then delivers sarcastic, guilt-inducing feedback—culminating in a final, comprehensive verdict. It's all in good fun (and maybe a little motivation)!

---

## Features

- **Conversational AI:** Uses Gemini 2.0 Flash via [LiteLLM](https://github.com/BerriAI/litellm) to generate context-aware, judgmental questions and responses.
- **Session Memory:** Remembers your answers and uses them for increasingly pointed questions and judgments.
- **Final Judgment:** After 8 questions, delivers a comprehensive, disappointed-parent-style verdict.
- **Fallbacks:** If the LLM is unavailable, fallback questions and responses keep the experience going.
- **Streamlit UI:** Clean, interactive web interface with stats and playful design.

---

## Getting Started

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd Judgey\ boat
```

### 2. Install Dependencies

Make sure you have Python 3.8+ installed.

```sh
pip install -r requirements.txt
```

### 3. Set Up Your Gemini API Key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

You can get a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 4. Run the App

```sh
streamlit run main.py
```

Open the provided local URL in your browser.

---

## Usage

- Click **"Bring on the Judgment! 😤"** to start.
- Answer each question honestly (or not—you'll be judged either way).
- After 8 questions, receive your final verdict.
- Use the sidebar for stats, recent confessions, and an "Emergency Escape" button to reset.

---

## File Structure

- `main.py`: Main Streamlit app and JudgeyBot logic.
- `requirements.txt`: Python dependencies.
- `.env`: Your Gemini API key (not included in repo).

---

## Customization

- **Change Number of Questions:** Edit `self.max_questions` in the `JudgeyBot` class in `main.py`.
- **Modify Tone or Prompts:** Adjust prompt templates in the `generate_question`, `generate_judgment`, and `generate_final_judgment` methods.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Disclaimer

This app is for entertainment purposes only. Judgey Bot is not a substitute for real parental advice or therapy. 😏

---

## Credits

- Built with [Streamlit](https://streamlit.io/)
- LLM powered by [LiteLLM](https://github.com/BerriAI/litellm) and Gemini 2.0 Flash

---

Enjoy your judgment! 😤
