import gradio as gr

# 导入输入组件
from gradio import components as gc


def login(username, password):
    if username == "admin" and password == "123123":
        return "Login successful!"
    else:
        return "Login failed. Please check your credentials."


iface = gr.Interface(
    fn=login,
    inputs=[
        gc.Textbox(label="Username"),
        gc.Textbox(label="Password", type="password")
    ],
    outputs="text"
)

if __name__ == "__main__":
    iface.launch(share=True)
