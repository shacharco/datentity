from mistralai import Mistral
import json


class Translator:
    def __init__(self):
        self.text_placeholder = "text_placeholder"
        self.format_relationships_placeholder = "format_relationships_placeholder"
        self.format_objects_placeholder = "format_objects_placeholder"
        self.api_key = "vGluYcppWpS6nSVvfWGdhwynZVjBaXLb"
        self.texts = []
        self.formats = []
        self.formatted_data = {}
        self.prompt = f"""
            Convert the following text into a structured format based on the given format definition.

            Text: "{self.text_placeholder}"
            
            Format definition:
            - The result must contain two main sections: `objects` and `graph`.
            - `objects`: A list of objects. The objects must contain the following fields by according to the types:
                {self.format_objects_placeholder}
            - `graph`: A list of connections between objects. Each connection must include the following fields:
                {self.format_relationships_placeholder}            
            Use the information from the text to populate all necessary fields in the format definition. Ensure the result strictly adheres to this format.
            """

    def add_format(self, format):
        self.formats.append(format)

    def parse(self, text):
        for format in self.formats:
            prompt = self.prompt
            prompt = prompt.replace(self.text_placeholder, text)
            prompt = prompt.replace(self.format_objects_placeholder, str(format["objects"]))
            prompt = prompt.replace(self.format_relationships_placeholder, str(format["relationships"]))
            # Call the LLM (GPT-4 or another model)
            try:
                self.formatted_data = self.send_llm_api_request(prompt)  # Convert JSON string to Python dictionary
                return self.formatted_data
            except Exception as e:
                print(f"Error generating format: {e}")
                return None
            except SyntaxError as e:
                print(f"SyntaxError generating format: {e}")
                return None

    def send_llm_api_request(self, prompt):
        url = "https://api.ai21.com/studio/v1/j1-large/complete"

        model = "mistral-large-latest"

        client = Mistral(api_key=self.api_key)

        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )
        answer = chat_response.choices[0].message.content
        start = answer.find("{")
        end = answer.rfind("}")
        return json.loads(answer[start:end+1])
