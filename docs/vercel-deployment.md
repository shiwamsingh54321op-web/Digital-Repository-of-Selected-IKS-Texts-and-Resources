# Deploying IKS Digital Repository on Vercel

This repository is pre-configured for deployment on [Vercel](https://vercel.com) with automated builds, client-side routing, and optional serverless API integration.

---

## Deployment Architecture

You can deploy the project on Vercel in one of two configurations:

### Configuration 1: Full-Stack on Vercel (Frontend + Serverless API)
The repository includes a top-level [`vercel.json`](../vercel.json) and serverless entry point [`api/index.py`](../api/index.py):
- **Frontend**: Built from `frontend/` with Vite and served via Vercel's Edge CDN.
- **Backend API**: Python FastAPI serverless function mounted at `/api/*`.
- **Database**: The SQLite database (`iks_repository.db`) is automatically initialized and seeded in `/tmp` on cold start with all 52 domains, 32 canonical texts, 9 licenses, and 12 institutions.

### Configuration 2: Edge Frontend on Vercel + Dedicated Backend (Recommended for high concurrency)
- **Frontend**: Deployed on Vercel.
- **Backend**: Hosted on [Render](https://render.com), [Railway](https://railway.app), Fly.io, or VPS.
- **Configuration**: Set the environment variable in Vercel:
  ```env
  VITE_API_BASE_URL=https://your-backend-service.onrender.com/api
  ```

---

## 🚀 1-Click Deployment via Vercel Dashboard (Recommended)

Since the repository is already published on GitHub:
[`https://github.com/shiwamsingh54321op-web/Digital-Repository-of-Selected-IKS-Texts-and-Resources`](https://github.com/shiwamsingh54321op-web/Digital-Repository-of-Selected-IKS-Texts-and-Resources)

Follow these simple steps:

1. **Sign in to Vercel**:
   Go to **[https://vercel.com/login](https://vercel.com/login)** and sign in with your GitHub account (`shiwamsingh54321op-web`).

2. **Import Repository**:
   - Go to **[https://vercel.com/new](https://vercel.com/new)**.
   - Under **"Import Git Repository"**, find:
     `Digital-Repository-of-Selected-IKS-Texts-and-Resources`
   - Click the blue **"Import"** button.

3. **Configure Project Settings**:
   - **Project Name**: `iks-digital-repository` (or leave default).
   - **Framework Preset**: `Vite` (automatically detected).
   - **Root Directory**:
     - For **Full-Stack (Frontend + Serverless Backend)**: Leave as `./` (Root).
     - For **Frontend-Only**: Select `frontend`.
   - **Build Command**: `cd frontend && npm install && npm run build` (or `npm run build` if Root is `frontend`).
   - **Output Directory**: `frontend/dist` (or `dist` if Root is `frontend`).

4. **Environment Variables (Optional)**:
   - If connecting to an external FastAPI backend URL, add:
     - `VITE_API_BASE_URL` = `https://your-backend-api-url.com/api`

5. **Deploy**:
   - Click **"Deploy"**.
   - In ~45-60 seconds, your site will be live on a `*.vercel.app` URL (e.g. `https://iks-digital-repository.vercel.app`)!

---

## 💻 Deploying via Vercel CLI (Command Line)

If you prefer to deploy from your terminal:

```bash
# 1. Open your terminal in the frontend directory
cd frontend

# 2. Run Vercel CLI
npx vercel

# 3. Follow the interactive prompts:
# ? Set up and deploy? [Y/n] y
# ? Which scope? (Select your personal account)
# ? Link to existing project? [y/N] n
# ? What's your project's name? iks-digital-repository
# ? In which directory is your code located? ./
# ? Want to modify these settings? [y/N] n

# 4. Deploy to production
npx vercel --prod
```

---

## 🔄 Automatic Continuous Deployment (CI/CD)

Whenever you push new commits to branch `main` on GitHub:
```bash
git push origin main
```
Vercel automatically detects the push, runs the build, and publishes the update with zero downtime.

---

## 🛠️ Verification Checklist After Deployment

- [ ] **Home Page**: Dynamic metrics display, hero search functions.
- [ ] **Explore Page**: Filters by domain, resource type, language, and access status.
- [ ] **Resource Details**: Dublin Core elements render, citations copy correctly.
- [ ] **Knowledge Domains**: 2-tier domain tree expands.
- [ ] **Client-Side Routing**: Refreshing deep links (e.g. `/explore`, `/domains`) does not return 404 (handled by `vercel.json` rewrites).
- [ ] **Admin Portal**: Accessible at `/admin/login`.
