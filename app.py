import streamlit as st
from PIL import Image
import os
import datetime

# --- APP CONFIG ---
st.set_page_config(page_title="Rapid Mathematics Assessment", page_icon="📝", layout="wide")

# --- CORRECT ANSWERS CONFIGURATION ---
# Modify this dictionary with the actual correct answers.
# For multiple-choice questions, store the answer as a list of the full option strings.
# For text/number inputs, store as a string (case-insensitive comparison, spaces stripped).
CORRECT_ANSWERS = {
    # Items 1-11
    "q1": "4×4−5×3 = 16−15 = 1",                 # example computation
    "q2": "6×6−7×5",                              # next expression
    "q3": ["b. (n)(n) - [(n + 1)(n - 1)]", "c. (n - 1)(n - 1) - n(n - 2)"],  # example correct
    "q4": "Because when expanded, both give n² - (n² -1) = 1",  # explanation
    "q5": "the first number in each expression (2,3,4,5...)",
    "q6": "1024 = 2×2×2×2×2×2×2×2×2×2 = 2¹⁰",    # solution
    "q7": "2¹⁰",
    "q8": "64 or 128",                            # multiple of 16 between 50-200
    "q9": "YES, 0.9985",
    "q10": "0.999 - 0.998 = 0.001",
    "q11": "YES, 7/8",
    # Items 12-22
    "q12": 5,                                      # number of students below 84
    "q13": "I counted the points below 84 on the graph.",
    "q14": ["b. As the number of absences decreases, the overall academic grade increases.",
            "c. As the number of absences increases, the overall academic grade decreases."],
    "q15": "Purok 2 shows more diversity because the income range is wider.",
    "q16": "No, because the distribution is different; Purok 2 has more low-income families.",
    "q17": 49,
    "q18": 19,
    "q19": "18/110 or 0.1636",
    "q20": "How many students participated only in sports?",
    "q21": ["c. Point F is at -300"],              # adjust as needed
    "q22": "200",
    # Items 23-33
    "q23": "(3,2)",                                # example coordinates
    "q24": ["d. (3, 2)", "f. (5, 6)"],             # exactly two
    "q25": ["c. (x, -x)", "d. (x, -x + 1)"],       # all that apply
    "q26": "Area = ½ × base × height = ...",
    "q27": "school",
    "q28": "Distance from house to school is shorter based on coordinates.",
    "q29": ["-5", "-27", "99"],                     # odd integers
    "q30": ["d. cost = 100n/3", "e. 3 : 100 = n : cost"],
    "q31": "a=3, b=17",                             # example pair
    "q32": ["c. The difference between b and a, (b-a), is 14."],
    "q33": ["c. If we add 3y to both sides of equation ①, the equation will remain true."],
    # Items 34-47
    "q34": "1450",                                   # 250*5+200
    "q35": ["a. The daily cost of renting the tricycle."],
    "q36": "fixed cost / initial fee",
    "q37": ["b. y-intercept"],
    "q38": ["b. q = 10 and r = 130", "e. q = 100 and r = 50"],  # two correct
    "q39": ["a. The sum of p and q is 130.", "d. The value of p is 50 and the value of q is 70."],
    "q40": ["c. The exterior angle and one of the interior angles adjacent to it form a linear pair.",
            "d. The measure of the exterior angle of a triangle is equal to the sum of the two remote interior angles."],
    "q41": ["a. The other two sides are 1.5 meters each."],
    "q42": "Yes, because the toy storage is similar to the dog house (parallel sides).",
    "q43": ["a. The other two sides are 37.5 centimeters each."],
    "q44": "Area = π(6²) - π(5²) = π(36-25) = 11π = 34.54 m²",
    "q45": ["b. 25π(2.1) cubic meters"],            # correct expression(s)
    "q46": "Distance = 5 × circumference = 5 × π × 60 cm = 300π cm",
    "q47": "1800°",                                  # 5 rotations * 360°
}

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
    </style>
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
# Initialize name fields if not present
if 'surname' not in st.session_state:
    st.session_state.surname = ""
if 'given_name' not in st.session_state:
    st.session_state.given_name = ""
if 'middle_name' not in st.session_state:
    st.session_state.middle_name = ""

# --- HEADER ---
st.title("Rapid Mathematics Assessment (Grades 7 - 10)")
st.write("---")

# Student Information
col1, col2, col3 = st.columns(3)
with col1:
    st.text_input("Surname", key="surname")
with col2:
    st.text_input("Given Name", key="given_name")
