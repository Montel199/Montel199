import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Halima", layout="centered")

# Final Polish: Custom Cursor, Typewriter Effect, and Interactive Teddy
custom_content = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap');

    * { cursor: none; } /* We will create a custom heart cursor */

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

    /* --- CUSTOM HEART CURSOR --- */
    #cursor {
        position: fixed;
        width: 20px;
        height: 20px;
        background: #ff69b4;
        border-radius: 50%;
        pointer-events: none;
        z-index: 9999;
        transform: translate(-50%, -50%);
        box-shadow: 0 0 15px #ff69b4;
    }

    /* --- BACKGROUND ELEMENTS --- */
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
        0% { transform: translate(100vw, -10vh) rotate(-45deg); opacity: 1; }
        20% { transform: translate(50vw, 40vh) rotate(-45deg); opacity: 0; }
        100% { opacity: 0; }
    }

    /* --- TEDDY WITH SPEECH BUBBLE --- */
    .teddy-container {
        position: fixed;
        bottom: 20px;
        left: 20px;
        z-index: 100;
    }
    .teddy {
        font-size: 80px;
        animation: sway 3s ease-in-out infinite;
    }
    .bubble {
        position: absolute;
        top: -40px;
        left: 60px;
        background: white;
        color: #333;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 12px;
        font-weight: bold;
        white-space: nowrap;
        opacity: 0;
        animation: fadeInOut 5s infinite;
    }
    @keyframes fadeInOut { 0%, 100% { opacity: 0; } 50% { opacity: 1; } }

    /* --- MAIN CARD --- */
    .card {
        background: rgba(20, 20, 20, 0.85);
        padding: 40px 20px;
        border-radius: 30px;
        border: 3px solid #ff69b4;
        box-shadow: 0 0 30px #ff69b4;
        text-align: center;
        width: 85%;
        max-width: 380px;
        z-index: 10;
        position: relative;
    }

    /* Typewriter Effect */
    .typewriter h1 {
        overflow: hidden;
        border-right: .15em solid #ff69b4;
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: .10em;
        animation: typing 3.5s steps(30, end), blink-caret .5s step-end infinite;
        font-family: 'Dancing Script', cursive;
        color: white;
    }
    @keyframes typing { from { width: 0 } to { width: 100% } }
    @keyframes blink-caret { from, to { border-color: transparent } 50% { border-color: #ff69b4 } }

    button {
        width: 180px;
        padding: 12px;
        font-size: 1.2rem;
        border-radius: 25px;
        border: none;
        font-weight: 600;
        transition: 0.3s;
    }

    #yes-btn {
        background: #ff4b4b;
        color: white;
        box-shadow: 0 0 20px #ff4b4b;
        margin-top: 20px;
    }

    #no-btn {
        background: #444;
        color: #888;
        position: absolute;
    }
</style>

<div id="cursor"></div>
<div id="bg-layer"></div>

<div class="teddy-container">
    <div class="bubble" id="teddy-talk">Click Yes! 🐾</div>
    <div class="teddy">🧸</div>
</div>

<div class="card" id="main-card">
    <div class="typewriter">
        <p style="color: #ff69b4; font-size: 1.2rem;">Hello beautiful...</p>
        <h1>Will you be mine?</h1>
    </div>
    <div style="margin-top:20px; font-family: 'Dancing Script'; font-size: 2rem; color: #ff69b4;">Halima 🌹</div>
    
    <div class="btn-container" style="height: 150px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <button id="yes-btn" onclick="celebrate()">Yes!</button>
        <button id="no-btn" onmouseover="moveNo()" ontouchstart="moveNo()">No</button>
    </div>
</div>

<script>
    // Cursor Movement
    const cursor = document.getElementById('cursor');
    document.addEventListener('mousemove', e => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
    });

    // Shooting Stars
    setInterval(() => {
        let s = document.createElement('div');
        s.className = 'shooting-star';
        s.style.left = Math.random() * 80 + 'vw';
        s.style.top = Math.random() * 40 + 'vh';
        document.getElementById('bg-layer').appendChild(s);
        setTimeout(() => s.remove(), 4000);
    }, 2500);

    let noCount = 0;
    function moveNo() {
        noCount++;
        const btn = document.getElementById('no-btn');
        btn.style.position = 'fixed';
        btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
        btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        
        const teddyTalk = document.getElementById('teddy-talk');
        if(noCount == 1) alert("You probably wish there was a 'maybe' answer 😂😆");
        if(noCount == 3) teddyTalk.innerText = "Hey! Stop that! 😡";
        if(noCount == 5) teddyTalk.innerText = "Just click YES already! 🙄";
    }

    function celebrate() {
        document.getElementById('main-card').innerHTML = `
            <div style="animation: fadeIn 1.5s;">
                <h1 style="font-family: 'Dancing Script'; font-size: 3.5rem; color: #ff69b4;">YAYYY! ❤️</h1>
                <p style="color: white; font-size: 1.2rem;">You just made my year, Halima!</p>
                <div style="font-size: 5rem; margin: 15px 0;">💖🌹✨</div>
                <p style="color: #ff69b4; font-weight: bold;">See you on the 14th! 🏹</p>
            </div>
        `;
        // Background Heart Explosion
        setInterval(() => {
            const h = document.createElement('div');
            h.innerHTML = '❤️';
            h.style.position = 'fixed';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.top = '110vh';
            h.style.fontSize = Math.random() * 30 + 10 + 'px';
            h.style.transition = '5s linear';
            document.body.appendChild(h);
            setTimeout(() => {
                h.style.top = '-10vh';
                h.style.left = (parseFloat(h.style.left) + (Math.random()*20 - 10)) + 'vw';
            }, 10);
            setTimeout(() => h.remove(), 5000);
        }, 100);
    }
</script>
"""

components.html(custom_content, height=800)
