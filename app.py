import streamlit as st
import pandas as pd
from fuzzy_mamdani import evaluate_sleep_quality, build_visualization_figure, get_rule_base

st.set_page_config(page_title="SLEEPZY - Fuzzy Mamdani", layout="wide", page_icon="🌙")

def main():
    st.title("🌙 SLEEPZY: Sleep Quality Expert System")
    st.markdown("Sistem Pakar Logika Fuzzy Mamdani untuk Menentukan Kualitas Tidur Mahasiswa")

    tabs = st.tabs(["🏠 Beranda & Prediksi", "📊 Dataset Baris 1-10", "📑 Rule Base", "ℹ️ Informasi Sistem"])

    with tabs[0]:
        st.header("Prediksi Kualitas Tidur")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Input Variabel")
            duration = st.slider("Durasi Tidur (Jam)", 4.0, 9.0, 7.0, 0.1)
            activity = st.slider("Aktivitas Fisik (Menit)", 0, 120, 30, 1)
            caffeine = st.slider("Asupan Kafein (Cangkir)", 0.0, 5.0, 1.0, 0.1)
            
            if st.button("Analisis Kualitas Tidur"):
                score, sim = evaluate_sleep_quality(duration, activity, caffeine)
                
                st.metric("Skor Kualitas Tidur", f"{score:.2f}")
                
                if score <= 5:
                    st.error("Kualitas Tidur: BURUK")
                elif score <= 7:
                    st.warning("Kualitas Tidur: CUKUP")
                else:
                    st.success("Kualitas Tidur: BAIK")
                    
        with col2:
            st.subheader("Visualisasi Mamdani")
            fig = build_visualization_figure(duration, activity, caffeine)
            st.pyplot(fig)

    with tabs[1]:
        st.header("Dataset Baris 1-10")
        try:
            df = pd.read_csv("student_sleep_patterns.csv")
            df_subset = df.head(10).copy()
            
            results = []
            for _, row in df_subset.iterrows():
                score, _ = evaluate_sleep_quality(
                    float(row["Sleep_Duration"]), 
                    float(row["Physical_Activity"]), 
                    float(row["Caffeine_Intake"])
                )
                results.append(round(score, 2))
            
            df_subset["Prediksi_SPK"] = results
            st.dataframe(df_subset, use_container_width=True)
            
            st.divider()
            for i, (_, row) in enumerate(df_subset.iterrows()):
                st.write(f"**Data ID {i+1}**: Durasi={row['Sleep_Duration']}, Aktivitas={row['Physical_Activity']}, Kafein={row['Caffeine_Intake']} → Skor: {results[i]}")
                fig_single = build_visualization_figure(
                    float(row["Sleep_Duration"]), 
                    float(row["Physical_Activity"]), 
                    float(row["Caffeine_Intake"])
                )
                st.pyplot(fig_single)
                st.divider()
                
        except Exception as e:
            st.error(f"Gagal memuat dataset: {e}")

    with tabs[2]:
        st.header("Visualisasi 27 Rule Base")
        st.info("Mapping output (Buruk, Cukup, Baik) berdasarkan kombinasi input Durasi, Aktivitas, dan Kafein.")
        
        rules = get_rule_base()
        duration_map = {"pendek": 5.0, "sedang": 6.5, "panjang": 8.0}
        activity_map = {"rendah": 30.0, "sedang": 60.0, "tinggi": 100.0}
        caffeine_map = {"rendah": 1.0, "sedang": 2.5, "tinggi": 4.0}

        for i, rule in enumerate(rules, 1):
            with st.expander(f"Rule {i}: IF Durasi {rule['durasi'].upper()} AND Aktivitas {rule['aktivitas'].upper()} AND Kafein {rule['kafein'].upper()} THEN {rule['output'].upper()}"):
                d = duration_map[rule['durasi']]
                a = activity_map[rule['aktivitas']]
                c = caffeine_map[rule['kafein']]
                
                score, sim = evaluate_sleep_quality(d, a, c)
                st.write(f"Testing dengan nilai: Durasi={d}, Aktivitas={a}, Kafein={c} → **Skor SPK: {score:.2f}**")
                fig = build_visualization_figure(d, a, c, simulation=sim)
                st.pyplot(fig)

    with tabs[3]:
        st.header("ℹ️ Informasi Sistem Pakar")
        
        st.subheader("1. Deskripsi Proyek")
        st.markdown("""
        **SLEEPZY** adalah sistem pakar berbasis **Logika Fuzzy Mamdani** yang dirancang untuk menganalisis dan memprediksi kualitas tidur mahasiswa. 
        Sistem ini mempertimbangkan tiga faktor gaya hidup utama: durasi tidur, tingkat aktivitas fisik, dan konsumsi kafein.
        """)

        st.subheader("2. Variabel Input (Antecedents)")
        st.markdown("""
        - **Durasi Tidur (4.0 - 9.0 jam):**
            - *Pendek*: 4.0 - 6.5 jam (Trapesium)
            - *Sedang*: 5.0 - 8.0 jam (Segitiga, puncak di 6.5)
            - *Panjang*: 6.5 - 9.0 jam (Trapesium)
        - **Aktivitas Fisik (0 - 120 menit):**
            - *Rendah*: 0 - 60 menit (Trapesium)
            - *Sedang*: 30 - 90 menit (Segitiga, puncak di 60)
            - *Tinggi*: 60 - 120 menit (Trapesium)
        - **Asupan Kafein (0 - 5 cangkir):**
            - *Rendah*: 0 - 2.5 cangkir (Trapesium)
            - *Sedang*: 1.0 - 4.0 cangkir (Segitiga, puncak di 2.5)
            - *Tinggi*: 3.0 - 5.0 cangkir (Trapesium)
        """)

        st.subheader("3. Variabel Output (Consequent)")
        st.markdown("""
        - **Skor Kualitas Tidur (1 - 10):**
            - *BURUK*: Skor 1 - 5
            - *CUKUP*: Skor 3 - 7
            - *BAIK*: Skor 5 - 10
        """)

        st.subheader("4. Proses Logika Mamdani")
        st.info("""
        1. **Fuzzifikasi**: Mengubah input tegas (crisp) menjadi derajat keanggotaan fuzzy.
        2. **Inferensi**: Menerapkan 27 Rule Base (IF-THEN) menggunakan operator MIN (And).
        3. **Agregasi**: Menggabungkan seluruh hasil aturan menggunakan operator MAX.
        4. **Defuzzifikasi**: Menghitung titik tengah (Centroid) dari area fuzzy untuk menghasilkan skor kualitas tidur akhir.
        """)

        st.subheader("5. Sinkronisasi Data")
        st.success("""
        Sistem ini telah disinkronkan sepenuhnya dengan **Analisis Manual (Excel)**:
        - Jumlah Aturan: 27 Aturan.
        - Metode Output: 3 Kategori Utama (Buruk, Cukup, Baik).
        - Dataset: Berdasarkan 10 baris pertama dari `student_sleep_patterns.csv`.
        """)

if __name__ == "__main__":
    main()