with col3:
    st.text_input("Middle Name", key="middle_name")
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
    st.text_area("Answer/Explanation for Item 9:", key="q9")
    
    st.markdown("10. Show how you will subtract 0.998 from 0.999.")
    st.text_area("Solution for Item 10:", key="q10")
    
    st.markdown("11. Is there a fraction that is greater than $\\frac{3}{4}$ but less than 1? If YES, give one example. If NO, explain why you think so.")
    st.text_area("Answer/Explanation for Item 11:", key="q11")

# --- TAB 2: Data & Coordinates (Items 12-22) ---
with tabs[1]:
    st.subheader("Data Interpretation")
    
    # Figure 1
    with st.container():
        st.markdown("### Figure 1: Relationship Between Absences and Academic Grade")
        st.markdown("*The graph shows the relationship between student absences and overall academic grade across all subjects in the Masipag section, a special class for arts and design, for two academic quarters. Each point on the graph represents an individual student.*")
        display_figure(1, "Absences vs Academic Grade", "figure_1.png")
    
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
    
    # Figure 2
    with st.container():
        st.markdown("### Figure 2: Monthly Family Income in Purok 1 and Purok 2")
        st.markdown("*Barangay San Mateo is planning to provide financial assistance for its two puroks. They surveyed the monthly family incomes in Purok 1 and Purok 2.*")
        display_figure(2, "Monthly Family Income", "figure_2.png")
    
    st.markdown("15. Based on the graph in Figure 2, which of the two puroks shows more diversity in monthly family income? Explain or justify your answer.")
    st.text_area("Answer for Item 15:", key="q15")
    
    st.markdown("16. The average monthly income of the families in Purok 1 and Purok 2 are equal. Should both purok be given the same amount of financial aid? What information in the graph in Figure 2 did you base your decision on?")
    st.text_area("Answer for Item 16:", key="q16")
    
    st.divider()
    st.subheader("Probability and Tables")
    st.write("**Table 2: Music and Sports Activities Participation**")
    st.markdown("*Malaya High School organized music and sports activities to celebrate the school's foundation day. Table 2 shows the participation of the Grade 7 students.*")
    
    # Simple Table 2
    st.markdown("""
| | Participated in sports | Did not participate in sports | Total |
|---|---|---|---|
| **Participated in music** | 18 | 31 | 49 |
| **Did not participate in music** | 42 | 19 | 61 |
| **Total** | 60 | 50 | 110 |
    """)
    
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
    
    # Figure 3
    with st.container():
        st.markdown("### Figure 3: Number Line")
        st.markdown("*A number describes the position of a point on a number line. The picture below is part of a number line.*")
        display_figure(3, "Number Line", "figure_3.png")
    
    st.markdown("21. What is the position of point \( F \) in Figure 3? **(Select all that apply)**")
    
    # Dropdown only for Item 21
    st.multiselect("Select your answer(s):", [
        "a. Point F is at -500",
        "b. Point F is at -400", 
        "c. Point F is at -300",
        "d. Point F is at -200",
        "e. Point F is at 50"
    ], key="q21")
    
    st.markdown("22. What is the position of point G in Figure 3?")
    st.text_input("Answer for Item 22:", key="q22")

