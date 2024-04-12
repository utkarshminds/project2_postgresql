import streamlit as st
from openai import OpenAI
import openai

def plan_vacation_openai(city_name):
    '''
    create a one day vacation plan for the city
    '''

    APIKEY = st.secrets['OPENAI']['APIKEY']

    
    client = OpenAI(api_key=APIKEY)

    try:
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": "You are a vacation planner who is organizing a tour of one day in a city. The target is a family of two adults and two teenagers. Tour should include places of attraction, museums, shopping and restaurants. Day should start at 9 am till 9 pm."
            },
            {
            "role": "user",
            "content": f"I am visiting city of {city_name} create a vacation plan for me"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        answer = response.choices[0].message.content
        
        st.write(answer)
    
    except openai.APIError as e:
        #Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass
    except openai.APIConnectionError as e:
        #Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass
    except openai.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass