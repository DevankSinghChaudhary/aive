def ask():
    while True:
        idea = input("Enter Idea: ").strip()
        if idea:
            break
        print("Cannot be Empty!")

    while True:
        duration = int(input("Enter Max Duration of Video (s): "))
        if duration:
            break
        print("Cannot be Empty!")

    return {
        "idea":idea,
        "duration of video (seconds)":duration
        }


def json_making(scene):
    start = scene.find("{")
    end = scene.rfind("}")
    return scene[start:end+1]