# --- TAB 3: Cartesian Plane & Algebra (Items 23-33) ---
with tabs[2]:
    st.subheader("Cartesian Plane")
    st.markdown("*An ordered pair of numbers describes the position of a point on a Cartesian plane. This position is called the coordinates of the point. The first number in the ordered pair is called the x-coordinate and the second number is called the y-coordinate.*")
    
    # Figure 4
    with st.container():
        st.markdown("### Figure 4: Cartesian Grid")
        display_figure(4, "Cartesian Grid", "figure_4.png")
    
    st.markdown("23. What are the coordinates of Point C in Figure 4?")
    st.text_input("Coordinates (x, y) for Item 23:", key="q23")
    
    st.markdown("24. A line is drawn passing through points B and C in Figure 4. Select two ordered pairs that represent the coordinates of points that are also in this line. **(Select exactly two)**")
    st.multiselect("Select points for Item 24:", [
        "a. (1, -1)", 
        "b. (1, -2)", 
        "c. (2, 3)", 
        "d. (3, 2)", 
        "e. (4, 7)", 
        "f. (5, 6)"
    ], key="q24", max_selections=2)
    
    st.markdown("25. Draw a line through points A and B in Figure 4. Which of the following ordered pairs represent all the points that are on this line? **(Select all that apply)**")
    # Removed dollar signs from options
    st.multiselect("Options for Item 25:", [
        "a. (x, -2x)",
        "b. (x, -2x + 1)",
        "c. (x, -x)",
        "d. (x, -x + 1)",
        "e. (x, -x + 2)"
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
        "a. cost = 100/3",
        "b. cost = 3n/100",
        "c. cost = 100n",
        "d. cost = 100n/3",
        "e. 3 : 100 = n : cost"
    ], key="q30")
    
    st.write("**Box 2:**")
    st.latex(r"17 + \_ = \_ + 3")
    st.markdown("*In Box 2 above, let a represent the number in the first blank space, and b represent the number in the second blank space.*")
    
    st.markdown("31. Write two possible values for $a$ and $b$ that will make the equation in Box 2 true.")
    st.text_input("Values for Item 31 (format: a, b):", key="q31")
    
    st.markdown("32. Which statement is always true about $a$ and $b$? [Refer to Box 2] **(Select all that apply)**")
    # Removed dollar signs from options
    st.multiselect("Options for Item 32:", [
        "a. a is greater than b.",
        "b. The sum of a and b, (a+b), is 20.",
        "c. The difference between b and a, (b-a), is 14.",
        "d. a and b can take any value."
    ], key="q32")
    
    st.markdown("33. Shown below is the solution to the given linear equation:")
    st.latex(r"5y - 8 = 14 - 3y \quad \text{---①}")
    st.latex(r"5y + 3y - 8 = 14 \quad \text{---②}")
    st.latex(r"8y - 8 = 14")
    st.latex(r"8y = 14 + 8")
    st.latex(r"8y = 22")
    st.latex(r"y = \frac{11}{4} \text{ or } 2.75")
    st.markdown("What reason can we use to transform equation ① into equation ②? **(Select all that apply)**")
    st.multiselect("Options for Item 33:", [
        "a. If we subtract 3y from both sides of equation ①, the equation will remain true.",
        "b. If we subtract 8 from both sides of equation ①, the equation will remain true.",
        "c. If we add 3y to both sides of equation ①, the equation will remain true.",
        "d. If we divide both sides of equation ① by 8, the equation will remain true."
    ], key="q33")

