def gs_matching_engine(hospital_prefs, student_prefs):
    free_hospitals = set(hospital_prefs.keys())
    free_students = set(student_prefs.keys())

    hospital_match = {h: None for h in hospital_prefs.keys()}
    student_match = {s: None for s in student_prefs.keys()}

    next_proposal_index = {h: 0 for h in hospital_prefs.keys()}

    num_proposals = 0

    while free_hospitals:
        h = free_hospitals.pop()

        if next_proposal_index[h] >= len(hospital_prefs[h]):
            continue

        a = hospital_prefs[h][next_proposal_index[h]]
        next_proposal_index[h] += 1
        num_proposals += 1

        if a in free_students:
            hospital_match[h] = a
            student_match[a] = h
            free_students.remove(a)

        else:
            h_prime = student_match[a]
            rank_h = student_prefs[a].index(h)
            rank_h_prime = student_prefs[a].index(h_prime)

            if rank_h < rank_h_prime:
                hospital_match[h] = a
                student_match[a] = h
                hospital_match[h_prime] = None
                free_hospitals.add(h_prime)
            else:
                free_hospitals.add(h)

    return hospital_match, num_proposals


def read_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        hospital_prefs = {}
        student_prefs = {}

        for i in range(n):
            line = f.readline().strip().split()
            preferences = [int(x) for x in line]
            hospital_id = i + 1
            hospital_prefs[hospital_id] = preferences

        for i in range(n):
            line = f.readline().strip().split()
            preferences = [int(x) for x in line]
            student_id = i + 1
            student_prefs[student_id] = preferences

    return hospital_prefs, student_prefs


def write_output(filename, matching, n):
    with open(filename, 'w') as f:
        for hospital_id in range(1, n + 1):
            student_id = matching[hospital_id]
            f.write(f"{hospital_id} {student_id}\n")

if __name__ == "__main__":
    input_file = "../data/example.in"
    output_file = "../data/example.out"
    hospital_prefs, student_prefs = read_input(input_file)
    n = len(hospital_prefs)
    matching, proposals = gs_matching_engine(hospital_prefs, student_prefs)
    write_output(output_file, matching, n)
    print(f"Matching written to {output_file}")
    print(f"Number of proposals: {proposals}")