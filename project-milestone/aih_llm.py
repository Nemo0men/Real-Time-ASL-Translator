from transformers import pipeline

# Initialize with a more capable model for controlled text generation
generator = pipeline('text-generation', model='gpt2')

def generate_sentence():
    print("Enter words to include in the sentence (separated by spaces):")
    user_input = input().strip()
    fragments = user_input.split()
    print(fragments)
    

    # More directive prompt that emphasizes using ALL the input words
    prompt = f"repeat the phrase 'hello world' exactly"
    
    # Adjust generation parameters for more controlled output
    output = generator(
        prompt,
        max_length=50,        # Shorter length to avoid rambling
        num_return_sequences=1,
        do_sample=True,
        temperature=0.6,      # Lower temperature for more focused output
        top_p=0.9,           # Add nucleus sampling
        truncation=True      # Explicitly enable truncation
    )
    
    generated_text = output[0]['generated_text']
    
    # Extract only the sentence after our prompt marker
    try:
        final_text = generated_text.split("Sentence:")[-1].strip()
        if not final_text:
            final_text = generated_text
    except:
        final_text = generated_text

    return final_text

if __name__ == "__main__":
    # Generate and print sentence
    result = generate_sentence()
    print("\nGenerated sentence:")
    print(result)