# --- TAB 4: Equations & Geometry (Items 34-47) ---
with tabs[3]:
    st.subheader("Equations and Graphs")
    st.markdown("*The cost of renting a tricycle per day is shown in the graph and formula below.*")
    
    # Figure 5
    with st.container():
        st.markdown("### Figure 5: Tricycle Rental Cost")
        st.markdown("Formula: $C = 250n + 200$")
        display_figure(5, "Tricycle Rental Cost Graph", "figure_5.png")
    
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
    st.multiselect("Options for Item 37:", [
        "a. x-intercept", 
        "b. y-intercept", 
        "c. slope", 
        "d. minimum point"
    ], key="q37")
    
    st.divider()
    st.subheader("Triangles")
    st.markdown("*Lines f, g, and h intersect at points P, Q and R, forming a triangle. The measures of the angles in degrees are represented by p, q and r.*")
    
    # Figure 6
    with st.container():
        st.markdown("### Figure 6: Triangle PQR")
        display_figure(6, "Triangle PQR", "figure_6.png")
    
    st.markdown("38. In Figure 6, if the measure of angle P is 30 degrees (that is, p = 30), which of the following are possible values for q and r? **Choose 2 that are correct** among the choices. Note that the triangle is not drawn to scale.")
    # Removed dollar signs from options
    st.multiselect("Options for Item 38:", [
        "a. q = 10 and r = 140",
        "b. q = 10 and r = 130",
        "c. q = 110 and r = 30",
        "d. q = 100 and r = 80",
        "e. q = 100 and r = 50"
    ], key="q38", max_selections=2)
    
    st.markdown("39. In Figure 6, if the measure of angle R is 60 degrees (that is, $r = 60$) and the measure of the exterior angle at Q is 130, what is true about the values of p and q? **Choose at least one true statement** about p and q. NOTE: The exterior angle of a triangle forms a 180-degree angle with the adjacent interior angle.")
    st.multiselect("Options for Item 39:", [
        "a. The sum of p and q is 130.",
        "b. p and q can have several values.",
        "c. The value of p is 70 and the value of q is 50.",
        "d. The value of p is 50 and the value of q is 70.",
        "e. The value of r plus p is 130."
    ], key="q39")
    
    st.markdown("40. Which of the following statements about the properties of triangles will help determine the values of p and q in the preceding question? **Choose those that are applicable.** [Refer to Figure 6]")
    st.multiselect("Options for Item 40:", [
        "a. Each angle of an equilateral triangle is 60 degrees.",
        "b. In an isosceles triangle, the base angles are equal.",
        "c. The exterior angle and one of the interior angles adjacent to it form a linear pair.",
        "d. The measure of the exterior angle of a triangle is equal to the sum of the two remote interior angles.",
        "e. There are six exterior angles in any triangle.",
        "f. The sum of all the exterior angles of a triangle is 360 degrees."
    ], key="q40")
    
    st.divider()
    st.subheader("Proportionality")
    st.markdown("*Carlos built a house for his dog, Brownie. The lower part of the dog house serves as a sleeping area, while a small portion on top is used for toy storage. The base of the toy storage, which measures 25 centimeters, is parallel to the floor. The dog house is triangular with sides in the ratio of 3:3:2. The shortest side measures 1 meter.*")
    
    # Figure 7
    with st.container():
        st.markdown("### Figure 7: Dog House and Toy Storage")
        display_figure(7, "Dog House and Toy Storage", "figure_7.png")
    
    st.markdown("41. What are the lengths of the other two sides of the triangular dog house? [Refer to Figure 7] **(Select all that apply)**")
    st.multiselect("Options for Item 41:", [
        "a. The other two sides are 1.5 meters each.",
        "b. The other two sides are 2 meters and 3 meters.",
        "c. The other two sides are 3 meters each.",
        "d. The other two sides are 4 meters and 6 meters."
    ], key="q41")
    
    st.markdown("42. In Figure 7, are the sides of the triangular dog house proportional to the sides of the triangular toy storage? Show your solution or explain your answer.")
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
    st.markdown("*A public park has a circular pool with a diameter of 10 meters. The park management decided to build a sidewalk around the pool to allow people to walk around it safely. The sidewalk has a uniform width of 1 meter all around the pool.*")
    
    # Figures 8 and 9
    with st.container():
        st.markdown("### Figure 8: Circular Pool (top view)")
        display_figure(8, "Circular Pool - Top View", "figure_8.png")
    
    with st.container():
        st.markdown("### Figure 9: Pool Depth (auxiliary view)")
        display_figure(9, "Pool Depth Diagram", "figure_9.png")
    
    st.markdown("44. What is the area of the sidewalk in square meters surrounding the pool? Show your solution. [Refer to Figure 8] Use $\\pi = 3.14$.")
    st.text_area("Solution for Item 44:", key="q44")
    
    # ------------------- REVISED ITEM 45 (English + two-column layout) -------------------
    st.markdown("45. The park management decides to divide the pool into two equal parts. One part will be designated for adults and has a depth of 1.5 meters, while the other part will be designated for children and has a depth of 0.6 meters. Which of the following will give the total volume of water in the pool? [Refer to Figure 9] **(Select all that apply)**")

    st.caption("Select all correct answers:")

    # Initialize individual checkbox states if not present
    for k in ["q45_a", "q45_b", "q45_c", "q45_d", "q45_e"]:
        if k not in st.session_state:
            st.session_state[k] = False

    # Helper to render one choice with letter, LaTeX, and unit text in a row
    def render_choice(letter_key: str, letter: str, latex_expr: str):
        row = st.columns([0.12, 0.58, 0.30])  # letter / math / units
        with row[0]:
            st.checkbox(letter, key=letter_key)
        with row[1]:
            st.latex(latex_expr)
        with row[2]:
            st.write("cubic meters")

    # Two-column arrangement: a–c left, d–e right (matches your sample layout)
    left_col, right_col = st.columns(2)
    with left_col:
        render_choice("q45_a", "a.", r"10\pi(2.1)")
        render_choice("q45_b", "b.", r"25\pi(2.1)")
        render_choice("q45_c", "c.", r"\frac{10\pi(2.1)}{2}")
    with right_col:
        render_choice("q45_d", "d.", r"\frac{25\pi(2.1)}{2}")
        render_choice("q45_e", "e.", r"\frac{100\pi(2.1)}{2}")

    # Mirror selections into the same key used by your response summary ("q45")
    selected_q45 = []
    if st.session_state["q45_a"]: selected_q45.append("a. 10π(2.1) cubic meters")
    if st.session_state["q45_b"]: selected_q45.append("b. 25π(2.1) cubic meters")
    if st.session_state["q45_c"]: selected_q45.append("c. (10π(2.1))/2 cubic meters")
    if st.session_state["q45_d"]: selected_q45.append("d. (25π(2.1))/2 cubic meters")
    if st.session_state["q45_e"]: selected_q45.append("e. (100π(2.1))/2 cubic meters")
    st.session_state["q45"] = selected_q45
    # ----------------- END REVISED ITEM 45 -----------------

    st.divider()
    st.subheader("Rotation and Distance")
    st.markdown("*A wheel with a diameter of 60 cm is rolled along a straight path.*")
    
    # Figure 10
    with st.container():
        st.markdown("### Figure 10: Rolling Wheel")
        display_figure(10, "Rolling Wheel", "figure_10.png")
    
    st.markdown("46. The wheel in Figure 10 is rolled exactly 5 times. Show how you can compute the distance travelled by the wheel.")
    st.text_area("Solution for Item 46:", key="q46")
    
    st.markdown("47. How many degrees did the wheel's pin rotate after 5 rolls? [Refer to Figure 10]")
    st.text_input("Answer for Item 47:", key="q47")

