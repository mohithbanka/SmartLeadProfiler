import streamlit as st
from main import run_lead_profiler

st.set_page_config(
    page_title="Lead Profiler",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("🧠 Lead Profiler")
st.write("Enter a company domain to get website info, emails, and lead score.")

domain = st.text_input("Company Domain (e.g., openai.com)", "")

if st.button("Run Profile"):
    if domain.strip() == "":
        st.error("Please enter a valid domain.")
    else:
        with st.spinner("Fetching and analyzing..."):
            profile = run_lead_profiler(domain.strip())
            if 'error' in profile:
                st.error(f"Error fetching website: {profile['error']}")
            else:
                st.subheader("Profile Summary")
                st.write(f"**Domain:** {profile.get('domain', 'N/A')}")
                st.write(f"**Website Title:** {profile.get('title', 'N/A')}")
                st.write(f"**Email Found:** {profile.get('email', 'N/A')}")
                st.write(f"**Lead Score:** {profile.get('score', 0)}")

                # Optional: Show raw JSON
                with st.expander("Show Full Profile Data"):
                    st.json(profile)

# Footer
st.markdown(
    """
    <style>
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div style='text-align: center; margin-top: 3rem; color: gray; font-size: 0.8rem;'>
        Made by Mohith
    </div>
    """,
    unsafe_allow_html=True,
)
