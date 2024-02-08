from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
import google.generativeai as genai
from api_key import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)


# function for LLM Model
def gemini_response(yt_transript,prompt):
     model = genai.GenerativeModel(model_name='gemini-pro')
     response = model.generate_content(prompt+yt_transript)
     return response.text


# function for get the particular video id
def youtube_transcript(youtube_video_url):
     try:
          script = youtube_video_url.split('=')[1]
          print(script)
          transcript_text = YouTubeTranscriptApi.get_transcript(script,languages=['de', 'en'])

          transcript = " "
          for i in transcript_text:
               transcript += " " + i['text']

          return transcript
     except Exception as e:
          raise e
    



prompt = '''
     You are Youtube video summarizer. You will be taking the transcript text
     and summarizing the entire video and providing the important summary in points
     within 250 words. Please provide the summary of the text given here: '''



# Initializing frontend with the help of Streamlit App
st.title('Youtube Video Note App')
youtube_link = st.text_input('Enter Your Youtube Link : ')

if youtube_link:
     videoid = youtube_link.split('=')[1]
     st.image(f"http://img.youtube.com/vi/{videoid}/0.jpg",use_column_width=True)


btn = st.button('Notes')

if btn:
    transcript_txt = youtube_transcript(youtube_link)

    if transcript_txt:
         result = gemini_response(transcript_txt,prompt)
         st.header('Your Note : ')
         st.write(result)





