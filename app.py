st.markdown("45. The park management decides to divide the pool into two equal parts. One part will be designated for adults and has a depth of 1.5 meters, while the other part will be designated for children and has a depth of 0.6 meters. Which of the following will give the total volume of water in the pool? [Refer to Figure 9] **(Select all that apply)**")

    # --- Two-column, professional layout exactly like the sample image ---
    st.caption("Pumili ng lahat ng tamang sagot:")

    # Initialize per-choice states (to keep selections persistent and to mirror into q45)
    for k in ["q45_a", "q45_b", "q45_c", "q45_d", "q45_e"]:
        if k not in st.session_state:
            st.session_state[k] = False

    # Small helper: renders a checkbox label (letter) + aligned LaTeX + unit text
    def render_choice(letter_key: str, letter: str, latex_expr: str):
        # Letter column + expression column
        cols = st.columns([0.12, 0.88])
        with cols[0]:
            st.checkbox(letter, key=letter_key)
        with cols[1]:
            # Put the math expression and the "cubic meters" like the sample
            expr_cols = st.columns([0.6, 0.4])
            with expr_cols[0]:
                st.latex(latex_expr)
            with expr_cols[1]:
                st.write("cubic meters")

    # Create two columns to mimic the side-by-side layout in your sample
    left_col, right_col = st.columns(2)

    with left_col:
        # a and b (plain products)
        render_choice("q45_a", "a.", r"10\pi(2.1)")
        render_choice("q45_b", "b.", r"25\pi(2.1)")
        # c (proper fraction)
        render_choice("q45_c", "c.", r"\frac{10\pi(2.1)}{2}")

    with right_col:
        # d and e (proper fractions)
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
