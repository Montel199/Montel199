import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Halima", layout="centered")

custom_content = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600&display=swap');

    * { cursor: none; -webkit-tap-highlight-color: transparent; user-select: none; } 

    body {
        margin: 0;
        /* Feature 1: Animated Mesh Gradient Background */
        background: linear-gradient(45deg, #0f0c29, #302b63, #24243e, #4a1936);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        overflow: hidden;
        height: 100vh;
        width: 100vw;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Poppins', sans-serif;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Custom Heart Cursor & Sparkle Trail */
    #cursor {
        position: fixed;
        width: 18px; height: 18px;
        background: #ff69b4;
        border-radius: 50%;
        pointer-events: none;
        z-index: 9999;
        transform: translate(-50%, -50%);
        box-shadow: 0 0 25px #ff69b4, 0 0 50px #ff1493;
    }

    .sparkle {
        position: fixed;
        width: 8px; height: 8px;
        background: rgba(255, 105, 180, 0.8);
        border-radius: 50%;
        pointer-events: none;
        z-index: 9998;
        animation: fadeOut 1.2s forwards;
    }
    @keyframes fadeOut { to { opacity: 0; transform: scale(0.2) translateY(-20px); } }

    /* Feature 2: Glassmorphism Card 3.0 */
    .card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(30px) saturate(150%);
        -webkit-backdrop-filter: blur(30px);
        padding: 50px 25px;
        border-radius: 50px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 25px 45px rgba(0,0,0,0.4), inset 0 0 15px rgba(255,255,255,0.1);
        text-align: center;
        width: 88%;
        max-width: 420px;
        z-index: 10;
        position: relative;
    }

    h1 {
        font-family: 'Dancing Script', cursive;
        font-size: 2.8rem;
        color: #fff;
        margin: 15px 0;
        text-shadow: 0 0 20px rgba(255, 105, 180, 0.8);
    }

    /* Neumorphic Buttons */
    #yes-btn {
        background: #ff1493;
        color: white;
        padding: 18px 50px;
        border-radius: 50px;
        border: none;
        font-weight: 600;
        font-size: 1.3rem;
        letter-spacing: 1px;
        box-shadow: 0 10px 30px rgba(255, 20, 147, 0.5);
        transition: 0.3s;
        animation: pulseHeart 2s infinite;
    }
    @keyframes pulseHeart {
        0%, 100% { transform: scale(1); box-shadow: 0 10px 30px rgba(255, 20, 147, 0.5); }
        50% { transform: scale(1.05); box-shadow: 0 15px 45px rgba(255, 20, 147, 0.7); }
    }

    #no-btn {
        background: rgba(255, 255, 255, 0.05);
        color: rgba(255,255,255,0.6);
        padding: 12px 35px;
        border-radius: 50px;
        border: 1px solid rgba(255,255,255,0.1);
        position: absolute;
    }

    /* Feature 3: Side Drawer Redesign */
    #side-drawer {
        position: fixed;
        right: -100%; top: 0;
        width: 90%; height: 100%;
        background: rgba(15, 12, 41, 0.95);
        backdrop-filter: blur(15px);
        z-index: 1000;
        transition: 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 40px;
        border-left: 3px solid #ff1493;
    }
    #side-drawer.open { right: 0; }

    .love-meter-container {
        position: fixed;
        top: 20px; left: 10%; width: 80%; height: 6px;
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        overflow: hidden;
        z-index: 100;
    }
    #love-meter-fill {
        height: 100%; width: 10%;
        background: linear-gradient(to right, #ff1493, #ff4b2b);
        transition: width 0.5s ease;
    }

    .teddy { position: fixed; bottom: 20px; left: 20px; font-size: 80px; z-index: 100; filter: drop-shadow(0 0 15px rgba(0,0,0,0.5)); }
</style>

<div class="love-meter-container"><div id="love-meter-fill"></div></div>
<div id="cursor"></div>
<div id="bg-layer"></div>
<div class="teddy">🧸</div>

<div id="side-drawer">
    <div style="position:absolute; top:30px; left:30px; color:#ff1493; font-size:40px;" onclick="toggleDrawer()">×</div>
    <h1 style="text-align:left; color:#ff1493;">My Wambooo... ❤️</h1>
    <p style="color: #fff; font-size: 1.2rem; line-height: 1.8; font-weight: 300;">
        You're the melody in my favorite song and the spark in my darkest nights. 
        Thank you for being exactly who you are. Halima, you have my whole heart, 
        today and every day after. ✨🌹
    </p>
