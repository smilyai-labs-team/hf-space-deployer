# HF Space Deployer

Source repository for the Hugging Face Space `hugging-science/test-gradio-agent-demo`.

Every push to `main` automatically deploys the Gradio app to Hugging Face through GitHub Actions.

## One required secret

In this GitHub repository, create an Actions secret named `HF_TOKEN`.

Use a fine-grained Hugging Face token that has the minimum permissions needed to create/write Spaces in the `hugging-science` organization. Do not commit the token to this repository.

## Deployment flow

```text
ChatGPT / GitHub edit
        ↓
GitHub main branch
        ↓
GitHub Actions
        ↓
hugging-science/test-gradio-agent-demo
```
