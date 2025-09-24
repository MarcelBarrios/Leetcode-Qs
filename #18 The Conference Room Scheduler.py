# You're an intern at a bustling tech company, and your first project is to build an 
# automated scheduling system for a single, highly sought-after conference room. You 
# are given a list of all the meeting requests for the day. Each request is an 
# interval with a start_time and an end_time.

# Your manager's goal is to maximize the number of meetings that can be held in this'
# ' room. However, there's a constraint: you cannot approve two meetings that overlap
# in time. For example, if one meeting is from 10 AM to 12 PM, you cannot approve
# another meeting that starts at 11 AM. A meeting that starts exactly when another 
# one ends is permissible (e.g., a 9-10 AM meeting and a 10-11 AM meeting are fine).

# Your task is to write a program that takes the list of all requested meeting times 
# and returns the maximum number of non-overlapping meetings that can be scheduled 
# for the day.

def schedule_meetings(meetings):
    """
    Calculates the maximum number of non-overlapping meetings that can be scheduled.

    :param meetings: A list of lists, where each inner list is [start_time, end_time].
    :return: The maximum number of meetings that can be scheduled.
    """
    # If there are no meetings, we can't schedule any.
    if not meetings:
        return 0

    # Sort the meetings based on their end time (the second element in the list).
    # This is the crucial greedy choice.
    meetings.sort(key=lambda x: x[1])

    # Schedule the first meeting (the one that finishes earliest).
    scheduled_meetings_count = 1
    # Keep track of the end time of the last meeting we scheduled.
    last_meeting_end_time = meetings[0][1]

    # Iterate through the rest of the meetings.
    for i in range(1, len(meetings)):
        current_meeting_start_time = meetings[i][0]
        
        # If the current meeting starts after or at the same time the last one ended,
        # it's a compatible, non-overlapping meeting.
        if current_meeting_start_time >= last_meeting_end_time:
            # Schedule this meeting.
            scheduled_meetings_count += 1
            # Update the end time to reflect this new meeting.
            last_meeting_end_time = meetings[i][1]
            
    return scheduled_meetings_count

# Example Usage:
meeting_requests = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [8, 9]]
max_meetings = schedule_meetings(meeting_requests)
print(f"The maximum number of meetings that can be scheduled is: {max_meetings}") # Expected output: 3
# O(n log n)