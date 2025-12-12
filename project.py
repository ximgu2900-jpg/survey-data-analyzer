# app.py
import streamlit as st
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# -----------------------------
# Language dictionary
# -----------------------------
TEXT = {
    "English": {
        "title": "Survey Data Analyzer",
        "sidebar_language": "Language / Bahasa",
        "sidebar_section": "Settings",
        "upload_label": "Upload survey data file (CSV or Excel)",
        "upload_help": "Upload the exported file from Google Forms (CSV or .xlsx).",
        "data_preview": "Data Preview",
        "select_numeric_cols": "Select numeric columns for descriptive analysis",
        "desc_header": "Descriptive Statistics",
        "assoc_header": "Association Analysis (Correlation)",
        "no_file": "Please upload your survey data file to start.",
        "select_x": "Select variable for X (Independent Variable)",
        "select_y": "Select variable for Y (Dependent Variable)",
        "select_method": "Select correlation method",
        "method_pearson": "Pearson (for normally distributed numeric data)",
        "method_spearman": "Spearman (for non-normal / ordinal data)",
        "run_analysis": "Run Correlation Analysis",
        "result_corr": "Correlation Result",
        "r_label": "Correlation coefficient (r)",
        "p_label": "p-value",
        "interp_header": "Interpretation",
        "strength": "Strength:",
        "direction": "Direction:",
        "sig": "Significance:",
        "strong": "Strong",
        "moderate": "Moderate",
        "weak": "Weak",
        "none": "Very weak or none",
        "positive": "Positive (when X increases, Y tends to increase)",
        "negative": "Negative (when X increases, Y tends to decrease)",
        "not_sig": "Not significant at α = 0.05",
        "sig_05": "Significant at α = 0.05",
        "sig_01": "Highly significant at α = 0.01",
        "freq_header": "Frequency Table (example for selected item)",
        "select_for_freq": "Select one column for frequency table",

        "features_title": "Main Features",
        "card1_title": "Descriptive Analysis",
        "card1_desc": "Summary statistics and basic visualizations of your survey data.",
        "card2_title": "Visual Charts",
        "card2_desc": "Bar charts and histograms to understand the data better.",
        "card3_title": "Correlation Analysis",
        "card3_desc": "Find relationships between variables using correlation tests.",

        "footer_note": "This web app was built using Streamlit for a Statistics I assignment (Group 11, Class 1).",
    },
    "Bahasa Indonesia": {
        "title": "Analisis Data Survei",
        "sidebar_language": "Bahasa / Language",
        "sidebar_section": "Pengaturan",
        "upload_label": "Unggah file data survei (CSV atau Excel)",
        "upload_help": "Unggah file hasil ekspor dari Google Forms (CSV atau .xlsx).",
        "data_preview": "Pratinjau Data",
        "select_numeric_cols": "Pilih kolom numerik untuk analisis deskriptif",
        "desc_header": "Statistika Deskriptif",
        "assoc_header": "Analisis Asosiasi (Korelasi)",
        "no_file": "Silakan unggah file data survei terlebih dahulu.",
        "select_x": "Pilih variabel X (Variabel Bebas)",
        "select_y": "Pilih variabel Y (Variabel Terikat)",
        "select_method": "Pilih metode korelasi",
        "method_pearson": "Pearson (untuk data numerik berdistribusi normal)",
        "method_spearman": "Spearman (untuk data tidak normal / ordinal)",
        "run_analysis": "Jalankan Analisis Korelasi",
        "result_corr": "Hasil Korelasi",
        "r_label": "Koefisien korelasi (r)",
        "p_label": "p-value",
        "interp_header": "Interpretasi",
        "strength": "Kekuatan:",
        "direction": "Arah:",
        "sig": "Signifikansi:",
        "strong": "Kuat",
        "moderate": "Sedang",
        "weak": "Lemah",
        "none": "Sangat lemah atau tidak ada",
        "positive": "Positif (saat X naik, Y cenderung naik)",
        "negative": "Negatif (saat X naik, Y cenderung turun)",
        "not_sig": "Tidak signifikan pada α = 0.05",
        "sig_05": "Signifikan pada α = 0.05",
        "sig_01": "Sangat signifikan pada α = 0.01",
        "freq_header": "Tabel Frekuensi (contoh untuk satu item)",
        "select_for_freq": "Pilih satu kolom untuk tabel frekuensi",

        "features_title": "Fitur Utama",
        "card1_title": "Analisis Deskriptif",
        "card1_desc": "Ringkasan statistik lengkap dan visualisasi data survei Anda.",
        "card2_title": "Grafik Visual",
        "card2_desc": "Grafik batang dan histogram untuk pemahaman data yang lebih baik.",
        "card3_title": "Analisis Korelasi",
        "card3_desc": "Temukan hubungan antar variabel dengan uji korelasi.",

        "footer_note": "Aplikasi ini dibuat dengan Streamlit untuk tugas Statistik I (Kelompok 11, Kelas 1).",
    },
    "Chinese": {
        "title": "调查数据分析器",
        "upload_label": "上传调查数据文件（CSV 或 Excel）",
        "upload_help": "上传从 Google Forms 导出的文件。",
        "no_file": "请先上传调查数据文件。",
        "desc_header": "描述性统计",
        "assoc_header": "关联分析（相关性）",
        "select_x": "选择 X 变量（自变量）",
        "select_y": "选择 Y 变量（因变量）",
        "select_method": "选择相关方法",
        "method_pearson": "皮尔逊相关（正态分布）",
        "method_spearman": "斯皮尔曼相关（非正态）",
        "run_analysis": "运行相关分析",
        "result_corr": "相关结果",
        "r_label": "相关系数 (r)",
        "p_label": "p 值",
        "interp_header": "解释",
        "strong": "强",
        "moderate": "中等",
        "weak": "弱",
        "none": "非常弱或无",
        "positive": "正相关",
        "negative": "负相关",
        "not_sig": "不显著 (α = 0.05)",
        "sig_05": "显著 (α = 0.05)",
        "sig_01": "高度显著 (α = 0.01)",

        "features_title": "主要功能",
        "card1_title": "描述性分析",
        "card1_desc": "提供完整的统计摘要与基础数据可视化。",
        "card2_title": "可视化图表",
        "card2_desc": "柱状图与直方图帮助你更好理解数据。",
        "card3_title": "相关性分析",
        "card3_desc": "使用相关检验来发现变量之间的关系。",

        "footer_note": "使用 Streamlit 构建，用于统计学作业。"
    },

    "Portuguese": {
        "title": "Analisador de Dados de Pesquisa",
        "upload_label": "Enviar arquivo de dados (CSV ou Excel)",
        "upload_help": "Envie o arquivo exportado do Google Forms.",
        "no_file": "Por favor, envie o arquivo de dados para iniciar.",
        "desc_header": "Estatísticas Descritivas",
        "assoc_header": "Análise de Associação (Correlação)",
        "select_x": "Selecione a variável X (Independente)",
        "select_y": "Selecione a variável Y (Dependente)",
        "select_method": "Selecione o método de correlação",
        "method_pearson": "Pearson (dados normais)",
        "method_spearman": "Spearman (dados não normais)",
        "run_analysis": "Executar Análise",
        "result_corr": "Resultado da Correlação",
        "r_label": "Coeficiente de correlação (r)",
        "p_label": "Valor p",
        "interp_header": "Interpretação",
        "strong": "Forte",
        "moderate": "Moderada",
        "weak": "Fraca",
        "none": "Muito fraca ou inexistente",
        "positive": "Positiva",
        "negative": "Negativa",
        "not_sig": "Não significativo (α = 0.05)",
        "sig_05": "Significativo (α = 0.05)",
        "sig_01": "Altamente significativo (α = 0.01)",

        "features_title": "Principais Recursos",
        "card1_title": "Análise Descritiva",
        "card1_desc": "Resumo estatístico completo com visualizações básicas.",
        "card2_title": "Gráficos Visuais",
        "card2_desc": "Gráficos de barras e histogramas para entender melhor os dados.",
        "card3_title": "Análise de Correlação",
        "card3_desc": "Encontre relações entre variáveis usando testes de correlação.",

        "footer_note": "Criado com Streamlit para a disciplina de Estatística."
    }
}

