def creative_scene_prompt(scene_json):
    if not scene_json:
        raise ValueError("Nothing from scenes!!")
    prompt = f"""
You are adding a creative editing layer to video scenes.

Your goal:
Decide HOW each scene should be visually presented.

INPUT:
- Scene JSON

OUTPUT:
- Same JSON + add "style" field

{{
  "scenes": [
    {{
      "scene_id":,
      "text": ["line1", "line2"],
      "visual_keywords": ["keyword1", "keyword2"],
      "highlight_words": ["word1"],
      "style": {{
        "scene_type": ["map_focus", "archival", "timeline", "stat", "portrait", "abstract"],
        "motion": ["zoom", "pan", "parallax", "static", "slow_drift"],
        "transition": ["cut", "fade", "swipe"],
        "overlay": ["title", "subtitle", "none", "data_card"],
        "emphasis": ["highlight", "underline", "glow", "none"]
      }}
    }}
  ]
}}

RETURN WITH ACTUAL VALUES INSIDE NOT JUST THIS STRUCTURE

STYLE RULES:

SCENE TYPE:
- map_focus → for places, geography, locations
- archival → for historical events, war, past footage
- stat → for numbers, deaths, economy, data
- portrait → for people or leaders
- timeline → for sequence of events
- abstract → for concepts or explanations

MOTION:
- map_focus → smooth_zoom_in or pan
- archival → slow_drift
- stat → subtle_zoom
- portrait → slow_zoom
- timeline → horizontal_pan
- abstract → parallax

OVERLAY:
- map → title label (place name)
- stat → data_card
- others → subtitle or none

EMPHASIS:
- highlight key words if important

IMPORTANT:
- Keep it minimal and clean
- Do not overuse effects
- Match visuals with meaning

Return only JSON.

INPUT SCENES:

{scene_json}
"""
    
    return prompt