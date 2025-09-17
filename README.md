# Anki Generate using CrewAI

Gerador de flashcards para Anki usando IA.

# Run

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