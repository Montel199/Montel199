import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Halima", layout="centered")

# Added Feature 2 (Sparkle Trail) and Feature 3 (Talking No Button)
custom_content = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap');

    * { cursor: none; } 

    body {
        margin: 0;
        background: radial-gradient(circle at center, #2d0b1e 0%, #000000 100%);
        overflow: hidden;
        height: 100vh;
        width: 100vw;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Poppins', sans-serif;
    }

    #cursor {
        position: fixed;
        width: 15px;
        height: 15px;
        background: #ff69b4;
        border-radius: 50%;
        pointer-events: none;
        z-index: 9999;
        transform: translate(-50%, -50%);
        box-shadow: 0 0 20px #ff69b4, 0 0 40px #ff1493;
    }

    /* Feature 2: Sparkle Particles Style */
    .sparkle {
        position: fixed;
        width: 6px;
        height: 6px;
        background: #ff69b4;
        border-radius: 50%;
        pointer-events: none;
        z-index: 9998;
        animation: fadeOut 1s forwards;
    }
    @keyframes fadeOut {
        to { opacity: 0; transform: scale(0.1); }
    }

    /* --- BACKGROUND ELEMENTS --- */
    .shooting-star {
        position: absolute;
        width: 2px;
        height: 2px;
        background: white;
        box-shadow: 0 0 10px 2px white;
        animation: shoot 4s linear infinite;
    }
    @keyframes shoot {
        0% { transform: translate(100vw, -10vh) rotate(-45deg); opacity: 1; }
        20% { transform: translate(50vw, 40vh) rotate(-45deg); opacity: 0; }
        100% { opacity: 0; }
    }

    /* --- MAIN CARD --- */
    .card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        padding: 40px 20px;
        border-radius: 40px;
        border: 2px solid rgba(255, 105, 180, 0.4);
        box-shadow: 0 0 50px rgba(255, 20, 147, 0.3);
        text-align: center;
        width: 85%;
        max-width: 400px;
        z-index: 10;
        position: relative;
        transition: 0.5s;
    }

    h1 {
        font-family: 'Dancing Script', cursive;
        font-size: 2.5rem;
        color: white;
        text-shadow: 0 0 15px #ff69b4;
    }

    /* --- BUTTONS --- */
    #yes-btn {
        background: linear-gradient(45deg, #ff1493, #ff4b4b);
        color: white;
        padding: 15px 40px;
        border-radius: 50px;
        border: none;
        font-weight: bold;
        box-shadow: 0 10px 20px rgba(255, 20, 147, 0.4);
        animation: heartbeat 1.5s infinite;
        cursor: pointer;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    #no-btn {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        padding: 10px 30px;
        border-radius: 50px;
        border: 1px solid rgba(255,255,255,0.2);
        position: absolute;
        transition: 0.2s;
        white-space: nowrap;
    }

    /* --- SLIDE DRAWER --- */
    #side-drawer {
        position: fixed;
        right: -100%;
        top: 0;
        width: 80%;
        height: 100%;
        background: linear-gradient(to left, #ff1493, #4a1936);
        z-index: 1000;
        transition: 0.6s cubic-bezier(0.19, 1, 0.22, 1);
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 30px;
        box-shadow: -10px 0 30px rgba(0,0,0,0.5);
    }
    #side-drawer.open { right: 0; }

    .close-btn {
        position: absolute;
        top: 20px;
        left: 20px;
        font-size: 30px;
        color: white;
    }

    /* Teddy */
    .teddy { position: fixed; bottom: 20px; left: 20px; font-size: 80px; z-index: 100; animation: sway 3s infinite; }
    @keyframes sway { 0%, 100% { transform: rotate(-5deg); } 50% { transform: rotate(5deg); } }
</style>

<div id="cursor"></div>
<div id="bg-layer"></div>
<div class="teddy">🧸</div>

