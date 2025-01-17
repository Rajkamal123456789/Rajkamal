import streamlit as st
import google.generativeai as genai 


st.set_page_config(page_title="Gemini Clone", page_icon="gc.ico")
st.image("gc.ico", width=200)

def front_end(): 
    
    st.html("<html><body><center><h1><font color=""Gray"">Gemini<h4><font color=""blue""> The Digital Sibling </center></body></html>")
    text=st.chat_input("Ask Gemini")
    return text


def Gemini_integration(text): 
            if text==None:
                pass 
            else:
                api_key = 'AIzaSyC4ni8FGnv7cNCHt5o74QWhilO6larwi_c' # API key
                genai.configure(api_key=api_key)
                model=genai.GenerativeModel('gemini-pro')
                chat=model.start_chat(history=[])
                response=chat.send_message(text)
                result=response.text
                st.write(result)
                return result

            
        


    
text=front_end()
result=Gemini_integration(text)


