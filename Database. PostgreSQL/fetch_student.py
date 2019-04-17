import psycopg2

PARAMS = '''dbname=netology_homework 
            user=homeworker 
            password=qwerty123'''


def create_db():
    with psycopg2.connect(PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute('''create table student (
                        id serial PRIMARY KEY,
                        name character varying(100) NOT NULL,
                        gpa numeric(10,2),
                        birth timestamp with time zone)''')
            cur.execute('''create table course (
                        id serial PRIMARY KEY,
                        name character varying(100) NOT NULL)''')
            cur.execute('''create table student_course (
                        id serial PRIMARY KEY,
                        student_id integer references student(id),
                        course_id integer references course(id))''')


def get_students(cur, course_id):
    cur.execute('select student.id, student.name, student_course.course_id, course.name from student join student_course \
                on student.id = student_course.student_id join course on course.id = student_course.course_id \
                where course.id = %s', (course_id,))
    return cur.fetchall()


def add_student(cur, student):
    cur.execute('insert into student (name, gpa, birth) values (%s, %s, %s)', (student['name'], student['gpa'], student['birth']))


def add_students(cur, course, students):
    cur.execute('select * from course where course.name = %s', (course['name'],))
    course_in_list = cur.fetchone()

    if course_in_list:
        course_id = course_in_list[0]
    else:
        cur.execute('insert into course (name) values (%s) returning id', (course['name'],))
        course_id = cur.fetchone()[0]

    students_ids = list()
    for student in students:
        cur.execute('insert into student (name, gpa, birth) values (%s, %s, %s) returning id', (student['name'], student['gpa'], student['birth']))
        students_ids.append(cur.fetchone()[0])

    for id in students_ids:
        cur.execute('insert into student_course (student_id, course_id) values (%s, %s)', (id, course_id,))


students = [
    {
        'name': 'Иван Иванов',
        'gpa': 6.1,
        'birth': '01.02.1977'
    },
    {
        'name': 'Петр Петров',
        'gpa': 6.1,
        'birth': '02.11.1987'
    },
    {
        'name': 'Бори Борисов',
        'gpa': 1.5,
        'birth': '03.12.1997'
    }
]

test_course = {
    'name': 'PY-21'
}


test_student = {
    'name': 'Test777  Test55',
    'gpa': 5.88,
    'birth': '12.08.1999'
}


def get_student(cur, student_id):
    cur.execute('select student.name from student where student.id = %s', (student_id,))
    return cur.fetchone()



if __name__ == '__main__':
    try:
        create_db()
    except psycopg2.errors.DuplicateTable as err:
        print('Такие таблицы уже существуют')

    with psycopg2.connect(PARAMS) as conn:
        with conn.cursor() as cur:
            add_student(cur, test_student)
            add_students(cur, test_course, students)

            get_by_course = get_students(cur, 1)
            print(get_by_course)

            get_by_id = get_student(cur, 2)
            print(get_by_id)
