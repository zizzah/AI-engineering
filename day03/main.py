from router import process_prompt



if __name__ == "__main__":
    prompt1 = "Explain the significance of the Turing Test in evaluating artificial intelligence."
    result = process_prompt(prompt1)
    print("\nProcessed Prompt Results:")
    for key, value in result.items():
        print(f"{key}: {value}")