import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Halima", layout="centered")

# Enhanced romantic aesthetic with cartoons and better animations
custom_content = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap');

    body {
        margin: 0;
        background: linear-gradient(180deg, #1a0a2e 0%, #4a1936 50%, #802b40 100%);
        overflow: hidden;
        height: 100vh;
        width: 100vw;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Poppins', sans-serif;
    }

    /* --- ANIMATED BACKGROUND ELEMENTS --- */
    
    /* Shooting Stars */
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
        0% { transform: translate(100vw, 0vh) rotate(-45deg); opacity: 1; width: 2px; }
        20% { transform: translate(70vw, 30vh) rotate(-45deg); opacity: 0; width: 100px; }
        100% { transform: translate(70vw, 30vh) rotate(-45deg); opacity: 0; }
    }

    /* Cartoon Clouds */
    .cloud {
        position: absolute;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50px;
        width: 150px;
        height: 50px;
        animation: drift var(--d) linear infinite;
        z-index: -1;
    }
    .cloud::after, .cloud::before {
        content: '';
        position: absolute;
        background: inherit;
        border-radius: 50%;
    }
    .cloud::after { width: 70px; height: 70px; top: -30px; left: 20px; }
    .cloud::before { width: 50px; height: 50px; top: -20px; right: 20px; }

    @keyframes drift {
        from { left: -200px; }
        to { left: 110vw; }
    }

    /* Floating Cartoon Hearts */
    .floating-heart {
        position: absolute;
        font-size: 25px;
        animation: floatUp 8s ease-in infinite;
        opacity: 0.6;
        filter: drop-shadow(0 0 5px #ff4b4b);
    }
    @keyframes floatUp {
        0% { transform: translateY(110vh) scale(0.5); opacity: 0; }
        50% { opacity: 0.8; }
        100% { transform: translateY(-20vh) scale(1.2); opacity: 0; }
    }

    /* --- MAIN CARD STYLING --- */
    .card {
        background: rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(15px);
        padding: 40px 20px;
        border-radius: 40px;
        border: 2px solid rgba(255, 105, 180, 0.3);
        text-align: center;
        width: 85%;
        max-width: 380px;
        box-shadow: 0 0 40px rgba(255, 75, 75, 0.2);
        z-index: 10;
        position: relative;
    }

    h1 {
        font-family: 'Dancing Script', cursive;
        font-size: 2.8rem;
        margin-bottom: 20px;
        color: #fff;
        text-shadow: 0 0 15px #ff4b4b, 0 0 30px #ff4b4b;
    }

    .btn-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
        margin-top: 30px;
        min-height: 120px;
    }

    button {
        padding: 15px 40px;
        font-size: 1.3rem;
        border-radius: 50px;
        border: none;
        font-weight: 600;
        cursor: pointer;
        transition: 0.3s;
    }

    #yes-btn {
        background: #ff4b4b;
        color: white;
        box-shadow: 0 0 20px rgba(255, 75, 75, 0.6);
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.08); box-shadow: 0 0 30px rgba(255, 75, 75, 0.8); }
        100% { transform: scale(1); }
    }

    #no-btn {
        background: rgba(255, 255, 255, 0.1);
        color: #ccc;
        position: absolute; /* Needed for the runaway logic */
    }
</style>

<div id="bg-layer"></div>

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
    const bg = document.getElementById('bg-layer');

    // Add Clouds
    for(let i=0; i<5; i++){
        let cloud = document.createElement('div');
        cloud.className = 'cloud';
        cloud.style.top = (Math.random() * 80) + 'vh';
        cloud.style.setProperty('--d', (Math.random() * 20 + 20) + 's');
        cloud.style.opacity = Math.random() * 0.5;
        bg.appendChild(cloud);
    }

    // Add Floating Hearts
    setInterval(() => {
        let heart = document.createElement('div');
        heart.className = 'floating-heart';
        heart.innerHTML = ['❤️','💖','✨','🌸'][Math.floor(Math.random()*4)];
        heart.style.left = Math.random() * 100 + 'vw';
        bg.appendChild(heart);
        setTimeout(() => heart.remove(), 8000);
    }, 1000);

    // Add Shooting Stars
    setInterval(() => {
        let star = document.createElement('div');
        star.className = 'shooting-star';
        star.style.top = Math.random() * 50 + 'vh';
        bg.appendChild(star);
        setTimeout(() => star.remove(), 4000);
    }, 3000);

    let alertShown = false;
    function moveNo() {
        const btn = document.getElementById('no-btn');
        const x = Math.random() * (window.innerWidth - 100);
        const y = Math.random() * (window.innerHeight - 100);
        btn.style.left = x + 'px';
        btn.style.top = y + 'px';
        
        if (!alertShown) {
            alert("You probably wish there was a 'maybe' answer 😂😆");
            alertShown = true;
        }
    }

    function celebrate() {
        document.getElementById('main-card').innerHTML = `
            <div style="animation: fadeIn 2s;">
                <h1 style="font-size: 3.5rem;">YAY! ❤️</h1>
                <p style="font-size: 1.3rem; color: #fff;">I knew you'd say yes, Halima!</p>
                <div style="font-size: 5rem; margin: 20px 0;">🧸🎀💌</div>
                <p style="font-style: italic; opacity: 0.7;">Best. Valentine's. Ever.</p>
            </div>
        `;
        // Rapid fire hearts on success
        for(let i=0; i<50; i++) {
            setTimeout(() => {
                let h = document.createElement('div');
                h.className = 'floating-heart';
                h.innerHTML = '💖';
                h.style.left = Math.random() * 100 + 'vw';
                h.style.animationDuration = '3s';
                bg.appendChild(h);
            }, i * 50);
        }
    }
</script>
"""

components.html(custom_content, height=800)
