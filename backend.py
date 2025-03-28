from fastapi import FastAPI
from crewai import Agent, Task, Crew
from langchain.chat_models import ChatOpenAI
import chromadb

app = FastAPI()

# Initialize AI Model
llm = ChatOpenAI(model="gpt-4", temperature=0.5)

# Initialize ChromaDB
client = chromadb.PersistentClient(path="./risk_data_db")
collection = client.get_or_create_collection("project_risk")

# Define AI Agent
risk_agent = Agent(
    role="Risk Scoring Agent",
    goal="Analyze transaction and investment risks in real-time.",
    backstory="An expert in financial risk assessment with deep knowledge of economic trends.",
    llm=llm
)

# Define Task
risk_task = Task(
    description="Analyze financial transactions and market trends for risks.",
    agent=risk_agent
)

# Crew Execution
crew = Crew(agents=[risk_agent], tasks=[risk_task])

@app.get("/analyze_risk/")
def analyze_risk():
    result = crew.kickoff()
    return {"risk_analysis": result}

@app.get("/query_risk/")
def query_risk(query: str):
    results = collection.query(query_texts=[query], n_results=1)
    return results

# Run API (if not running inside Jupyter)
if _name_ == "_main_":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
