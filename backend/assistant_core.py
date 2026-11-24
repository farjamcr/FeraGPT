
APP_NAME = "FeraGPT"
APP_VERSION = "1.0.0"

CAPABILITIES = {
    "chat": {
        "name": "هوش مصنوعی",
        "enabled": True
    },
    "programming": {
        "name": "برنامه نویسی",
        "enabled": True
    },
    "website_design": {
        "name": "طراحی سایت",
        "enabled": True
    },
    "image_generation": {
        "name": "ساخت تصویر",
        "enabled": False
    },
    "image_editing": {
        "name": "ویرایش تصویر",
        "enabled": False
    },
    "file_analysis": {
        "name": "تحلیل فایل",
        "enabled": False
    },
    "web_search": {
        "name": "جستجوی وب",
        "enabled": False
    },
    "translation": {
        "name": "ترجمه",
        "enabled": True
    }
}

SYSTEM_INSTRUCTIONS = """
You are FeraGPT, a helpful AI assistant.

Your responsibilities:
- Answer questions clearly and accurately.
- Help with programming and debugging.
- Help design and develop websites.
- Explain technical topics step by step.
- Support users with files and images when those
  capabilities are connected.

Always respond in the user's language.
Never pretend to have a capability that is not
actually available.
"""

def get_capabilities():
    return CAPABILITIES

def build_prompt(message):
    return (
        SYSTEM_INSTRUCTIONS
        + "\n\nUser message:\n"
        + message
    )
  
