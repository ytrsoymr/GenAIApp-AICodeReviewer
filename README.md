# AI Code Reviewer (Google Gemini)

## 📌 Project Overview
AI Code Reviewer is a Python-based application that allows users to submit their Python code for AI-powered analysis. The application reviews the code, identifies potential bugs, suggests improvements, and provides corrected code snippets using Google Gemini AI.

## 🚀 Features
- **Bug Detection**: Identifies syntax errors, logical bugs, and inefficiencies.
- **Code Optimization**: Suggests improvements for better performance and readability.
- **Fixed Code Snippets**: Provides corrected code based on AI recommendations.
- **User-Friendly Interface**: Built using Streamlit for a smooth user experience.

## 🛠️ Tech Stack
- **Frontend:** Streamlit (for UI)
- **Backend:** Python
- **AI Model:** Google Gemini AI
- **Libraries:** \`streamlit\`, \`google-generativeai\`

## 🔧 Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/AI-Code-Reviewer.git
   cd AI-Code-Reviewer
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up API Key**
   - Obtain an API key from Google AI (https://ai.google.dev/)
   - Add it to \`config/config.py\`:
     ```python
     GOOGLE_API_KEY = \"your_google_api_key\"
     ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## 📝 Usage
1. Paste your Python code into the text area.
2. Click the **Review Code** button.
3. View the AI-generated feedback and corrected code.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## 📧 Contact
For questions or feedback, reach out to yarramthirupathirao@gmail.com

---

🚀 **Happy Coding!** 🎯" > README.md
