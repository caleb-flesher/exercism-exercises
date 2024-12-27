def is_valid(isbn):
    # Using Rakeshksr's solution (which is beautiful)
    nums = list(isbn.replace("-", ""))
    if len(nums) != 10: return False
    if nums[-1] == "X": nums[-1] = 10

    # Needed to cast c to string to use isdigit()
    if not all(str(c).isdigit() for c in nums): return False
    return sum(int(x) * y for x, y in zip(nums, range(10, 0, -1))) % 11 == 0