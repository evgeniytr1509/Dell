def get_grade(key):
    if key == "F" or key == "FX" or key == "E" or key == "D" or key == "C" or key == "B" or key == "A":
        s1 = {"F" : 1, "FX" : 2, "E" : 3, "D" : 3, "C" : 4, "B" : 5, "A" : 5}
        print (s1 [key])
    else:
        return None
get_grade("E")


def get_description(key):
    if key == "F" or key == "FX" or key == "E" or key == "D" or key == "C" or key == "B" or key == "A":
        s2 = {"F" : "Unsatisfactorily", "FX" : "Unsatisfactorily", "E" : "Enough", "D" : "Satisfactorily", "C" : "Good", "B" : "Very good", "A" : "Perfectly"}
        print (s2 [key])
    else:
        return None

get_description("E")