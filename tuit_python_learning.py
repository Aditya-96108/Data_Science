
def get_student_data() :
    return [
        {'name': 'Manuj', 'scores': [85,90,95]},
        {'name':'Pranav', 'scores': [78,80,72]},
        {'name': 'Aditya', 'scores': [88,85,91]},
    ]


def analyze_performance(students):
    result={}
    for student in students :
        name = student['name']
        avg = calculate_average(student['scores'])
        result[name]=avg
    return result

def calculate_average(scores):
    return sum(scores)/len(scores)


def display_results(results):
    print("Average Scores are : ")
    for name in results :
        print(name + " , " + str(round(results[name],2)))

def main():
    student_data = get_student_data()
    average_scores= analyze_performance(student_data)
    display_results(average_scores)

main()