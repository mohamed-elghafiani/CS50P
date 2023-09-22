import Levenshtein


FILENAME = "conversations.txt"

def read_conversations(filename):
    # return conversations as a list [(prompt, response), (prompt, response), (), ...]
    conversations = []
    with open(filename) as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            prompt = lines[i]
            response = lines[i + 1]
            conversations.append((prompt, response))
        
    return conversations


def get_response(user_prompt, conversations):
    # conversations ==> [(prompt, response), (prompt, response), ...]
    scores = []
    # scores ==> [[response, distance], [response, distance], [response, distance], ...]
    for (prompt, response) in conversations:
        # compare prompt to user_prompt
        distance = Levenshtein.distance(user_prompt, prompt)
        scores.append([response, distance])

    best_response = min(scores, key=lambda score: score[1])[0]

    # A more concise way of extracting the best reponse
    # best_response = min(conversations, key=lambda x: Levenshtein.distance(x[0], user_prompt)) 

    return best_response



while True:
    user_prompt = input("You: ")
    if user_prompt == "exit":
        break

    conversations = read_conversations(FILENAME)
    response = get_response(user_prompt, conversations)

    print("Bot: ", response)