import streamlit as st
from PIL import Image
import os

# --- APP CONFIG ---
st.set_page_config(page_title="Rapid Mathematics Assessment", page_icon="📝", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    &lt;style&gt;
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 5px 5px 0px 0px;
        gap: 1px;
    }
    .stTabs [aria-selected="true"] { background-color: #e0e2e6; font-weight: bold; }
    .stMultiSelect [data-baseweb="select"] { margin-bottom: 15px; }
    .figure-container {
        border: 2px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        background-color: #f9f9f9;
        text-align: center;
    }
    .figure-caption {
        font-weight: bold;
        margin-top: 10px;
        color: #666;
    }
    &lt;/style&gt;
    """, unsafe_allow_html=True)

# --- RESET SESSION STATE FOR ITEM 3 ---
if 'q3' in st.session_state:
    del st.session_state['q3']

# --- FUNCTION TO DISPLAY FIGURES ---
def display_figure(figure_num, description, image_path=None):
    """Display figure with optional image"""
    st.markdown(f"**{description}**")
    
    if image_path and os.path.exists(image_path):
        # Display actual image
        image = Image.open(image_path)
        st.image(image, caption=f"Figure {figure_num}", use_container_width=True)
    else:
        # Display placeholder with instructions
        st.warning(f"⚠️ **Figure {figure_num}** would be displayed here.")
        st.info(f"📌 **Instructions:** To display Figure {figure_num}, save the image as 'figure_{figure_num}.png' in the same folder as this app.")
        
        # Optional: Show file uploader for users to upload images
        uploaded_file = st.file_uploader(f"Upload Figure {figure_num}", type=['png', 'jpg', 'jpeg'], key=f"upload_{figure_num}")
        if uploaded_file:
            st.image(uploaded_file, caption=f"Figure {figure_num} - {description}", use_container_width=True)

# --- SESSION STATE ---
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# --- HEADER ---
st.title("Rapid Mathematics Assessment (Grades 7 - 10)")
st.write("---")

# Assessment Instructions from PDF
st.markdown("""
## Assessment Instructions:

Your score on this test will help your teacher determine your readiness to learn the mathematics required at your grade level. You have **ninety (90) minutes** to complete this test.

Only the Questionnaire and Answer Sheet provided to you should be on your desk. Write all your solutions and answers, including any scratch work, directly on the Answer Sheet.

Before answering each question, double-check that the question numbers on your Answer Sheet match those on the Questionnaire to avoid misplaced answers. Please review your answers carefully before submitting your paper.

**i. For multiple-choice questions:**
Some multiple-choice questions may require selecting more than one answer. In such cases, write the letters of all your chosen options.

**ii. For short-answer questions:**
Provide clear and complete answers in the designated space provided on the Answer Sheet. Show all necessary calculations or explanations. You may write your explanations in English, Filipino, or Taglish.
""")

# --- SIDEBAR FORMULAS from PDF ---
with st.sidebar:
    st.header("📐 Formulas")
    st.markdown("""
    **Perimeter of a triangle:**  
    $P = a + b + c$
    
    **Area of a triangle:**  
    $A = \\frac{1}{2} \\times \\text{base} \\times \\text{height}$
    
    **Circumference of a circle:**  
    $C = 2\\pi r$
    
    **Area of a circle:**  
    $A = \\pi r^2$
    
    **Volume of a cylinder:**  
    $V = (\\text{area of the base}) \\times \\text{height}$
    """)
    
    st.divider()
    st.header("📁 Figure Files")
    st.markdown("""
    To display all figures, save these files in the app folder:
    - `figure_1.png` - Absences vs Academic Grade
    - `figure_2.png` - Monthly Family Income
    - `figure_3.png` - Number Line
    - `figure_4.png` - Cartesian Grid
    - `figure_5.png` - Tricycle Rental Cost
    - `figure_6.png` - Triangle PQR
    - `figure_7.png` - Dog House and Toy Storage
    - `figure_8.png` - Circular Pool (top view)
    - `figure_9.png` - Pool Depth (auxiliary view)
    - `figure_10.png` - Rolling Wheel
    """)

# --- MAIN TABS ---
tabs = st.tabs(["Items 1-11", "Items 12-22", "Items 23-33", "Items 34-47"])

# --- TAB 1: Number Expressions & Powers (Items 1-11) ---
with tabs[0]:
    st.subheader("Number Expressions")
    st.info("**Box 1:**")
    st.latex(r"2 \times 2 - 3 \times 1")
    st.latex(r"3 \times 3 - 4 \times 2")
    st.latex(r"4 \times 4 - 5 \times 3")
    st.latex(r"5 \times 5 - 6 \times 4")
    
    st.markdown("1. Your classmate said that each of the four expressions in Box 1 is equivalent to 1. Verify what your classmate said by showing your computation for the number expression $4 \\times 4 - 5 \\times 3$.")
    st.text_area("Your computation for Item 1:", key="q1")
    
    st.markdown("2. What must be the next number expression to $5 \\times 5 - 6 \\times 4$ in Box 1?")
    st.text_input("Answer for Item 2:", key="q2")
    
    st.markdown("3. Which of the following algebraic expressions represents the set of number expressions in Box 1? **(Select all that apply)**")
    
    st.multiselect("Select your answer(s):", [
        "a. (n)(n) - (n + 3)(n + 1)",
        "b. (n)(n) - [(n + 1)(n - 1)]", 
        "c. (n - 1)(n - 1) - n(n - 2)",
        "d. n² - 3n(1)",
        "e. n² - n - 1"
    ], key="q3")
    
    st.markdown("4. Explain or show why you think you have chosen the correct algebraic expressions for the set of number expressions in Box 1.")
    st.text_area("Explanation for Item 4:", key="q4")
    
    st.markdown("5. What does $n$ represent in your chosen expression in item 3?")
    st.text_input("Answer for Item 5:", key="q5")
    
    st.divider()
    st.subheader("Powers and Rational Numbers")
    
    # SIMPLE AND CLEAN TABLE 1 - Using Unicode superscript for professional look
    st.write("**Table 1**")
    
    st.markdown("""
| Exponential Form | Expanded Form | Power of 2 |
|---|---|---|
| 2² | 2 × 2 | 4 |
| 2³ | 2 × 2 × 2 | 8 |
| 2⁴ | 2 × 2 × 2 × 2 | 16 |
| 2⁵ | 2 × 2 × 2 × 2 × 2 | 32 |
    """)
    
    st.markdown("6. Show that 1024 is a power of 2. [Refer to Table 1]")
    st.text_area("Show solution for Item 6:", key="q6")
    
    st.markdown("7. Write the exponential form of 1024.")
    st.text_input("Answer for Item 7:", key="q7")
    
    st.markdown("8. Find a number that is a power of 2 that meets **BOTH** of these conditions:")
    st.markdown("* The number is a multiple of 16.  \n* The number is also more than 50 but less than 200.")
    st.text_input("Answer for Item 8:", key="q8")
    
    st.markdown("9. Is there a number between 0.998 and 0.999? If YES, give one example. If NO, explain why you think so.")
