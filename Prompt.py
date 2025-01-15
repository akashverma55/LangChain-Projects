# ================ Importing Libraries =============== #
from langchain_community.llms import Ollama
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import streamlit as st
from langchain.memory import ConversationBufferMemory

# ==================================================== #

# =========== Initializing the LLM Model ============ #
llm = Ollama(
    model='qwen'  # Model downloaded and available locally
)

# ==================================================== #

# ========= Prompt Templates Creation ================ #
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template='Tell me about {name}'
)

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template='{person} Date of birth?'
)

third_input_prompt = PromptTemplate(
    input_varibales = ['dob'],
    template = '5 major events happened on {dob} in the world'
)
# ==================================================== #

# =============== Storing the Content ================ #

person_memory = ConversationBufferMemory(input_key = 'name', memory_key = 'celebrity_history')
dob_memory = ConversationBufferMemory(input_key = 'person', memory_key = 'dob_history')
events_memory = ConversationBufferMemory(input_key = 'dob', memory_key = 'events_history')

# ==================================================== #

# ================= Creating Chains ================== #
chain1 = LLMChain(
    llm=llm,
    prompt=first_input_prompt,
    verbose=True,
    output_key='person',
    memory = person_memory
)

chain2 = LLMChain(
    llm=llm,
    prompt=second_input_prompt,
    verbose=True,
    output_key='dob',
    memory = dob_memory
)

chain3 = LLMChain(
    llm=llm,
    prompt=third_input_prompt,
    verbose=True,
    output_key='events',
    memory = events_memory
)

Chain = SequentialChain(
    chains= [chain1,chain2,chain3],
    input_variables = ['name'],
    output_variables = ['person','dob','events'],
    verbose=True,
)

# ==================================================== #

# =============== Streamlit Framework =============== #
st.title('Celebrity Details')
input_text = st.text_input("Ask Anything Here")

if input_text:
    # Use the chain to generate response
    response = Chain({'name':input_text})
    st.write(response)

    with st.expander('Person Name'):
        st.info(person_memory.buffer)

    with st.expander('Date'):
        st.info(dob_memory.buffer)

    with st.expander('Major Events'):
        st.info(events_memory.buffer)

# ==================================================== #
