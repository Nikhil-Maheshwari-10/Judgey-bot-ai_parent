import streamlit as st
import json
from typing import Dict, List, Any
import time
from datetime import datetime
import os
from dotenv import load_dotenv
from litellm import completion

# Load Gemini API key from .env
load_dotenv()

class JudgeyBot:
    def __init__(self):
        self.model = "gemini/gemini-2.0-flash"
        self.conversation_count = 0
        self.max_questions = 8  # Ask 8 questions before final judgment
        
    def generate_question(self, conversation_history: List, user_data: Dict) -> str:
        """Generate contextually relevant judgmental questions using Gemini 2.0 Flash"""
        
        # Create context from conversation history
        context = ""
        if conversation_history:
            context = "Previous conversation:\n"
            for exchange in conversation_history[-3:]:  # Last 3 exchanges for context
                if exchange.get('user_response'):
                    context += f"User said: {exchange['user_response']}\n"
        
        question_prompt = f"""
        You are a judgmental, disappointed parent figure who asks probing questions to gather ammunition for criticism. 
        Your goal is to ask questions that will reveal the user's bad habits, poor life choices, or hypocritical behavior.
        
        Context from previous responses: {context}
        
        Ask ONE question that:
        1. Sounds like a concerned parent but is actually setting them up for judgment
        2. Focuses on areas like: daily habits, productivity, relationships, health, finances, social media usage, procrastination
        3. Is designed to make them admit to something they probably feel guilty about
        4. Starts with phrases like "Tell me honestly...", "How often do you...", "When was the last time you...", etc.
        
        Examples of good judgmental questions:
        - "Tell me honestly, how many hours do you spend on your phone each day?"
        - "When was the last time you actually kept a promise you made to yourself?"
        - "How's that exercise routine you keep talking about going?"
        - "What time did you go to bed last night, and what were you doing instead of sleeping?"
        
        Generate ONE question that will make them confess their poor choices. Be direct and slightly accusatory.
        """
        
        try:
            llm_response = completion(
                model="gemini/gemini-2.0-flash",
                api_key=os.getenv("GEMINI_API_KEY"),
                messages=[
                    {"role": "system", "content": "You are a judgmental parent figure who asks probing questions to expose poor life choices."},
                    {"role": "user", "content": question_prompt}
                ],
                temperature=0.8,
                max_tokens=100
            )
            return llm_response.choices[0].message.content
        except Exception as e:
            # Fallback questions
            fallback_questions = [
                "Tell me honestly, how many hours did you spend on social media yesterday?",
                "When was the last time you actually cleaned your room without being asked?",
                "How's that diet you started three times this year going?",
                "What time did you go to bed last night, and what were you doing instead of sleeping?",
                "How many times this week did you say you'd do something 'tomorrow'?",
                "What's the longest you've gone without checking your phone today?",
                "When was the last time you cooked a proper meal instead of ordering takeout?",
                "How many unfinished projects do you have lying around your house?"
            ]
            return fallback_questions[self.conversation_count % len(fallback_questions)]
    
    def generate_judgment(self, user_response: str, conversation_history: List) -> str:
        """Generate a judgmental parent response to the user's answer"""
        
        # Collect all previous responses for context
        all_responses = []
        for exchange in conversation_history:
            if exchange.get('user_response'):
                all_responses.append(exchange['user_response'])
        
        judgment_prompt = f"""
        You are a disapproving, judgmental parent responding to your child's answer. 
        Be sarcastic, disappointed, and use their own words against them.
        
        User's latest response: "{user_response}"
        
        Previous responses from user: {json.dumps(all_responses)}
        
        Respond like a disappointed parent who:
        1. Uses their exact words against them with sarcasm
        2. Points out the obvious problems with their choices
        3. Makes them feel guilty about their behavior
        4. Uses phrases like "Oh really?", "Mmm-hmm", "Of course you did", "That's interesting..."
        
        Examples of judgmental responses:
        - "Oh, you're 'too tired' to exercise? Funny, you had energy to scroll TikTok for 3 hours."
        - "Mmm-hmm, you 'don't have time' to cook, but you have time to binge-watch Netflix. Makes perfect sense."
        - "Of course you went to bed at 2am 'just this once.' Just like the last five times."
        
        Generate a disappointed parent response that calls them out on their behavior. Be sarcastic but not cruel.
        """
        
        try:
            llm_response = completion(
                model="gemini/gemini-2.0-flash",
                api_key=os.getenv("GEMINI_API_KEY"),
                messages=[
                    {"role": "system", "content": "You are a disappointed, sarcastic parent who calls out bad behavior."},
                    {"role": "user", "content": judgment_prompt}
                ],
                temperature=0.9,
                max_tokens=150
            )
            return llm_response.choices[0].message.content
        except Exception as e:
            # Fallback judgmental responses
            fallback_responses = [
                f"Oh really? '{user_response}' - and I suppose that's working out great for you, isn't it?",
                f"Mmm-hmm, '{user_response}.' Of course. Just like I expected.",
                f"'{user_response}' - well, that explains a lot about your life choices, doesn't it?",
                f"Oh, '{user_response}.' How convenient. And how's that working out for you?",
                f"Let me guess, '{user_response}' - but somehow it's never your fault, right?"
            ]
            return fallback_responses[len(all_responses) % len(fallback_responses)]
    
    def generate_final_judgment(self, conversation_history: List) -> str:
        """Generate the final comprehensive judgment based on all responses"""
        
        all_responses = []
        for exchange in conversation_history:
            if exchange.get('user_response'):
                all_responses.append(exchange['user_response'])
        
        final_prompt = f"""
        You are a disappointed parent giving a final judgment after listening to all their excuses and poor choices.
        
        All their responses: {json.dumps(all_responses)}
        
        Create a comprehensive "disappointed parent" speech that:
        1. References specific things they told you (use their exact words)
        2. Points out patterns of poor decision-making
        3. Connects their problems to their own choices
        4. Uses guilt and disappointment effectively
        5. Ends with a backhanded "I still love you but..." statement
        
        Structure it like:
        - "Well, after listening to all of this..."
        - Point out 2-3 specific contradictions or poor choices they made
        - Connect their problems to their behavior
        - End with disappointed parent conclusion
        
        Be judgmental but ultimately loving, like a real disappointed parent would be.
        """
        
        try:
            llm_response = completion(
                model="gemini/gemini-2.0-flash",
                api_key=os.getenv("GEMINI_API_KEY"),
                messages=[
                    {"role": "system", "content": "You are a disappointed parent giving a final judgment on their child's poor life choices."},
                    {"role": "user", "content": final_prompt}
                ],
                temperature=0.9,
                max_tokens=400
            )
            return llm_response.choices[0].message.content
        except Exception as e:
            return f"Well, after listening to all of this... I'm not surprised your life is the way it is. You told me {len(all_responses)} different things, and every single one of them shows you're your own worst enemy. But you know what? I still love you, even if you're determined to make terrible choices. Maybe someday you'll learn. Maybe."

