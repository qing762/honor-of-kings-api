import sys
import aiohttp
import subprocess
import json
import asyncio
import re
import os


if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    print("No file provided as command-line argument.")
    sys.exit(1)


async def lintCheck():
    print("Checking format and style...")
    try:
        subprocess.run(
            [
                "flake8",
                ".",
                "--count",
                "--select=E9,F63,F7,F82",
                "--show-source",
                "--statistics",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Linting failed! {str(e)}")
        sys.exit(1)
    try:
        subprocess.run(
            [
                "flake8",
                ".",
                "--count",
                "--max-complexity=30",
                "--max-line-length=300",
                "--statistics",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Linting failed! {str(e)}")
        sys.exit(1)
    print("Linting passed!\n\n")


async def validateLinks():
    print("Validating links...")
    file = sys.argv[1]

    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)

    data_str = json.dumps(data)

    url_pattern = re.compile(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    )
    urls = re.findall(url_pattern, data_str)

    all_links_valid = True
    invalidURL = []

    async with aiohttp.ClientSession() as session:
        for url in urls:
            try:
                response = await session.get(
                    url,
                    headers={
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
                    },
                    timeout=aiohttp.ClientTimeout(total=5),
                )
                if response.status == 200:
                    print("0")
                else:
                    print(f"Link is invalid: {url}")
                    allLinksValid = False
                    invalidURL.append(url)
            except (aiohttp.ClientError, asyncio.TimeoutError):
                continue

    if allLinksValid:
        print("All links are valid!\n\n")
    else:
        print(f"Invalid links found:\n{invalidURL}\n\n")
        sys.exit(1)

if __name__ == "__main__":
    try:
        asyncio.run(lintCheck())
        asyncio.run(validateLinks())
        print("All check passed!")
    except KeyboardInterrupt:
        print("Process stopping due to keyboard interrupt")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
