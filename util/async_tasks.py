import asyncio


def split(collection, length):
    return [collection[i:i+length] for i in range(0, len(collection), length)]


async def run_by_chunks(func, sequence, chunk_length, *args, **params):
    if not len(sequence):
        return []

    chunks = split(sequence, chunk_length)
    tasks = [func(chunk, *args, **params) for chunk in chunks]
    results = await asyncio.gather(*tasks)

    return results
