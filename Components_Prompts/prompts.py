from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
import streamlit as st 

model = OllamaLLM(model='llama3.2:1b')

st.header('Research Tool')


paper_input = st.selectbox('Select paper to be summarised',['Select..',"Attention is all you need","BERT: Pre-training of Deep Bidirectional Transformers","GPT-3: language models are few shot learners"])

style_input = st.selectbox('Select explanation style',['Beginner-friendly','Technical','Code-oriented','Mathematical'])

length_input =st.selectbox('Select output length',['Short','Medium','Long'])

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input','length_input'],
validate_template=True
)
chain = template|model
if st.button('Summarise'):
    output =chain.invoke({'paper_input':paper_input,
                  'style_input':style_input,
                  'length_input':length_input})
    print('Output generated..')
    st.write(output)