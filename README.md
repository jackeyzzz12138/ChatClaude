# ChatClaude
> [!IMPORTANT]
> The software is still in beta, maybe some updates later.  
> you need to key in your own endpoint and api-key.

## background
Because some third-party transporters use the old api format, not support new Claude api like `v1/message`. To use old post method like
```bash
# example
https:/xxx.xxx/v1/completions
Authorization: Bearer sk-...
{
    "model": "claude-3-opus-20240229",
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": "Hello, world"}
    ]
}
```
No products compatible with this method were found for use ~~Maybe~~.

## usage
```bash
pip install -r requirements.txt
python app.py
```

## TODO
- [ ] streaming output.
- [ ] save history.
- [ ] support vercel and huggingface space.

