import streamlit as st

# --- APP CONFIG ---
st.set_page_config(page_title="Rapid Mathematics Assessment", page_icon="📝", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
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
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# --- HEADER ---
st.title("Rapid Mathematics Assessment (Grades 7 - 10)")
st.write("---")
st.markdown("""
**Assessment Instructions:** Your score on this test will help your teacher determine your readiness to learn the mathematics required at your grade level. You have **ninety (90) minutes** to complete this test.  
* **Multiple-choice:** Select the letter(s) of all correct options. For questions requiring multiple correct answers, you may select more than two choices.  
* **Short-answer:** Show necessary calculations or explanations (English, Filipino, or Taglish).
""")

# --- SIDEBAR FORMULAS ---
with st.sidebar:
    st.header("📐 Formulas")
    st.latex(r"P = a + b + c")
    st.latex(r"A = \frac{1}{2} \times base \times height")
    st.latex(r"C = 2\pi r")
    st.latex(r"A = \pi r^2")
    st.latex(r"V = (\text{area of the base}) \times height")

# --- MAIN TABS ---
tabs = st.tabs(["Items 1-11", "Items 12-22", "Items 23-33", "Items 34-47"])

# --- TAB 1: Number Expressions & Powers ---
with tabs[0]:
    st.subheader("Number Expressions")
    st.info("**Box 1:**")
    st.latex(r"2 \times 2 - 3 \times 1")
    st.latex(r"3 \times 3 - 4 \times 2")
    st.latex(r"4 \times 4 - 5 \times 3")
    st.latex(r"5 \times 5 - 6 \times 4")
    
    st.markdown("1. Your classmate said that each of the four expressions in Box 1 is equivalent to 1. Verify what your classmate said by showing your computation for the number expression $4 \times 4 - 5 \times 3$.")
    st.text_area("Your computation for Item 1:", key="q1")
    
    st.markdown("2. What must be the next number expression to $5 \times 5 - 6 \times 4$ in Box 1?")
    st.text_input("Answer for Item 2:", key="q2")
    
    st.markdown("3. Which of the following algebraic expressions represents the set of number expressions in Box 1? **(Select all that apply)**")
    st.multiselect("Options for Item 3:", [
        "a. $(n)(n) - (n + 3)(n + 1)$",
        "b. $(n)(n) - [(n + 1)(n - 1)]$",
        "c. $(n - 1)(n - 1) - n(n - 2)$",
        "d. $n^2 - 3n(1)$",
        "e. $n^2 - n - 1$"
    ], key="q3")
    
    st.markdown("4. Explain or show why you think you have chosen the correct algebraic expressions for the set of number expressions in Box 1.")
    st.text_area("Explanation for Item 4:", key="q4")
    
    st.markdown("5. What does $n$ represent in your chosen expression in item 3?")
    st.text_input("Answer for Item 5:", key="q5")
    
    st.divider()
    st.subheader("Powers and Rational Numbers")
    st.write("**Table 1: Powers of 2**")
    st.latex(r"2^2 = 4, \quad 2^3 = 8, \quad 2^4 = 16, \quad 2^5 = 32")
    
    st.markdown("6. Show that 1024 is a power of 2. [Refer to Table 1]")
    st.text_area("Show solution for Item 6:", key="q6")
    
    st.markdown("7. Write the exponential form of 1024.")
    st.text_input("Answer for Item 7:", key="q7")
    
    st.markdown("8. Find a number that is a power of 2 that meets **BOTH** of these conditions:")
    st.markdown("* The number is a multiple of 16.  \n* The number is also more than 50 but less than 200.")
    st.text_input("Answer for Item 8:", key="q8")
    
    st.markdown("9. Is there a number between 0.998 and 0.999? If YES, give one example. If NO, explain why you think so.")
    st.text_area("Answer/Explanation for Item 9:", key="q9")
    
    st.markdown("10. Show how you will subtract 0.998 from 0.999.")
    st.text_area("Solution for Item 10:", key="q10")
    
    st.markdown("11. Is there a fraction that is greater than $\\frac{3}{4}$ but less than 1? If YES, give one example. If NO, explain why you think so.")
    st.text_area("Answer/Explanation for Item 11:", key="q11")

# --- TAB 2: Data & Coordinates ---
with tabs[1]:
    st.subheader("Data Interpretation")
    st.write("**Figure 1: Relationship Between Absences and Academic Grade**")
    # Placeholder for image
    st.warning("⚠️ Figure 1 would be displayed here")
    
    st.markdown("12. How many students had an overall academic grade below 84? [Refer to Figure 1]")
    st.number_input("Count for Item 12:", step=1, key="q12")
    
    st.markdown("13. Explain why you think your answer in item 12 is correct based on the information shown in the graph in Figure 1.")
    st.text_area("Explanation for Item 13:", key="q13")
    
    st.markdown("14. Which of the following can be a correct interpretation of the data presented in the graph in Figure 1? **(Select all that apply)**")
    st.multiselect("Options for Item 14:", [
        "a. As the number of absences increases, the overall academic grade also increases.",
        "b. As the number of absences decreases, the overall academic grade increases.",
        "c. As the number of absences increases, the overall academic grade decreases.",
        "d. As the number of absences decreases, the overall academic grade also decreases."
    ], key="q14")
    
    st.divider()
    st.write("**Figure 2: Monthly Family Income in Purok 1 and Purok 2**")
    st.warning("⚠️ Figure 2 would be displayed here")
    
    st.markdown("15. Based on the graph in Figure 2, which of the two puroks shows more diversity in monthly family income? Explain or justify your answer.")
    st.text_area("Answer for Item 15:", key="q15")
    
    st.markdown("16. The average monthly income of the families in Purok 1 and Purok 2 are equal. Should both purok be given the same amount of financial aid? What information in the graph in Figure 2 did you base your decision on?")
    st.text_area("Answer for Item 16:", key="q16")
    
    st.divider()
    st.subheader("Probability and Tables")
    st.write("**Table 2: Music and Sports Activities Participation**")
    st.table({
        "": ["Participated in music", "Did not participate in music", "Total"],
        "Participated in sports": [18, 42, 60],
        "Did not participate in sports": [31, 19, 50],
        "Total": [49, 61, 110]
    })
    
    st.markdown("17. How many students participated in the music activity?")
    st.number_input("Count for Item 17:", step=1, key="q17")
    
    st.markdown("18. How many students did not participate in any of the two activities?")
    st.number_input("Count for Item 18:", step=1, key="q18")
    
    st.markdown("19. What is the probability of selecting a student who participated in both music and sports activities?")
    st.text_input("Answer for Item 19 (as fraction or decimal):", key="q19")
    
    st.markdown("20. Write a question that can be answered using the information in Table 2.")
    st.text_input("Question for Item 20:", key="q20")
    
    st.divider()
    st.subheader("Coordinates")
    st.write("**Figure 3: Number Line**")
    st.warning("⚠️ Figure 3 would be displayed here")
    
    st.markdown("21. What is the position of point F in Figure 3? **(Select all that apply)**")
    st.multiselect("Options for Item 21:", ["a. -500", "b. -400", "c. -300", "d. -200", "e. 50"], key="q21")
    
    st.markdown("22. What is the position of point G in Figure 3?")
    st.text_input("Answer for Item 22:", key="q22")

# --- TAB 3: Cartesian Plane & Algebra ---
with tabs[2]:
    st.subheader("Cartesian Plane")
    st.write("**Figure 4: Cartesian Grid**")
    st.warning("⚠️ Figure 4 would be displayed here")
    
    st.markdown("23. What are the coordinates of Point C in Figure 4?")
    st.text_input("Coordinates (x, y) for Item 23:", key="q23")
    
    st.markdown("24. A line is drawn passing through points B and C in Figure 4. Select two ordered pairs that represent the coordinates of points that are also in this line. **(Select exactly two)**")
    st.multiselect("Select points for Item 24:", ["(1, -1)", "(1, -2)", "(2, 3)", "(3, 2)", "(4, 7)", "(5, 6)"], key="q24", max_selections=2)
    
    st.markdown("25. Draw a line through points A and B in Figure 4. Which of the following ordered pairs represent all the points that are on this line? **(Select all that apply)**")
    st.multiselect("Options for Item 25:", [
        "a. $(x, -2x)$",
        "b. $(x, -2x + 1)$",
        "c. $(x, -x)$",
        "d. $(x, -x + 1)$",
        "e. $(x, -x + 2)$"
    ], key="q25")
    
    st.markdown("26. In Figure 4, connecting the points A, B and C will form a triangle, called triangle ABC. What is the area of triangle ABC? Show your method for getting the area.")
    st.text_area("Solution for Item 26:", key="q26")
    
    st.markdown("27. A point represents position. Suppose in Figure 4, point A represents the position of your house, point B represents the position of your school and point C represents the position of the barangay hall. There is a straight road that you can take to the school and the barangay hall from your house. Which is the shorter walk from your house, going to the school or to the barangay hall?")
    st.text_input("Answer for Item 27:", key="q27")
    
    st.markdown("28. Show or explain how you determined your answer in item 27.")
    st.text_area("Explanation for Item 28:", key="q28")
    
    st.divider()
    st.subheader("Algebraic Reasoning")
    st.markdown("29. If $r$ is an integer, select all possible values that can be represented by $2r - 1$. **(Select all that apply)**")
    st.multiselect("Values for Item 29:", ["-5", "-27", "-82", "99", "46", "122"], key="q29")
    
    st.markdown("30. At a fruit stand, apples are priced at 3 for Php100. Which of the following expressions can be used to find the amount to be paid (cost) for any number ($n$) of apples? **(Select all that apply)**")
    st.multiselect("Options for Item 30:", [
        "a. $cost = 100/3$",
        "b. $cost = 3n/100$",
        "c. $cost = 100n$",
        "d. $cost = 100n/3$",
        "e. $3 : 100 = n : cost$"
    ], key="q30")
    
    st.write("**Box 2:** $17 + a = b + 3$")
    st.markdown("31. Write two possible values for $a$ and $b$ that will make the equation in Box 2 true.")
    st.text_input("Values for Item 31:", key="q31")
    
    st.markdown("32. Which statement is always true about $a$ and $b$? [Refer to Box 2] **(Select all that apply)**")
    st.multiselect("Options for Item 32:", [
        "a. $a$ is greater than $b$.",
        "b. The sum of $a$ and $b$, $(a+b)$ is 20.",
        "c. The difference between $b$ and $a$, $(b-a)$ is 14.",
        "d. $a$ and $b$ can take any value."
    ], key="q32")
    
    st.markdown("33. Shown below is the solution to the given linear equation:")
    st.latex(r"5y - 8 = 14 - 3y \quad \text{(Equation 1)}")
    st.latex(r"5y + 3y - 8 = 14 \quad \text{(Equation 2)}")
    st.markdown("What reason can we use to transform equation 1 into equation 2? **(Select all that apply)**")
    st.multiselect("Options for Item 33:", [
        "a. If we subtract $3y$ from both sides, the equation remains true.",
        "b. If we subtract $8$ from both sides, the equation remains true.",
        "c. If we add $3y$ to both sides, the equation remains true.",
        "d. If we divide both sides by $8$, the equation remains true."
    ], key="q33")

# --- TAB 4: Equations & Geometry ---
with tabs[3]:
    st.subheader("Equations and Graphs")
    st.write("**Figure 5: Tricycle Rental Cost ($C = 250n + 200$)**")
    st.warning("⚠️ Figure 5 would be displayed here")
    
    st.markdown("34. How much does it cost to rent the tricycle for 5 days? [Refer to Figure 5]")
    st.text_input("Answer for Item 34:", key="q34")
    
    st.markdown("35. What does the number 250 in the formula represent? [Refer to Figure 5] **(Select all that apply)**")
    st.multiselect("Options for Item 35:", [
        "a. The daily cost of renting the tricycle.",
        "b. The number of days the tricycle is rented.",
        "c. The fixed cost of renting the tricycle.",
        "d. The total cost of renting for one day."
    ], key="q35")
    
    st.markdown("36. In Figure 5, what does the number 200 in the formula represent?")
    st.text_input("Answer for Item 36:", key="q36")
    
    st.markdown("37. What aspect of the graph in Figure 5 represents the 200 in the formula? **(Select all that apply)**")
    st.multiselect("Options for Item 37:", ["a. x-intercept", "b. y-intercept", "c. slope", "d. minimum point"], key="q37")
    
    st.divider()
    st.subheader("Triangles")
    st.write("**Figure 6: Triangle $PQR$**")
    st.warning("⚠️ Figure 6 would be displayed here")
    
    st.markdown("38. In Figure 6, if the measure of angle $P$ is 30 degrees (that is, $p = 30$), which of the following are possible values for $q$ and $r$? **(Select all that apply)**")
    st.multiselect("Options for Item 38:", [
        "a. $q = 10$ and $r = 140$",
        "b. $q = 10$ and $r = 130$",
        "c. $q = 110$ and $r = 30$",
        "d. $q = 100$ and $r = 80$",
        "e. $q = 100$ and $r = 50$"
    ], key="q38")
    
    st.markdown("39. In Figure 6, if the measure of angle $R$ is 60 degrees (that is, $r = 60$) and the measure of the exterior angle at $Q$ is 130, what is true about the values of $p$ and $q$? **(Select all that apply)**")
    st.multiselect("Options for Item 39:", [
        "a. The sum of $p$ and $q$ is 130.",
        "b. $p$ and $q$ can have several values.",
        "c. The value of $p$ is 70 and $q$ is 50.",
        "d. The value of $p$ is 50 and $q$ is 70.",
        "e. The value of $r$ plus $p$ is 130."
    ], key="q39")
    
    st.markdown("40. Which of the following statements about the properties of triangles will help determine the values of $p$ and $q$ in the preceding question? **(Select all that apply)**")
    st.multiselect("Options for Item 40:", [
        "a. Each angle of an equilateral triangle is 60 degrees.",
        "b. In an isosceles triangle, the base angles are equal.",
        "c. The exterior angle and the adjacent interior angle form a linear pair.",
        "d. The measure of the exterior angle is equal to the sum of the two remote interior angles.",
        "e. There are six exterior angles in any triangle.",
        "f. The sum of all exterior angles is 360 degrees."
    ], key="q40")
    
    st.divider()
    st.subheader("Proportionality")
    st.write("**Figure 7: Dog House and Toy Storage**")
    st.warning("⚠️ Figure 7 would be displayed here")
    
    st.markdown("41. If the sides of the dog house have a ratio of 3:3:2 and the shortest side is 1 meter, what are the lengths of the other two sides? **(Select all that apply)**")
    st.multiselect("Options for Item 41:", [
        "a. The other two sides are 1.5 meters each.",
        "b. The other two sides are 2 meters and 3 meters.",
        "c. The other two sides are 3 meters each.",
        "d. The other two sides are 4 meters and 6 meters."
    ], key="q41")
    
    st.markdown("42. In Figure 7, are the sides of the triangular dog house proportional to the sides of the triangular toy storage? Show your solution or explain.")
    st.text_area("Answer for Item 42:", key="q42")
    
    st.markdown("43. The base of the toy storage measures 25 centimeters. What are the lengths of its other two sides? [Refer to Figure 7] **(Select all that apply)**")
    st.multiselect("Options for Item 43:", [
        "a. The other two sides are 37.5 centimeters each.",
        "b. The other two sides measure 50 and 75 centimeters.",
        "c. The other two sides are 75 centimeters each.",
        "d. The other two sides measure 100 and 150 centimeters."
    ], key="q43")
    
    st.divider()
    st.subheader("Circles and Volumes")
    st.write("**Figure 8 & 9: Circular Pool with Sidewalk**")
    st.warning("⚠️ Figure 8 & 9 would be displayed here")
    
    st.markdown("44. What is the area of the sidewalk in square meters surrounding the pool? Show your solution. [Refer to Figure 8] Use $\pi = 3.14$.")
    st.text_area("Solution for Item 44:", key="q44")
    
    st.markdown("45. The pool has depths of 1.5 meters and 0.6 meters. Which of the following will give the total volume of water in the pool? [Refer to Figure 9] **(Select all that apply)**")
    st.multiselect("Options for Item 45:", [
        "a. $10\pi(2.1)$ cubic meters",
        "b. $25\pi(2.1)$ cubic meters",
        "c. $10\pi(2.1)^2$ cubic meters",
        "d. $25\pi(2.1)^2$ cubic meters",
        "e. $100\pi(2.1)^2$ cubic meters"
    ], key="q45")
    
    st.divider()
    st.subheader("Rotation and Distance")
    st.write("**Figure 10: Rolling Wheel (Diameter = 60 cm)**")
    st.warning("⚠️ Figure 10 would be displayed here")
    
    st.markdown("46. The wheel in Figure 10 is rolled exactly 5 times. Show how you can compute the distance travelled by the wheel.")
    st.text_area("Solution for Item 46:", key="q46")
    
    st.markdown("47. How many degrees did the wheel's pin rotate after 5 rolls? [Refer to Figure 10]")
    st.text_input("Answer for Item 47:", key="q47")

# --- FOOTER ---
if st.button("Complete Assessment"):
    st.balloons()
    st.success("Responses submitted successfully!")
