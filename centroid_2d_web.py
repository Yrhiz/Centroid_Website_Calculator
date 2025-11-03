import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Detect theme mode safely
theme = st.get_option("theme.base") or "light"

# Define color palettes
if theme == "dark":
    bg_color = "#b4dc87"
    app_bg = "#ffd0de"
    text_color = "000000"
    accent_pink = "#e4f8ba"
    accent_green = "#ffd0de"
    input_bg = "#b4dc87"
    input_border = accent_teal
    button_bg = f"linear-gradient(90deg, {accent_pink} 0%, {accent_teal} 100%)"
else:
    bg_color = "#b4dc87"
    app_bg = "#ffd0de"
    text_color = "#000000"
    accent_pink = "#e4f8ba"
    accent_teal = "#ffd0de"
    input_bg = "#b4dc87"
    input_border = accent_teal
    button_bg = f"linear-gradient(90deg, {accent_pink} 0%, {accent_teal} 100%)"

# 🍵 Sakura & Matcha Themed UI
st.markdown("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap");

/* General Layout */
body {
    background: #ffd0de; /* Sakura pink */
    color: #2f4f1f;
    font-family: "Inter", sans-serif;
}

.stApp {
    background: #ffd0de; /* keep the pink background */
    border-radius: 25px;
    padding: 30px 40px;
}

/* Headers and Titles */
h1, h2, h3 {
    color: #7ea04d !important; /* darker matcha green */
    font-weight: 700;
    text-align: center;
}

/* Section Headings (e.g. Add Filled Shape, Add Hole) */
.css-10trblm, .css-1v3fvcr, .stMarkdown h2 {
    color: #7ea04d !important;
}

