# StyleMate AI - System Architecture

## Vision

StyleMate AI is an AI-powered fashion consultant that helps users create coordinated outfits using garments they already own.

---

## Core Modules

### 1. Vision Engine
Responsible for understanding uploaded garment images.

Outputs:
- Garment Type
- Colour
- Pattern
- Fabric
- Confidence

---

### 2. Fashion Intelligence Engine
Responsible for fashion reasoning.

Outputs:
- Matching Bottoms
- Footwear
- Accessories
- Occasion
- Season
- Trend Score

---

### 3. Shopping Engine

Responsible for finding matching products online.

Sources:
- Myntra
- AJIO
- Amazon
- Flipkart

---

### 4. User Interface

Built using Streamlit.

Responsibilities:
- Image Upload
- Display Fashion Analysis
- Show Recommendations