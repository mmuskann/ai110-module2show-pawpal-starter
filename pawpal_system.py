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

    def task_count(self) -> int:
        return len(self.tasks)


@dataclass
class BlockTime:
    constraint_name: str
    block_start: Optional[str] = None
    block_end: Optional[str] = None
    priority: Optional[int] = None
    description: Optional[str] = None

    def set_block_time(self, start_time: str, end_time: str):
        self.block_start = start_time
        self.block_end = end_time

    def change_priority(self, priority: int):
        self.priority = priority

    def set_description(self, description: str):
        self.description = description


@dataclass
class PreferredTime:
    constraint_name: str
    preferred_start: Optional[str] = None
    preferred_end: Optional[str] = None
    priority: Optional[int] = None
    description: Optional[str] = None

    def set_preferred_time(self, start_time: str, end_time: str):
        self.preferred_start = start_time
        self.preferred_end = end_time

    def change_priority(self, priority: int):
        self.priority = priority

    def set_description(self, description: str):
        self.description = description


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: list[Pet] = []
        self.block_times: list[BlockTime] = []
        self.preferred_times: list[PreferredTime] = []

    def change_name(self, new_name: str):
        self.name = new_name

    def delete_owner(self):
        self.pets.clear()
        self.block_times.clear()
        self.preferred_times.clear()

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def delete_pet(self, pet: Pet):
        if pet in self.pets:
            self.pets.remove(pet)

    def add_block_time(self, block_time: BlockTime):
        self.block_times.append(block_time)

    def delete_block_time(self, block_time: BlockTime):
        if block_time in self.block_times:
            self.block_times.remove(block_time)

    def add_preferred_time(self, preferred_time: PreferredTime):
        self.preferred_times.append(preferred_time)

    def delete_preferred_time(self, preferred_time: PreferredTime):
        if preferred_time in self.preferred_times:
            self.preferred_times.remove(preferred_time)


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self) -> list[tuple[Pet, Task]]:
        all_tasks = []
        for pet in self.owner.pets:
            for task in pet.tasks:
                all_tasks.append((pet, task))
        return all_tasks

