from deep_translator import GoogleTranslator
import os
from datetime import datetime

class Translate:
    
    def split_text(text, max_length):
        """Divide o texto em partes menores que max_length caracteres."""
        return [text[i:i + max_length] for i in range(0, len(text), max_length)]

    def translate_text(text, target_language="pt"):
        """Traduza o texto usando GoogleTranslator respeitando o limite de 5000 caracteres."""
        translator = GoogleTranslator(target=target_language)
        max_length = 5000
        parts = Translate.split_text(text, max_length)
        
        translated_parts = []
        for part in parts:
            translated_part = translator.translate(part)
            translated_parts.append(translated_part)
        
        translated_parts = [translator.translate(part) for part in parts]
        return ''.join(translated_parts)
    
    def save_to_file(text, directory="viagens"):
        # Cria o diretório se ele não existir
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Gera o nome do arquivo com data e hora atuais
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"translated_{timestamp}.txt"
        file_path = os.path.join(directory, file_name)

        # Escreve o texto no arquivo
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)
