def pascal_row(prev=None):
  return [1] + [prev[i]+prev[i+1] for i in range(len(prev)-1)] + [1] if prev or prev == [] else [1]


if __name__ == "__main__":
    n = int(input())
    row = []
    for x in range(n):
        row = pascal_row(row)
        print(*row)