# -----------------------------
# Helper functions
# -----------------------------
def interpret_strength(r, lang):
    ar = abs(r)
    if ar >= 0.7:
        return TEXT[lang]["strong"]
    elif ar >= 0.4:
        return TEXT[lang]["moderate"]
    elif ar >= 0.2:
        return TEXT[lang]["weak"]
    else:
        return TEXT[lang]["none"]

def interpret_significance(p, lang):
    if p < 0.01:
        return TEXT[lang]["sig_01"]
    elif p < 0.05:
        return TEXT[lang]["sig_05"]
    else:
        return TEXT[lang]["not_sig"]

# -----------------------------
# Streamlit layout (Beautiful UI)
# -----------------------------
st.set_page_config(page_title="Survey Data Analyzer", layout="wide")

# --- CSS Background + Card ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1557683316-973673baf926?auto=format&fit=crop&w=1600&q=80&v=8");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .block-container { padding-top: 2.5rem; max-width: 1100px; }

    .hero-card {
        background: rgba(255,255,255,0.92);
        border-radius: 28px;
        padding: 44px 40px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.12);
        margin: 18px 0 28px 0;
        text-align: center;
    }
    .hero-title {
        font-size: 56px;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 10px;
    }
    .hero-subtitle {
        font-size: 18px;
        opacity: 0.8;
        margin-top: 6px;
    }

    section[data-testid="stFileUploaderDropzone"] {
        background: rgba(255,255,255,0.92);
        border: 2px dashed #9aa5b1;
        border-radius: 18px;
        padding: 18px;
    }
    .stButton button {
        border-radius: 14px !important;
        padding: 10px 16px !important;
        font-weight: 700 !important;
    }
    header[data-testid="stHeader"] { background: rgba(0,0,0,0); }

    /* ===== Feature Section ===== */
    .feature-wrap{
    background: rgba(255,255,255,0.90);
    border-radius: 26px;
    padding: 28px 26px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.12);
    margin: 18px 0 18px 0;
    }

    .cards-grid{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin-bottom: 12px;
    }

    .card-box{
    background: rgba(255,255,255,0.95);
    border-radius: 22px;
    padding: 22px 20px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.10);
    min-height: 180px;
    }

    .card-emoji{
    font-size: 34px;
    margin-bottom: 8px;
    }

    .card-title{
    font-size: 22px;
    font-weight: 800;
    margin: 0 0 6px 0;
    }

    .card-desc{
    font-size: 15px;
    opacity: 0.8;
    margin: 0;
    line-height: 1.4;
    }

    @media (max-width: 900px){
    .cards-grid{ grid-template-columns: 1fr; }
    }
    </style>
  
    """,
    unsafe_allow_html=True
)

# --- Language buttons (no sidebar) ---
if "lang" not in st.session_state:
    st.session_state["lang"] = "English"

c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
with c1:
    if st.button("🇮🇩 Bahasa Indonesia", use_container_width=True):
        st.session_state["lang"] = "Bahasa Indonesia"
with c2:
    if st.button("🇬🇧 English", use_container_width=True):
        st.session_state["lang"] = "English"
with c3:
    if st.button("🇨🇳 中文", use_container_width=True):
        st.session_state["lang"] = "Chinese"
with c4:
    if st.button("🇵🇹 Português", use_container_width=True):
        st.session_state["lang"] = "Portuguese"

lang = st.session_state["lang"]
t = TEXT[lang]

# --- Hero card ---
subtitle = "Unggah file Excel/CSV untuk memulai analisis" if lang == "Bahasa Indonesia" else "Upload your Excel/CSV file to start the analysis"
st.markdown(
    f"""
    <div class="hero-card">
        <div class="hero-title">{t["title"]}</div>
        <div class="hero-subtitle">{subtitle}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Feature section (Front page) ---
