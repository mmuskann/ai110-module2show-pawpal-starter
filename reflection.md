# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The three core actions the user should be able to perform are add their pet, add their constraint, and add their pet care task. So, the classes would be the pet class, constraint class and task class. Pet class is reponsible for the pet's information such as name, etc. The constraint class is to allow the owner to add certains times they are not available, their preferences, and prioirty of task or each pet if they have mutliple. The task class is responsible for putting tasks with the pet object/ making a list of tasks. There should be also an owner class to assign the pet to the owner.

Brainstorm:

Owner Class {
    constructor {
        --> name
    }
    method {
        --> delete owner
        --> delete pet from owner
        --> change name
    }
}

Pet Class {
    constructor {
        --> pet_name
    }
    method {
        --> remove pet
        --> pet age
        --> pet type?
    }
}

Constraint Class {
    constructor {
        -->constraint name
    }
    method {
        --> remove constrain
        --> block time (start time, end time)
        --> perfered time (start time, end time)
        --> priority
        --> change block time
        --> change perfered time
        --> change priority
        --> constraint description
    }
}

Task Class {
    constructor {
        -->task name
    }
    method {
        --> delete task 
        --> task description
        --> add task priority
    }
}


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