/* Buttons (Add Rectangle / Add Hole) */
.stButton button {
    background: linear-gradient(90deg, #b4dc87, #ffa6c0); /* matcha + sakura */
    color: #2f4f1f !important;
    border-radius: 28px;
    padding: 12px 28px;
    font-weight: 700;
    font-size: 16px;
    border: none;
    box-shadow:
      4px 4px 10px rgba(180, 220, 135, 0.4),
      -4px -4px 10px rgba(255, 166, 192, 0.5);
    transition: all 0.3s ease;
}

.stButton button:hover {
    filter: brightness(1.1);
    box-shadow:
      6px 6px 12px rgba(180, 220, 135, 0.6),
      -6px -6px 12px rgba(255, 166, 192, 0.6);
}

/* Input Boxes (Matcha Green) */
.stNumberInput input, .stSelectbox select {
    background: #e4f8ba !important; /* light matcha green boxes */
    color: #2f4f1f !important;
    border: 2px solid #b4dc87;
    border-radius: 15px;
    padding: 14px 18px;
    font-size: 15px;
    box-shadow:
      inset 5px 5px 10px rgba(180, 220, 135, 0.3),
      inset -5px -5px 10px rgba(255,255,255,0.8);
    transition: border-color 0.1s ease;
}

.stNumberInput input:focus, .stSelectbox select:focus {
    outline: none;
    border-color: #ffa6c0; /* Sakura pink highlight */
    box-shadow: 0 0 14px #ffa6c0;
}

/* Sidebar */
.sidebar .sidebar-content {
    background: #ffd0de;
    border-radius: 20px;
    padding: 20px;
    color: #2f4f1f;
}
</style>
""", unsafe_allow_html=True)


# --- SIDEBAR ---
st.sidebar.title("📚 About This Website")

# Centered image from local PNG file
st.sidebar.markdown(
    """
    <div style="text-align:center; margin-bottom:15px;">
        <a href="https://en.wikipedia.org/wiki/File:Triangle.Centroid.svg" target="_blank">
            <img src="Triangle.Centroid.png"
                 width="180"
                 style="border-radius:10px;
                        box-shadow:0 4px 12px rgba(0,0,0,0.15);
                        border:2px solid #f06292;"/>
        </a>
        <p style="margin-top:8px; color:#f06292; font-weight:600;">About Centroid</p>
    </div>
    """,
    unsafe_allow_html=True
)



# Styled info box for centroid definition
st.sidebar.markdown(f"""
<div style="
    background-color:{'#e4f8ba' if theme == 'light' else '#e4f8ba'};
    border-left: 5px solid {accent_teal};
    padding: 15px 20px;
    border-radius: 12px;
    margin-top: 15px;
    margin-bottom: 15px;
    color:{text_color};
">
<h3 style="color:#FF90BB; margin-top:0;">📘 What is a Centroid?</h3>
<p style="font-size:15px; line-height:1.5;">
The <b>centroid</b> (also called the <b>center of gravity</b> or <b>center of mass</b>) 
is the <b>geometric center</b> of a shape — the point where it would 
perfectly <b>balance</b> if made from a uniform material.<br><br>
For <b>composite shapes</b>, the centroid is found by taking a 
<b>weighted average</b> of each part’s area and position.
</p>
</div>
""", unsafe_allow_html=True)

# How the app works
st.sidebar.markdown(f"""
<div style="color:{text_color}; font-size:15px;">
<h3 style="color:#FF90BB;">⚙️ How This Centroid Calculator Works</h3>
<ol>
<li>Add <b>shapes</b> (rectangle, triangle, or circle).</li>
<li>Indicate the <b>Area</b> of the shape.</li>
<li>Determine the <b>Center on X and Y</b> of the shape from bottom left.</li>
<li>Add <b>holes</b> (cutouts) if needed.</li>
<li>Same with <b>shape</b> provide necessary information.</li>
<li>Click the <b>Visualization & Results</b> to find the results.</li>
<li>The calculator calculates the <b>overall centroid</b> using all shapes and holes.</li>
</ol>
</div>
""", unsafe_allow_html=True)

# --- Formula section ---
st.sidebar.markdown(f"""
<div style="color:{text_color}; font-size:15px; margin-top:10px;">
<h3 style="color:#74a12e;">🧮 Formula</h3>
</div>
""", unsafe_allow_html=True)

st.sidebar.latex(r"""
\bar{x} = \frac{\sum A_i x_i}{\sum A_i}, \quad 
\bar{y} = \frac{\sum A_i y_i}{\sum A_i}
""")

st.sidebar.markdown(f"""
<ul style="color:{text_color}; font-size:15px;">
<li><b>Aᵢ</b> = area of each shape (negative for holes)</li>
<li><b>(xᵢ, yᵢ)</b> = centroid coordinates of each shape</li>
</ul>
""", unsafe_allow_html=True)

# Learning resources
st.sidebar.markdown(f"""
<div style="color:{text_color}; font-size:15px; margin-top:10px;">
<h3 style="color:#FF90BB;">🌐 Learn More</h3>
<ul>
<li><a href="https://www.khanacademy.org/science/physics/linear-momentum/center-of-mass/v/center-of-mass" target="_blank">Khan Academy: Center of Mass</a></li>
<li><a href="https://engineeringstatics.org/Chapter_07-centroids.html" target="_blank">Engineering Statics: Centroid</a></li>
<li><a href="https://youtu.be/pBKFiCie2JE?si=byLc1q3VdfNY-K9I" target="_blank">YouTube Tutorial</a></li>
</ul>
</div>
""", unsafe_allow_html=True)

# --- Contact & Footer ---
st.sidebar.markdown(f"""
<hr style="border: 1px solid {accent_teal}; margin-top:20px; margin-bottom:10px;">
<div style="font-size:14px; color:{text_color}; text-align:center; line-height:1.6;">
<p><b>💡 Have a question?</b><br>
Reach out to the creator:</p>

<p><b>Raizen Yrhiz C. Jose</b><br>
📧 <a href="mailto:yrhizj@gmail.com" style="color:#74a12e; text-decoration:none;">yrhizj@gmail.com</a></p>

<p style="margin-top:20px; font-style:italic; color:#FF90BB; font-weight:600;">
"Balance your shapes, balance your world 🌸"
</p>

<p style="font-size:12px; color:gray;">© 2025 Huntrix Centroid Calculator</p>
</div>
""", unsafe_allow_html=True)

# --- MAIN CONTENT ---
st.title("🎯 Centroid & Center of Gravity Calculator (2D)")

st.markdown(
    """
    <p style='text-align: justify; font-size: 17px; color: #000000; line-height: 1.7; margin-top: 10px;'>
    Welcome to the <b style='color:#74a12e;'> Centroid & Center of Gravity Calculator (2D)</b> — 
    a <b style='color:#74a12e;'>modern, interactive tool</b> for exploring the 
    <b style='color:#74a12e;'>balance point of composite shapes</b>. 
    This platform allows you to <b style='color:#74a12e;'>create and modify geometric figures</b>, 
    visualize their <b style='color:#74a12e;'>combined centroid</b>, and understand how each part 
    contributes to the <b style='color:#74a12e;'>system’s equilibrium</b>. <br><br>

    Designed with <b style='color:#74a12e;'>clarity, creativity, and precision</b> in mind, 
    this app transforms centroid computation into an 
    <b style='color:#74a12e;'>intuitive, visually appealing learning experience</b> 
    for <b style='color:#74a12e;'>students</b>, <b style='color:#74a12e;'>engineers</b>, 
    and <b style='color:#74a12e;'>enthusiasts</b> alike. 💫
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# Tabs for inputs and visualization
tab1, tab2 = st.tabs(["➕ Add Shapes & Holes", "📈 Visualization & Results"])

if "shapes" not in st.session_state:
    st.session_state.shapes = []
if "holes" not in st.session_state:
    st.session_state.holes = []

# --- TAB 1 ---
with tab1:
    st.header("Add Composite Shapes")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Add Filled Shape")
        shape_type = st.selectbox("Shape Type", ["Rectangle", "Triangle", "Circle"], key="shape_type")
        if shape_type == "Rectangle":
            length = st.number_input("Length (horizontal)", min_value=0.1, value=2.0, key="rect_len")
            width = st.number_input("Width (vertical)", min_value=0.1, value=2.0, key="rect_w")
            centroid_x = st.number_input("Centroid X", value=0.0, key="rect_cent_x")
            centroid_y = st.number_input("Centroid Y", value=0.0, key="rect_cent_y")
            area = length * width
            if st.button("Add Rectangle", key="add_rect"):
                st.session_state.shapes.append(("Rectangle", (length, width), (centroid_x, centroid_y), area))
                st.success("Rectangle added!")

        elif shape_type == "Triangle":
            base = st.number_input("Base (horizontal)", min_value=0.1, value=2.0, key="tri_base")
            height = st.number_input("Height (vertical)", min_value=0.1, value=2.0, key="tri_height")
            centroid_x = st.number_input("Centroid X", value=0.0, key="tri_cent_x")
            centroid_y = st.number_input("Centroid Y", value=0.0, key="tri_cent_y")
            area = 0.5 * base * height
            if st.button("Add Triangle", key="add_tri"):
                st.session_state.shapes.append(("Triangle", (base, height), (centroid_x, centroid_y), area))
                st.success("Triangle added!")

        elif shape_type == "Circle":
            radius = st.number_input("Radius", min_value=0.1, value=1.0, key="circ_radius")
            centroid_x = st.number_input("Centroid X", value=0.0, key="circ_cent_x")
            centroid_y = st.number_input("Centroid Y", value=0.0, key="circ_cent_y")
            area = np.pi * radius ** 2
            if st.button("Add Circle", key="add_circ"):
                st.session_state.shapes.append(("Circle", (radius,), (centroid_x, centroid_y), area))
                st.success("Circle added!")

    with col2:
        st.subheader("Add Hole (Cutout)")
        hole_type = st.selectbox("Hole Type", ["Rectangle", "Triangle", "Circle"], key="hole_type")

        if hole_type == "Rectangle":
            length = st.number_input("Length (horizontal)", min_value=0.1, value=1.0, key="hole_rect_len")
            width = st.number_input("Width (vertical)", min_value=0.1, value=1.0, key="hole_rect_w")
            centroid_x = st.number_input("Centroid X", value=0.0, key="hole_rect_cent_x")
            centroid_y = st.number_input("Centroid Y", value=0.0, key="hole_rect_cent_y")
            area = length * width
            if st.button("Add Rectangle Hole", key="add_hole_rect"):
                st.session_state.holes.append(("Rectangle", (length, width), (centroid_x, centroid_y), area))
                st.success("Rectangle hole added!")

        elif hole_type == "Triangle":
            base = st.number_input("Base (horizontal)", min_value=0.1, value=1.0, key="hole_tri_base")
            height = st.number_input("Height (vertical)", min_value=0.1, value=1.0, key="hole_tri_height")
            centroid_x = st.number_input("Centroid X", value=0.0, key="hole_tri_cent_x")
            centroid_y = st.number_input("Centroid Y", value=0.0, key="hole_tri_cent_y")
            area = 0.5 * base * height
            if st.button("Add Triangle Hole", key="add_hole_tri"):
                st.session_state.holes.append(("Triangle", (base, height), (centroid_x, centroid_y), area))
                st.success("Triangle hole added!")

        elif hole_type == "Circle":
            radius = st.number_input("Radius", min_value=0.1, value=0.5, key="hole_circ_radius")
            centroid_x = st.number_input("Centroid X", value=0.0, key="hole_circ_cent_x")
            centroid_y = st.number_input("Centroid Y", value=0.0, key="hole_circ_cent_y")
            area = np.pi * radius ** 2
            if st.button("Add Circle Hole", key="add_hole_circ"):
                st.session_state.holes.append(("Circle", (radius,), (centroid_x, centroid_y), area))
                st.success("Circle hole added!")

# --- TAB 2 ---
with tab2:
    st.header("Composite Shape Visualization & Centroid")

    if len(st.session_state.shapes) == 0:
        st.info("Add shapes in the first tab to start visualization.")
    else:
        total_area = sum(s[3] for s in st.session_state.shapes) - sum(h[3] for h in st.session_state.holes)
        sum_x = sum(s[3] * s[2][0] for s in st.session_state.shapes) - sum(h[3] * h[2][0] for h in st.session_state.holes)
        sum_y = sum(s[3] * s[2][1] for s in st.session_state.shapes) - sum(h[3] * h[2][1] for h in st.session_state.holes)

        if total_area <= 0:
            st.error("Total area is zero or negative. Please check shapes and holes.")
        else:
            centroid_x = sum_x / total_area
            centroid_y = sum_y / total_area
            st.success(f"Composite centroid:\n**X = {centroid_x:.3f}, Y = {centroid_y:.3f}** with total area {total_area:.3f}")

            fig = go.Figure()

            for stype, params, (cx, cy), _ in st.session_state.shapes:
                if stype == "Rectangle":
                    length, width = params
                    fig.add_shape(type="rect",
                                  x0=cx - length/2, y0=cy - width/2,
                                  x1=cx + length/2, y1=cy + width/2,
                                  fillcolor=f"rgba(213,180,221,0.5)",
                                  line_color="rgba(213,180,221,1)")
                elif stype == "Triangle":
                    base, height = params
                    x0 = cx - base/3
                    y0 = cy - height/3
                    points = [(x0, y0), (x0 + base, y0), (x0 + base/3, y0 + height)]
                    fig.add_trace(go.Scatter(x=[p[0] for p in points] + [points[0][0]],
                                             y=[p[1] for p in points] + [points[0][1]],
                                             fill='toself',
                                             fillcolor='rgba(162, 196, 230,0.5)',
                                             line=dict(color='rgba(162, 196, 230,1)'),
                                             mode='lines', showlegend=False))
                elif stype == "Circle":
                    r = params[0]
                    theta = np.linspace(0, 2 * np.pi, 100)
                    x = cx + r * np.cos(theta)
                    y = cy + r * np.sin(theta)
                    fig.add_trace(go.Scatter(x=x, y=y,
                                             fill='toself',
                                             fillcolor='rgba(248, 176, 209,0.5)',
                                             line=dict(color='rgba(248, 176, 209,1)'),
                                             mode='lines', showlegend=False))

            for htype, params, (cx, cy), _ in st.session_state.holes:
                if htype == "Rectangle":
                    length, width = params
                    fig.add_shape(type="rect",
                                  x0=cx - length/2, y0=cy - width/2,
                                  x1=cx + length/2, y1=cy + width/2,
                                  fillcolor="white",
                                  line_color="rgba(200,200,200,1)")
                elif htype == "Triangle":
                    base, height = params
                    x0 = cx - base/3
                    y0 = cy - height/3
                    points = [(x0, y0), (x0 + base, y0), (x0 + base/3, y0 + height)]
                    fig.add_trace(go.Scatter(x=[p[0] for p in points] + [points[0][0]],
                                             y=[p[1] for p in points] + [points[0][1]],
                                             fill='toself',
                                             fillcolor='white',
                                             line=dict(color='rgba(150,150,150,1)'),
                                             mode='lines', showlegend=False))
                elif htype == "Circle":
                    r = params[0]
                    theta = np.linspace(0, 2 * np.pi, 100)
                    x = cx + r * np.cos(theta)
                    y = cy + r * np.sin(theta)
                    fig.add_trace(go.Scatter(x=x, y=y,
                                             fill='toself',
                                             fillcolor='white',
                                             line=dict(color='rgba(150,150,150,1)'),
                                             mode='lines', showlegend=False))

            fig.add_trace(go.Scatter(x=[centroid_x], y=[centroid_y],
                                     mode="markers+text",
                                     text=["C"],
                                     textposition="top center",
                                     marker=dict(color="red", size=12),
                                     name="Centroid"))

            fig.update_layout(width=700, height=600, xaxis_title="X", yaxis_title="Y",
                              title="Composite Shape Visualization with Centroid",
                              xaxis=dict(scaleanchor="y", scaleratio=1))
            st.plotly_chart(fig)
