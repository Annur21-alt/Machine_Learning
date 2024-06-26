def time_to_complete_project(time_worker1, time_worker2):
    # Calculate the combined work rate
    combined_rate = 1 / time_worker1 + 1 / time_worker2
    
    # Calculate the time required for both workers to complete the project together
    time_required = 1 / combined_rate
    
    return time_required

# Example 1: Worker A (12 hours) and Worker B (16 hours)
time_project1 = time_to_complete_project(12, 16)
print(f"Time required for Worker A and Worker B to complete the project together: {time_project1:.2f} hours")

# Example 2: Worker C (8 hours) and Worker D (10 hours)
time_project2 = time_to_complete_project(8, 10)
print(f"Time required for Worker C and Worker D to complete the project together: {time_project2:.2f} hours")