import streamlit as st
import pandas as pd

st.title("📊 プロジェクト課題仮説スコア診断（フェーズ0）")

# 入力画面
st.header("1. Hスコアを入力してください")

newness = st.selectbox("新規性", [0, 3, 5])
belief = st.selectbox("固定観念", [0, 3, 5])
spread = st.selectbox("波及性", [0, 3, 5])

# スコア計算
score_h = (newness * belief) + spread
st.write(f"👉 あなたの課題仮説スコア（H）は **{score_h} 点** です。")

# ベンチマーク比較
bench = pd.read_csv("benchmark_56.csv")  # 54社データ（H列含む）
rank = (bench["H"] < score_h).mean() * 100

# 判定ゾーン
if score_h <= 12:
    zone = "🔴 失敗ゾーン"
    advice = "課題の新規性が弱いです。隠れた真実を掘り起こしましょう。"
elif score_h <= 20:
    zone = "🟡 要注意ゾーン"
    advice = "課題は悪くないですが、固定観念の突破力が弱いです。業界慣習を見直しましょう。"
else:
    zone = "🟢 成功ゾーン"
    advice = "強い課題仮説です。次はMVPで顧客の声を取りに行きましょう。"

# 結果画面
st.header("2. 診断結果")
st.subheader(zone)
st.write(advice)
st.write(f"あなたのスコアは54社ベンチマークの **上位 {rank:.1f}%** に位置します。")

# 面談誘導
st.header("3. 次のアクション")
st.write("📩 詳細レポートをご希望の場合は、面談にてフィードバックいたします。")
