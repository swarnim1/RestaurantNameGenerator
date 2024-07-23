from huggingface_hub import InferenceClient

'''This methold make api call to llama 3 instruct''' 
def llm(promt :str)->str:
    final_message = ""
    client = InferenceClient(
        "meta-llama/Meta-Llama-3-8B-Instruct",
        token="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",
        
    )

    for message in client.chat_completion(
        messages=[{"role": "user", "content": promt}],
        max_tokens=500,
        stream=True,
    ):  
        final_message = final_message + str(message.choices[0].delta.content)
    return final_message

