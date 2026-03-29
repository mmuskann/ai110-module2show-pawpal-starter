import streamlit as st
from pawpal_system import Task, Pet, BlockTime, PreferredTime, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Owner & Pet")

owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    task_time = st.text_input("Time (e.g. 08:00)", value="08:00")
with col3:
    priority = st.number_input("Priority (1=high)", min_value=1, max_value=10, value=1)

task_description = st.text_input("Description (optional)", value="")
task_frequency = st.selectbox("Frequency", ["daily", "weekly", "as needed"])

if st.button("Add task"):
    new_task = Task(task_name=task_title)
    new_task.set_time(task_time)
    new_task.set_priority(int(priority))
    new_task.set_frequency(task_frequency)
    if task_description:
        new_task.set_description(task_description)
    st.session_state.tasks.append(new_task)

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table([
        {
            "Task": t.task_name,
            "Time": t.time,
            "Priority": t.priority,
            "Frequency": t.frequency,
            "Description": t.description or "",
            "Completed": t.completed,
        }
        for t in st.session_state.tasks
    ])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    owner = Owner(name=owner_name)
    pet = Pet(pet_name=pet_name)
    pet.set_type(species)
    for task in st.session_state.tasks:
        pet.add_task(task)
    owner.add_pet(pet)

    scheduler = Scheduler(owner=owner)
    all_tasks = scheduler.get_all_tasks()

    if all_tasks:
        st.success(f"Schedule for {owner.name}'s pet {pet.pet_name} ({pet.type}) — {pet.task_count()} task(s):")
        st.table([
            {
                "Pet": p.pet_name,
                "Task": t.task_name,
                "Time": t.time,
                "Priority": t.priority,
                "Frequency": t.frequency,
                "Description": t.description or "",
                "Completed": t.completed,
            }
            for p, t in all_tasks
        ])
    else:
        st.warning("No tasks to schedule. Add tasks above first.")
