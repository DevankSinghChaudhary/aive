def extract_page_data(page):
    data = {
        "title": page.title,
        "summary": page.summary.strip(),
        "sections": []
    }

    for section in page.sections[:10]:
        text = section.text.strip()

        if len(text) > 50:
            data["sections"].append({
                "title": section.title,
                "text": section.text[:500]
            })

    return data