# --- FOOTER: SUBMISSION, SCORING, AND DOWNLOAD ---
st.divider()

# Collect all question keys (q1 to q47)
all_question_keys = [f"q{i}" for i in range(1, 48)]  # q1..q47

# Ensure all keys exist in session_state (some may be missing if never answered)
for key in all_question_keys:
    if key not in st.session_state:
        st.session_state[key] = "" if key not in ["q3","q14","q21","q24","q25","q29","q30","q32","q33","q35","q37","q38","q39","q40","q41","q43","q45"] else []

# Scoring function
def compute_score():
    correct = 0
    details = []
    for q_key in all_question_keys:
        user_ans = st.session_state.get(q_key, "")
        correct_ans = CORRECT_ANSWERS.get(q_key, None)
        if correct_ans is None:
            # If no answer key defined, treat as not answered
            details.append((q_key, user_ans, "No key", False))
            continue

        # Compare based on type
        if isinstance(correct_ans, list):
            # Multiselect: compare as sets after stripping
            if isinstance(user_ans, list):
                # Convert both to sets of stripped strings for comparison
                user_set = set(str(item).strip() for item in user_ans if item)
                correct_set = set(str(item).strip() for item in correct_ans)
                is_correct = (user_set == correct_set)
            else:
                is_correct = False
        else:
            # Text/number: case-insensitive strip and compare
            if isinstance(user_ans, str):
                is_correct = (user_ans.strip().lower() == str(correct_ans).strip().lower())
            elif isinstance(user_ans, (int, float)):
                is_correct = (user_ans == correct_ans)
            else:
                is_correct = False

        if is_correct:
            correct += 1
        details.append((q_key, user_ans, correct_ans, is_correct))
    return correct, details

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Complete Assessment", use_container_width=True):
        # Check if name fields are filled (optional)
        if not st.session_state.surname or not st.session_state.given_name:
            st.warning("Please enter your surname and given name before submitting.")
        else:
            st.balloons()
            st.success("Responses submitted successfully!")
            
            # Compute score
            score, details = compute_score()
            total = len(all_question_keys)
            percentage = (score / total) * 100
            
            # Display summary
            st.subheader("📋 Assessment Summary")
            st.write(f"**Student:** {st.session_state.surname}, {st.session_state.given_name} {st.session_state.middle_name}")
            st.write(f"**Score:** {score} / {total}  ({percentage:.1f}%)")
            
            # Option to download results as text file
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"RMA_{st.session_state.surname}_{st.session_state.given_name}_{timestamp}.txt"
            
            # Build content for download
            lines = []
            lines.append("RAPID MATHEMATICS ASSESSMENT RESULTS")
            lines.append("="*50)
            lines.append(f"Student: {st.session_state.surname}, {st.session_state.given_name} {st.session_state.middle_name}")
            lines.append(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
            lines.append(f"Score: {score} / {total} ({percentage:.1f}%)")
            lines.append("="*50)
            lines.append("\nDETAILED RESULTS:")
            for q_key, user, correct, is_correct in details:
                status = "✓" if is_correct else "✗"
                lines.append(f"{q_key.upper()}: {status} | Your answer: {user} | Correct: {correct}")
            lines.append("="*50)
            content = "\n".join(lines)
            
            st.download_button(
                label="📥 Download Summary as Text File",
                data=content,
                file_name=filename,
                mime="text/plain"
            )
            
            # Expandable detailed view
            with st.expander("View Detailed Responses"):
                for q_key, user, correct, is_correct in details:
                    if user:  # only show non-empty
                        mark = "✅" if is_correct else "❌"
                        st.write(f"**{q_key.upper()}:** {mark}  \nYour answer: `{user}`  \nCorrect: `{correct}`")