<div id="side-drawer">
    <div class="close-btn" onclick="toggleDrawer()">×</div>
    <h1 style="font-size: 2.5rem;">For My Wambooo... ❤️</h1>
    <p style="color: white; font-size: 1.2rem; line-height: 1.6;">
        "I just wanted to say that you're the most amazing part of my day. 
        I don't just want you for Valentine's, I want you for every day after that. 
        You're my forever choice." 🏹🌹
    </p>
</div>

<div class="card" id="main-card">
    <div id="content">
        <p style="color: #ff69b4; font-size: 1.2rem; letter-spacing: 2px;">HI BEAUTIFUL</p>
        <h1>Will you be my Valentine, Halima? 🌹</h1>
        <div style="height: 150px; position: relative; margin-top: 30px;">
            <button id="yes-btn" onclick="celebrate()">Yes!</button>
            <button id="no-btn" onmouseover="moveNo()" ontouchstart="moveNo()">No</button>
        </div>
    </div>
</div>

<script>
    const cursor = document.getElementById('cursor');
    
    // Feature 2: Sparkle Trail Logic
    document.addEventListener('mousemove', e => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
        createSparkle(e.clientX, e.clientY);
    });

    // Touch support for Sparkle Trail
    document.addEventListener('touchmove', e => {
        const touch = e.touches[0];
        cursor.style.left = touch.clientX + 'px';
        cursor.style.top = touch.clientY + 'px';
        createSparkle(touch.clientX, touch.clientY);
    });

    function createSparkle(x, y) {
        const sparkle = document.createElement('div');
        sparkle.className = 'sparkle';
        sparkle.style.left = x + 'px';
        sparkle.style.top = y + 'px';
        document.body.appendChild(sparkle);
        setTimeout(() => sparkle.remove(), 1000);
    }

    // Shooting Stars
    setInterval(() => {
        let s = document.createElement('div');
        s.className = 'shooting-star';
        s.style.left = Math.random() * 80 + 'vw';
        s.style.top = Math.random() * 40 + 'vh';
        document.getElementById('bg-layer').appendChild(s);
        setTimeout(() => s.remove(), 4000);
    }, 2000);

    // Feature 3: Talking No Button Logic
    let noMessages = ["No", "Are you sure? 🤨", "Wrong button! ❌", "Try again! 😂", "Halima pls... 🥺", "Nope! 🏃‍♂️"];
    let noCount = 0;

    function moveNo() {
        const btn = document.getElementById('no-btn');
        btn.style.position = 'fixed';
        btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
        btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        
        // Update button text
        noCount++;
        btn.innerText = noMessages[noCount % noMessages.length];
    }

    function toggleDrawer() {
        document.getElementById('side-drawer').classList.toggle('open');
    }

    function celebrate() {
        document.getElementById('main-card').innerHTML = `
            <div style="animation: fadeIn 1s;">
                <h1 style="font-size: 2.2rem;">Good choice baby! ❤️</h1>
                <p style="color: white; font-size: 1.1rem; margin-bottom: 20px;">I am so lucky to have you.</p>
                <div style="font-size: 4rem;">💖✨💍</div>
                <hr style="border: 0; border-top: 1px solid #ff69b4; margin: 20px 0;">
                <p style="color: #ff69b4;">Guess nini Wambooo? 🤔</p>
                <button onclick="toggleDrawer()" style="background:#ff69b4; color:white; border:none; width:50px; height:50px; border-radius:50%; font-size:1.5rem; margin-top:10px; cursor:pointer;">?</button>
            </div>
        `;
        
        // Celebration Hearts
        setInterval(() => {
            const h = document.createElement('div');
            h.innerHTML = '❤️';
            h.style.position = 'fixed';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.top = '110vh';
            h.style.fontSize = Math.random() * 20 + 10 + 'px';
            h.style.transition = '5s linear';
            h.style.color = '#ff1493';
            document.body.appendChild(h);
            setTimeout(() => { h.style.top = '-10vh'; }, 10);
            setTimeout(() => h.remove(), 5000);
        }, 150);
    }
</script>
"""

components.html(custom_content, height=800)
