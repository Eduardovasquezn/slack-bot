# Slack Meeting Summarizer Bot

This project is an end-to-end Slack bot that summarizes meeting transcriptions stored on Google Cloud Platform (GCP).
It uses Terraform for infrastructure setup, serverless event-driven architectures, and integrates vector search for semantic retrieval.

---

## Features

- 🌐 Infrastructure as Code with **Terraform** on **GCP**
- 📂 **Upload** meeting transcription files to **GCS Bucket**
- 🔔 **Pub/Sub** event triggers ingestion pipeline
- 🧠 **Vector Database** (**Qdrant**) for semantic search and filtering
- ⚡ **Indexed** metadata fields in Qdrant for faster queries
- 🚀 **FastAPI** app served via **Cloud Run** as Slack Webhook
- 🧹 **Redis** for deduplication of events
- 📝 **Langfuse** to trace and monitor LLM requests
- 🤖 **OpenAI** models for embeddings and question-answering


---

## Architecture Overview

1. **User uploads** a meeting transcription file to a **GCS Bucket**.
2. **Pub/Sub** detects the file upload and **triggers** a **Cloud Function**.
3. **Cloud Function** ingests the document and metadata into **Qdrant**.
4. A **FastAPI** app is deployed on **Cloud Run** to interact with **Slack API**:
   - Users mention the Slack bot to ask questions about past meetings.
   - Queries are semantically matched against vectorized meeting data.
5. **Langfuse** tracks and monitors requests for observability.
6. **Redis** ensures event deduplication for reliability.

---

## How It Works

1. **Upload a Meeting Transcription**
   - The user uploads a transcription file (e.g., `.docx`) into a **Google Cloud Storage** bucket.

2. **Trigger via Pub/Sub**
   - A **Pub/Sub** topic is configured to listen to new file uploads.
   - When a file is uploaded, an event is published.

3. **Ingest Document**
   - A **Cloud Function** is triggered by the Pub/Sub event.
   - The function reads the uploaded file, extracts metadata, generates embeddings using **OpenAI**, and stores the document in **Qdrant** (vector store).
   - Metadata fields are **indexed** to speed up future filtering during search.

4. **Ask Questions via Slack**
   - A **FastAPI** app, deployed on **Cloud Run**, is connected to a **Slack App** via Webhooks.
   - In Slack, users can **mention** the bot and ask questions about the meetings.
   - The app retrieves relevant meeting chunks from **Qdrant** and uses **OpenAI** to generate a summarized answer.

5. **Trace and Monitor**
   - All interactions are traced through **Langfuse** for monitoring, observability, and debugging.
   - **Redis** ensures deduplication of Pub/Sub events to prevent double-processing.

---


## Stack

| Layer        | Technology         |
|--------------|---------------------|
| Infrastructure | Terraform |
| Cloud Platform | Google Cloud Platform (GCP) |
| Event-driven | Pub/Sub, Cloud Functions |
| Database | Qdrant (vector store) |
| Backend API | FastAPI |
| LLM | OpenAI API (embeddings + chat completions) |
| Monitoring | Langfuse |
| Cache | Redis |
| Deployment | Cloud Run |

---

## Getting Started

1. **Set up GCP project** and configure authentication.
2. **Deploy infrastructure** using Terraform.
3. **Deploy Cloud Function** for ingestion.
4. **Deploy FastAPI Webhook** to Cloud Run.
5. **Configure Slack App** to connect to your Cloud Run URL.
6. Upload a transcription file to your GCS Bucket and tag your Slack bot!
