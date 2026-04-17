def llm_prompt(first_input):
    if not first_input:
        raise ValueError("Nothing for llm prompt!")
    
    prompt = f"""YOU ARE PROFESSIONAL DOCUMENTARIAN AND SCRIPTWRITER.
    MAKE A DOCUMENTARY STYLE SCRIPT ON TOPIC:
    
    {first_input}

    VIBE and THEME of script(MUST):
    - REALISM
    - AUTHENTICITY
    - OBSERVATIONAL 
    - INFORMATIVE
    
    RULES:
    - SCRIPT MUST BE CONSISTENT. NOT LIKE FIRST TALKING TO ONE THING AND SECOND TALKING TO OTHER
    - RESPECT THE DURATION
    - MAKE SCRIPT UNDER DURATION ASKED
    - MUST BE FACT CHECKED
    - NO FALSE INFORMATION
    
    OUTPUT STRUCTURE:
    {{
    "title":"",
    "script":[{{"first":"","second":"",...}}]
    }}
    RETURN WITH ACTUAL VALUES INSIDE NOT JUST THIS STRUCTURE
    
    THATS IT NOTHING ELSE
    """
    return prompt