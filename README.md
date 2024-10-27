Here’s a structured README file for your project:

---

# ATS Resume Expert

## Overview

ATS Resume Expert is a Streamlit-based application designed to evaluate resumes against job descriptions using Google Generative AI's Gemini model. This tool provides detailed feedback on how well a resume matches specific job requirements in fields such as data science, AI, and big data. Additional features include skill improvement suggestions, percentage match scoring, and visa sponsorship analysis.

## Features

- **Resume Analysis**: Compare resumes against job descriptions and get detailed feedback on strengths and weaknesses.
- **Skill Improvement Suggestions**: Receive tailored advice on how to improve your resume to better match job requirements.
- **Percentage Match**: Get a percentage score indicating how closely your resume matches the job description.
- **Visa Sponsorship Analysis**: Determine if the job offers visa sponsorship and the types of sponsorship available.

## Prerequisites

- **Python 3.7+**
- **Poppler**: Required for PDF to image conversion.
- **Streamlit**: For running the web application.
- **Google Generative AI API**: For resume analysis using the Gemini model.

## Installation

### Step 1: Install Python Packages

First, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/ats-resume-expert.git
cd ats-resume-expert
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Step 2: Install Poppler

Poppler is necessary for converting PDF files to images. You can install Poppler on your system as follows:

- **Windows**:
  1. Download the latest release from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/).
  2. Extract the downloaded file and add the `bin` directory to your system's PATH environment variable.

- **macOS**:
  ```bash
  brew install poppler
  ```

- **Linux**:
  ```bash
  sudo apt-get install poppler-utils
  ```

### Step 3: Set Up Google Generative AI

1. Obtain an API key from Google Generative AI.
2. Create a `.env` file in the project directory with your API key:

```plaintext
GOOGLE_API_KEY=your_google_api_key
```

## Usage

To start the application, run:

```bash
streamlit run App.py
```

Upload a resume in PDF format and enter the job description you wish to compare it against. Select from the available options to receive analysis, suggestions, or visa sponsorship information.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.


## Contact

For any inquiries, feel free to reach out to me at [bora.h@northeastern.edu](mailto:bora.h@northeastern.edu).
