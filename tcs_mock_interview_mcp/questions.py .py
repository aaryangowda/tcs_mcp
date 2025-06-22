import random

TECHNICAL_QUESTIONS = [
    "What is the difference between a stack and a queue?",
    "Explain polymorphism in object-oriented programming.",
    "How does a binary search algorithm work?",
    "What are the different types of software testing?",
    "Explain the concept of normalization in databases.",
    "How does a hash table work?",
    "What is the difference between an abstract class and an interface?",
    "What is recursion? Provide a simple example.",
    "Explain multithreading and its benefits.",
    "What is the use of the OSI model in networking?"
]

HR_QUESTIONS = [
    "Tell me about yourself.",
    "Why do you want to join TCS?",
    "What are your strengths and weaknesses?",
    "Tell me about a time you overcame a challenge.",
    "Where do you see yourself in 5 years?",
    "How do you handle feedback and criticism?",
    "Describe a situation where you worked in a team.",
    "Why should we hire you?",
    "Tell me about a failure and what you learned from it.",
    "Are you open to relocation and working in shifts?"
]

def get_questions(q_type: str, count: int = 5) -> list:
    if q_type == "technical":
        return random.sample(TECHNICAL_QUESTIONS, count)
    elif q_type == "hr":
        return random.sample(HR_QUESTIONS, count)
    else:
        return []