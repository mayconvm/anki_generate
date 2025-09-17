from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from anki.models.questions_answers import ListQuestionsAnswers

@CrewBase
class LatestAiDevelopmentCrew():
	agents: List[BaseAgent]
	tasks: List[Task]

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
			cache=True,
			tools=[SerperDevTool()]
		)

	@agent
	def question_answer_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['question_answer_specialist'],
			verbose=True,
			cache=True,
			output_pydantic=ListQuestionsAnswers,
		)

	@task
	def search_task(self) -> Task:
		return Task(
			config=self.tasks_config['search_task'],
		)

	@task
	def question_answer_task(self) -> Task:
		return Task(
			config=self.tasks_config['question_answer_task'],
			output_file='report.md',
			output_pydantic=ListQuestionsAnswers,
		)

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
