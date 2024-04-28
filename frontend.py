import gradio as gr
from main import get_response

demo = gr.Interface(
    fn = get_response,
    inputs=gr.components.Textbox(label='Input'),
    outputs=gr.components.Textbox(label='Output'),
    title = "Code Review Assistant"
)

if __name__ == "__main__":
    demo.launch()