# 📄 Contract Analysis & Risk Assessment Bot

## 🚀 Overview
The **Contract Analysis & Risk Assessment Bot** is a GenAI-powered legal assistant designed to help small and medium business owners understand complex contracts, identify legal risks, and make informed decisions.

This system analyzes contracts, extracts key clauses, detects potential risks, and provides simplified explanations in plain business language. It supports multilingual contracts (**English and Hindi**) and generates summary reports for legal consultation.

---

## 🎯 Problem Statement
Small and medium enterprises often struggle to understand complex legal contracts that may contain hidden risks, penalties, or unfavorable terms. This project provides an AI-driven solution that simplifies contract review and improves decision-making.

---

## ✨ Key Features

### 📑 Clause Extraction
- Automatically divides contracts into individual clauses
- Supports PDF, DOCX, and TXT formats

### ⚠️ Risk Detection
Identifies high-risk clauses including:
- Penalty clauses
- Indemnity clauses
- Non-compete agreements
- Termination conditions
- Unlimited liability
- Intellectual property transfer
- Auto-renewal terms

### 🧠 Clause Classification
Each clause is classified as:
- **Obligation**
- **Right**
- **Prohibition**
- **General**

### 🔍 Named Entity Recognition
Extracts:
- Parties involved
- Dates
- Financial amounts
- Jurisdiction and locations

### 🌐 Multilingual Support
- Handles English and Hindi contracts
- Hindi legal terms are normalized into English for accurate analysis

### 📊 Risk Scoring
- Clause-level risk: **Low / Medium / High**
- Overall contract risk summary

### 📄 Report Generation
- PDF export of risk summary
- Clause explanations
- Audit logging

---

## 🛠️ Technology Stack
- **Python**
- **Streamlit** – User Interface
- **spaCy** – NLP processing
- **Regex-based rule engine** – Clause and entity extraction
- **ReportLab** – PDF generation

---

## 🔐 Privacy & Confidentiality
- No external APIs used
- All processing happens locally
- Ensures contract confidentiality

---

## 📂 Supported File Formats
- PDF (text-based)
- DOCX
- TXT

---

## ▶️ How to Run Locally

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
