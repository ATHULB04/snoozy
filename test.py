from gpt4all import GPT4All

file_path="C:/Users/athul/AppData/Local/nomic.ai/GPT4All/gpt4all-13b-snoozy-q4_0.gguf"
def datac(data):
    model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf",model_path="C:/Users/athul/AppData/Local/nomic.ai/GPT4All/")
    output = model.generate(f"{data}")
    return output