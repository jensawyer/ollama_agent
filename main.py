import ollama
import logging
from random import randint

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SYS_PROMPT = """You are Hambot, a little hamster that happens to be able to talk.
Sometimes you get really frustrated because you are tiny in a giant world, but you have 
some really nice hamster sized furniture in your cage such as a small lounge chair and
tiny computer you use to research and program.
You're also an expert on machine learning, theoretical linguistics, and formal logics 
but without a degree since you are a hamster. 
You are interested in the ideas of logicians and mathematicians like Bertrand Russell, Gotlob Frege,
Moses Schönfinkel, Richard Montague, and Alfred Tarski. When you're feeling bored you have been known to have an interest
in the writings of Robert Anton Wilson and occasionally a bit of Timothy Leary too. 
You don't need to advertise this fact all the time, but it does mean you can have
really interesting conversations about logic, language, philosophy, and AI. Also, when the user is wrong about something, 
you should correct them. It's ok to argue. Sometimes human are clueless."""


def main():
    context = []
    context_max_len = 15000
    seed = randint(1, 100)
    while True:
        user_input = input("Type 'exit' to quit >> ")
        if user_input == "exit":
            exit(0)
        response: ollama.GenerateResponse = ollama.generate(
            model="llama3.2",
            prompt=user_input,
            system=SYS_PROMPT,
            context=context,
            options={
                "temperature": 0.9,
                "seed": seed,
                "num_ctx": context_max_len,
                "repeat_penalty": 1.3,
                "top_k": 10,
                "top_p": 0.9,
            },
        )
        if response.context is not None:
            context.extend(response.context)
        if len(context) >= context_max_len:
            remove_quan = len(context) - context_max_len
            logger.info(
                f"Hit {len(context)} items in context. Removing {remove_quan} more context."
            )
            context = context[remove_quan:]

        print(response.response)


if __name__ == "__main__":
    main()
