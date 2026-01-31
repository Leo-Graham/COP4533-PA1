import time

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

    return n, hospital_prefs, student_prefs


def read_matching(filename, n):
    matching = {}

    with open(filename, 'r') as f:
        for i in range(n):
            line = f.readline().strip().split()
            hospital_id = int(line[0])
            student_id = int(line[1])
            matching[hospital_id] = student_id

    return matching


def check_validity(matching, n):
    if len(matching) != n:
        return False

    for hospital_id in matching.keys():
        if hospital_id < 1 or hospital_id > n:
            return False

    for student_id in matching.values():
        if student_id < 1 or student_id > n:
            return False

    student_counts = {}
    for hospital_id, student_id in matching.items():
        if student_id in student_counts:
            return False
        student_counts[student_id] = hospital_id

    if len(student_counts) != n:
        matched_students = set(student_counts.keys())
        all_students = set(range(1, n + 1))
        missing_students = all_students - matched_students
        return False, f"Some students are not matched: {missing_students}"

    return True, "Matching is valid"


def check_stability(matching, hospital_prefs, student_prefs, n):
    student_matching = {}
    for hospital_id, student_id in matching.items():
        student_matching[student_id] = hospital_id

    for h in range(1, n + 1):
        for s in range(1, n + 1):
            current_student_of_h = matching[h]
            current_hospital_of_s = student_matching[s]

            if current_student_of_h == s:
                continue

            h_prefs = hospital_prefs[h]
            rank_s = h_prefs.index(s)
            rank_current = h_prefs.index(current_student_of_h)
            h_prefers_s = rank_s < rank_current

            s_prefs = student_prefs[s]
            rank_h = s_prefs.index(h)
            rank_current = s_prefs.index(current_hospital_of_s)
            s_prefers_h = rank_h < rank_current

            if h_prefers_s and s_prefers_h:
                return False, (h, s)

    return True, None


def verify_matching(input_file, matching_file):
    n, hospital_prefs, student_prefs = read_input(input_file)

    matching = read_matching(matching_file, n)

    is_valid, validity_info = check_validity(matching, n)

    if not is_valid:
        print(f"INVALID: {validity_info}")
        return

    is_stable, blocking_pair = check_stability(matching, hospital_prefs, student_prefs, n)

    if is_stable:
        print("VALID STABLE")
    else:
        h, s = blocking_pair
        print(f"UNSTABLE: Hospital {h} and Student {s} form a blocking pair")


if __name__ == "__main__":
    input_file = "../data/example.in"
    matching_file = "../data/example.out"
    start = time.time()
    verify_matching(input_file, matching_file)
    end = time.time()
    print(f"Time elapsed: {end - start:.9f} seconds")