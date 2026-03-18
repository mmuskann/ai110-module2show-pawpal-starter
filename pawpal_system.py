from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Task:
    task_name: str
    description: Optional[str] = None
    priority: Optional[int] = None
    time: Optional[str] = None
    frequency: Optional[str] = None
    completed: bool = False

    def set_description(self, description: str):
        self.description = description

    def set_priority(self, priority: int):
        self.priority = priority

    def set_time(self, time: str):
        self.time = time

    def set_frequency(self, frequency: str):
        self.frequency = frequency

    def set_completed(self, completed: bool):
        self.completed = completed


@dataclass
class Pet:
    pet_name: str
    age: Optional[int] = None
    type: Optional[str] = None
    tasks: list[Task] = field(default_factory=list)

    def set_age(self, age: int):
        self.age = age

    def set_type(self, type: str):
        self.type = type

    def add_task(self, task: Task):
        self.tasks.append(task)

    def delete_task(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)


@dataclass
class Constraint:
    constraint_name: str
    description: Optional[str] = None
    priority: Optional[str] = None
    block_start: Optional[str] = None
    block_end: Optional[str] = None
    preferred_start: Optional[str] = None
    preferred_end: Optional[str] = None

    def remove_constraint(self):
        pass

    def set_block_time(self, start_time: str, end_time: str):
        pass

    def set_preferred_time(self, start_time: str, end_time: str):
        pass

    def change_priority(self, priority: str):
        pass

    def set_description(self, description: str):
        pass


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: list[Pet] = []
        self.constraints: list[Constraint] = []

    def change_name(self, new_name: str):
        self.name = new_name

    def delete_owner(self):
        self.pets.clear()
        self.constraints.clear()

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def delete_pet(self, pet: Pet):
        if pet in self.pets:
            self.pets.remove(pet)

    def add_constraint(self, constraint: Constraint):
        self.constraints.append(constraint)

    def delete_constraint(self, constraint: Constraint):
        if constraint in self.constraints:
            self.constraints.remove(constraint)

