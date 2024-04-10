import requests

def Claude_completions(endpoint, api, model, content):
    endPoint = endpoint

    headers = {'Authorization': f'Bearer {api}'}

    payload = \
    {
        "model": f"{model}",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": f"{content}"} 
        ]
    }

    r = requests.post(endPoint, headers=headers, json=payload)
    r = r.json()

    content_list = r['content']

    for context in content_list:
        if 'text' in context:
            return context['text']
        
    return "Something went wrong..."




