# 💸 Money Buddy – Your Savage Gen-Z Finance Bestie

**Money Buddy** isn’t your boring finance tracker.  
It’s an **AI-powered roast machine** that takes your transactions, crunches the numbers,  
and then absolutely **clowns you for your poor life choices** 💀.

Think of it as **Mint.com + Standup Comedy 🎤**.

---

## ⚡ Features

- 📂 Upload CSV of your spends (bank SMS parsing later 👀)  
- 🧩 Smart categorization → Food, Travel, Subscriptions, etc.  
- 📊 Analytics → Charts for spend, top vendors, anomalies.  
- 🔥 Roast Generator → Gen-Z savage roast instead of boring insights.  
- 🤖 Powered by **Gemini AI** → Witty punch-up for maximum humiliation.  
- 🚀 Deploy anywhere → Works on Railway & Google Cloud Run.  

---

## 🏗️ Project Structure

```

money-buddy-agent/
│── app.py                   # Streamlit UI
│── utils.py                 # Categorization & analytics
│── llm.py                   # Roast generator with Gemini API
│── requirements.txt          # Python dependencies
│── Dockerfile                # For Cloud Run deployment
│── sample\_transactions.csv   # Demo CSV data
│── README.md                 # You are here

````

---

## ⚙️ Setup & Run Locally

### 1. Clone repo
```bash
git clone https://github.com/your-username/money-buddy-agent.git
cd money-buddy-agent
````

### 2. Create virtual environment

```bash
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Create a `.env` file:

```
GEMINI_API_KEY=your_secret_key_here
```

### 5. Run Streamlit app

```bash
streamlit run app.py
```

Open in browser → [http://localhost:8501](http://localhost:8501) 🎉

---

## ☁️ Deployments

### 🚄 Railway (1-click MVP hosting)

1. Push repo to GitHub.
2. Create project on **Railway**.
3. Add `GEMINI_API_KEY` in Environment Variables.
4. Set Start Command:

   ```bash
   streamlit run app.py --server.port $PORT --server.address 0.0.0.0
   ```
5. Ship it 🚀.

---

### 🌩️ Google Cloud Run (scalable hosting)

**Build & push:**

```bash
gcloud builds submit --tag gcr.io/<project-id>/money-buddy
```

**Deploy:**

```bash
gcloud run deploy money-buddy \
  --image gcr.io/<project-id>/money-buddy \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated \
  --set-env-vars GEMINI_API_KEY=your_secret_key
```

Cloud Run gives you a public URL → share with friends and flex 😎.

---

## 🎤 Example Roast

Upload a CSV →

> **Bruh, ₹7k on Swiggy this month?? Who you feeding, the Avengers?? 🍔💀**

---

## 📌 Roadmap

* 🔗 SMS/UPI parsing (auto ingest).
* 🏆 Gamified savings challenges.
* 🎭 Voice-mode roasts.
* 🎨 Meme/GIF generator with your financial L’s.

---

## 🤝 Contribute

Pull requests welcome — bring your best roasts.
If you make it less savage, you’re instantly **blocked** 💀.

---

## ⚠️ Disclaimer

Money Buddy is for **fun & awareness only**.
Not financial advice. If you’re broke, that’s on you bestie 💸😂.


