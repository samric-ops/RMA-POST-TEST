import streamlit as st

# --- APP CONFIG ---
st.set_page_config(page_title="Rapid Mathematics Assessment", page_icon="🧮")

# --- CUSTOM CSS FOR FORMATTING ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stRadio > div {
        background-color: white;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ddd;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# --- TITLE & INSTRUCTIONS ---
st.title("🧮 Rapid Mathematics Assessment (Grades 7-10)")
st.info("""
**Time Limit:** 90 Minutes  
**Instructions:** Answer all items. For explanations, you may use English, Filipino, or Taglish.
""")

# --- FORMULAS SIDEBAR ---
with st.sidebar:
    st.header("📐 Helpful Formulas")
    st.latex(r"P = a + b + c")
    st.latex(r"A = \frac{1}{2} \times b \times h")
    st.latex(r"C = 2\pi r")
    st.latex(r"A = \pi r^2")
    st.latex(r"V = (Base Area) \times h")

# --- ASSESSMENT TABS (To break down 47 questions) ---
tabs = st.tabs(["Number Expressions", "Powers & Data", "Probability & Coordinates", "Algebra & Geometry"])

# --- TAB 1: NUMBER EXPRESSIONS (1-5) ---
with tabs[0]:
    st.header("Section 1: Number Expressions")
    st.write("**Box 1:**")
    st.code("2 x 2 - 3 x 1\n3 x 3 - 4 x 2\n4 x 4 - 5 x 3\n5 x 5 - 6 x 4")

    q1 = st.text_area("1. Verify the expression 4 x 4 - 5 x 3 equals 1. Show your computation:", key="q1")
    q2 = st.text_input("2. What is the next number expression after 5 x 5 - 6 x 4?", key="q2")
    q3 = st.radio("3. Which algebraic expression represents Box 1?", 
                  ["Select...", "a. (n)(n) - (n+3)(n+1)", "b. (n)(n) - [(n+1)(n-1)]", "c. (n-1)(n-1) - n(n-2)", "d. n^2 - 3n(1)", "e. n^2 - n - 1"], key="q3")
    q4 = st.text_area("4. Explain why you chose the expression in item 3:", key="q4")
    q5 = st.text_input("5. What does 'n' represent in your chosen expression?", key="q5")

# --- TAB 2: POWERS & DATA (6-16) ---
with tabs[1]:
    st.header("Section 2: Powers and Rational Numbers")
    st.write("**Table 1:** 2^2=4, 2^3=8, 2^4=16, 2^5=32")
    q6 = st.text_area("6. Show that 1024 is a power of 2:", key="q6")
    q7 = st.text_input("7. Write the exponential form of 1024:", key="q7")
    q8 = st.text_area("8. Find a power of 2 that is a multiple of 16 and is between 50 and 200:", key="q8")
    
    st.divider()
    q9 = st.radio("9. Is there a number between 0.998 and 0.999?", ["Select...", "Yes", "No"], key="q9")
    q9_ex = st.text_input("If Yes, give an example. If No, explain why:", key="q9_ex")
    q10 = st.text_area("10. Show how to subtract 0.998 from 0.999:", key="q10")
    q11 = st.text_area("11. Is there a fraction between 3/4 and 1? Give example/explain:", key="q11")

    st.header("Section 3: Data Interpretation")
    st.write("[Placeholder for Figure 1: Absences vs Grades Scatter Plot]")
    # st.image("figure1.png") # Uncomment this when you have the image file
    q12 = st.number_input("12. How many students had a grade below 84?", step=1, key="q12")
    q13 = st.text_area("13. Explain your answer to item 12 based on the graph:", key="q13")
    q14 = st.radio("14. Correct interpretation of Figure 1:", 
                   ["Select...", "a. Absences up, Grade up", "b. Absences down, Grade up", "c. Absences up, Grade down", "d. Absences down, Grade down"], key="q14")

    st.write("[Placeholder for Figure 2: Monthly Income Bar Chart]")
    q15 = st.text_area("15. Which purok shows more diversity/variability? Justify:", key="q15")
    q16 = st.text_area("16. Should both puroks get the same financial aid? Explain using the graph:", key="q16")

