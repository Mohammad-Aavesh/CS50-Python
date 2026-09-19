import project

list1 = ["Kunal", "Aman", "Tara", "Priya", "Zoya", "Sahil", "Riya"]
list2 = [78.0, 92.0, 45.0, 88.0, 67.0, 95.0]
list3 = ["Indore", "Bhopal", "Indore", "Gwalior", "Bhopal", "Indore", "Gwalior"]
list4 = [10.0, 20.0, 30.0, 40.0, 50.0]


def test_calculations():
    assert project.calculations(list1) == ['Categoric', '7',
                                           ['Aman', 'Kunal', 'Priya', 'Riya', 'Sahil', 'Tara', 'Zoya'],
                                           [['Aman', '1'], ['Kunal', '1'], ['Priya', '1'], ['Riya', '1'], ['Sahil', '1'], ['Tara', '1'], ['Zoya', '1']]]
    assert project.calculations(list2) == ['Numeric', '6', '465.0', '77.5', '83.0', '95.0', '45.0']
    assert project.calculations(list3) == ['Categoric', '3', ['Bhopal', 'Gwalior', 'Indore'], [
        ['Bhopal', '2'], ['Gwalior', '2'], ['Indore', '3']]]
    assert project.calculations(list4) == ['Numeric', '5', '150.0', '30.0', '30.0', '50.0', '10.0']


def test_numerical_calculations():
    assert project.numerical_calculations(sorted(list2)) == [
        'Numeric', '6', '465.0', '77.5', '83.0', '95.0', '45.0']
    assert project.numerical_calculations(sorted(list4)) == [
        'Numeric', '5', '150.0', '30.0', '30.0', '50.0', '10.0']
    assert project.numerical_calculations(sorted([])) == ["None"]


def test_categorical_calculations():
    assert project.categorical_calculations(sorted(list1)) == ['Categoric', '7',
                                                               ['Aman', 'Kunal', 'Priya', 'Riya',
                                                                   'Sahil', 'Tara', 'Zoya'],
                                                               [['Aman', '1'], ['Kunal', '1'], ['Priya', '1'], ['Riya', '1'], ['Sahil', '1'], ['Tara', '1'], ['Zoya', '1']]]
    assert project.categorical_calculations(sorted(list3)) == ['Categoric', '3', [
        'Bhopal', 'Gwalior', 'Indore'], [['Bhopal', '2'], ['Gwalior', '2'], ['Indore', '3']]]


def test_median_calculator():
    assert project.median_calculator(sorted(list2)) == "83.0"
    assert project.median_calculator(sorted(list4)) == "30.0"
