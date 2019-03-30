import psycopg2


def create_db(name, fields):
    table_fields = ', '.join(fields)
    with psycopg2.connect('dbname=netology_homework user=homeworker password=qwerty123') as conn:
        with conn.cursor() as cur:
            cur.execute(f'create table {name} ({table_fields})')


# fields_for_student = ['id integer NOT NULL', 'name character varying(100) NOT NULL', \
#                       'gpa numeric(10,2)', ' birth timestamp with time zone']
# create_db('student', fields_for_student)

# fields_for_course = ['id integer NOT NULL', 'name character varying(100) NOT NULL']
# create_db('course', fields_for_course)

# fields_for_course = ['id serial PRIMARY KEY', 'student_id integer', 'course_id integer']
# create_db('student_course', fields_for_course)


def get_students(course_id):
    with psycopg2.connect('dbname=netology_homework user=homeworker password=qwerty123') as conn:
        with conn.cursor() as cur:
            cur.execute('select student.id, student.name, student_course.course_id, course.name from student join student_course \
            on student.id = student_course.student_id join course on course.id = student_course.course_id \
            where course.id = %s', (course_id,))
            print(cur.fetchall())


# get_students(1)


def add_students(course_id, students):
    with psycopg2.connect('dbname=netology_homework user=homeworker password=qwerty123') as conn:
        with conn.cursor() as cur:
            for student in students:
                student_id = student['id']
                student_name = student['name']
                student_gpa = student['gpa']
                student_birth = student['birth']
                cur.execute('insert into student (id, name, gpa, birth) values (%s, %s, %s, %s) returning name',
                            (student_id, student_name, student_gpa, student_birth))
                cur.execute('insert into student_course (student_id, course_id) values (%s, %s)',
                            (student_id, course_id,))


# students = [
#     {
#         'id': 555,
#         'name': 'Иван Иванов',
#         'gpa': 6.1,
#         'birth': '01.02.1977'
#     },
#     {
#         'id': 444,
#         'name': 'Петр Петров',
#         'gpa': 6.1,
#         'birth': '02.11.1987'
#     },
#     {
#         'id': 333,
#         'name': 'Бори Борисов',
#         'gpa': 1.5,
#         'birth': '03.12.1997'
#     }
# ]
#
# add_students(1,students)


def add_student(student):
    student_id = student['id']
    student_name = student['name']
    student_gpa = student['gpa']
    student_birth = student['birth']
    with psycopg2.connect('dbname=netology_homework user=homeworker password=qwerty123') as conn:
        with conn.cursor() as cur:
            cur.execute('insert into student (id, name, gpa, birth) values (%s, %s, %s, %s) returning name',
                        (student_id, student_name, student_gpa, student_birth))
            print(cur.fetchone())


# student = {
#     'id': 27,
#     'name': 'Test777  Test55',
#     'gpa': 5.88,
#     'birth': '12.08.1999'
# }
#
# add_student(student)


def get_student(student_id):
    with psycopg2.connect('dbname=netology_homework user=homeworker password=qwerty123') as conn:
        with conn.cursor() as cur:
            cur.execute('select student.name from student where student.id = %s', (student_id,))
            print(cur.fetchall())

# get_student(555)
