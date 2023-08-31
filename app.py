from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate

import os
os.environ["OPENAI_API_KEY"] = "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"


llm = OpenAI(temperature=0.7)

# template1 = '''I want you to act as a acting financial advisor for people.
# In an easy way, explain the basics of {financial_concept}.'''
#
# prompt1 = PromptTemplate(
#     input_variables = ['financial_concept'],
#     template = template1
# )
#
# prompt1.format(financial_concept='income tax')
#
# chain1 = LLMChain(llm=llm,prompt=prompt1)
# chain1.run('income tax')

# template2='''In an easy way translate the following sentence '{sentence}' into {target_language}'''
#
# language_prompt = PromptTemplate(
#     input_variables = ["sentence","target_language"],
#     template=template2
# )
#
# language_prompt.format(sentence="How are you",target_language='chinese')
#
# chain2 = LLMChain(llm=llm,prompt=language_prompt)
#
# data = chain2({
#     'sentence':"What is the meaning of emmanuel?",
#     'target_language':'chinese'
# })
#
# print("English Sentence:", data['sentence'])
# print("Target Language:", data['target_language'])
# print("Translated Text:")
# print(data['text'])
#
# data = chain2({
#     'sentence':"Hello How are you?",
#     'target_language':'swahili'
# })
#
# print("English Sentence:", data['sentence'])
# print("Target Language:", data['target_language'])
# print("Translated Text:")
# print(data['text'])
#
# template3 = """ I am travelling to {location}. What are the top 3 things I can do while I am there.
# Be very specific and respond as three bullet points """
#
#
# travel_prompt = PromptTemplate(
#     input_variables=["location"],
#     template=template3,
# )
#
# travel_prompt = travel_prompt.format(location='Paris')
#
# print(f"LLM Output: {llm(travel_prompt)}")

# Chain 1: Tell me about celebrity
first_input_prompt = PromptTemplate(
    input_variables = ['name'],
    template = "Tell me about celebrity {name}"
)
chain1 = LLMChain(
    llm=llm,
    prompt=first_input_prompt,
    output_key='person'
)

# Chain 2: celebrity DOB
second_input_prompt = PromptTemplate(
    input_variables = ['person'],
    template = "when was {person} born"
)
chain2 = LLMChain(
    llm=llm,
    prompt=second_input_prompt,
    output_key='dob'
)

# Chain 3: 5 major events on that day
third_input_prompt = PromptTemplate(
    input_variables = ['dob'],
    template = "Mention 5 major events happened around {dob} in the world"
)
chain3 = LLMChain(
    llm=llm,
    prompt=third_input_prompt,
    output_key='description'
)

#combining chains
from langchain.chains import SequentialChain
celebrity_chain = SequentialChain(
    chains=[chain1,chain2,chain3],
    input_variables=['name'],
    output_variables=['person','dob','description']
)
data = celebrity_chain({'name':"MS Dhoni"})
print("Name:", data['name'])
print("Date of Birth:", data['dob'])
print("Description:")
print(data['person'])
print("Historical Events:")
print(data['description'])