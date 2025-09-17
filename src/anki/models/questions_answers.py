from pydantic import BaseModel, Field
from typing import List

class QuestionsAnswers(BaseModel):
    topic: str = Field(..., description="Topic of the question and answer")
    question: str = Field(..., description="Question text")
    answer: str = Field(..., description="Answer text")
    number: int = Field(..., description="Question number")

class ListQuestionsAnswers(BaseModel):
    items: List[QuestionsAnswers] = Field(..., description="List of items with Questions and Answers")
    def __iter__(self):
        return iter(self.items)
