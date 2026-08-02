"""
Punto de entrada para probar el asistente por consola (modo texto).
La voz se añadirá en una capa posterior sin tocar este flujo: solo
se sustituye la fuente de 'user_text' por la salida del STT.

Uso:
    export ANTHROPIC_API_KEY="tu_api_key"
    python main.py
"""

from core.router import AssistantCore


def main():
    print("=== Asistente IA (modo texto) ===")
    print("Escribe 'salir' para terminar.\n")

    assistant = AssistantCore()

    while True:
        user_text = input("Tú: ").strip()
        if user_text.lower() in ("salir", "exit", "quit"):
            print("Nova: ¡Hasta luego!")
            break
        if not user_text:
            continue

        respuesta = assistant.handle_message(user_text)
        print(f"Nova: {respuesta}\n")


if __name__ == "__main__":
    main()
