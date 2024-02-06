import utils
import json
import streamlit as st
from streaming import StreamHandler

from langchain.llms import OpenAI
from langchain.chains import ConversationChain

from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain_community.chat_models import ChatOpenAI


st.set_page_config(page_title="Try it out!", page_icon="💬")
st.header('Try it out')

utils.configure_openai_api_key()

print(st.session_state)
# Multiline string
# Split the text into segments based on double newline, indicating separation between entries
segments = st.session_state.examples.strip().split('\n\n')
#print(segments)
#print('done printing segments')
# Parse each segment into a dictionary with 'statement' and 'response' keys
data = []
for segment in segments:
    lines = segment.split('\n')
    entry = {
        "statement": lines[0].split(': ', 1)[1],  # Split once and take the second part as the value
        "response": lines[1].split(': ', 1)[1]    # Split once and take the second part as the value
    }
    data.append(entry)

#print(data);
#print(type(data))
#examples = json.dumps(data, indent=4)
examples = data
# Print the formatted JSON object
#print(examples)
#print('type of examples is ' + type(examples))
#print(st.session_state.prefix)
example_prompt = PromptTemplate(
  input_variables=[], template=st.session_state.prefix
)
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Statement: {statement}",
    input_variables=["statement"]
)

llm = ChatOpenAI(model_name='gpt-3.5-turbo-16k')

statement = st.text_area('Enter a statement or question from the bot', '')
if st.button('Submit'):
  response = llm.predict(prompt.format(statement=statement))
  st.write(response)
