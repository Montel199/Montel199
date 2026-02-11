import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Halima", layout="centered")

# Enhanced CSS/JS for Mobile and Aesthetics
custom_content = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap');

    body {
        margin: 0;
        background: radial-gradient(circle at top, #200122, #000000);
        overflow: hidden;
        height: 100vh;
        width: 100vw;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Poppins', sans-serif;
        color: white;
    }

    /* Star Background */
    #star-container {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: -1;
    }

    .star {
        position: absolute;
        background: white;
        border-radius: 50%;
        opacity: 0.5;
        animation: twinkle var(--duration) infinite;
    }

    @keyframes twinkle { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }

    /* Floating Hearts */
    .heart-bg {
        position: absolute;
        color: rgba(255, 75, 75, 0.3);
        font-size: 20px;
        animation: floatUp 6s linear infinite;
        z-index: -1;
    }

    @keyframes floatUp {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
    }

    .card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 40px 20px;
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        width: 85%;
        max-width: 400px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    h1 {
        font-family: 'Dancing Script', cursive;
        font-size: 2.5rem;
        margin-bottom: 30px;
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .btn-container {
        position: relative;
        height: 150px; /* Space for the runaway button */
    }

    button {
        padding: 12px 35px;
        font-size: 1.2rem;
        border-radius: 50px;
        border: none;
        font-weight: 600;
        transition: 0.3s;
        touch-action: manipulation;
    }

    #yes-btn {
        background: linear-gradient(45deg, #ff416c, #ff4b2b);
        color: white;
        box-shadow: 0 4px 15px rgba(255, 65, 108, 0.4);
    }

    #no-btn {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        background: #333;
        color: #888;
        white-space: nowrap;
    }

    .success-msg { animation: fadeIn 2s; }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
</style>

<div id="star-container"></div>
<div id="heart-container"></div>

<div class="card" id="main-card">
    <div id="content">
        <h1>Will you be my Valentine, Halima? 🌹</h1>
        <div class="btn-container">
            <button id="yes-btn" onclick="celebrate()">Yes!</button>
            <button id="no-btn" onmouseover="moveNo()" ontouchstart="moveNo()">No</button>
        </div>
    </div>
</div>

<script>
    // Create Twinkling Stars
    const stars = document.getElementById('star-container');
    for (let i = 0; i < 80; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.width = star.style.height = Math.random() * 3 + 'px';
        star.style.top = Math.random() * 100 + '%';
        star.style.left = Math.random() * 100 + '%';
        star.style.setProperty('--duration', Math.random() * 3 + 2 + 's');
        stars.appendChild(star);
    }

    // Floating Hearts background
    setInterval(() => {
        const heart = document.createElement('div');
        heart.className = 'heart-bg';
        heart.innerHTML = '❤️';
        heart.style.left = Math.random() * 100 + 'vw';
        heart.style.fontSize = Math.random() * 20 + 10 + 'px';
        document.getElementById('heart-container').appendChild(heart);
        setTimeout(() => heart.remove(), 6000);
    }, 500);

    let alertShown = false;

    function moveNo() {
        const btn = document.getElementById('no-btn');
        // Calculate random position within the card boundaries
        const maxX = window.innerWidth - 100;
        const maxY = window.innerHeight - 50;
        
        btn.style.position = 'fixed';
        btn.style.left = Math.random() * maxX + 'px';
        btn.style.top = Math.random() * maxY + 'px';

        if (!alertShown) {
            alert("You probably wish there was a 'maybe' answer 😂😆");
            alertShown = true;
        }
    }

    function celebrate() {
        document.getElementById('main-card').innerHTML = `
            <div class="success-msg">
                <h1 style="font-size: 3rem;">❤️ Yay! ❤️</h1>
                <p style="font-size: 1.2rem;">My heart is all yours now, Halima.</p>
                <div style="font-size: 4rem; margin-top: 20px;">🎊💍✨</div>
                <p style="margin-top: 20px; font-style: italic; opacity: 0.8;">I can't wait to celebrate with you!</p>
            </div>
        `;
        // Add extra confetti-like hearts
        for(let i=0; i<30; i++) {
            setTimeout(() => {
                const h = document.createElement('div');
                h.className = 'heart-bg';
                h.innerHTML = '💖';
                h.style.left = Math.random() * 100 + 'vw';
                h.style.color = '#ff4b4b';
                document.getElementById('heart-container').appendChild(h);
            }, i * 100);
        }
    }
</script>
"""

components.html(custom_content, height=700)
