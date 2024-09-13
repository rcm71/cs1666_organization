import argparse
from dataclasses import dataclass
from yaml import load, dump
try:
	from yaml import CLoader as Loader
except ImportError:
	from yaml import Loader

@dataclass
class TeamMember:
	lastname: str
	score: int
	desc: str

	def __post_init__(self):
		if not isinstance(self.score, int) or not (-2 <= self.score <= 2):
			raise ValueError(f"Invalid score of {self.score} for team member {self.lastname}")

@dataclass
class Report:
	manager_lastname: str
	week: int
	team_members: list[TeamMember]

	def __post_init__(self):
		if not isinstance(self.week, int):
			raise ValueError(f"Invalid week: {self.week}")

		self.team_members = [ TeamMember(lastname=name, **vals) for name, vals in self.team_members.items() ]

def main():
	parser = argparse.ArgumentParser(description="sanity check a management week report YAML file")
	parser.add_argument("fname", help="file name to check")
	args = parser.parse_args()

	print("Checking...", end="", flush=True)

	try:
		with open(args.fname) as inf:
			report = Report(**load(inf, Loader=Loader))
	except Exception as e:
		print("ERROR!\n")
		raise
	else:
		print("OK!")

if __name__ == "__main__":
	main()
