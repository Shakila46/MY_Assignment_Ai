#  Pro Assignment Humanizer

A sleek and efficient Streamlit web application designed to generate human-like, academic assignment answers using Groq's advanced LLM API. The application not only generates high-quality textual responses but also formats and exports them directly as downloadable PDF documents.

##  Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#-usage)
- [Author](#-author)

##  Features

* **AI-Powered Generation:** Utilizes Groq's `llama-3.3-70b-versatile` model to generate fluent, natural English paragraphs tailored for academic assignments.
* **Humanized Output:** System prompts are specifically engineered to avoid robotic formatting (like bulleted lists) and write in a natural, student-like tone.
* **Instant PDF Export:** Automatically cleans text encoding and generates a cleanly formatted PDF report complete with headers, footers, and page numbers using `fpdf`.
* **User-Friendly UI:** A clean, responsive, and intuitive web interface built with Streamlit.

##  Tech Stack

* **Frontend & Framework:** [Streamlit](https://streamlit.io/)
* **AI Inference:** [Groq API](https://wow.groq.com/)
* **PDF Generation:** [FPDF](https://pyfpdf.readthedocs.io/)
* **Language:** Python 3.x

##  Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have Python installed on your system. You will also need a Groq API Key, which you can obtain from the [Groq Cloud Console](https://console.groq.com/).

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Shakila46/MY_Assignment_Ai.git](https://github.com/Shakila46/MY_Assignment_Ai.git)
   cd MY_Assignment_Ai
