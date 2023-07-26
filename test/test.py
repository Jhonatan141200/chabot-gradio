# --------------Base-------------------

import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    
if __name__ == "__main__":
    demo.launch()   
    
# --------------Block Structure-------------------

import gradio as gr

def greet(name):
    return "Hello " + name + "!"

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")
   
demo.launch()

# -------------------  Gradio with custom CSS and JavaScript --------------------------
import gradio as gr

blocks = gr.Blocks()

with blocks as demo:
    subject = gr.Textbox(placeholder="subject")
    verb = gr.Radio(["ate", "loved", "hated"])
    object = gr.Textbox(placeholder="object")

    with gr.Row():
        btn = gr.Button("Create sentence.")
        reverse_btn = gr.Button("Reverse sentence.")
        foo_bar_btn = gr.Button("Append foo")
        reverse_then_to_the_server_btn = gr.Button(
            "Reverse sentence and send to server."
        )

    def sentence_maker(w1, w2, w3):
        return f"{w1} {w2} {w3}"

    output1 = gr.Textbox(label="output 1")
    output2 = gr.Textbox(label="verb")
    output3 = gr.Textbox(label="verb reversed")
    output4 = gr.Textbox(label="front end process and then send to backend")

    btn.click(sentence_maker, [subject, verb, object], output1)
    reverse_btn.click(
        None, [subject, verb, object], output2, _js="(s, v, o) => o + ' ' + v + ' ' + s"
    )
    verb.change(lambda x: x, verb, output3, _js="(x) => [...x].reverse().join('')")
    foo_bar_btn.click(None, [], subject, _js="(x) => x + ' foo'")

    reverse_then_to_the_server_btn.click(
        sentence_maker,
        [subject, verb, object],
        output4,
        _js="(s, v, o) => [s, v, o].map(x => [...x].reverse().join(''))",
    )

demo.launch()

# ---------------------- Blocks ---------------------

import gradio as gr 
from transformers import pipeline

sentiment_classifier = pipeline("text-classification", return_all_scores=True)

def classifier(text):
    pred = sentiment_classifier(text)
    return {p["label"]: p["score"] for p in pred[0]}

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Input Text")
            with gr.Row():
                classify = gr.Button("Classify Sentiment")
        with gr.Column():
            label = gr.Label(label="Predicted Sentiment")

    classify.click(classifier, input_text, label)
demo.launch()