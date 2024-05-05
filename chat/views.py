from django.shortcuts import render
from django.http import StreamingHttpResponse
from .ollama_api import generate_response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        user_input = request.POST["user_input"]
        prompt = f"User: {user_input}\nAI:"
        response = generate_response(prompt)
        #print(response['message']['content'])
        print(response)
        return StreamingHttpResponse(response, content_type='text/plain')
    return render(request, "chat.html")