import streamlit as st

st.title("AI Resume Analyzer")

st.write("Paste your resume below and get instant feedback.")

resume = st.text_area("Your Resume")

# Expanded skill list (more realistic)
skills = [
    "python", "java", "c++", "sql", "machine learning",
    "data analysis", "deep learning", "git", "flask", "streamlit",
    "tensorflow", "pandas", "numpy", "html", "css"
]

if st.button("Analyze Resume"):

    found_skills = []

    # Skill detection
    for skill in skills:
        if skill.lower() in resume.lower():
            found_skills.append(skill)

    st.subheader("Detected Skills")

    if found_skills:
        st.write(", ".join(found_skills))
    else:
        st.write("No technical skills detected.")

    # Score system
    score = len(found_skills)

    st.subheader("Resume Score")
    st.write(f"{score} / {len(skills)}")

    # Feedback system
    st.subheader("Feedback")

    if score < 3:
        st.write("⚠️ Your resume is weak. Add more technical skills and projects.")
    elif score < 6:
        st.write("⚡ Good start, but you should add more advanced skills.")
    else:
        st.write("✅ Strong resume! You have solid technical coverage.")

    # Extra improvement tips
    st.subheader("Suggestions")
    st.write("- Add real projects with GitHub links")
    st.write("- Include internships or practical experience")
    st.write("- Highlight AI/ML or backend work if possible")