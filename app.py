import os
import shutil
import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("Hello, World!")
    text_in=gr.Textbox(label="Text")
    text_out=gr.Textbox(label="Text")
    run_button=gr.Button("Run")
    def run_button_clicked(text_in):
        return text_in *2
    run_button.click(run_button_clicked,inputs=text_in,outputs=text_out)

demo.launch(share=True)