def generator(topic, q_count, difficulty):
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

    # Chain 1: Generate the Questions
    quiz_prompt = PromptTemplate(
        input_variables=['topic', 'q_count', 'difficulty'],
        template="I want {q_count} MCQ Questions on {topic} with {difficulty} level..."
    )
    # Renamed for clarity
    quiz_chain = LLMChain(llm=llm, prompt=quiz_prompt, output_key='quiz_content')

    # Chain 2: Generate the Solutions
    solution_prompt = PromptTemplate(
        input_variables=['quiz_content'], # Takes output of chain 1
        template="Answer all these questions: {quiz_content}..."
    )
    # Renamed for clarity
    solution_chain = LLMChain(llm=llm, prompt=solution_prompt, output_key='solution_content')

    # Sequential Chain to link them
    final_chain = SequentialChain(
        chains=[quiz_chain, solution_chain],
        input_variables=['topic', 'q_count', 'difficulty'],
        output_variables=['quiz_content', 'solution_content']
    )
    
    response = final_chain({'topic': topic, 'q_count': q_count, 'difficulty': difficulty})
    return response
