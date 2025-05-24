import tiktoken

#GPT-3.5-Turbo
model = "gpt-3.5-turbo"
encoding = tiktoken.encoding_for_model(model)
tokens_list = encoding.encode("You are a product categorizer.")

print(f"Tokens list: {tokens_list}")
print(f"Number of tokens: {len(tokens_list)}")
print(f"For the model {model} it costs ${len(tokens_list)/1000*0.002}:")
      
#GPT-4
model = "gpt-4"
encoding = tiktoken.encoding_for_model(model)
tokens_list = encoding.encode("You are a product categorizer.")

print(f"Tokens list: {tokens_list}")
print(f"Number of tokens: {len(tokens_list)}")
print(f"For the model {model} it costs ${len(tokens_list)/1000*0.03}:")

print(f"The GPT-4 cost is {0.03/0.001} bigger than the GPT-3.5-Turbo cost.")