from openai import OpenAI

class MySummarizeAssistant:
    def __init__(self):
        self.messages = [
            {"role": "system",
             "content":
                 "You are very good at summarizing and extracting content. You will Summarize the article in 100 words or less. Focus on the main points, avoiding unnecessary details, and ensure the summary captures the essence of the content."}]
        self.client = OpenAI()

    def ask_assistant(self, question):
        self.messages.append({"role": "user", "content": question})
        response = self.client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=self.messages
        )
        answer = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})
        return answer

    def text_to_speech(self, text):
        return self.client.audio.speech.create(
            model="tts-1",
            voice="fable",
            input=text
        )
