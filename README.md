# Django Ollama Chat App

This Django project showcases the power of building local AI-powered chat applications using the Ollama library and Meta's Llama 3 model 

[Accompanying post with additional info here](https://scoutapm.com/blog/building-ai-with-ollama-and-django)

**Key Features**

* **Local AI :**  Leverages Ollama to run the Llama 3 model locally
* **Django Framework:** Built on the Django web framework
* **Real-time Streaming:**  Chat interface displays AI responses as they are generated
* **Open Source:**  Fully open-source code, allowing you to explore, modify, and extend the project to your liking

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/scoutapp/ollama-django
   cd your-repo-name

2. **Start Ollama: (If you haven't already)**
   ```bash
   docker pull ollama/ollama
   docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
   docker exec -it ollama ollama run llama3

3. **Set Up Virtual Environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt 

5. **Run the Server:**
   ```bash
   python manage.py runserver

**Chat Away:** Open your browser and visit http://localhost:8000/chat/ to start chatting with your AI

**Project Structure**

chat/: Contains the Django app for the chat interface and Ollama interaction.
templates/: HTML template for the chat interface.
requirements.txt: Lists the project dependencies.

**Future Enhancements**

Improved Styling: CSS enhancements for a more visually appealing chat interface.
Reduced Latency: Optimization techniques to minimize response delays.
Additional Models: Integration of other Ollama-supported models.
Multimodal AI: Exploration of combining text with images and audio.

**Contributing**

Contributions are welcome! Feel free to open issues, submit pull requests, or share your feedback to help improve this project.

**Acknowledgements**

[Ollama](https://ollama.com/download): For providing a powerful library for local AI model execution.

[Django](https://www.djangoproject.com): For the excellent web development framework.

[Llama 3](https://llama.meta.com/llama3): The open-source AI model that powers this chat app.

