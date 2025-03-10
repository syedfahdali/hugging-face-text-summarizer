from transformers import pipeline
import gradio as gr

# Load the summarization pipeline
model = pipeline("summarization")

# Define the prediction function
def predict(prompt):
    summary = model(prompt)[0]["summary_text"]  # Corrected key access
    return summary

# Create the Gradio interface using Blocks
with gr.Blocks() as demo:
    gr.Markdown("## Text Summarization")
    textbox = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
    output = gr.Textbox(label="Summary")
    submit_btn = gr.Button("Summarize")
    submit_btn.click(fn=predict, inputs=textbox, outputs=output)

# Launch the Gradio app
demo.launch()