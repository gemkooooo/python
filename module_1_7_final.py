grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#сортируем по алфавиту
students = sorted(students)
#{'Aaron', 'Johnny', 'Bilbo', 'Khendrik', 'Steve'}

averageRatingS0 = sum(list(map(float, grades[0])))/len(list(map(float, grades[0])))
averageRatingS1 = sum(list(map(float, grades[1])))/len(list(map(float, grades[1])))
averageRatingS2 = sum(list(map(float, grades[2])))/len(list(map(float, grades[2])))
averageRatingS3 = sum(list(map(float, grades[3])))/len(list(map(float, grades[3])))
averageRatingS4 = sum(list(map(float, grades[4])))/len(list(map(float, grades[4])))

averageRating = (averageRatingS0, averageRatingS1, averageRatingS2, averageRatingS3, averageRatingS4)

print(dict(zip(students, averageRating)))



