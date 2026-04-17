from data import ask, json_making
from research import get_data
from providers import llm, llm_prompt, scene_llm, scene_prompt, creative_scene_prompt, creative_llm


def main():
    
    user_input = ask()
    print("Started Processing")
    
    query = user_input["idea"]
    duration = user_input["duration of video (seconds)"]
    
    first_input = get_data(query)
    prompt = llm_prompt(first_input)
    script = llm(prompt)
    print(script)
    max_scenes = duration // 5

    s_prompt = scene_prompt(script, duration, max_scenes)
    scene_json = scene_llm(s_prompt)
    print(scene_json)
    
    creative_prompt = creative_scene_prompt(scene_json)
    scene = creative_llm(creative_prompt)
    scene_json = json_making(scene)
    print(scene_json)


if __name__ == "__main__":
    main()