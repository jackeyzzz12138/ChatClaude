
'''
待添加功能：
- streaming，打字机特效。
- 保存聊天记录。
'''

import gradio as gr
from Claude_completions import Claude_completions
# 声明全局变量
global prompt_f, model_f, api_f, endpoint_f
prompt_f = model_f = api_f = endpoint_f = None

with gr.Blocks() as demo:

    gr.Markdown(
        '''
        # Claude Api Chatbot   
        This is a beta version, maybe some mistakes. Welcome to feedback.
        '''
    )

    chatbot = gr.Chatbot()

    msg = gr.Textbox(label="Enter your prompt.")

    with gr.Row():
        model = gr.Dropdown(label="Model", choices=["claude-3-haiku-20240307", "claude-3-sonnet-20240229", "claude-3-opus-20240229"])
        api = gr.Textbox(label="API Key", type="password")
        endpoint = gr.Textbox(label="EndPoint", placeholder="https://xxxx.xx/v1/completions")
    
    btn = gr.Button("submit")

    def combine(prompt, model, api, endpoint):
        global prompt_f, model_f, api_f, endpoint_f  # 使用 global 关键字，以便更新全局变量
        prompt_f, model_f, api_f, endpoint_f = prompt, model, api, endpoint
    
    btn.click(combine, inputs = [msg, model, api, endpoint])
    

    clear = gr.ClearButton([msg, chatbot])
    
    def respond(message, chat_history):
        global prompt_f, model_f, api_f, endpoint_f
        bot_message = Claude_completions(endpoint_f, api_f, model_f, prompt_f)
        chat_history.append((message, bot_message))
        return "", chat_history
    
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

    gr.Markdown(
        '''
        ## usage
        - Fulfill all blocks.
        - Click submit.
        - Focus on the prompt block, and key the enter.
        '''
    )
if __name__ == "__main__":
    demo.launch()