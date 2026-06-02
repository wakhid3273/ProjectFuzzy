from __future__ import annotations

import streamlit as st

from fuzzy_mamdani import build_visualization_figure, evaluate_sleep_quality, get_rule_base


def get_rule_base_inputs() -> list[dict]:
    """Generate input values untuk setiap rule base"""
    # Mapping untuk setiap kategori fuzzy ke nilai crips
    duration_map = {"pendek": 5.0, "sedang": 6.5, "panjang": 8.0}
    activity_map = {"rendah": 30.0, "sedang": 60.0, "tinggi": 100.0}
    caffeine_map = {"rendah": 1.0, "sedang": 2.5, "tinggi": 4.0}
    
    inputs = []
    for i, rule in enumerate(get_rule_base(), 1):
        inputs.append({
            "rule_number": i,
            "durasi_tidur": duration_map[rule["durasi"]],
            "aktivitas_fisik": activity_map[rule["aktivitas"]],
            "kafein": caffeine_map[rule["kafein"]],
            "rule": rule,
        })
    return inputs


def main() -> None:
    st.set_page_config(page_title="SLEEPZY", page_icon="💤", layout="wide")

    st.title("SLEEPZY")
    st.caption("Visualisasi Fuzzy Mamdani untuk 27 Rule Base")

    rule_inputs = get_rule_base_inputs()

    st.subheader("Grafik Hasil 27 Rule Base Fuzzy")
    
    for row_start in range(0, len(rule_inputs), 2):
        left_column, right_column = st.columns(2)
        for offset, column in enumerate((left_column, right_column)):
            idx = row_start + offset
            if idx >= len(rule_inputs):
                continue

            rule_data = rule_inputs[idx]
            hasil, simulation = evaluate_sleep_quality(
                rule_data["durasi_tidur"],
                rule_data["aktivitas_fisik"],
                rule_data["kafein"],
            )

            with column:
                st.markdown(
                    f"**R{rule_data['rule_number']}**  \n"
                    f"Durasi: {rule_data['durasi_tidur']} jam | Aktivitas: {rule_data['aktivitas_fisik']} | "
                    f"Kafein: {rule_data['kafein']} | Hasil: {hasil:.2f} / 10  \n"
                    f"Expected Output: {rule_data['rule']['output'].replace('_', ' ').title()}"
                )

                figure = build_visualization_figure(
                    rule_data["durasi_tidur"],
                    rule_data["aktivitas_fisik"],
                    rule_data["kafein"],
                    simulation,
                )
                st.pyplot(figure, clear_figure=True, width='stretch')


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()