# Name: Donavan McFadden
# Student ID: Donmcf8357
# Date: October 27, 2026
# Assignment: 4.7 Performance Assessment - Advanced Pandas and Charting
# Description: This program stores a pretend roster of 10 students in an
# array. It uses a MultiIndex to pair each student with Math and Science,
# builds a DataFrame of their grades, groups the grades to find the average
# for each subject, and shows the averages in a vertical bar graph.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    print("Student ID: Donmcf8357")  # Start the program by printing my Student ID

    # Store the classroom roster of 10 students in an array
    studentRoster = np.array(["Ava", "Brandon", "Carmen", "Darius", "Elena",
                              "Felix", "Grace", "Hassan", "Imani", "Jordan"])
    subjectList = ["Math", "Science"]  # The two subjects each student is graded in

    # Step 3: Create an index for student and subject using the MultiIndex function
    gradeIndex = pd.MultiIndex.from_product([studentRoster, subjectList],  # Pair every student with every subject
                                            names=["Student", "Subject"])  # Name the two index levels

    # Step 4: Create a DataFrame of grades for each student in the two subjects
    gradeList = [95, 88, 82, 91, 90, 79, 76, 85, 98, 93,  # Math, Science grades for the first 5 students
                 84, 80, 89, 94, 92, 87, 78, 83, 96, 90]  # Math, Science grades for the last 5 students
    gradeTable = pd.DataFrame({"Grade": gradeList}, index=gradeIndex)  # Build the DataFrame using the MultiIndex

    # Step 5: Display the DataFrame
    print("\nClassroom Grades")  # Print a heading for the DataFrame
    print(gradeTable)  # Show every student's Math and Science grade

    # Step 6: Group by subject and find the mean grade for each subject
    subjectAverages = gradeTable.groupby(level="Subject").mean()  # Average the grades for each subject
    print("\nAverage Grade by Subject")  # Print a heading for the averages
    print(subjectAverages.round(2))  # Show the averages rounded to two decimal places

    # Display the vertical bar graph of the subject averages
    subjectAverages.plot(kind="bar", legend=False, rot=0, figsize=(5.5, 4))  # Make a vertical bar for each subject
    plt.title("Average Grade by Subject - Donmcf8357")  # Add a title with my Student ID
    plt.xlabel("Subject")  # Label the x-axis
    plt.ylabel("Average Grade")  # Label the y-axis
    plt.tight_layout()  # Keep the labels from getting cut off
    plt.show()  # Display the bar graph window


main()  # Call main() to run the program
