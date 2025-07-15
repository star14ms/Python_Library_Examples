from module import Human

class_ai = [
    Human("김민서", 23, "Male"),
    Human("이지한", 17, "Male"),
    Human("노지완", 17, "Male"),
    Human("김시헌", 17, "Male"),
    Human("유채민", 17, "Female"),
    Human("이송민", 17, "Male"),
    Human("장준민", 17, "Male"),
    Human("김재원", 17, "Male"),
    Human("김재원", 17, "Male"),
    Human("임현서", 17, "Male"),
    Human("이재빈", 17, "Male"),
    Human("권태욱", 17, "Male"),
    Human("이동현", 17, "Male"),
    Human("임주원", 17, "Male"),
    Human("김성현", 17, "Male"),
    Human("강은성", 17, "Female"),
]


for student in class_ai:
    student.say_hello()
