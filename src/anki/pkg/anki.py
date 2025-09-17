import genanki
from genanki import Deck, Note, Model, Package
from anki.models.questions_answers import QuestionsAnswers

def create_anki_model(modelId: int, titleDeck: str) -> Model:
    return Model(
        modelId,
        titleDeck,
        fields=[
            {'name': 'Topic'},
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
            'name': '{{Topic}}',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])

def create_anki_deck(deckId: int, titleDeck: str) -> Deck:
    return genanki.Deck(
        deckId,
        titleDeck
    )

def create_anki_card(ankiModel: Model, deck: Deck, questionsAnswers: QuestionsAnswers):
    deck.add_note(
        Note(
            model=ankiModel,
            fields=[questionsAnswers.topic, questionsAnswers.question, questionsAnswers.answer]
        )
    )

def create_anki_package(titleDeck: str, deck: Deck):
    print(f"Create the deck file: {titleDeck}.apkg")
    genanki.Package(deck).write_to_file(f'{titleDeck}.apkg')
