import os

# app_mode = os.environ.get("APP_MODE", "DEVELOPMENT")
# Port = os.environ.get("PORT", "8000")

# print(app_mode)
# print(Port)

api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("open ai env var is not set")

print(api_key)