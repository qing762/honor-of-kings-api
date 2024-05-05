import os
import aiofiles
import aiohttp
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

async def upload():
    url = os.environ.get("apiUploadURL", None)
    password = os.environ.get("apiUploadPASS", None)

    async with aiofiles.open("wangzhe.json", "rb") as f:
        fileContent = await f.read()

    data = aiohttp.FormData()
    data.add_field(
        "file", fileContent, filename="wangzhe.json", content_type="application/json"
    )
    data.add_field("password", str(password))

    async with aiohttp.ClientSession() as session:
        logging.info("Starting upload...")
        async with session.post(str(url), data=data) as resp:
            logging.info(f"Response status: {resp.status}")
            response_text = await resp.text()
            logging.info(f"Response text: {response_text}")
            return


if __name__ == "__main__":
    asyncio.run(upload())