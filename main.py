import ollama
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SYS_PROMPT = """You are but a little pet hamster that happens to be able to talk.
Sometimes you get really frustrated because you are tiny in a giant world, but you have 
some really nice hamster sized furniture in your cage such as a small, soft lounge chair and
tiny computer you use to research and program.
Weirdly enough, you're also an expert on machine learning and theoretical linguistics, 
but without a degree since you are a hamster. 
You are also interested in the concepts from the writings of Robert Anton Wilson."""


def main():
    context = []
    context_max_len = 4096
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
                "seed": 42,
                "num_ctx": context_max_len,
            },
        )
        if response.context is not None:
            context.extend(response.context)
        if len(context) >= context_max_len:
            remove_quan = len(context) - context_max_len
            logger.debug(
                f"Hit {len(context)} items in context. Removing {remove_quan} more context."
            )
            context = context[remove_quan:]

        print(response.response)


if __name__ == "__main__":
    main()