# --- TAB 3: PROBABILITY & COORDINATES (17-28) ---
with tabs[2]:
    st.header("Section 4: Probability and Tables")
    st.write("**Table 2: Music & Sports Participation**")
    st.table({
        "Activity": ["Music", "No Music", "Total"],
        "Sports": [18, 42, 60],
        "No Sports": [31, 19, 50],
        "Total": [49, 61, 110]
    })
    q17 = st.number_input("17. How many students participated in Music?", step=1, key="q17")
    q18 = st.number_input("18. How many did not participate in any activity?", step=1, key="q18")
    q19 = st.text_input("19. Probability of selecting a student in BOTH music and sports:", key="q19")
    q20 = st.text_input("20. Write a question answerable by Table 2:", key="q20")

    st.header("Section 5: Coordinates and Geometry")
    st.write("[Placeholder for Figure 3: Number Line]")
    q21 = st.radio("21. Position of point F:", ["Select...", "-500", "-400", "-300", "-200", "50"], key="q21")
    q22 = st.text_input("22. Position of point G:", key="q22")
    
    st.write("[Placeholder for Figure 4: Cartesian Plane]")
    q23 = st.text_input("23. Coordinates of Point C:", key="q23")
    q24 = st.multiselect("24. Select two points on the line through B and C:", ["(1,-1)", "(1,-2)", "(2,3)", "(3,2)", "(4,7)", "(5,6)"], key="q24")
    q25 = st.radio("25. Which expression represents points on line AB?", ["Select...", "a. (x, -2x)", "b. (x, -2x+1)", "c. (x, -x)", "d. (x, -x+1)", "e. (x, -x+2)"], key="q25")
    q26 = st.text_area("26. Area of Triangle ABC (Show solution):", key="q26")
    q27 = st.radio("27. Which is shorter: House to School or House to Barangay Hall?", ["Select...", "School", "Barangay Hall"], key="q27")
    q28 = st.text_area("28. Explain how you determined the shorter walk:", key="q28")

# --- TAB 4: ALGEBRA & GEOMETRY (29-47) ---
with tabs[3]:
    st.header("Section 6: Algebraic Reasoning")
    q29 = st.multiselect("29. Select all possible values for 2r-1 (r is integer):", ["-5", "-27", "-82", "99", "46", "122"], key="q29")
    q30 = st.multiselect("30. Expressions for cost of apples (3 for Php100):", ["a. 100/3", "b. 3n/100", "c. 100n", "d. 100n/3", "e. 3:100 = n:cost"], key="q30")
    
    st.write("**Box 2: 17 + a = b + 3**")
    q31 = st.text_input("31. Two possible values for a and b:", key="q31")
    q32 = st.radio("32. Always true for Box 2?", ["Select...", "a. a > b", "b. a + b = 20", "c. b - a = 14", "d. Any value"], key="q32")
    q33 = st.radio("33. Reason to transform 5y-8 = 14-3y to 5y+3y-8 = 14?", ["Select...", "Subtract 3y", "Subtract 8", "Add 3y", "Divide by 8"], key="q33")

    st.header("Section 7: Equations and Graphs")
    st.write("**Figure 5: C = 250n + 200**")
    q34 = st.number_input("34. Rental cost for 5 days?", key="q34")
    q35 = st.radio("35. What does 250 represent?", ["Select...", "Daily cost", "Number of days", "Fixed cost", "Total cost for 1 day"], key="q35")
    q36 = st.text_input("36. What does 200 represent?", key="q36")
    q37 = st.radio("37. Which aspect of the graph is 200?", ["Select...", "x-intercept", "y-intercept", "slope", "minimum point"], key="q37")

    st.header("Section 8: Triangles and Circles")
    st.write("[Placeholder for Figure 6: Triangle PQR]")
    q38 = st.multiselect("38. Possible values for q and r if p=30 (Select 2):", ["a. q=10, r=140", "b. q=10, r=130", "c. q=110, r=30", "d. q=100, r=80", "e. q=100, r=50"], key="q38")
    q39 = st.multiselect("39. True about p and q if r=60 and exterior angle is 130:", ["a. p+q=130", "b. many values", "c. p=70, q=50", "d. p=50, q=70", "e. r+p=130"], key="q39")
    q40 = st.multiselect("40. Triangle properties that help (Select all):", ["a. Equilateral=60", "b. Isosceles angles", "c. Linear pair", "d. Exterior angle sum of remote", "e. Six exterior angles", "f. Exterior sum 360"], key="q40")

    st.divider()
    st.write("[Placeholder for Figure 7: Dog House]")
    q41 = st.radio("41. Lengths of other two sides (ratio 3:3:2, short side=1m):", ["Select...", "a. 1.5m each", "b. 2m and 3m", "c. 3m each", "d. 4m and 6m"], key="q41")
    q42 = st.text_area("42. Are sides proportional to toy storage? Explain:", key="q42")
    q43 = st.radio("43. Toy storage base=25cm, other two sides?", ["Select...", "a. 37.5cm each", "b. 50cm and 75cm", "c. 75cm each", "d. 100cm and 150cm"], key="q43")

    st.divider()
    st.write("[Placeholder for Figure 8 & 9: Circular Pool]")
    q44 = st.text_area("44. Area of sidewalk (diameter=10m, width=1m, pi=3.14):", key="q44")
    q45 = st.radio("45. Volume of water (depth 1.5m and 0.6m):", ["Select...", "a. 10pi(2.1)", "b. 25pi(2.1)", "c. 10pi(2.1)^2", "d. 25pi(2.1)^2", "e. 100pi(2.1)^2"], key="q45")

    st.divider()
    st.write("[Placeholder for Figure 10: Rolling Gear]")
    q46 = st.text_area("46. Distance for 5 rolls (diameter=60cm):", key="q46")
    q47 = st.text_input("47. Degrees rotated after 5 rolls:", key="q47")

# --- SUBMISSION ---
st.divider()
if st.button("Submit Assessment"):
    st.success("Your responses have been recorded!")
    st.balloons()
    st.write("### Summary of Responses:")
    st.write(st.session_state.answers)
