from crewai import Agent, Task, Crew, Process

# Use model identifier as string (ensure it's compatible with Ollama)
model = "ollama/llama3.2"  # Use model identifier as a string

email = input("Enter your email address: ")
print("received,", email)

classifier = Agent(
    role='email classifier',
    goal="Accurately classify emails based on their importance. Give every email one of these ratings: 'important', 'casual' or 'spam'.",
    backstory="You are an AI assistant whose only job is to classify emails accurately and honestly. Do not be afraid of giving emails a bad rating if they are not important. Your job is to help the user manage their inbox.",
    verbose=True,
    allow_delegation=False,
    llm=model,  # Pass as string model identifier
)

responder = Agent(
    role='email responder',
    goal="Based on the importance of the email, write a concise and simple response. If the email is rated 'important', write a formal response. If the email is rated 'casual', write a casual response. If the email is rated 'spam', ignore the email. No matter what, be very concise.",
    backstory="You are an AI assistant whose only job is to write short responses to emails based on their importance. The importance of the email will be provided to you by the 'classifier' agent.",
    verbose=True,
    allow_delegation=False,
    llm=model
)

classify_email = Task(
    description=f"Classify the '{email}'",
    agent=classifier,
    expected_output="One of these three options: 'important', 'casual' or 'spam'",
)

respond_to_email = Task(
    description=f"Respond to the email: '{email}' based on the importance provided by the 'classifier' agent",
    agent=responder,
    expected_output="A very concise response to the email based on the importance provided by the 'classifier' agent",
)

crew = Crew(
    agents=[classifier, responder],
    tasks=[classify_email, respond_to_email],
    process=Process.sequential
)

output = crew.kickoff()
print(output)
