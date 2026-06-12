import streamlit as st
import time

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="PMB UPGRIS Chatbot",
    page_icon="🔴",
    layout="wide"
)

# --- 1.Splash Screen (UPGRIS Style) ---
if 'splash_done' not in st.session_state:
    st.session_state.splash_done = False

if not st.session_state.splash_done:
    # Menggunakan HTML & CSS untuk animasi splash screen resmi UPGRIS
    splash_placeholder = st.empty()
    with splash_placeholder.container():
        st.markdown(
            """
            <style>
            .splash-container {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                min-height: 80vh;
                height: auto;
                background-color: #0C2340; /* Latar belakang Biru Navy UPGRIS */
                font-family: 'Open Sans', sans-serif;
                border-radius: 15px;
                padding: 40px 20px;
                box-sizing: border-box;
                text-align: center;
            }
            .splash-logo-img {
                max-width: 150px; /* Ukuran maksimal logo image */
                width: 35%;       /* Responsif mengikuti lebar layar */
                height: auto;
                margin-bottom: 20px;
            }
            .upgris-logo {
                font-size: 65px;
                font-weight: 800;
                color: #FFFFFF; /* Teks Utama Putih */
                margin-bottom: 5px;
                letter-spacing: -1px;
                line-height: 1.2;
            }
            .upgris-dot {
                color: #E62129; /* Titik Merah khas Logo UPGRIS */
            }
            .subtitle {
                font-size: 20px;
                font-weight: 600;
                color: #FFC72C; /* Subtitle Kuning Emas */
                margin-bottom: 30px;
                letter-spacing: 2px;
            }
            .loader {
                border: 4px solid rgba(255, 255, 255, 0.2);
                border-top: 4px solid #FFC72C; /* Loader berputar Kuning Emas */
                border-radius: 50%;
                width: 45px;
                height: 45px;
                animation: spin 1s linear infinite;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            /* --- Responsive Media Queries --- */
            @media (max-width: 768px) {
                .upgris-logo {
                    font-size: 42px;
                }
                .subtitle {
                    font-size: 16px;
                    letter-spacing: 1px;
                    margin-bottom: 25px;
                }
                .splash-logo-img {
                    max-width: 110px;
                    width: 40%;
                }
                .loader {
                    width: 35px;
                    height: 35px;
                }
            }
            @media (max-width: 480px) {
                .upgris-logo {
                    font-size: 32px;
                }
                .subtitle {
                    font-size: 14px;
                }
                .splash-logo-img {
                    max-width: 90px;
                }
            }

            /* Menyembunyikan elemen bawaan Streamlit saat splash screen aktif */
            [data-testid="stHeader"] {display: none;}
            .stMainBlockContainer {padding-top: 0rem;}
            </style>
            <div class="splash-container">
                <img src="https://via.placeholder.com/150/FFC72C/0C2340?text=LOGO" class="splash-logo-img" alt="Logo UPGRIS">
                <div class="upgris-logo">PMB UPGRIS<span class="upgris-dot">.</span></div>
                <div class="subtitle">Mendidik Sepenuh Hati</div>
                <div class="loader"></div>
            </div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(2.5)  # Menampilkan splash screen selama 2.5 detik
        st.session_state.splash_done = True
        st.rerun()

# --- Custom CSS untuk Keseluruhan Sistem UI ---
st.markdown(
    """
    <style>
    /* ================= 1. CUSTOM TOP & APP HEADER ================= */
    /* Mengubah warna latar belakang bar menu kanan atas Streamlit */
    [data-testid="stHeader"] {
        background-color: #0C2340 !important;
    }
    /* Mengubah warna teks/ikon tombol menu di pojok kanan atas */
    [data-testid="stHeader"] button {
        color: #FFC72C !important;
    }
    /* Menghias running-line progress dekorator atas dengan warna Merah UPGRIS */
    [data-testid="stDecoration"] {
        background-image: linear-gradient(90deg, #E62129, #FFC72C) !important;
    }

    /* ================= 2. CUSTOM FOOTER SYSTEM ================= */
    .custom-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0C2340; /* Latar Navy */
        color: #FFFFFF; /* Teks Putih */
        text-align: center;
        padding: 8px 0;
        font-size: 13px;
        font-family: 'Open Sans', sans-serif;
        border-top: 3px solid #E62129; /* Garis pembatas Merah */
        z-index: 999;
    }
    .custom-footer span {
        color: #FFC72C; /* Highlight Kuning Emas */
        font-weight: bold;
    }
    /* Memberi jarak aman di paling bawah agar konten utama tidak tertutup footer tetap */
    .stMainBlockContainer {
        padding-bottom: 50px !important;
    }

    /* ================= 3. INTERNAL INTERACTIVE COMPONENTS ================= */
    /* Mengubah Tombol Utama & Hover Effect */
    div.stButton > button:first-child {
        background-color: #0C2340;
        color: #FFFFFF;
        border-radius: 8px;
        border: 2px solid #0C2340;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #E62129; /* Berubah Merah saat Hover */
        border-color: #E62129;
        color: white;
    }
    
    /* Mengubah Warna Custom State Box (Inaktif) */
    div[data-testid="stAlert"] {
        border-radius: 8px !important;
        background-color: #f0f4f8 !important;
        color: #0C2340 !important;
        border-left: 5px solid #0C2340 !important;
    }
    
    /* Mengubah Warna State Box yang Aktif (Override st.success) */
    div[data-testid="element-container"]:has(div.stAlert) .st-emotion-cache-12w0qpk {
        background-color: rgba(230, 33, 41, 0.1) !important;
        border-left: 5px solid #E62129 !important;
    }

    /* Logo di Batang Header Utama Aplikasi */
    .header-logo {
        font-size: 34px;
        font-weight: 800;
        color: #0C2340;
        letter-spacing: -1px;
        display: inline-block;
    }
    .header-dot {
        color: #E62129;
    }
    
    /* ================= MODIFIKASI CHAT INPUT (PROFESIONAL & MENARIK) ================= */
    /* Desain Container Utama Chat Input */
    div[data-testid="stChatInput"] {
        border: 2px solid #e0e0e0 !important;
        border-radius: 28px !important;
        padding: 4px 10px !important;
        background-color: #ffffff !important;
        box-shadow: 0 4px 15px rgba(12, 35, 64, 0.08) !important;
        transition: all 0.3s ease-in-out !important;
    }
    
    /* Efek Fokus saat Kolom Diklik (Warna Biru Navy UPGRIS & Glow Merah Lembut) */
    div[data-testid="stChatInput"]:focus-within {
        border-color: #0C2340 !important;
        box-shadow: 0 4px 18px rgba(230, 33, 41, 0.15), 0 0 0 3px rgba(12, 35, 64, 0.1) !important;
    }
    
    /* Pengaturan Area Ketik (Textarea) */
    div[data-testid="stChatInput"] textarea {
        color: #0C2340 !important;
        font-family: 'Open Sans', sans-serif !important;
        font-size: 15px !important;
    }
    
    /* Mengubah Warna Tombol Kirim (Ikon Panah) Menjadi Merah UPGRIS */
    div[data-testid="stChatInput"] button {
        background-color: #E62129 !important;
        color: #ffffff !important;
        border-radius: 50% !important;
        padding: 5px !important;
        transition: transform 0.2s ease, background-color 0.2s ease !important;
    }
    
    /* Efek Hover Pada Tombol Kirim */
    div[data-testid="stChatInput"] button:hover {
        background-color: #0C2340 !important;
        transform: scale(1.08);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Definisi Konten State (Q) ---
STATES = {
    'q0': { 
        'name': 'Menu Utama', 
        'text': "Halo! Selamat datang di **Layanan Informasi PMB UPGRIS Care**.\n\nSilakan pilih menu dengan mengetik angkanya:\n\n* 🔴 **[1]** Jadwal Pendaftaran\n* 🔴 **[2]** Syarat Dokumen\n* 🔴 **[3]** Kuota Jalur Penerimaan\n* 🔴 **[4]** Panduan Cara Daftar\n* ❌ **[9]** Akhiri Sesi" 
    },
    'q1': { 
        'name': 'Info Jadwal', 
        'text': "📅 **Jadwal Resmi PMB UPGRIS**\n- **Pendaftaran Online:** 1 - 10 Juli\n- **Verifikasi Berkas:** 2 - 12 Juli\n- **Pengumuman:** 15 Juli\n- **Daftar Ulang:** 16 - 18 Juli\n\nKetik **[0]** untuk kembali ke Menu Utama." 
    },
    'q2': { 
        'name': 'Info Syarat', 
        'text': "📄 **Syarat Dokumen PMB UPGRIS**\n1. Scan Kartu Keluarga asli\n2. Scan Akta Kelahiran\n3. Surat Keterangan Lulus (SKL)\n4. Pas Foto 3x4 background merah\n\nKetik **[0]** untuk kembali ke Menu Utama." 
    },
    'q3': { 
        'name': 'Info Kuota', 
        'text': "📊 **Kuota Jalur Penerimaan**\n- **Jalur Zonasi:** 50%\n- **Jalur Prestasi:** 30%\n- **Jalur Afirmasi:** 15%\n- **Jalur Pindah Tugas Ortu:** 5%\n\nKetik **[0]** untuk kembali ke Menu Utama." 
    },
    'q4': { 
        'name': 'Panduan', 
        'text': "💻 **Panduan Cara Daftar**\n1. Kunjungi website resmi PMB UPGRIS\n2. Klik 'Buat Akun' menggunakan NISN\n3. Isi biodata & pilih jalur\n4. Unggah dokumen persyaratan\n5. Cetak Bukti Pendaftaran\n\nKetik **[0]** untuk kembali ke Menu Utama." 
    },
    'q5': { 
        'name': 'Selesai (Final)', 
        'text': "Terima kasih telah menggunakan layanan Chatbot PMB UPGRIS. Semoga sukses dengan pendaftarannya!\n\n*(Sesi Berakhir. Ketik **'mulai'** jika ingin merestart chatbot)*" 
    }
}

# --- Inisialisasi Session State (Memory) ---
if 'current_state' not in st.session_state:
    st.session_state.current_state = 'q0'
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": STATES['q0']['text']}]
if 'transition_log' not in st.session_state:
    st.session_state.transition_log = [("System Start", "-", "q0")]

# --- Fungsi Logika Transisi DFA (δ) ---
def process_input(user_input):
    val = user_input.strip().lower()
    prev_state = st.session_state.current_state
    
    if prev_state == 'q5' and val == 'mulai':
        st.session_state.current_state = 'q0'
        return True, STATES['q0']['text'], prev_state, 'q0'
        
    if val == '0' and prev_state not in ['q0', 'q5']:
        st.session_state.current_state = 'q0'
        return True, STATES['q0']['text'], prev_state, 'q0'
        
    if prev_state == 'q0':
        if val == '1': next_state = 'q1'
        elif val == '2': next_state = 'q2'
        elif val == '3': next_state = 'q3'
        elif val == '4': next_state = 'q4'
        elif val == '9': next_state = 'q5'
        else:
            return False, "⚠️ Pilihan tidak tersedia. Harap masukkan nomor menu yang valid (1/2/3/4/9).", prev_state, prev_state
            
        st.session_state.current_state = next_state
        return True, STATES[next_state]['text'], prev_state, next_state
        
    elif prev_state in ['q1', 'q2', 'q3', 'q4']:
        return False, "💡 Anda sedang berada di dalam menu. Ketik **[0]** terlebih dahulu untuk kembali ke Menu Utama.", prev_state, prev_state
        
    elif prev_state == 'q5':
        return False, "Sesi Anda telah berakhir. Ketik **'mulai'** untuk mengaktifkan kembali mesin chatbot.", prev_state, prev_state

# --- UI Header Atas ---
col_logo, col_title = st.columns([1.5, 4])
with col_logo:
    st.markdown('<div class="header-logo">PMB UPGRIS<span class="header-dot">.</span></div>', unsafe_allow_html=True)
with col_title:
    st.caption("🔴 **PMB Care Chatbot Visualizer (Universitas PGRI Semarang)** — Berbasis Finite State Automata (DFA)")

st.markdown("---")

# --- Layout Utama (2 Kolom) ---
col1, col2 = st.columns([1.2, 1], gap="large")

# ================= KOLOM 1: INTERFACES CHAT =================
with col1:
    st.markdown("### 💬 Chatbot Otomata")
    
    chat_container = st.container(height=420)
    
    with chat_container:
        for msg in st.session_state.messages:
            if msg["role"] == "assistant":
                with st.chat_message("assistant", avatar="🔴"):
                    st.markdown(msg["content"])
            else:
                with st.chat_message("user"):
                    st.markdown(msg["content"])

    if prompt := st.chat_input("Ketik pilihan atau perintah di sini..."):
        with chat_container:
            with st.chat_message("user"):
                st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        is_valid, bot_reply, p_state, n_state = process_input(prompt)
        st.session_state.transition_log.insert(0, (p_state, prompt, n_state))
        
        time.sleep(0.4)  # Simulasi jeda mengetik chatbot
        with chat_container:
            with st.chat_message("assistant", avatar="🔴"):
                st.markdown(bot_reply)
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        
        st.rerun()

# ================= KOLOM 2: AUTOMATA VISUALIZATION =================
with col2:
    st.markdown("### ⚙️ ANALISIS PROSES DFA")
    
    # Detail Spesifikasi Formal Mesin
    with st.expander("📋 Detail Komponen Formal DFA (M)", expanded=False):
        st.code(
            "Q (Himpunan State) : {q0, q1, q2, q3, q4, q5}\n"
            "Σ (Input Alfabet)  : {'0', '1', '2', '3', '4', '9', 'mulai'}\n"
            "S (State Awal)     : q0\n"
            "F (State Akhir)    : {q5}\n"
            "δ (Fungsi Transisi): δ(Current_State, Input) = Next_State",
            language="text"
        )
        
    st.write("**Alur State Saat Ini:**")
    c_state = st.session_state.current_state
    
    # Visualisasi Grid Aktif / Inaktif
    grid1, grid2 = st.columns(2)
    with grid1:
        if c_state == 'q0': st.success("🔴 **q0 — Menu Utama (Aktif)**") 
        else: st.info("q0 — Menu Utama")
        
        if c_state == 'q2': st.success("🔴 **q2 — Info Syarat (Aktif)**") 
        else: st.info("q2 — Info Syarat")
        
        if c_state == 'q4': st.success("🔴 **q4 — Panduan Daftar (Aktif)**") 
        else: st.info("q4 — Panduan Daftar")
        
    with grid2:
        if c_state == 'q1': st.success("🔴 **q1 — Info Jadwal (Aktif)**") 
        else: st.info("q1 — Info Jadwal")
        
        if c_state == 'q3': st.success("🔴 **q3 — Info Kuota (Aktif)**") 
        else: st.info("q3 — Info Kuota")
        
        if c_state == 'q5':
            st.warning("🎯 **q5 — Selesai (Final State)**")
        else:
            st.text("q5 — Selesai (Final State)")

    # Log Terminal Fungsi Transisi
    st.write("**Log Fungsi Transisi ($\delta$):**")
    log_box = ""
    for p, i, n in st.session_state.transition_log:
        if p == "System Start":
            log_box += f"System Start → {n}\n"
        else:
            log_box += f"δ({p}, \"{i}\") → {n}\n"
            
    st.code(log_box, language="bash")

# ================= 4. INJEKSI ELEMEN FOOTER UTAMA =================
st.markdown(
    """
    <div class="custom-footer">
        © 2026 Universitas PGRI Semarang. 
        Powered by <span>DFA Driver Engine Engine Chatbot Visualizer</span>
    </div>
    """, 
    unsafe_allow_html=True
)
