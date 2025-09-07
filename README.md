# AI Chatbot Agent

A full-stack AI chatbot application with LangGraph, supporting multiple AI providers (Groq, OpenAI) and web search capabilities via Tavily.

## Features

- 🤖 Multiple AI model support (Groq, OpenAI)
- 🔍 Web search integration with Tavily
- 🎨 Modern Streamlit frontend
- ⚡ FastAPI backend
- 🌐 Deployable to Vercel (frontend) and Render (backend)

## Deployment Guide

### Prerequisites

1. GitHub repository with your code
2. API keys for:
   - Groq API
   - Tavily API  
   - OpenAI API

### Step 1: Deploy Backend to Render

1. **Go to [Render.com](https://render.com)** and sign up/login
2. **Click "New +" → "Web Service"**
3. **Connect your GitHub repository**
4. **Configure the service:**
   - **Name**: `chatbot-backend` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn backend:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free

5. **Add Environment Variables:**
   - `GROQ_API_KEY`: Your Groq API key
   - `TAVILY_API_KEY`: Your Tavily API key
   - `OPENAI_API_KEY`: Your OpenAI API key

6. **Click "Create Web Service"**
7. **Wait for deployment** (5-10 minutes)
8. **Copy the deployed URL** (e.g., `https://your-app-name.onrender.com`)

### Step 2: Deploy Frontend to Vercel

1. **Go to [Vercel.com](https://vercel.com)** and sign up/login
2. **Click "New Project"**
3. **Import your GitHub repository**
4. **Configure the project:**
   - **Framework Preset**: Other
   - **Root Directory**: `./` (root)
   - **Build Command**: Leave empty
   - **Output Directory**: Leave empty

5. **Add Environment Variables:**
   - `BACKEND_URL`: Your Render backend URL (e.g., `https://your-app-name.onrender.com`)

6. **Click "Deploy"**
7. **Wait for deployment** (2-3 minutes)
8. **Your app will be live!**

### Step 3: Update CORS (Optional but Recommended)

After getting your Vercel URL, update the CORS settings in `backend.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-vercel-app.vercel.app"],  # Replace with your Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Then redeploy to Render.

## Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp env.example .env
   # Edit .env with your API keys
   ```

3. **Run backend:**
   ```bash
   python3 backend.py
   ```

4. **Run frontend:**
   ```bash
   streamlit run frontend.py
   ```

## Project Structure

```
├── agent.py          # AI agent logic with LangGraph
├── backend.py        # FastAPI backend server
├── frontend.py       # Streamlit frontend
├── requirements.txt  # Python dependencies
├── vercel.json       # Vercel configuration
├── render.yaml       # Render configuration
└── env.example       # Environment variables template
```

## API Endpoints

- `GET /` - Health check
- `POST /chat` - Chat with AI agent

## Troubleshooting

### Common Issues:

1. **Connection refused**: Make sure backend is deployed and running
2. **CORS errors**: Update CORS settings with your Vercel domain
3. **API key errors**: Verify all environment variables are set correctly
4. **Build failures**: Check that all dependencies are in requirements.txt

### Support

If you encounter issues, check:
- Render deployment logs
- Vercel deployment logs
- Browser console for frontend errors
- API response status codes
