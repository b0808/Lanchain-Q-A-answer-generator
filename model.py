import os
import streamlit as st
from langchain.prompts import PromptTemplate

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from API import GOOGLE_API_KEY
def generotor(a,b,c):
    

    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)
    from langchain.chains import LLMChain

    prompt_template_name = PromptTemplate(
            input_variables=['topic','Que','diff'],
            template=" i want {Que} number of MCQ Question on {topic} with {diff} level with 4 option Question with newline for each question and each option also on newline "
        )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name,output_key= 'Que_no')

    prompt_template_items = PromptTemplate(
            input_variables=['Que_no'],
            template="""answer this all questions  {Que_no} with each solution start with Question number Solution: and each solution is on newline"""
        )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items,output_key = "Sol")

    from langchain.chains import SequentialChain

    chain = SequentialChain(chains = [name_chain,food_items_chain],input_variables = ['topic','Que','diff'],output_variables = ['Que_no','Sol'])
    response = chain({'topic': a, 'Que': b, 'diff': c})
    return response

