""" import streamlit as st
import requests
import os

MODEL_ENDPOINTS = {
    "FAB-GPT-Pro": "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/fab-gpt-pro/execute",
    "FAB-Codex": "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/fab-codex/execute",
    "FAB-Azure": "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/fab-azure/execute",
    "FAB-GoogleAI": "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/fab-googleai/execute"
}

FAB_HEADERS = {
    'content-type': 'application/json',
    'x-user-id': 'tejasvi-poc',
    'x-authentication': 'api-key D8762AA1BA98FB28EEE6EA45:2a33da34fa1e9a863aed86153e77a2a7'
}

LANGUAGES = [
    "Python", "JavaScript", "ESQL", "SAP ABAB", "Salesforce Apex",
    "Java", "C#", "Go", "Ruby", "TypeScript"
]

LANGUAGE_MAP = {
    "Python": "python",
    "JavaScript": "javascript",
    "ESQL": "text",
    "SAP ABAB": "text",
    "Salesforce Apex": "text",
    "Java": "java",
    "C#": "csharp",
    "Go": "go",
    "Ruby": "ruby",
    "TypeScript": "typescript"
}

MODELS = [
    "FAB-GPT-Pro",
    "FAB-Codex",
    "FAB-Azure",
    "FAB-GoogleAI"
]

st.set_page_config(page_title="FAB Code Assistant", layout="wide")
st.title("FAB Code Generation & Optimization Assistant")

st.sidebar.header("Settings")
model_choice = st.sidebar.radio("Choose AI Model:", MODELS)
language_choice = st.sidebar.selectbox("Select Programming Language:", LANGUAGES)
syntax_lang = LANGUAGE_MAP[language_choice]
FAB_API_ENDPOINT = MODEL_ENDPOINTS[model_choice]

st.subheader("Code Generation via Prompt")
user_prompt = st.text_area("Enter your prompt:", height=150)

if st.button("Generate Code"):
    if user_prompt:
        full_prompt = f"Write {language_choice} code for the following task:\n\n{user_prompt}"
        with st.spinner("Generating code from FAB Agent..."):
            try:
                response = requests.post(
                    FAB_API_ENDPOINT,
                    headers=FAB_HEADERS,
                    json={"input": {"query": full_prompt}}
                )
                response.raise_for_status()
                code_output = response.json().get("output", "No code returned.")
                st.code(code_output, language=syntax_lang)

                st.download_button(
                    label="Download Generated Code",
                    data=code_output,
                    file_name=f"generated_code.{syntax_lang}.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt to generate code.")

st.subheader("Optimize Uploaded Code")
uploaded_file = st.file_uploader("Upload code file to optimize", type=["py", "js", "txt", "java", "cs"])
file_content = uploaded_file.read().decode("utf-8") if uploaded_file else ""

if st.button("Optimize Code") and uploaded_file:
    optimize_prompt = (
        f"Optimize this {language_choice} code for the fastest possible execution while maintaining identical output. "
        f"Focus on performance improvements, algorithmic optimizations, and language-specific best practices. "
        f"Respond only with code; do not explain your work.\n\n{file_content}"
    )

    with st.spinner("Optimizing code via FAB Agent..."):
        try:
            response = requests.post(
                FAB_API_ENDPOINT,
                headers=FAB_HEADERS,
                json={"input": {"query": optimize_prompt}}
            )
            response.raise_for_status()
            optimized_code = response.json().get("output", "No optimized code returned.")
            st.code(optimized_code, language=syntax_lang)

            st.download_button(
                label="Download Optimized Code",
                data=optimized_code,
                file_name=f"optimized_code.{syntax_lang}.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"Error: {e}")

st.subheader("Code Conversion")
conversion_target = st.selectbox("Convert code to: (Target Language)", LANGUAGES)
conversion_syntax = LANGUAGE_MAP[conversion_target]

if uploaded_file:
    if st.button("Convert Code"):
        conversion_prompt = (
            f"Convert the following {language_choice} code into {conversion_target}. "
            f"Only respond with equivalent, runnable code. Do not explain your work.\n\n{file_content}"
        )

        with st.spinner("Converting code via FAB Agent..."):
            try:
                response = requests.post(
                    FAB_API_ENDPOINT,
                    headers=FAB_HEADERS,
                    json={"input": {"query": conversion_prompt}}
                )
                response.raise_for_status()
                converted_code = response.json().get("output", "No converted code returned.")
                st.code(converted_code, language=conversion_syntax)

                st.download_button(
                    label="Download Converted Code",
                    data=converted_code,
                    file_name=f"converted_code.{conversion_syntax}.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.warning("Please upload a code file to convert.")


###
import streamlit as st
import requests
import os

FAB_API_ENDPOINT = "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/test-01/execute"
FAB_HEADERS = {
    'content-type': 'application/json',
    'x-user-id': 'tejasvi-poc',
    'x-authentication': 'api-key D8762AA1BA98FB28EEE6EA45:2a33da34fa1e9a863aed86153e77a2a7'
}

LANGUAGES = [
    "Python", "JavaScript", "ESQL", "SAP ABAB", "Salesforce Apex",
    "Java", "C#", "Go", "Ruby", "TypeScript"
]

MODELS = [
    "FAB-GPT-Pro",
    "FAB-Codex",
    "FAB-Azure",
    "FAB-GoogleAI"
]

st.set_page_config(page_title="FAB Code Assistant", layout="wide")
st.title("FAB Code Generation & Optimization Assistant")

st.sidebar.header("Settings")
model_choice = st.sidebar.radio("Choose AI Model:", MODELS)
language_choice = st.sidebar.selectbox("Select Programming Language:", LANGUAGES)

st.subheader("Code Generation via Prompt")
user_prompt = st.text_area("Enter your prompt:", height=150)

if st.button("Generate Code"):
    if user_prompt:
        with st.spinner("Generating code from FAB Agent..."):
            try:
                response = requests.post(
                    FAB_API_ENDPOINT,
                    headers=FAB_HEADERS,
                    json={"input": {"query": user_prompt}}
                )
                response.raise_for_status()
                code_output = response.json().get("output", "No code returned.")
                st.code(code_output, language=language_choice.lower())

                st.download_button(
                    label="Download Generated Code",
                    data=code_output,
                    file_name=f"generated_code.{language_choice.lower()}",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt to generate code.")

st.subheader("Optimize Uploaded Code")
uploaded_file = st.file_uploader("Upload code file to optimize", type=["py", "js", "txt", "java", "cs"])

if st.button("Optimize Code") and uploaded_file:
    code_to_optimize = uploaded_file.read().decode("utf-8")
    optimize_prompt = (
        f"Optimize this {language_choice} code for the fastest possible execution while maintaining identical output. "
        f"Focus on performance improvements, algorithmic optimizations, and language-specific best practices. "
        f"Respond only with code; do not explain your work.\n\n{code_to_optimize}"
    )

    with st.spinner("Optimizing code via FAB Agent..."):
        try:
            response = requests.post(
                FAB_API_ENDPOINT,
                headers=FAB_HEADERS,
                json={"input": {"query": optimize_prompt}}
            )
            response.raise_for_status()
            optimized_code = response.json().get("output", "No optimized code returned.")
            st.code(optimized_code, language=language_choice.lower())

            st.download_button(
                label="Download Optimized Code",
                data=optimized_code,
                file_name=f"optimized_code.{language_choice.lower()}",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"Error: {e}")

st.subheader("Code Conversion")
conversion_target = st.selectbox("Convert code to: (Target Language)", LANGUAGES)

if st.button("Convert Code") and uploaded_file:
    original_code = uploaded_file.read().decode("utf-8")
    conversion_prompt = (
        f"Convert the following {language_choice} code into {conversion_target}. "
        f"Only respond with equivalent, runnable code. Do not explain your work.\n\n{original_code}"
    )

    with st.spinner("Converting code via FAB Agent..."):
        try:
            response = requests.post(
                FAB_API_ENDPOINT,
                headers=FAB_HEADERS,
                json={"input": {"query": conversion_prompt}}
            )
            response.raise_for_status()
            converted_code = response.json().get("output", "No converted code returned.")
            st.code(converted_code, language=conversion_target.lower())

            st.download_button(
                label="Download Converted Code",
                data=converted_code,
                file_name=f"converted_code.{conversion_target.lower()}",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"Error: {e}")

elif uploaded_file is None and st.button("Convert Code"):
    st.warning("Please upload a code file to convert.")

user_prompt = st.text_area("Enter your prompt:", height=150)

if st.button("Generate Code"):
    if user_prompt:
        with st.spinner("Contacting FAB Agent..."):
            code_output = generate_code(model_choice, language_choice, user_prompt)
            st.code(code_output, language=language_choice.lower())

            # Optional: Add download button to save generated code
            st.download_button(
                label="Download Code",
                data=code_output,
                file_name=f"generated_code.{language_choice.lower()}",
                mime="text/plain"
            )
    else:
        st.warning("Please enter a prompt.") """

