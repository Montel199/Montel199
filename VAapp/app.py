import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Halima", layout="centered")

custom_content = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap');

    * { cursor: none; -webkit-tap-highlight-color: transparent; } 

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

    /* Custom Cursor & Sparkle Trail */
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
    @keyframes fadeOut { to { opacity: 0; transform: scale(0.1); } }

    /* New: Touch Ripple Effect */
    .ripple {
        position: fixed;
        border: 2px solid #ff69b4;
        border-radius: 50%;
        pointer-events: none;
        animation: ripple-out 0.8s ease-out forwards;
        z-index: 9997;
    }
    @keyframes ripple-out {
        from { width: 0; height: 0; opacity: 0.5; }
        to { width: 150px; height: 150px; opacity: 0; }
    }

    /* Shooting Stars */
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

    /* Main Card Styled */
    .card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(25px);
        padding: 40px 20px;
        border-radius: 40px;
        border: 2px solid rgba(255, 105, 180, 0.4);
        box-shadow: 0 0 50px rgba(255, 20, 147, 0.3);
        text-align: center;
        width: 85%;
        max-width: 400px;
        z-index: 10;
        position: relative;
    }

    h1 {
        font-family: 'Dancing Script', cursive;
        font-size: 2.5rem;
        color: white;
        text-shadow: 0 0 15px #ff69b4;
    }

    #yes-btn {
        background: linear-gradient(45deg, #ff1493, #ff4b4b);
        color: white;
        padding: 15px 45px;
        border-radius: 50px;
        border: none;
        font-weight: bold;
        box-shadow: 0 10px 25px rgba(255, 20, 147, 0.5);
        animation: heartbeat 1.5s infinite;
        cursor: pointer;
    }
    @keyframes heartbeat { 0% { transform: scale(1); } 50% { transform: scale(1.08); } 100% { transform: scale(1); } }

    #no-btn {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        padding: 10px 30px;
        border-radius: 50px;
        border: 1px solid rgba(255,255,255,0.2);
        position: absolute;
        transition: 0.15s;
    }

    /* Side Drawer */
    #side-drawer {
        position: fixed;
        right: -100%;
        top: 0;
        width: 85%;
        height: 100%;
        background: linear-gradient(to bottom, #4a1936, #1a0a2e);
        z-index: 1000;
        transition: 0.6s cubic-bezier(0.19, 1, 0.22, 1);
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 30px;
        box-shadow: -15px 0 40px rgba(0,0,0,0.8);
        border-left: 2px solid #ff69b4;
    }
    #side-drawer.open { right: 0; }

    /* New: Polaroid Effect */
    .polaroid {
        position: fixed;
        width: 60px;
        height: 70px;
        background: white;
        padding: 5px;
        padding-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        animation: floatPolaroid 6s linear infinite;
        z-index: 5;
    }
    .polaroid div { width: 100%; height: 100%; background: #ff69b4; opacity: 0.3; }
    @keyframes floatPolaroid {
        from { transform: translateY(110vh) rotate(0deg); opacity: 1; }
        to { transform: translateY(-20vh) rotate(360deg); opacity: 0; }
    }

    .teddy { position: fixed; bottom: 20px; left: 20px; font-size: 80px; z-index: 100; animation: sway 3s infinite; }
    @keyframes sway { 0%, 100% { transform: rotate(-5deg); } 50% { transform: rotate(5deg); } }
</style>

<div id="cursor"></div>
<div id="bg-layer"></div>
<div class="teddy">🧸</div>

<div id="side-drawer">
    <div style="position:absolute; top:20px; left:20px; color:white; font-size:30px;" onclick="toggleDrawer()">×</div>
    <h1 style="font-size: 2.2rem; color:#ff69b4;">For My Wambooo... ❤️</h1>
    <p style="color: white; font-size: 1.1rem; line-height: 1.7;">
        "Every shooting star I've seen, I wished for someone like you. 
        Thank you for being my reality. You're not just my Valentine, 
        you're my favorite person in every universe." 🏹✨
    </p>
</div>

<div class="card" id="main-card">
    <div id="content">
        <p style="color: #ff69b4; font-size: 1.1rem; letter-spacing: 4px; font-weight: 300;">HEY BEAUTIFUL</p>
        <h1>Will you be my Valentine, Halima? 🌹</h1>
        <div style="height: 150px; position: relative; margin-top: 30px;">
            <button id="yes-btn" onclick="celebrate()">Yes!</button>
            <button id="no-btn" onmouseover="moveNo()" ontouchstart="moveNo()">No</button>
        </div>
    </div>
</div>

<script>
    const cursor = document.getElementById('cursor');
    
    // Trail & Ripple Logic
    document.addEventListener('mousemove', e => handleMove(e.clientX, e.clientY));
    document.addEventListener('touchstart', e => {
        const touch = e.touches[0];
        createRipple(touch.clientX, touch.clientY);
    });
    document.addEventListener('touchmove', e => {
        const touch = e.touches[0];
        handleMove(touch.clientX, touch.clientY);
    });

    function handleMove(x, y) {
        cursor.style.left = x + 'px';
        cursor.style.top = y + 'px';
        createSparkle(x, y);
    }

    function createSparkle(x, y) {
        const s = document.createElement('div');
        s.className = 'sparkle';
        s.style.left = x + 'px'; s.style.top = y + 'px';
        document.body.appendChild(s);
        setTimeout(() => s.remove(), 1000);
    }

    function createRipple(x, y) {
        const r = document.createElement('div');
        r.className = 'ripple';
        r.style.left = (x - 75) + 'px'; r.style.top = (y - 75) + 'px';
        document.body.appendChild(r);
        setTimeout(() => r.remove(), 8000);
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

    let noMessages = ["No", "Rethink! 🧐", "Oops! 🤭", "Close... 🤏", "Wait, what? 😂", "Try again! 🏃‍♀️"];
    let noCount = 0;

    function moveNo() {
        const btn = document.getElementById('no-btn');
        btn.style.position = 'fixed';
        btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
        btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        noCount++;
        btn.innerText = noMessages[noCount % noMessages.length];
    }

    function toggleDrawer() { document.getElementById('side-drawer').classList.toggle('open'); }

    function celebrate() {
        document.getElementById('main-card').innerHTML = `
            <div style="animation: fadeIn 1s;">
                <h1 style="font-size: 2rem;">Good choice baby! ❤️</h1>
                <p style="color: white; font-size: 1.1rem;">I am lucky to have you.</p>
                <div style="font-size: 4rem; margin: 10px 0;">💖✨💍</div>
                <hr style="border: 0; border-top: 1px solid #ff69b4; margin: 20px 0;">
                <p style="color: #ff69b4;">Guess nini Wambooo? 🤔</p>
                <button onclick="toggleDrawer()" style="background:#ff69b4; color:white; border:none; width:60px; height:60px; border-radius:50%; font-size:1.8rem; margin-top:10px; cursor:pointer; box-shadow: 0 0 20px #ff69b4;">?</button>
            </div>
        `;
        
        // Final Extra: Polaroid Wall & Hearts
        setInterval(() => {
            const h = document.createElement('div');
            h.innerHTML = Math.random() > 0.8 ? '📸' : '❤️';
            h.className = 'polaroid'; 
            h.style.left = Math.random() * 90 + 'vw';
            h.style.animationDuration = (Math.random() * 3 + 4) + 's';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 6000);
        }, 300);
    }
</script>
"""

components.html(custom_content, height=800)
