# importing render and redirect
from django.shortcuts import render, redirect
# importing the openai API
import openai
# import the generated API key from the secret_key file

# loading the API key from the secret_key file
openai.api_key = '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'

# this is the home view for handling home page logic
def chatbot(request):
        chatbot_response= None
    # the try statement is for sending request to the API and getting back the response
    # formatting it and rendering it in the template
        # checking if the request method is POST
        if request.method == 'POST':
            # getting prompt data from the form
            # prompt = request.POST.get('prompt')
            user_input = request.POST.get('user_input')
    
            prompt = user_input
            # making a request to the API 
            response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.5, max_tokens=256)
            # formatting the response input
            formatted_response = response['choices'][0]['text']
            # bundling everything in the context
            print(formatted_response)
            chatbot_response = formatted_response
        return render(request,'main.html',{"response": chatbot_response})

































# from django.shortcuts import render
# import openai,os
# from dotenv import load_dotenv
# load_dotenv

# api_key=os.getenv("OPENAI_KEY",None)

# def chatbot(request):
  
#   # chatbot_response =None
#   if api_key is not None and  request.method == "POST":
#     openai.api_key = api_key
#     user_input = request.POST.get('user_input')
    
#     prompt = user_input

#     response =  openai.Completion.create(
#       model="text-davinci-003",
#       prompt= prompt,
#       max_tokens=1024,
#       stop = None,
#       temparature=0.5
#     )
#     print(response)
#     return render(request,'main.html')