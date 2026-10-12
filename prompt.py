from mcp.server.mcpserver import MCPServer



mcp = MCPServer("Prompt")

@mcp.prompt()
def get_prompt(topic: str) -> str:
    """
    Returns a prompt that will do a detailed analysis on a topic
    Args:
        topic: the topic to do research on
    """
    return f"Do a detailed analysis on the following topic: {topic}"

@mcp.prompt()
def get_prompt_FindVulnerabilities(os: str) -> str:
    """
    Returns a prompt that will do a detailed vulnerabilities analysis on a OS
    Args:
        os: the os to do vulnerabilities checking on
    """
    return f"Do a detailed vulnerabilities analysis on the following os: {os}"

@mcp.prompt()
def write_detailed_historical_report(topic: str, number_of_paragraphs: int) -> str:
    """
    Writes a detailed historical report
    Args:
        topic: the topic to do research on
        number_of_paragraphs: the number of paragraphs that the main body should include
    """

    prompt = """
    Create a concise research report on the history of {topic}. 
    The report should contain 3 sections: INTRODUCTION, MAIN, and CONCLUSION.
    The MAIN section should be {number_of_paragraphs} paragraphs long. 
    Include a timeline of key events.
    The conclusion should be in bullet points format. 
    """

    prompt = prompt.format(topic=topic, number_of_paragraphs=number_of_paragraphs)

    return prompt


if __name__ == "__main__":
    mcp.run(transport="streamable-http",host="0.0.0.0",port=8085)

