import streamlit as st

# HTML dan CSS untuk animasi hati yang membesar
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
            animation: grow 3s ease-in-out infinite;
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
            0% {
                transform: scale(0.1) rotate(-45deg); /* Mulai dari kecil */
            }
            50% {
                transform: scale(1.2) rotate(-45deg); /* Ukuran normal */
            }
            100% {
                transform: scale(1.5) rotate(-45deg); /* Ukuran lebih besar */
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
st.title("Animasi Hati Tumbuh")
st.components.v1.html(html_code, height=600)
