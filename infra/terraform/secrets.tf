/**
 * Copyright 2024 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


# --------- Secrets for the init-db job ---------

# Create db_admin_user secret
resource "google_secret_manager_secret" "openai_api_key" {
  project   = var.google_cloud_run_project
  secret_id = "OPENAI_API_KEY"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret" "qdrant_api_key" {
  project   = var.google_cloud_run_project
  secret_id = "QDRANT_API_KEY"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret" "qdrant_url" {
  project   = var.google_cloud_run_project
  secret_id = "QDRANT_URL"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret" "slack_bot_token" {
  project   = var.google_cloud_run_project
  secret_id = "SLACK_BOT_TOKEN"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret" "slack_bot_user_id" {
  project   = var.google_cloud_run_project
  secret_id = "SLACK_BOT_USER_ID"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret" "slack_signing_secret" {
  project   = var.google_cloud_run_project
  secret_id = "SLACK_SIGNING_SECRET"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret" "langfuse_public_key" {
  project   = var.google_cloud_run_project
  secret_id = "LANGFUSE_PUBLIC_KEY"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret" "langfuse_secret_key" {
  project   = var.google_cloud_run_project
  secret_id = "LANGFUSE_SECRET_KEY"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret" "langfuse_host" {
  project   = var.google_cloud_run_project
  secret_id = "LANGFUSE_HOST"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret" "redis_host" {
  project   = var.google_cloud_run_project
  secret_id = "REDIS_HOST"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret" "redis_port" {
  project   = var.google_cloud_run_project
  secret_id = "REDIS_PORT"
  replication {
    auto {}
  }
}


resource "google_secret_manager_secret" "redis_username" {
  project   = var.google_cloud_run_project
  secret_id = "REDIS_USERNAME"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret" "redis_password" {
  project   = var.google_cloud_run_project
  secret_id = "REDIS_PASSWORD"
  replication {
    auto {}
  }
}
