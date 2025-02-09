import openai
import os

import openai

# Configuración de la API de OpenAI (asegúrate de tener tu API Key)
openai.api_key = "TU_API_KEY"

# Función para generar contenido con Zero-Shot Prompting
def zero_shot_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Eres un asistente experto en marketing automotriz."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Ejemplo de Zero-Shot Prompting
prompt_zero_shot = "Genera una descripción publicitaria para un auto eléctrico deportivo."
print("Zero-Shot Output:\n", zero_shot_prompt(prompt_zero_shot))

# Few-Shot Prompting con ejemplos
few_shot_examples = """
Ejemplo 1:
Usuario: Genera una descripción para un SUV familiar.
Asistente: El nuevo SUV X es la combinación perfecta de confort y seguridad para toda la familia. Con amplio espacio interior y tecnología de punta, cada viaje será una experiencia inigualable.

Ejemplo 2:
Usuario: Genera una descripción para un auto deportivo.
Asistente: El modelo Z redefine la velocidad y la elegancia con su diseño aerodinámico y motor de alto rendimiento. Siente la adrenalina en cada curva.
"""

def few_shot_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Eres un asistente experto en marketing automotriz."},
                  {"role": "user", "content": few_shot_examples + "\nUsuario: " + prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Ejemplo de Few-Shot Prompting
prompt_few_shot = "Genera una descripción para una camioneta todoterreno."
print("Few-Shot Output:\n", few_shot_prompt(prompt_few_shot))

# Chain of Thought Prompting
cot_prompt = """
Analiza los puntos clave para una campaña de marketing de un sedán de lujo:
1. Identifica las características más destacadas del sedán de lujo.
2. Explica cómo esas características pueden atraer a clientes potenciales.
3. Redacta una descripción de marketing persuasiva basada en estos puntos.
"""

def chain_of_thought_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Eres un asistente experto en marketing automotriz."},
                  {"role": "user", "content": cot_prompt + "\n" + prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Ejemplo de Chain of Thought Prompting
prompt_cot = "Genera una campaña para un sedán de lujo premium."
print("Chain of Thought Output:\n", chain_of_thought_prompt(prompt_cot))