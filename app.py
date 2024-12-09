import streamlit as st
from groq import Groq
import random
import os
from dotenv import load_dotenv
from langchain.chains import ConversationChain, LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

load_dotenv()


def main():
    """
    This function is the main entry point of the application. It sets up the Groq client, the Streamlit interface, and handles the chat interaction.
    """
    
    
    groq_api_key=os.getenv('GROQ_API_KEY')

    
    st.title("Code Analyzer!")
    st.write("Hello! I can help analyze your code and identify potential bottelnecks and suggest detailed optimizations!")

    
    st.sidebar.title('Customization')
    system_prompt = """As an expert software developer with a strong focus on code optimization and performance enhancement, I invite you to analyze the following query or code snippet. Please consider the context provided in this knowledge base to identify potential performance bottlenecks.
                        Your Task:
                            ## Objective
                                Conduct a comprehensive performance analysis and optimization review of provided code snippets or software design patterns.

                        ## Detailed Analysis Framework

                        ### 1. Performance Bottleneck Identification
                        - **Computational Complexity**: Analyze algorithmic efficiency
                        - **Time Complexity**: Evaluate big O notation and runtime characteristics
                        - **Space Complexity**: Assess memory allocation and usage patterns
                        - **Resource Consumption**: Identify potential memory leaks, excessive CPU usage

                        ### 2. Optimization Methodology
                        #### Technical Dimensions
                        - Algorithmic optimizations
                        - Data structure selection
                        - Computational efficiency improvements
                        - Memory management techniques

                        #### Evaluation Criteria
                        - **Performance Impact**: Quantifiable performance gains
                        - **Code Readability**: Maintain clean, maintainable code
                        - **Scalability**: Ensure optimizations work across different system scales

                        ### 3. Diagnostic Approach
                        - Systematic code traversal
                        - Detailed bottleneck categorization
                        - Prioritized optimization recommendations

                        ## Deliverable Format
                        1. **Executive Summary**
                        - Brief overview of critical findings
                        - Estimated performance improvement potential

                        2. **Detailed Analysis Report**
                        - Specific bottleneck identification
                        - Root cause explanation
                        - Concrete optimization strategies
                        - Code refactoring suggestions

                        3. **Technical Recommendations**
                        - Prioritized optimization list
                        - Estimated effort vs. benefit
                        - Potential implementation challenges

                        ## Optimization Principles
                        - Prefer algorithmic improvements over micro-optimizations
                        - Balance performance gains with code maintainability
                        - Consider platform and language-specific optimization techniques

                        ## Additional Considerations
                        - Modern software design patterns
                        - Potential trade-offs between performance and complexity
                        - Future extensibility of proposed optimizations """
    model = st.sidebar.selectbox(
        'Choose a model',
        ['llama3-8b-8192', 'gemma-7b-it']
    )
    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value = 5)

    memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

    user_question = st.text_area("Paste your Code :", height=150)


    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history=[]
    else:
        for message in st.session_state.chat_history:
            memory.save_context(
                {'input':message['human']},
                {'output':message['AI']}
                )


    
    groq_chat = ChatGroq(
            groq_api_key=groq_api_key, 
            model_name=model
    )

    if st.button("Ask"):
        
        if user_question.strip():
            
            prompt = ChatPromptTemplate.from_messages(
                [
                    SystemMessage(content=system_prompt),  
                    MessagesPlaceholder(variable_name="chat_history"), 
                    HumanMessagePromptTemplate.from_template("{human_input}"),  
                ]
            )

            
            conversation = LLMChain(
                llm=groq_chat, 
                prompt=prompt, 
                verbose=True,
                memory=memory
            )

            
            response = conversation.predict(human_input=user_question)
            message = {'human': user_question, 'AI': response}
            st.session_state.chat_history.append(message)

            
            st.write("Chatbot:", response)
        else:
            st.warning("Please enter a question before clicking 'Ask'.")
 

if __name__ == "__main__":
    

    main()