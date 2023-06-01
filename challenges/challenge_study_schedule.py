# permanence_period = [(1, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]


def is_integer(time):
    return isinstance(time[0], int) and isinstance(time[1], int)


def study_schedule(permanence_period, target_time):
    sum = 0
    if isinstance(target_time, int) == False:
        return None

    for student_times in permanence_period:
        if is_integer(student_times) == False:
            return None

        if student_times[0] <= target_time <= student_times[1]:
            sum += 1
    return sum


# print(study_schedule(permanence_period, 4))
