import os
from pypdf import PdfReader
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
llm = OpenAI(api_key=API_KEY)


def extract_first_page_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    text += reader.pages[0].extract_text() + "\n"
    text += reader.pages[1].extract_text() + "\n"
    return text


def get_name_from_chatgpt(text):
    prompt = """
    You are an AI assistant. Just give me the name of the paper.

    Correct format of the name:
    Year. Author1 (et al.) Title

    Example of correct format of the name:
    2023. Liu et al. Instruction position matters in sequence generation with large language models
    2024. Koo et al. Benchmarking cognitive biases in large language models as evaluators
    2025. Deldjoo and Noia. Cfairllm --- Consumer fairness evaluation in large-language model recommender system
    """
    messages = [
        {
            "role": "system",
            "content": prompt,
        },
        {"role": "user", "content": text},
    ]

    completion = llm.chat.completions.create(model="gpt-4o-mini", messages=messages)
    abstract = completion.choices[0].message.content.strip()
    return abstract


def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf") and not filename.startswith("."):
            print(filename)
            file_path = os.path.join(folder_path, filename)
            text = extract_first_page_text(file_path)
            name = get_name_from_chatgpt(text)
            new_filename = name + ".pdf"
            os.rename(file_path, os.path.join(folder_path, new_filename))


if __name__ == "__main__":
    os.system("clear")
    folder_path = "/Users/armin/Desktop/HEC/Research/Data Analytics Group/LLM fairness"
    rename_files(folder_path)
