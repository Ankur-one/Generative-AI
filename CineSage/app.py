import streamlit as st

from core import extract_information


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="CineSage AI",
    page_icon="🎬",
    layout="wide",
)


# ============================================================
# Header
# ============================================================

st.title("🎬 CineSage AI")

st.subheader(
    "Information Extraction & Summarization"
)

st.write(
    "Enter a paragraph and CineSage will extract all "
    "important information available in the text."
)

st.divider()


# ============================================================
# Input
# ============================================================

st.subheader("📝 Enter Paragraph")

paragraph = st.text_area(
    "Movie / Content Paragraph",
    placeholder=(
        "Example:\n\n"
        "Interstellar is a science fiction film directed by "
        "Christopher Nolan. Released in 2014, the film stars "
        "Matthew McConaughey, Anne Hathaway, Jessica Chastain "
        "and Michael Caine..."
    ),
    height=300,
    label_visibility="collapsed",
)


# ============================================================
# Analyze Button
# ============================================================

if st.button(
    "🔍 Extract Information",
    type="primary",
    use_container_width=True,
):

    if not paragraph.strip():

        st.warning(
            "Please enter a paragraph before analyzing."
        )

    else:

        with st.spinner(
            "CineSage is extracting information..."
        ):

            try:

                result = extract_information(
                    paragraph
                )

                st.success(
                    "Information extracted successfully!"
                )

                st.divider()

                # ============================================
                # Result
                # ============================================

                st.subheader("🎯 Extracted Information")

                st.markdown(result)

            except Exception as e:

                st.error(
                    f"An error occurred: {str(e)}"
                )


# ============================================================
# Footer
# ============================================================

st.divider()

st.caption(
    "CineSage AI • Information Extraction & Summarization "
    "• TinyLlama + LangChain"
)