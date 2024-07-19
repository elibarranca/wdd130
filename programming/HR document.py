with open ("hr_system.txt") as f:
    for line in f:
        clean_line =line.strip( )
        parts = clean_line.split(" ")

    name = parts [0]
    id_number = parts[1]
    title = parts[2]
    salary = float(parts [3])
    
    pay = salary/24

    if title.lower() == "engineer":
        pay += 1000

    print(f"Name: {name} (ID: {id_number}), Title: {title} - Salary: ${pay:.2f}")