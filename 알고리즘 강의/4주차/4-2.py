def max_meetings(meetings):
    meetings.sort(key=lambda x: x[1])

    max_count = 0
    last_end_time = 0

    for start, end in meetings:
        if start >= last_end_time: 
            max_count += 1
            last_end_time = end

    return max_count

meetings = [(0, 6), (1, 4), (3, 5), (3, 8), (5, 7), (8, 9)]
print(max_meetings(meetings))