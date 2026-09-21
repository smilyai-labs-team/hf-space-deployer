import gradio as gr


def echo(message: str) -> str:
    """Echo a message back with a tiny demo prefix."""
    return f"🧪 Hugging Science demo says: {message}"


def add_numbers(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


with gr.Blocks(title="Hugging Science — Gradio Test") as demo:
    gr.Markdown(
        """
# 🧪 Hugging Science — Gradio Test

Tiny Gradio demo deployed automatically from GitHub.

It also exposes the named Gradio API functions as MCP tools when MCP mode is supported by the installed Gradio version.
"""
    )

    with gr.Tab("Echo"):
        message = gr.Textbox(label="Message", placeholder="Type something...")
        echo_output = gr.Textbox(label="Output")
        gr.Button("Echo 🚀").click(
            echo,
            inputs=message,
            outputs=echo_output,
            api_name="echo",
        )

    with gr.Tab("Calculator"):
        with gr.Row():
            a = gr.Number(label="A", value=2)
            b = gr.Number(label="B", value=3)
        sum_output = gr.Number(label="A + B")
        gr.Button("Add").click(
            add_numbers,
            inputs=[a, b],
            outputs=sum_output,
            api_name="add_numbers",
        )


if __name__ == "__main__":
    demo.launch(mcp_server=True)
