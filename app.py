import streamlit as st
from transformers import pipeline
import textwrap

# ---------- Page Config ----------
st.set_page_config(
    page_title="BART Text Summarizer",
    page_icon="📝",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.big-title {
    font-size: 40px;
    font-weight: 800;
    margin-bottom: 0px;
}
.sub-title {
    font-size: 16px;
    color: #9aa0a6;
    margin-top: 0px;
}
.card {
    padding: 18px;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(255,255,255,0.03);
}
.small-tag {
    display: inline-block;
    padding: 6px 10px;
    border-radius: 999px;
    font-size: 12px;
    border: 1px solid rgba(255,255,255,0.15);
    margin-right: 6px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Load Model (Cached) ----------
@st.cache_resource
def load_summarizer(model_name: str):
    return pipeline("summarization", model=model_name)

# ---------- Sidebar ----------
st.sidebar.title("⚙️ Settings")

model_name = st.sidebar.selectbox(
    "Choose Model",
    [
        "facebook/bart-large-cnn",
        "sshleifer/distilbart-cnn-12-6"
    ],
    index=0
)

max_len = st.sidebar.slider("Max summary length", 30, 200, 80)
min_len = st.sidebar.slider("Min summary length", 10, 120, 30)
do_sample = st.sidebar.checkbox("Creative summary (do_sample)", value=False)

st.sidebar.markdown("---")
st.sidebar.write("✅ Tip: If your laptop is slow, choose **DistilBART** (faster).")

summarizer = load_summarizer(model_name)

# ---------- Session State for History ----------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------- Header ----------
st.markdown('<div class="big-title">📝 BART Text Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Without Fine-Tuning • Hugging Face Transformers • Streamlit</div>', unsafe_allow_html=True)

st.markdown(
    "<span class='small-tag'>⚡ Fast</span>"
    "<span class='small-tag'>🤖 Pretrained</span>"
    "<span class='small-tag'>📌 Summarization</span>",
    unsafe_allow_html=True
)

st.write("")

# ---------- Layout ----------
col1, col2 = st.columns([1.1, 0.9], gap="large")

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📥 Input Text")

    sample_text = """Artificial intelligence is changing the world very fast. 
It is used in healthcare, education, finance, and many other industries.
AI helps companies automate tasks, improve productivity, and make better decisions."""

    text = st.text_area("Paste or type your text here:", value=sample_text, height=260)

    word_count = len(text.split())
    char_count = len(text)

    c1, c2, c3 = st.columns(3)
    c1.metric("Words", word_count)
    c2.metric("Characters", char_count)
    c3.metric("Model", "BART" if "bart" in model_name else "Other")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📤 Summary Output")

    summarize_btn = st.button("✨ Summarize", use_container_width=True)

    if summarize_btn:
        if text.strip() == "":
            st.warning("Please enter some text first!")
        else:
            with st.spinner("Generating summary..."):
                # Safety: max_length should be greater than min_length
                if max_len <= min_len:
                    st.error("Max length must be greater than Min length.")
                else:
                    result = summarizer(
                        text,
                        max_length=max_len,
                        min_length=min_len,
                        do_sample=do_sample
                    )

                    summary_text = result[0]["summary_text"].strip()

                    st.success(summary_text)

                    # Save history
                    st.session_state.history.insert(0, {
                        "input": text,
                        "summary": summary_text,
                        "model": model_name
                    })

                    st.download_button(
                        "⬇️ Download Summary (.txt)",
                        data=summary_text,
                        file_name="summary.txt",
                        mime="text/plain",
                        use_container_width=True
                    )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- History Section ----------
st.write("")
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🕒 History (Last Summaries)")

if len(st.session_state.history) == 0:
    st.info("No summaries yet. Click **Summarize** to generate one.")
else:
    for i, item in enumerate(st.session_state.history[:5], start=1):
        with st.expander(f"Summary #{i} • Model: {item['model']}"):
            st.write("✅ **Summary:**")
            st.write(item["summary"])
            st.write("---")
            st.write("📌 **Input (first 300 chars):**")
            st.code(textwrap.shorten(item["input"], width=300, placeholder="..."))

clear_btn = st.button("🗑️ Clear History")
if clear_btn:
    st.session_state.history = []
    st.success("History cleared ✅")

st.markdown("</div>", unsafe_allow_html=True)

st.caption("Made with ❤️ using Hugging Face + Streamlit")
