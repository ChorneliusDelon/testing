import streamlit as st

# HTML dan CSS untuk animasi love
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .heart {
            position: relative;
            width: 50px;
            height: 50px;
            background-color: red;
            transform: rotate(-45deg);
            animation: grow 2s infinite;
        }
        .heart::before,
        .heart::after {
            content: "";
            position: absolute;
            width: 50px;
            height: 50px;
            background-color: red;
            border-radius: 50%;
        }
        .heart::before {
            top: -25px;
            left: 0;
        }
        .heart::after {
            top: 0;
            left: -25px;
        }
        @keyframes grow {
            0%, 100% {
                transform: scale(1) rotate(-45deg);
            }
            50% {
                transform: scale(1.5) rotate(-45deg);
            }
        }
    </style>
</head>
<body>
    <div class="heart"></div>
</body>
</html>
"""

# Tampilkan animasi di Streamlit
st.title("Animasi Hati yang Tumbuh")
st.components.v1.html(html_code, height=600)
