import streamlit as st
import os

from parser import extract_text
from clause_extractor import extract_clauses
from risk_engine import detect_risk
from llm_helper import explain_clause
from report_generator import generate_pdf
from entity_extractor import extract_entities
from hindi_normalizer import normalize_hindi
from contract_classifier import classify_contract
from audit_logger import save_audit
from clause_analyzer import classify_clause_type

st.title("📄 AI Contract Risk Analysis Bot")
st.caption("Analyze contracts, detect risks, and simplify legal language")

uploaded_file = st.file_uploader("Upload Contract", type=["pdf", "docx", "txt"])

if uploaded_file:
    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = extract_text(file_path)
    text = normalize_hindi(text)

    contract_type = classify_contract(text)

    st.subheader("📌 Contract Type Detected")
    st.success(contract_type)

    clauses = extract_clauses(text)
    entities = extract_entities(text)

    st.subheader("🔍 Key Entities Found")
    st.write("**Parties:**", entities["Parties"])
    st.write("**Dates:**", entities["Dates"])
    st.write("**Money:**", entities["Money"])
    st.write("**Locations:**", entities["Locations"])

    st.subheader("📑 Clause Analysis")

    risk_counts = {"High": 0, "Medium": 0, "Low": 0}

    for clause in clauses:
        risk = detect_risk(clause)
        explanation = explain_clause(clause)
        clause_type = classify_clause_type(clause)

        risk_counts[risk] += 1

        st.write("----")
        st.write(f"**Clause:** {clause[:200]}...")
        st.write(f"**Clause Type:** {clause_type}")
        st.write(f"**Risk Level:** {risk}")

        if risk == "High":
            st.error(f"🔴 {explanation}")
        elif risk == "Medium":
            st.warning(f"🟡 {explanation}")
        else:
            st.success(f"🟢 {explanation}")

    st.subheader("📊 Overall Contract Risk Score")

    if risk_counts["High"] >= 2:
        overall = "HIGH"
        st.error("🔴 Overall Risk: HIGH")
    elif risk_counts["Medium"] >= 2:
        overall = "MEDIUM"
        st.warning("🟡 Overall Risk: MEDIUM")
    else:
        overall = "LOW"
        st.success("🟢 Overall Risk: LOW")

    save_audit(uploaded_file.name, overall)

    if st.button("📄 Download Report"):
        summary = [
            f"Contract Type: {contract_type}",
            f"High Risk Clauses: {risk_counts['High']}",
            f"Medium Risk Clauses: {risk_counts['Medium']}",
            f"Low Risk Clauses: {risk_counts['Low']}"
        ]
        generate_pdf(summary)
        st.success("Report Generated Successfully!")
