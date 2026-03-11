from ddgs import DDGS

def search_web(query):
    """
    Searches the web using DuckDuckGo and returns a summary of the first result.
    """
    try:
        results = DDGS().text(query, max_results=1)
        if results:
            first_result = results[0]
            return f"{first_result['title']}: {first_result['body']}"
        else:
            return None
    except Exception as e:
        return f"Error al conectar con la red: {e}"

if __name__ == "__main__":
    # Test
    print(search_web("Quien gano el mundial 2022?"))
