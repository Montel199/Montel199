import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Halima", layout="centered")

# Updated code to match the aesthetic: Teddy, Glowing Borders, and Shooting Stars
custom_content = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap');

    body {
        margin: 0;
        background: radial-gradient(circle at center, #4a1936 0%, #1a0a2e 100%);
        overflow: hidden;
        height: 100vh;
        width: 100vw;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Poppins', sans-serif;
    }

    /* --- BACKGROUND ANIMATIONS --- */
    #bg-layer {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: -1;
    }

    .shooting-star {
        position: absolute;
        width: 2px;
        height: 2px;
        background: white;
        box-shadow: 0 0 10px 2px white;
        border-radius: 50%;
        opacity: 0;
        animation: shoot 4s linear infinite;
    }
    @keyframes shoot {
        0% { transform: translate(100vw, -10vh) rotate(-45deg); opacity: 1; width: 2px; }
        20% { transform: translate(50vw, 40vh) rotate(-45deg); opacity: 0; width: 100px; }
        100% { opacity: 0; }
    }

    /* --- THE TEDDY BEAR --- */
    .teddy {
        position: fixed;
        bottom: 20px;
        left: 20px;
        font-size: 80px;
        z-index: 100;
        animation: sway 3s ease-in-out infinite;
        filter: drop-shadow(0 0 10px rgba(0,0,0,0.5));
    }
    @keyframes sway {
        0%, 100% { transform: rotate(-5deg) translateY(0); }
        50% { transform: rotate(5deg) translateY(-10px); }
    }

    /* --- MAIN CARD (Matches the Image) --- */
    .card {
        background: rgba(30, 30, 30, 0.9);
        padding: 40px 20px;
        border-radius: 30px;
        border: 3px solid #ff69b4; /* Pink Border */
        box-shadow: 0 0 20px #ff69b4, inset 0 0 10px #ff69b4;
        text-align: center;
        width: 85%;
        max-width: 380px;
        z-index: 10;
        position: relative;
    }

    h1 {
        font-family: 'Dancing Script', cursive;
        font-size: 2.2rem;
        color: white;
        margin-bottom: 20px;
        text-shadow: 0 0 10px #ff4b4b;
    }

    .btn-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        margin-top: 20px;
    }

    button {
        width: 180px;
        padding: 12px;
        font-size: 1.2rem;
        border-radius: 25px;
        border: none;
        font-weight: 600;
        cursor: pointer;
        transition: 0.3s;
    }

    #yes-btn {
        background: #ff4b4b;
        color: white;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.5);
    }

    #no-btn {
        background: #555;
        color: #ddd;
        position: absolute; /* Crucial for runaway logic */
    }

    /* Floating elements for second page */
    .floating-heart {
        position: absolute;
        animation: floatUp 5s linear infinite;
        z-index: 5;
    }
    @keyframes floatUp {
        from { transform: translateY(100vh); opacity: 1; }
        to { transform: translateY(-10vh); opacity: 0; }
    }
</style>

<div id="bg-layer"></div>
<div class="teddy">🧸</div>

<div class="card" id="main-card">
    <div id="content">
        <p style="color: #ff69b4; font-size: 1.5rem; margin-bottom: 5px;">hi</p>
        <h1>Will you be my Valentine, Halima? 🌹</h1>
        <div class="btn-container">
            <button id="yes-btn" onclick="celebrate()">Yes!</button>
            <button id="no-btn" onmouseover="moveNo()" ontouchstart="moveNo()">No</button>
        </div>
    </div>
</div>

<script>
    const bg = document.getElementById('bg-layer');

    // Create background stars
    for(let i=0; i<50; i++) {
        let star = document.createElement('div');
        star.style.position = 'absolute';
        star.style.width = '2px';
        star.style.height = '2px';
        star.style.background = 'white';
        star.style.left = Math.random() * 100 + 'vw';
        star.style.top = Math.random() * 100 + 'vh';
        star.style.opacity = Math.random();
        bg.appendChild(star);
    }

    // Shooting stars
    setInterval(() => {
        let s = document.createElement('div');
        s.className = 'shooting-star';
        s.style.left = Math.random() * 50 + 'vw';
        s.style.top = Math.random() * 50 + 'vh';
        bg.appendChild(s);
        setTimeout(() => s.remove(), 4000);
    }, 2000);

    let alertShown = false;
    function moveNo() {
        const btn = document.getElementById('no-btn');
        const x = Math.random() * (window.innerWidth - 150);
        const y = Math.random() * (window.innerHeight - 50);
        btn.style.left = x + 'px';
        btn.style.top = y + 'px';
        btn.style.position = 'fixed'; // Pops it out of the card to move anywhere
        
        if (!alertShown) {
            alert("You probably wish there was a 'maybe' answer 😂😆");
            alertShown = true;
        }
    }

    function celebrate() {
        document.getElementById('main-card').innerHTML = `
            <div style="animation: fadeIn 1s;">
                <h1 style="font-size: 3rem;">YAY! ❤️</h1>
                <p style="color: #fff;">I knew you'd say yes, Halima!</p>
                <div style="font-size: 5rem; margin: 20px 0;">💖💍✨</div>
                <p style="font-style: italic; color: #ff69b4;">Best. Valentine. Ever.</p>
            </div>
        `;
        // Explosion of hearts
        for(let i=0; i<40; i++) {
            setTimeout(() => {
                let h = document.createElement('div');
                h.className = 'floating-heart';
                h.innerHTML = '❤️';
                h.style.left = Math.random() * 100 + 'vw';
                h.style.fontSize = (Math.random() * 20 + 20) + 'px';
                document.body.appendChild(h);
            }, i * 100);
        }
    }
</script>
"""

components.html(custom_content, height=800)
