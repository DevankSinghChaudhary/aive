import wikipediaapi


wiki = wikipediaapi.Wikipedia(
    user_agent = 'AI-Video_editor (devanksinghchaudhary@gmail.com)',
    language="en"
)

def search_page(query):
    results = wiki.search(query, limit=5)

    if not results.pages:
        return None

    best_title = list(results.pages.keys())[0]

    page = wiki.page(best_title)

    return page if page.exists() else None