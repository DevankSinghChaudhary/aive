from .extractor import extract_page_data
from .wiki_client import search_page


def get_data(query):
    page = search_page(query)

    if not page:
        return {"error":"nothing for search"}
    
    return extract_page_data(page)

