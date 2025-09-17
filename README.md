# Anki Generate using CrewAI

Gerador de flashcards para Anki usando IA.

# Run
## Environment Variables
* Crie um arquivo `.env` baseado no `.env.example` e preencha as chaves

## Sync
```bash
PYTHONPATH=src uv sync
```

## Exec
```shell
PYTHONPATH=src uv run src/anki/main.py --topic 'AWS Certified AI Practitioner' --modelId 1807392318 --deckId 1807392318
```

# Output
Será gerado um arquivo com a extensão `.apkg` que pode ser importado diretamente no Anki.

# Ref
* [crewAI](https://github.com/crewAIInc/crewAI/tree/main)
* [genanki](https://github.com/kerrickstaley/genanki)
* [ankiweb](https://ankiweb.net/)
* [Agentes Inteligentes](https://physia.com.br/crewai1/)
