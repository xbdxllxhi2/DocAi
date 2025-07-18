# -*- coding: utf-8 -*-
"""testGenerator.ipynb

Automatically generated by Colab.
"""

!pip install --quiet --upgrade langchain langchain-community langchain-chroma
!pip install -qU langchain-openai
!pip install --upgrade --quiet  GitPython tiktoken

import getpass
import os


os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

from langchain.prompts import PromptTemplate

template = """
You are an expert Java developer. Your task is to generate unit test cases for the following Java code.

Code:
{java_code}

Please write JUnit test cases with proper assertions, mocking where necessary, and include comments.
just plain java code or javaodc.

Output:
"""
prompt = PromptTemplate(
    input_variables=["java_code"],
    template=template,
)

from langchain.chains import LLMChain

# Initialize the chain
chain = LLMChain(llm=llm, prompt=prompt)

# Example Java code for which to generate test cases
java_code = """
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
    public int subtract(int a, int b) {
        return a - b;
    }
}
"""

# Generate test cases
test_cases = chain.run(java_code)
print(test_cases)

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

feedback = "Please add edge cases and include tests for null inputs."
improved_test_cases = conversation.run(f"{test_cases}\n{feedback}")
print(improved_test_cases)
