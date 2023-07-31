import json
import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/msmarco-distilbert-base-tas-b"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def closest_attr(source, attr_list):
    api_result = \
        query(
                {
                    "inputs": {
                        "source_sentence": source,
                        "sentences": attr_list
                    }
                }
            )
    print(api_result)
    max_index = api_result.index(max(api_result))
    return max_index, attr_list[max_index]
