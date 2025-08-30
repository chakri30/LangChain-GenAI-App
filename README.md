Project Title
LangChain GenAI App with Memory

Description
This is a simple Generative AI application built using the LangChain framework. It demonstrates how to create a conversational chatbot that can remember previous interactions within a session using the ConversationBufferMemory component. The application is a starting point for building more complex, context-aware AI applications.

Features
Conversational Memory: The AI can remember and refer to the history of the conversation, providing a more natural and coherent user experience.

LangChain Integration: Utilizes LangChain's core components like ConversationChain and ChatPromptTemplate to orchestrate the application's logic.

Modular Design: The project is structured to be easily expanded with additional features like agents, tools, or Retrieval-Augmented Generation (RAG).

Setup and Installation
Follow these steps to set up and run the project locally.

Clone the repository:

Bash

git clone https://github.com/your_username/LangChain-GenAI-App.git
cd LangChain-GenAI-App
(Note: Replace your_username with your actual GitHub username.)

Create a virtual environment:

Bash

python -m venv venv
Activate the virtual environment:

Windows: venv\Scripts\activate

macOS/Linux: source venv/bin/activate

Install dependencies:

Bash

pip install -r requirements.txt
(Note: You will need to create a requirements.txt file by running pip freeze > requirements.txt after you have installed all the packages.)

Configuration
This project uses a Google Gemini API key.

Get your API key:

Go to Google AI Studio and create a new API key.

Set up the .env file:

Create a file named .env in the root of your project.

Add your API key to the file in the following format:

GOOGLE_API_KEY="your_api_key_here"
The .env file is included in the .gitignore file to ensure your key is not uploaded to GitHub.

Usage
Run the app.py script from your terminal to start the conversation.

Bash

python app.py
The script will automatically run three turns of a conversation, demonstrating how the AI retains context. To create a continuous, interactive chat, you can modify the app.py file with a loop.

Author
Ch. Chakri
