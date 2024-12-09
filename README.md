
# Code Analyzer AI Tool

# Overview

The **Code Analyzer AI Tool is a web-based application built using Streamlit and Groq's AI-powered tools.
It helps users identify performance bottlenecks in code snippets and provides actionable suggestions for optimization. 
The tool focuses on algorithmic efficiency, time and space complexity, memory management, and overall performance improvement.**
---

## Features

- **Code Snippet Analysis**: Users can input code snippets, and the AI will analyze the code to identify potential performance bottlenecks.
- **Optimization Suggestions**: Based on the analysis, the AI provides detailed suggestions for optimization, including algorithmic improvements, memory management, and code refactoring.
- **Interactive Interface**: The application is built using Streamlit, providing a user-friendly interface where users can input code and view the analysis results in real-time.
- **Model Customization**: Users can choose between different models to fine-tune the analysis and suggestions.

---

## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Groq API key (requires account with Groq)

### Steps to Run the Application

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/code-analyzer.git
   cd code-analyzer
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate  # For Windows
   pip install -r requirements.txt
   ```


## After setting up the environment, run the Streamlit app with the following command:

```bash
streamlit run app.py

```

# Design Choices

## Streamlit for the Frontend
- **Description**: Streamlit is used for building the user interface due to its simplicity and rapid prototyping capabilities. It allows for easy integration of interactive elements like text inputs, buttons, and sliders.

## Groq AI Integration
- **Description**: The AI model is integrated via Groq, which is utilized to analyze the provided code snippets and identify bottlenecks. This integration provides high-level analysis based on system performance metrics such as time complexity, memory usage, and CPU consumption.

## LangChain for Chat-like Interaction
- **Description**: LangChain is used to manage the flow of conversation, with memory and context being saved between user inputs. This ensures that the conversation (analysis of code) remains consistent, allowing the AI to provide context-aware suggestions.

## Customizable Model Selection
- **Description**: Users can select different models (llama3-8b-8192 and gemma-7b-it) based on their specific needs for code analysis. This adds flexibility to the tool for various use cases.

# Assumptions and Limitations

## Assumptions
- The code snippets provided by users are in a format that the AI model can process, assuming basic knowledge of common programming languages.
- The AI's suggestions are based on best practices for code optimization but may not cover all edge cases.

## Limitations
- **Scope of Analysis**: The tool provides general performance suggestions but does not cover language-specific or domain-specific optimizations.
- **Input Length**: There may be limitations on the size of code snippets that can be analyzed, especially for very large codebases.
- **Model Limitations**: The analysis is only as good as the AI model's training and may not be 100% accurate in all cases.
