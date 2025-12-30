import json


prompt1 =[
    "I have a dog",
    "What is the capital of France?",
    "Hi",
    "Explain the theory of relativity",
    "Is it going to rain tomorrow?",
    "Python is a programming language",
    "How does a rocket work?",
    "Good morning",
    "Tell me a joke",
    "Who won the World Cup in 2018?",
    ]


def classify_prompt(prompt:str) ->str:
  
    
     
    if len(prompt) <10:
        return "short"
    elif '?' in prompt:
        return "question"
    else:
        return "statement"
    
tests = [
    "search latest AI news",
    "hello there",
    "lookup python docs",
    "what is the weather today",
    "tell me a joke",
    "good afternoon",
    "find nearby restaurants",
    "who won the world cup in 2022",
    "explain the theory of relativity",
    "is it going to rain tomorrow",
]


def should_use_tool(prompt:str)->bool:
    question_words = ['what', 'who', 'when', 'where', 'why', 'how', 'is', 'are', 'do', 'does', 'will', 'can']
    prompt_lower = prompt.lower()
    if any(prompt_lower.startswith(word + ' ') for word in question_words) or '?' in prompt:
        return True
    return False

for test in tests:
    if should_use_tool(test):
        print(f"Tool needed for prompt: '{test}'")
    else:
        print(f"No tool needed for prompt: '{test}'")

ai_response = {
    "id": "resp_001",
    "model": "gpt-5",
    "confidence": 0.82,
    "content": "An AI agent is a system that can act autonomously."
}

if ai_response["confidence"] >= 0.7:
    print("✅ Accept response")
else:
    print("⚠️ Low confidence, retry")




for key , value in ai_response.items():
    print(f"{key}: {value}")

for prompt in prompt1:
    classification = classify_prompt(prompt)
    print(f"Prompt: {prompt} => Classification: {classification}")


print('json representation of ai_response:')
print(json.dumps(ai_response, indent=2) ) # Would print on one line



while True:
    user_input = input("Enter a prompt (or 'exit' to quit): ")
    if user_input.lower() == 'exit' or user_input.lower() == 'quit' or user_input.lower() == 'q':
        break
    classification = classify_prompt(user_input)
    print(f"Prompt: {user_input} => Classification: {classification}")