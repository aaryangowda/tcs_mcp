from fastapi import FastAPI, Request
import random

app = FastAPI()

technical_questions = [
    "Can you explain the concept of Object-Oriented Programming (OOP)?",
    "Walk me through the Software Development Life Cycle (SDLC). Why is each phase important?",
    "What are some commonly used data structures and their applications?",
    "Can you explain the Agile Model and its key benefits in software development?",
    "What are the main differences between SQL and NoSQL databases?",
    "What are the core principles of a Database Management System (DBMS)?",
    "Which sorting algorithms are you familiar with? Can you discuss their time complexities?",
    "Explain the difference between a process and a thread in Operating Systems.",
    "Tell me about common network protocols and their functions — for example, TCP/IP or HTTP.",
    "Could you write a program to reverse a string or calculate the factorial of a number?"
]

hr_questions = [
    "To start off, tell me about yourself.",
    "Why do you want to join TCS?",
    "What are your biggest strengths and one area you'd like to improve?",
    "Are you open to relocating for a job?",
    "Would you be comfortable working in night shifts if required?",
    "Where do you see yourself five years from now?",
    "What do you know about TCS and its competitors?",
    "Would you say you’re a team player? Could you share an example?",
    "How do you handle pressure or tight deadlines?",
    "What are your salary expectations, if any?"
]

@app.post("/generate_question")
async def generate_question(request: Request):
    body = await request.json()
    q_type = body.get("type", "").lower()
    if q_type == "technical":
        question = random.choice(technical_questions)
    elif q_type == "hr":
        question = random.choice(hr_questions)
    else:
        question = "Invalid type. Please specify 'technical' or 'hr'."
    return {"question": question}
