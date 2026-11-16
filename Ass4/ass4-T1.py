def forward_chaining():

    symptoms_no=int(input("Enter no. of symptoms: "))

    facts=set()

    for _ in range(symptoms_no):
        fact=str(input("Enter disease: "))
        facts.add(fact)


    rules=[({"fever","cough"},"flu"),
          ({"fever","flu"},"dengue"),
          ({"fever","cough","body_pain"},"severe flu")]

    print()

    new_facts=True

    while True:
        new_facts=False

        for condition,conclusion in rules:
            if condition.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                print("New disease: ",conclusion)
                new_facts=True

        if new_facts==False:
            break

    print("\nAll disease: ",facts)

   
   
def backward_chaining():

    facts = set()

    symptoms_no = int(input("Enter no. of symptoms: "))

    for _ in range(symptoms_no):
        fact = str(input("Enter symptom: "))
        facts.add(fact)

    rules = [
        ({"fever", "cough"}, "flu"),
        ({"fever", "flu"}, "dengue"),
        ({"fever", "cough", "body_pain"}, "severe flu")
    ]

    goal = input("Enter disease to check: ")

    def prove(goal):
       
        if goal in facts:
            return True

       
        for condition, conclusion in rules:
            if conclusion == goal:
                print("Checking:", goal)

               
                for fact in condition:
                    if not prove(fact):
                        return False

                print("Proved:", goal)
                return True

       
        return False

    print()

    if prove(goal):
        print("\nDisease is present:", goal)
    else:
        print("\nDisease cannot be proved:", goal)


choice=int(input("Enter choice: "))
if choice==1:
    forward_chaining()
elif choice==2:
    backward_chaining()