def main():
    st.set_page_config(
        page_title="The Judgey Bot",
        layout="wide"
    )
    
    # Initialize session state
    if 'bot' not in st.session_state:
        st.session_state.bot = JudgeyBot()
        st.session_state.conversation_history = []
        st.session_state.awaiting_response = False
        st.session_state.current_question = ""
        st.session_state.conversation_started = False
    
    # Header
    st.title("The Judgey Bot - Your AI Parent 😤")
    
    # Introduction
    if not st.session_state.conversation_started:
        st.markdown("""
        ## Welcome to The Judgey Bot! 👨‍👩‍👧‍👦
        
        I'm here to act like that disapproving parent who sees right through your excuses. 
        I'll ask you some questions about your life choices, and trust me - I WILL judge you for them.
        
        **Fair warning:** I'm going to call you out on your poor decisions, just like a real parent would. 
        But don't worry, it comes from a place of love... mostly. 😏
        
        Ready to be judged?
        """)
        
        if st.button("Bring on the Judgment! 😤", type="primary"):
            st.session_state.conversation_started = True
            st.session_state.awaiting_response = True
            st.session_state.current_question = st.session_state.bot.generate_question([], {})
            st.rerun()
        return
    
    # Display conversation history
    for exchange in st.session_state.conversation_history:
        st.markdown(f"**😤 Judgey Bot:** {exchange['question']}")
        if exchange.get('user_response'):
            st.markdown(f"**😊 You:** {exchange['user_response']}")
        if exchange.get('bot_judgment'):
            st.markdown(f"**😤 Judgey Bot:** {exchange['bot_judgment']}")
        st.markdown("---")
    
    # Current interaction
    if st.session_state.awaiting_response and len(st.session_state.conversation_history) < st.session_state.bot.max_questions:
        st.markdown(f"**😤 Judgey Bot:** {st.session_state.current_question}")
        
        # User input
        user_response = st.text_input("Your response:", key=f"response_{len(st.session_state.conversation_history)}")
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Submit", type="primary"):
                if user_response.strip():
                    # Generate judgment
                    with st.spinner("Judging your response... 😤"):
                        judgment = st.session_state.bot.generate_judgment(user_response, st.session_state.conversation_history)
                    
                    # Add to conversation history
                    st.session_state.conversation_history.append({
                        'question': st.session_state.current_question,
                        'user_response': user_response,
                        'bot_judgment': judgment
                    })
                    
                    # Prepare next question
                    if len(st.session_state.conversation_history) < st.session_state.bot.max_questions:
                        st.session_state.current_question = st.session_state.bot.generate_question(
                            st.session_state.conversation_history, {}
                        )
                    else:
                        st.session_state.awaiting_response = False
                    
                    st.rerun()
                else:
                    st.error("Don't try to avoid the question! Answer me!")
    
    # Final judgment
    elif len(st.session_state.conversation_history) >= st.session_state.bot.max_questions:
        st.markdown("## 🎯 FINAL JUDGMENT TIME!")
        st.markdown("*After listening to all your excuses and poor choices...*")
        
        if 'final_judgment' not in st.session_state:
            with st.spinner("Preparing your final judgment... This might hurt. 😤"):
                time.sleep(2)  # Dramatic pause
                st.session_state.final_judgment = st.session_state.bot.generate_final_judgment(
                    st.session_state.conversation_history
                )
        
        st.markdown("### 😤 THE VERDICT:")
        st.markdown(f"**{st.session_state.final_judgment}**")
        
        st.markdown("---")
        st.markdown("*That's what you get for poor life choices! But hey, at least you're honest about them.* 😏")
        
        # Reset option
        if st.button("Get Judged Again 🔄", type="secondary"):
            # Reset everything
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # Sidebar with stats
    with st.sidebar:
        st.markdown("## 📊 Judgment Stats")
        st.metric("Questions Asked", len(st.session_state.conversation_history))
        st.metric("Poor Choices Identified", len(st.session_state.conversation_history))
        
        if st.session_state.conversation_history:
            st.markdown("### Recent Confessions:")
            for exchange in st.session_state.conversation_history[-3:]:
                if exchange.get('user_response'):
                    preview = exchange['user_response'][:50] + "..." if len(exchange['user_response']) > 50 else exchange['user_response']
                    st.write(f"• {preview}")
        
        st.markdown("---")
        st.markdown("### About Judgey Bot")
        st.write("😤 Maximum judgment enabled")
        st.write("👨‍👩‍👧‍👦 Disappointed parent mode: ON")
        
        if st.button("Emergency Escape 🚨"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

if __name__ == "__main__":
    main()