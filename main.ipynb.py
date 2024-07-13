
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

llm=CTransformers(model='model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})

output = llm("what is india")
print(output)