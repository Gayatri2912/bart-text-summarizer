<div align="center">

# 📝 BART Text Summarizer

### AI-Powered Text Summarization in Seconds

## 🎯 About

A **production-ready web application** that automatically generates high-quality text summaries using Facebook's **BART** (Bidirectional and Auto-Regressive Transformers) model. Built with **Streamlit** for an intuitive user interface and **Hugging Face Transformers** for state-of-the-art NLP capabilities.

Perfect for summarizing news articles, research papers, long emails, and documents without any external API dependencies.



## ✨ Key Features

- 🤖 **Dual AI Models** - Choose between BART Large (high quality) or DistilBART (faster)
- ⚡ **Smart Caching** - Models load once and stay in memory for instant processing
- 🎛️ **Customizable Length** - Adjust summary output from 30-200 words
- 🎲 **Creative Mode** - Enable text sampling for varied summarization styles
- 📜 **History Tracking** - Review your last 5 summaries with original text
- 💾 **Export Options** - Download summaries as text files
- 🌙 **Modern Interface** - Clean, dark-themed UI built with Streamlit
- 🐳 **Docker Support** - Run anywhere with containerization
- 🔄 **CI/CD Pipeline** - Automated testing and deployment via GitHub Actions

---


## 🧠 Models

**BART Large CNN** - State-of-the-art model with 406M parameters, trained on CNN/DailyMail dataset. Best for production environments requiring high accuracy.

**DistilBART CNN** - Distilled version with 306M parameters. 40% faster while maintaining 95% of original quality. Ideal for resource-constrained environments.

Both models run locally without requiring API keys or internet connection after initial download.



## ⚙️ CI/CD Pipeline

Fully automated development workflow:

- **Continuous Integration** - Runs on every push/PR with dependency installation, syntax validation, and import testing
- **Continuous Deployment** - Automatically builds and publishes Docker images to GitHub Container Registry on main branch updates
- **Release Automation** - Creates GitHub releases with auto-generated notes when version tags are pushed


## 📊 Performance

- **Processing Speed**: 2-5 seconds per summary (BART Large on modern CPU)
- **Accuracy**: ROUGE-1 score of 44.16, ROUGE-L of 40.90
- **Memory Usage**: ~2GB RAM with model loaded
- **Supported Input**: Up to 1024 tokens (~750 words)


## 📄 License

Released under MIT License - free for personal and commercial use.

## 🙌 Acknowledgements

Built with powerful open-source tools:
- **Hugging Face Transformers** for pretrained models
- **Streamlit** for rapid web app development
- **Facebook BART** research and model architecture
- **Docker** for containerization
<img width="1919" height="734" alt="Screenshot 2026-02-26 000142" src="https://github.com/user-attachments/assets/1e08a66a-be5e-4fbb-9ece-5b3945a803ba" />
