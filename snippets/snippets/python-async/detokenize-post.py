import cohere
import asyncio

co = cohere.AsyncClient("<<apiKey>>")


async def main():
    response = await co.detokenize(
        tokens=[8466, 5169, 2594, 8, 2792, 43], model="command"  # optional
    )
    print(response)

asyncio.run(main())