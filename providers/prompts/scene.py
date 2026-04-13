def scene_prompt(script, duration, max_scene):
    if not script:
        raise ValueError("No script for scene building")

    prompt = f"""
Convert this script into a modern short-form explainer video structure.

Your job is to:
1. Ensure factual accuracy
2. Improve flow between scenes
3. Keep it natural and realistic

OUTPUT:
Return ONLY valid JSON:
{{
  "scenes": [
    {{
      "text": ["line1", "line2"],
      "visual_keywords": [],
      "highlight_words": []
    }}
  ]
}}

RULES:
- Max scenes: {max_scene}
- Total duration: {duration} seconds

TEXT:
- 1-2 lines per scene
- Each line: 5-12 words
- Each line must express ONLY ONE idea
- Prefer short, simple sentences
- Split complex or dense information into multiple lines
- Avoid combining multiple facts in one sentence
- Use natural, spoken tone (not academic or dramatic)

FLOW:
- Scenes must connect smoothly
- Use simple transitions when needed (Then, Soon after, Minutes later)
- Maintain narrative continuity from start to end

STRUCTURE:
- One key moment per scene
- Keep chronological order
- Cover full story clearly

ENDING:
- Final scene must feel complete and conclusive
- Summarize impact, outcome, or meaning

VISUALS:
- 2-4 simple, searchable keywords per scene

HIGHLIGHTS:
- 1-2 important words per scene (dates, names, key terms)

DO NOT:
- Add fake precision (exact times, numbers unless certain)
- Add cinematic directions
- Change structure

DO NOT INCLUDE:
- Camera directions
- Sound effects
- Long or complex sentences
- Dates or time in every line, use consitent words like (days later, some time later, etc)

SCRIPT:
{script}
"""
    return prompt