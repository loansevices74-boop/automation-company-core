import yaml

def translate_message(message, lang):
    translations = {
        "en": message,
        "fr": "Automatisation intelligente pour votre entreprise!",
        "es": "¡Automatización inteligente para tu negocio!",
        "zh": "为您的企业提供智能自动化！"
    }
    return translations.get(lang, message)

if __name__ == "__main__":
    with open("global_scaling/config.yml") as f:
        config = yaml.safe_load(f)
    for lang in config['languages']:
        print(f"{lang}: {translate_message('Smart automation for your business!', lang)}")