st.markdown(
    f"""
    <div class="feature-wrap">
      <h2>✨ {t["features_title"]}</h2>
    </div>

    <div class="cards-grid">
      <div class="card-box">
        <div class="card-emoji">📈</div>
        <div class="card-title">{t["card1_title"]}</div>
        <p class="card-desc">{t["card1_desc"]}</p>
      </div>

      <div class="card-box">
        <div class="card-emoji">📊</div>
        <div class="card-title">{t["card2_title"]}</div>
        <p class="card-desc">{t["card2_desc"]}</p>
      </div>

      <div class="card-box">
        <div class="card-emoji">🔗</div>
        <div class="card-title">{t["card3_title"]}</div>
        <p class="card-desc">{t["card3_desc"]}</p>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)


uploaded_file = st.file_uploader(t["upload_label"], type=["csv", "xlsx"], help=t["upload_help"])

if uploaded_file is None:
    st.info(t["no_file"])
    st.write(t["footer_note"])
else:
    # Read data
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    df['X_total'] = df[['X1','X2','X3','X4','X5']].sum(axis=1)
    df['Y_total'] = df[['Y1','Y2','Y3','Y4','Y5']].sum(axis=1)


    st.subheader(t["data_preview"])
    st.dataframe(df.head())

    # Detect numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if len(numeric_cols) == 0:
        st.warning("No numeric columns detected. Please check your file.")
    else:
        # -----------------------------
        # Descriptive Statistics
        # -----------------------------
        st.subheader(t["desc_header"])
        selected_desc_cols = st.multiselect(t["select_numeric_cols"], numeric_cols, default=numeric_cols)

        if selected_desc_cols:
            desc = df[selected_desc_cols].describe().T  # transpose for better view
            st.dataframe(desc)
            # ---------- Charts for Descriptive Statistics ----------
            st.markdown("### 📊 Charts (Composite Scores)")

            cA, cB = st.columns(2)

            with cA:
                st.write("Histogram: X_total")
                fig, ax = plt.subplots()
                ax.hist(df["X_total"].dropna(), bins=10)
                ax.set_xlabel("X_total")
                ax.set_ylabel("Frequency")
                st.pyplot(fig)

            with cB:
                st.write("Histogram: Y_total")
                fig, ax = plt.subplots()
                ax.hist(df["Y_total"].dropna(), bins=10)
                ax.set_xlabel("Y_total")
                ax.set_ylabel("Frequency")
                st.pyplot(fig)

            cC, cD = st.columns(2)

            with cC:
                st.write("Boxplot: X_total")
                fig, ax = plt.subplots()
                ax.boxplot(df["X_total"].dropna(), vert=True)
                ax.set_ylabel("X_total")
                st.pyplot(fig)

            with cD:
                st.write("Boxplot: Y_total")
                fig, ax = plt.subplots()
                ax.boxplot(df["Y_total"].dropna(), vert=True)
                ax.set_ylabel("Y_total")
                st.pyplot(fig)


            # Frequency table for one selected item
            st.markdown(f"### {t['freq_header']}")
            freq_col = st.selectbox(t["select_for_freq"], selected_desc_cols)
            freq_table = df[freq_col].value_counts().sort_index()
            st.write(freq_table)

        # -----------------------------
        # Association Analysis
        # -----------------------------
        st.subheader(t["assoc_header"])
        col1, col2, col3 = st.columns(3)

        with col1:
            x_var = st.selectbox(t["select_x"], numeric_cols)
        with col2:
            y_var = st.selectbox(t["select_y"], numeric_cols)
        with col3:
            method = st.selectbox(
                t["select_method"],
                [t["method_pearson"], t["method_spearman"]]
            )

        if st.button(t["run_analysis"]):
            # Drop NA for selected columns
            data = df[[x_var, y_var]].dropna()

            if t["method_pearson"] in method:
                r, p = stats.pearsonr(data[x_var], data[y_var])
            else:
                r, p = stats.spearmanr(data[x_var], data[y_var])

            st.markdown(f"### {t['result_corr']}")
            st.write(f"{t['r_label']}: {r:.3f}")
            st.write(f"{t['p_label']}: {p:.5f}")

            # ---------- Scatter Plot for Correlation ----------
            st.markdown("### 📈 Scatter Plot")

            fig, ax = plt.subplots()
            ax.scatter(data[x_var], data[y_var])
            ax.set_xlabel(x_var)
            ax.set_ylabel(y_var)
            ax.set_title(f"{x_var} vs {y_var}")
            st.pyplot(fig)


            strength = interpret_strength(r, lang)
            direction = t["positive"] if r > 0 else (t["negative"] if r < 0 else t["none"])
            sig_text = interpret_significance(p, lang)

            st.markdown(f"### {t['interp_header']}")
            st.write(f"- {t['strength']} {strength}")
            st.write(f"- {t['direction']} {direction}")
            st.write(f"- {t['sig']} {sig_text}")

    st.write("---")
    st.write(t["footer_note"])
