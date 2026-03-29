# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Testing PawPal+

### Run the tests

```bash
python -m pytest
```

### What the tests cover

The test suite in `tests/test_pawpal.py` covers the core scheduling logic across all major classes:

- **Task** — default attribute values, and all setter methods (`set_description`, `set_priority`, `set_time`, `set_frequency`, `set_completed`)
- **Pet** — adding/deleting tasks, `task_count()`, and edge cases like deleting a task that isn't in the list
- **Owner** — adding/deleting pets, block times, and preferred times; `delete_owner()` clearing all data; `change_name()`
- **Scheduler** — `get_all_tasks()` across zero, one, and multiple pets; `get_all_tasks_sorted()` for chronological ordering with `None` times sorted last; `complete_daily_task()` for recurring task logic (marks done, spawns a new identical task, and skips non-daily tasks); `get_time_conflicts()` for detecting duplicate time slots within and across pets

### Confidence Level

4 out of 5 stars

The unit tests cover all major classes and a wide range of edge cases (None values, multi-pet scenarios, recurring tasks, conflict detection). Confidence is high for the core scheduling logic. One star is held back because there are no integration or UI-level tests for the Streamlit `app.py` layer, so end-to-end behavior remains manually verified.
