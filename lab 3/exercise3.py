# A construction project requires two workers to complete. 
# Worker A can complete the project in 12 hours, while Worker B can complete the same project in 16 hours. 
# How long will it take for both workers to complete the project if they work together?
# Another project requires Worker C, who can complete it in 8 hours, and Worker D, who can complete it in 10 hours. 
# How long will it take for both workers to complete this project if they work together?
# Write a simple, generic Python program to assist in calculating the time required for two workers 
# to complete a project when working together. The program must take all these numbers (12, 16) as input 
# and calculate the required time. Finally, print the result. 
# Please note that the same program must work for the second problem as well (8, 10).

WorkRate_WorkerA = int(input ("Please enter work rate for Worker A:"))
WorkRate_WorkerB = int(input ("Please enter work rate for Worker B:"))

TotalRateA_B = (1 / WorkRate_WorkerA) + (1 / WorkRate_WorkerB)
TimeComplete_project =float( 1 / TotalRateA_B)

print (f"Time complete for worker A and worker B:{TimeComplete_project:.2f}")