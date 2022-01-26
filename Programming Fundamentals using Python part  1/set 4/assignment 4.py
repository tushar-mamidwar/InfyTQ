"""
Problem Statement
Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
{
"P":"Pediatrics",
"O":"Orthopedics",
"E":"ENT
}

Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.

Note:

Assume that there is always only one medical speciality which is visited by maximum number of patients.

Perform case sensitive string comparison wherever necessary.

Sample Input                                     Expected Output

[101,P,102,O,302,P,305,P]                           Pediatrics

[101,O,102,O,302,P,305,E,401,O,656,O]               Orthopedics

[101,O,102,E,302,P,305,P,401,E,656,O,987,E]             ENT
"""

# lex_auth_012693816757551104165


def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    # write your logic here
    patient_count = {"P": 0, "O": 0, "E": 0}
    for i in range(1, len(patient_medical_speciality_list), 2):
        patient_count[patient_medical_speciality_list[i]] += 1
    max_key = ""
    max_value = 0
    for speciality, frequency in patient_count.items():
        if frequency > max_value:
            max_value = frequency
            max_key = speciality
    return medical_speciality[max_key]
    return speciality


# provide different values in the list and test your program
patient_medical_speciality_list = [301, "P", 302, "P", 305, "P", 401, "E", 656, "E"]
medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality(patient_medical_speciality_list, medical_speciality)
print(speciality)
