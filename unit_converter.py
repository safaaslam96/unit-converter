import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔁", layout="centered")

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

# Toggle with icon
col1, col2 = st.columns([0.1, 1])
with col1:
    st.markdown(
        "<span style='color:#0d3b66; font-weight:700; font-size:22px;'></span>", 
        unsafe_allow_html=True
    )
with col2:
    dark_mode = st.checkbox(
        label="Dark Mode",
        value=st.session_state.dark_mode,
        key="dark_mode_toggle",
        help="Toggle dark/light mode"
    )

st.session_state.dark_mode = dark_mode

# Theme settings
dark_mode_colors = {
    "bg": "linear-gradient(180deg, #0d3b66 0%, #5fa8d3 100%)",
    "text": "#ffffff",
    "button_bg": "#ffffff",
    "button_text": "#0d3b66",
    "shadow": "rgba(13, 59, 102, 0.4)",
    "result": "#e0f7fa",
    "input_bg": "rgba(255, 255, 255, 0.9)"
}

light_mode_colors = {
    "bg": "linear-gradient(180deg, #87ceeb 0%, #b0e0e6 100%)",
    "text": "#0d3b66",
    "button_bg": "#ffffff",
    "button_text": "#0d3b66",
    "shadow": "rgba(13, 59, 102, 0.2)",
    "result": "#2563eb",
    "input_bg": "white"
}

theme = dark_mode_colors if dark_mode else light_mode_colors

# CSS Styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background: {theme['bg']};
        color: {theme['text']};
        font-family: 'Segoe UI', sans-serif;
        padding: 2rem;
    }}
    .stNumberInput input,
    div[role="combobox"] > div > div > input {{
        background-color: {theme['input_bg']} !important;
        color: {theme['button_text']} !important;
        padding: 0.6rem 1rem;
        border-radius: 12px;
        font-size: 17px;
        font-weight: 600;
        border: 1.8px solid transparent;
        box-shadow: 0 4px 8px {theme['shadow']};
    }}
    .stNumberInput input:focus,
    div[role="combobox"] > div > div > input:focus {{
        border-color: {theme['button_text']} !important;
        box-shadow: 0 0 10px {theme['button_text']};
    }}
    div[role="listbox"] {{
        font-size: 16px;
        border-radius: 10px;
        box-shadow: 0 6px 15px {theme['shadow']};
    }}
    button[kind="primary"] {{
        background-color: {theme['button_bg']} !important;
        color: {theme['button_text']} !important;
        padding: 14px 36px;
        border-radius: 35px;
        font-size: 18px;
        font-weight: 700;
        box-shadow: 0 6px 15px {theme['shadow']};
        transition: all 0.3s ease;
        margin-top: 20px;
    }}
    button[kind="primary"]:hover {{
        transform: scale(1.08);
        box-shadow: 0 10px 25px {theme['shadow']};
    }}
    .result-box {{
        margin-top: 30px;
        font-size: 26px;
        font-weight: 700;
        color: {theme['result']};
        text-shadow: 0 0 8px {theme['result']};
        animation: slideFade 1s ease forwards;
        opacity: 0;
    }}
    @keyframes slideFade {{
        0% {{ transform: translateY(20px); opacity: 0; }}
        100% {{ transform: translateY(0); opacity: 1; }}
    }}
    h1 {{
        color: {theme['text']};
        font-weight: 900;
        margin-bottom: 1rem;
    }}
    label[for="dark_mode_toggle"] {{
        font-size: 14px;
        font-weight: 600;
    }}
    /* Make checkbox tick black */
    input[type="checkbox"] {{
        accent-color: black !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1>🔁 Unit Converter</h1>", unsafe_allow_html=True)

unit_keys = ["", "meter", "kilometer", "gram", "kilogram"]

def selectbox_with_placeholder(label, key):
    return st.selectbox(
        label,
        unit_keys,
        index=0,
        format_func=lambda x: "Select unit" if x == "" else x.capitalize(),
        key=key
    )

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
    }
    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        return value * conversions[key]
    else:
        return "Conversion not supported"

value = st.number_input("Enter the value:", min_value=1.0, step=1.0, key="value_input")
unit_from = selectbox_with_placeholder("Convert from:", key="unit_from")
unit_to = selectbox_with_placeholder("Convert to:", key="unit_to")

with st.form(key="convert_form"):
    submit = st.form_submit_button(label="Convert", disabled=(unit_from == "" or unit_to == ""))
    if submit:
        result = convert_units(value, unit_from, unit_to)
        st.markdown(f'<div class="result-box">Converted value: {result}</div>', unsafe_allow_html=True)