import streamlit as st
import requests
import os

MODEL_ENDPOINTS = {
    "FAB-GPT-Pro": "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/fab-gpt-pro/execute",
    "FAB-Codex": "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/fab-codex/execute",
    "FAB-Azure": "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/fab-azure/execute",
    "FAB-GoogleAI": "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/fab-googleai/execute"
}

FAB_HEADERS = {
    'content-type': 'application/json',
    'x-user-id': 'tejasvi-poc',
    'x-authentication': 'api-key D8762AA1BA98FB28EEE6EA45:2a33da34fa1e9a863aed86153e77a2a7'
}

LANGUAGES = [
    "Python", "JavaScript", "ESQL", "SAP ABAB", "Salesforce Apex",
    "Java", "C#", "Go", "Ruby", "TypeScript"
]

LANGUAGE_MAP = {
    "Python": "python",
    "JavaScript": "javascript",
    "ESQL": "text",
    "SAP ABAB": "text",
    "Salesforce Apex": "text",
    "Java": "java",
    "C#": "csharp",
    "Go": "go",
    "Ruby": "ruby",
    "TypeScript": "typescript"
}

MODELS = [
    "FAB-GPT-Pro",
    "FAB-Codex",
    "FAB-Azure",
    "FAB-GoogleAI"
]

