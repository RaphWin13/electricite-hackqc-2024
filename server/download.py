import json
from pathlib import Path
import requests

with open("./download_urls.json", "r") as file:
  sources = json.load(file)

download_directory = Path("./infra/data/download")
if not download_directory.exists():
  download_directory.mkdir(parents=True)

for source in sources:
  print("---------------------------------------")
  print("Fetching from source...")
  print(f"License information available at {source['license_info_url']}")

  for data_url in source["data_urls"]:
    print(f"Fetching file from {data_url['url']} ...")
    
    try:
      response = requests.get(data_url["url"])

      file_extension = data_url["url"].split(".")[-1].split("?")[0]
      file_path = download_directory.joinpath(data_url["name"] + file_extension)

      with open(file_path, mode="wb") as file:
        file.write(response.content)
    except Exception as e:
      print(f"File at {data_url['url']} could not be downloaded: {e}")
