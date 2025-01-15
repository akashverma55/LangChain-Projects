# LangChain-Ollama Streamlit Application

## Overview
This project is a Streamlit-based application that leverages the **Qwen model** from **Ollama** to deliver AI-powered insights on a variety of topics. With a focus on structured and contextualized responses, the app uses **LangChain** to handle multi-step queries, making it ideal for exploring detailed information about people, events, and more.

---

## Features

### 1. **Customizable Prompting**
   - Utilizes `PromptTemplate` from LangChain to create dynamic and context-aware queries.

### 2. **Memory Integration**
   - Implements `ConversationBufferMemory` to retain context across multiple queries and maintain structured conversations.

### 3. **Chained LLMs**
   - Employs `LLMChain` and `SequentialChain` to build multi-step processes for generating rich, detailed responses.

### 4. **User-Friendly UI**
   - A simple and intuitive front-end powered by Streamlit to interact with the AI seamlessly.

---

## How It Works
1. **User Input**: Enter a query in the Streamlit interface (e.g., "Tell me about Albert Einstein").
2. **Processing**: The app:
   - Generates an initial response based on the input.
   - Extracts specific details like the subject's date of birth.
   - Fetches related historical events or additional insights.
3. **Output**: Displays structured and detailed information with context maintained across queries.

---

## Tech Stack

- **LangChain**: For building the LLM chains and memory management.
- **Ollama**: Running the Qwen model locally for AI processing.
- **Streamlit**: Creating an interactive web-based interface.
- **Python**: Backend logic and integrations.

---

## Installation and Setup

### Prerequisites
1. Python 3.8 or higher
2. Ollama installed with the Qwen model downloaded locally.
3. Virtual environment tools like `venv` or `conda`.

### Steps
1. Clone the repository:
   ```bash
   git clone <github.com/akashverma55/>
   cd <LangChain-Projects>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run Prompt.py
   ```

---

## Example Usage
1. **Query**: "Tell me about Nikola Tesla."
   - **Response**: Tesla was a Serbian-American inventor, engineer, and futurist known for his contributions to alternating current (AC) power systems.

2. **Query**: "Nikola Tesla's date of birth?"
   - **Response**: July 10, 1856.

3. **Query**: "5 major events on July 10, 1856."
   - **Response**: A list of historical events tied to the specified date.

---

## File Structure
```
.
├── Prompt.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── constants.py         # Stores API keys or sensitive information
├── README.md            # Project documentation
└── .gitignore           # Ignored files
```

---

## License
Feel free to use, modify, and distribute the code.

---

## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## Acknowledgments
- **LangChain Team** for their excellent library.
- **Ollama** for providing a powerful local LLM solution.
- **Streamlit** for simplifying web app development.

---

## Contact
For questions or feedback, reach out at [akvakv150@example.com].

