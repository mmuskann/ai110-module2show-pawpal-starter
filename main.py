from pawpal_system import Owner, Pet, Task, Scheduler
# Create owner
owner = Owner("Alex")

# Create pets
buddy = Pet(pet_name="Buddy", age=3, type="Dog")
whiskers = Pet(pet_name="Whiskers", age=5, type="Cat")

# Add tasks to Buddy
buddy.add_task(Task(task_name="Morning Walk", description="30-minute walk around the block", time="7:00 AM", priority=1))
buddy.add_task(Task(task_name="Feeding", description="1 cup of dry food", time="8:00 AM", priority=2))
buddy.add_task(Task(task_name="Evening Walk", description="20-minute walk", time="6:00 PM", priority=1))

# Add tasks to Whiskers
whiskers.add_task(Task(task_name="Feeding", description="Half can of wet food", time="8:30 AM", priority=1))
whiskers.add_task(Task(task_name="Playtime", description="10 minutes with feather toy", time="5:00 PM", priority=2))

# Add pets to owner
owner.add_pet(buddy)
owner.add_pet(whiskers)

# Print today's schedule
scheduler = Scheduler(owner)
all_tasks = scheduler.get_all_tasks()
all_tasks.sort(key=lambda x: x[1].time or "")

print("=" * 40)
print(f"  Today's Schedule for {owner.name}")
print("=" * 40)

for pet, task in all_tasks:
    status = "[DONE]" if task.completed else "[ ]"
    print(f"{status} {task.time:>8}  [{pet.pet_name}] {task.task_name}")
    if task.description:
        print(f"           {task.description}")

print("=" * 40)
