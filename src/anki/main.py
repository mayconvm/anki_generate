from anki.crew import LatestAiDevelopmentCrew
from anki.models.questions_answers import ListQuestionsAnswers
from pkg.anki import create_anki_model, create_anki_deck, create_anki_card, create_anki_package
import argparse

def run(args):
    """
    Run the crew.
    """
    inputs = {
        'topic': args.topic
    }
    
    crew = LatestAiDevelopmentCrew().crew()
    result = crew.kickoff(inputs=inputs)
    
    pydantic_result = result.pydantic
    
    create_anki(args.modelId, args.deckId, args.topic, pydantic_result)


def create_anki(modelId: int, deckId: int, titleDeck: str, result: ListQuestionsAnswers):
    model = create_anki_model(modelId, titleDeck)
    deck = create_anki_deck(deckId, titleDeck)

    print(f"Prepared deck: {titleDeck}")
    print(f"Total items: {len(result.items)}")

    for item in result.items:
        create_anki_card(model, deck, item)
    
    create_anki_package(titleDeck, deck)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make a new deck Anki")
    parser.add_argument('--topic', type=str, help='Topic for the Anki deck', required=True)
    parser.add_argument('--modelId', type=int, help='Model ID for the Anki Model', default='1607392319')
    parser.add_argument('--deckId', type=int, help='Deck ID for the Anki deck', default='1607392319')
    args = parser.parse_args()
    
    run(args)
