# NDIS Chatbot Deployment on Azure Using Docker

This guide explains how to containerize your NDIS chatbot (Gradio + local TXT knowledge base) and deploy it to **Azure Container Instances (ACI)** or **Azure App Service**.

---

## 1️⃣ Project Structure

ndis_chatbot/
├─ ndis_chatbot.py # Chatbot Python script
├─ ndis_pages_text.txt # NDIS knowledge base text
├─ requirements.txt # Python dependencies
├─ Dockerfile


---

## 2️⃣ requirements.txt

```txt
langchain
openai
faiss-cpu
gradio
beautifulsoup4
```

## 3️⃣ Dockerfile

```txt
# Use Python 3.11 slim
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Gradio default port
EXPOSE 7860

# Set environment variable for OpenAI API key (can be overridden at runtime)
ENV OPENAI_API_KEY=""

# Run chatbot
CMD ["python", "ndis_chatbot.py"]
```

## 4️⃣ Update Gradio Launch in ndis_chatbot.py

### Make sure Gradio listens on all interfaces:

```txt
iface.launch(server_name="0.0.0.0", server_port=7860)
```

## 5️⃣ Build Docker Image

```txt
docker build -t ndis-chatbot .
```

## 6️⃣ Run Locally for Testing

```txt
docker run -e OPENAI_API_KEY="your_openai_api_key" -p 7860:7860 ndis-chatbot
```
### Access in browser: http://localhost:7860

## 7️⃣ Push to Azure Container Registry (ACR)

### Login to Azure and create a registry:

```txt
az acr create --resource-group myResourceGroup --name myACRName --sku Basic
az acr login --name myACRName
```

### Tag and push Docker image:

```txt
docker tag ndis-chatbot myacrname.azurecr.io/ndis-chatbot:latest
docker push myacrname.azurecr.io/ndis-chatbot:latest
```

## 8️⃣ Deploy to Azure Container Instance (ACI)

```txt
az container create \
  --resource-group myResourceGroup \
  --name ndis-chatbot \
  --image myacrname.azurecr.io/ndis-chatbot:latest \
  --cpu 1 --memory 2 \
  --registry-login-server myacrname.azurecr.io \
  --registry-username <ACR_USERNAME> \
  --registry-password <ACR_PASSWORD> \
  --dns-name-label ndischatbotapp \
  --ports 7860 \
  --environment-variables OPENAI_API_KEY="your_openai_api_key"
```

### Public URL: http://ndischatbotapp.<region>.azurecontainer.io:7860

## 9️⃣ Optional: Deploy to Azure App Service (Linux + Docker)

```txt
Create a Web App in Azure Portal → choose Docker Container.

Use the ACR image you pushed above.

Set environment variable OPENAI_API_KEY in App Service settings.

Update Gradio launch as in Step 4. App will start automatically.
```

## ✅ Key Notes

```txt
The bot only uses the local TXT file and FAISS vector store. No live web scraping occurs.

FAISS index is built from TXT at startup; for faster startup with large files, save/load the index.

Adjust CPU/memory depending on usage.

Gradio default port 7860 is exposed and mapped for web access.
```

