import time

def format_results(results, max_results=3):
    """Formats search results into a readable string for Ollama"""
    start_time = time.time()
    formatted_docs = ""

    for i, result in enumerate(results):
        if i >= max_results:
            break

        # Format title, URL, and content for readability
        title = result.get("title", "No Title")
        url = result.get("url", "#")  # If URL is missing, use '#'
        content = result.get("content", "No Content Available")

        # Clean formatting to avoid special characters interfering with LLM output
        formatted_docs += f"**Title:** {title}\n **URL:** {url}\n **Content:** {content[:500]}...\n\n"

    end_time = time.time()
    print("Time taken to format results:", end_time - start_time)
    
    return formatted_docs if formatted_docs else "No relevant documents found."
