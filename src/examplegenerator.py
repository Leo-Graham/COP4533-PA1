import random


def generate_input_file(n, filename):
    with open(filename, 'w') as f:
        f.write(f"{n}\n")

        for i in range(n):
            preferences = list(range(1, n + 1))
            random.shuffle(preferences)
            f.write(" ".join(map(str, preferences)) + "\n")

        for i in range(n):
            preferences = list(range(1, n + 1))
            random.shuffle(preferences)
            f.write(" ".join(map(str, preferences)) + "\n")

if __name__ == "__main__":
    n_values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    for n in n_values:
        filename = f"example_{n}.in"
        generate_input_file(n, filename)