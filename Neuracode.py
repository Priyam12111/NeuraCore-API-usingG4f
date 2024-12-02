from g4f.client import Client


def sendMsg(msg):
    try:
        client = Client()
        response = client.chat.completions.create(
            # model="gpt-3.5-turbo",
            # model="gpt-4",
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": msg}],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    print(sendMsg("""How much water should I give to tulsi daily? (No Chinese)"""))