</div>

<div class="card" id="main-card">
    <div id="content">
        <p style="color: #ff69b4; font-size: 0.9rem; letter-spacing: 5px; margin-bottom: 0;">PREMIUM COLLECTION</p>
        <h1>Be my Valentine, Halima?</h1>
        <div style="height: 180px; position: relative; margin-top: 40px; display: flex; align-items: center; justify-content: center;">
            <button id="yes-btn" onclick="celebrate()">YES, I WILL!</button>
            <button id="no-btn" onmouseover="moveNo()" ontouchstart="moveNo()">No</button>
        </div>
    </div>
</div>

<script>
    const cursor = document.getElementById('cursor');
    const meter = document.getElementById('love-meter-fill');
    let meterWidth = 10;

    // Movement & Ripple
    document.addEventListener('mousemove', e => handleInteraction(e.clientX, e.clientY));
    document.addEventListener('touchmove', e => {
        handleInteraction(e.touches[0].clientX, e.touches[0].clientY);
    });

    function handleInteraction(x, y) {
        cursor.style.left = x + 'px';
        cursor.style.top = y + 'px';
        createSparkle(x, y);
    }

    function createSparkle(x, y) {
        const s = document.createElement('div');
        s.className = 'sparkle';
        s.style.left = x + 'px'; s.style.top = y + 'px';
        document.body.appendChild(s);
        setTimeout(() => s.remove(), 1200);
    }

    let noMessages = ["No", "Error 404", "Try Again!", "Not an Option", "Nope!", "Haha No."];
    let noCount = 0;

    function moveNo() {
        const btn = document.getElementById('no-btn');
        btn.style.position = 'fixed';
        btn.style.left = Math.random() * (window.innerWidth - 120) + 'px';
        btn.style.top = Math.random() * (window.innerHeight - 60) + 'px';
        noCount++;
        btn.innerText = noMessages[noCount % noMessages.length];
        
        // Fill meter as she tries to click "No"
        if(meterWidth < 90) {
            meterWidth += 10;
            meter.style.width = meterWidth + '%';
        }
    }

    function toggleDrawer() { document.getElementById('side-drawer').classList.toggle('open'); }

    function celebrate() {
        meter.style.width = '100%';
        document.getElementById('main-card').innerHTML = `
            <div style="animation: fadeIn 1.2s cubic-bezier(0.4, 0, 0.2, 1);">
                <h1 style="font-size: 2.2rem; color: #ff1493;">GOOD CHOICE BABY! ❤️</h1>
                <p style="color: #fff; font-size: 1.1rem; opacity: 0.8;">I am the luckiest person alive.</p>
                <div style="font-size: 4.5rem; margin: 25px 0; filter: drop-shadow(0 0 15px #ff1493);">✨💍💖</div>
                <hr style="border: 0; border-top: 1px solid rgba(255,20,147,0.3); margin: 25px 0;">
                <p style="color: #ff69b4; font-weight: 600; letter-spacing: 2px;">GUESS NINI WAMBOOO? 🤔</p>
                <button onclick="toggleDrawer()" style="background:transparent; color:#ff1493; border: 2px solid #ff1493; width:70px; height:70px; border-radius:50%; font-size:2rem; margin-top:15px; cursor:pointer; transition: 0.4s;">?</button>
            </div>
        `;
        
        // Finale: Continuous Heart & Star Rain
        setInterval(() => {
            const h = document.createElement('div');
            h.innerHTML = ['❤️','✨','💖','🌸'][Math.floor(Math.random()*4)];
            h.style.position = 'fixed';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.top = '110vh';
            h.style.fontSize = Math.random() * 30 + 15 + 'px';
            h.style.transition = (Math.random() * 2 + 3) + 's ease-in';
            h.style.opacity = Math.random();
            document.body.appendChild(h);
            setTimeout(() => { h.style.top = '-10vh'; h.style.transform = `rotate(${Math.random()*360}deg)`; }, 50);
            setTimeout(() => h.remove(), 5000);
        }, 100);
    }
</script>
"""

components.html(custom_content, height=800)