st.set_page_config(page_title="FAB Code Assistant", layout="wide")
st.title("FAB Code Generation & Optimization Assistant")

st.sidebar.header("Settings")
model_choice = st.sidebar.radio("Choose AI Model:", MODELS)
language_choice = st.sidebar.selectbox("Select Programming Language:", LANGUAGES)
syntax_lang = LANGUAGE_MAP[language_choice]
FAB_API_ENDPOINT = MODEL_ENDPOINTS[model_choice]

def unescape_code(text):
    try:
        return text.encode('utf-8').decode('unicode_escape')
    except Exception:
        return text  # fallback if decoding fails

st.subheader("Code Generation via Prompt")
user_prompt = st.text_area("Enter your prompt:", height=150)

if st.button("Generate Code"):
    if user_prompt:
        full_prompt = f"Write {language_choice} code for the following task:\n\n{user_prompt}"
        with st.spinner("Generating code from FAB Agent..."):
            try:
                response = requests.post(
                    FAB_API_ENDPOINT,
                    headers=FAB_HEADERS,
                    json={"input": {"query": full_prompt}}
                )
                response.raise_for_status()
                code_output = response.json().get("output", "No code returned.")
                code_output = unescape_code(code_output)
                st.text_area("Generated Code", code_output, height=300)

                st.download_button(
                    label="Download Generated Code",
                    data=code_output,
                    file_name=f"generated_code.{syntax_lang}.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt to generate code.")

st.subheader("Optimize Uploaded Code")
uploaded_file = st.file_uploader("Upload code file to optimize", type=["py", "js", "txt", "java", "cs"])
file_content = uploaded_file.read().decode("utf-8") if uploaded_file else ""

if st.button("Optimize Code") and uploaded_file:
    optimize_prompt = (
        f"Optimize this {language_choice} code for the fastest possible execution while maintaining identical output. "
        f"Focus on performance improvements, algorithmic optimizations, and language-specific best practices. "
        f"Respond only with code; do not explain your work.\n\n{file_content}"
    )

    with st.spinner("Optimizing code via FAB Agent..."):
        try:
            response = requests.post(
                FAB_API_ENDPOINT,
                headers=FAB_HEADERS,
                json={"input": {"query": optimize_prompt}}
            )
            response.raise_for_status()
            optimized_code = response.json().get("output", "No optimized code returned.")
            optimized_code = unescape_code(optimized_code)
            st.text_area("Optimized Code", optimized_code, height=300)

            st.download_button(
                label="Download Optimized Code",
                data=optimized_code,
                file_name=f"optimized_code.{syntax_lang}.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"Error: {e}")

st.subheader("Code Conversion")
conversion_target = st.selectbox("Convert code to: (Target Language)", LANGUAGES)
conversion_syntax = LANGUAGE_MAP[conversion_target]

if uploaded_file:
    if st.button("Convert Code"):
        conversion_prompt = (
            f"Convert the following {language_choice} code into {conversion_target}. "
            f"Only respond with equivalent, runnable code. Do not explain your work.\n\n{file_content}"
        )

        with st.spinner("Converting code via FAB Agent..."):
            try:
                response = requests.post(
                    FAB_API_ENDPOINT,
                    headers=FAB_HEADERS,
                    json={"input": {"query": conversion_prompt}}
                )
                response.raise_for_status()
                converted_code = response.json().get("output", "No converted code returned.")
                converted_code = unescape_code(converted_code)
                st.text_area("Converted Code", converted_code, height=300)

                st.download_button(
                    label="Download Converted Code",
                    data=converted_code,
                    file_name=f"converted_code.{conversion_syntax}.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.warning("Please upload a code file to convert.")
