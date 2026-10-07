needs_user_input = True

study_plan = {}

while needs_user_input:
    subject = input("Enter subject name: ")
    if not subject:
        needs_user_input = False
        break
    valid_allocated_time = False
    while not valid_allocated_time:
        try:
            allocated_time = input(f"Enter time allocated for {subject}: ")
            if not allocated_time:
                needs_user_input = False
                break
            allocated_time = int(allocated_time)
            if allocated_time < 0:
                raise ValueError
            valid_allocated_time = True
            study_plan[subject] = allocated_time
        except ValueError:
            print("Please enter a valid time in minutes.")

if study_plan.keys():
    print(study_plan)
