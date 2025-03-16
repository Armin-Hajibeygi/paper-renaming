# paper-renaming
`paper-renaming` is a Python script designed to automate the renaming of papers.

## Features
- Extracts text from the first page of PDF files.
- Uses OpenAI's GPT model to generate a name for the paper.
- Renames PDF files based on the generated name.

## Requirements
- Python 3.x
- `pypdf` library
- `openai` library
- `python-dotenv` library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Armin-Hajibeygi/paper-renaming.git
    cd paper-renaming
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate 
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your OpenAI API key:
    ```sh
    API_KEY="your_openai_api_key"
    ```

## Usage
1. Place the PDF files you want to rename in a folder.

2. Update the `folder_path` variable in `renaming.py` to the path of your folder:
    ```python
    folder_path = "/path/to/your/folder"
    ```

3. Run the script:
    ```sh
    python renaming.py
    ```