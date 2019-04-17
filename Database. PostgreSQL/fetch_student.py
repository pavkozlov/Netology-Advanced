import psycopg2

PARAMS = 'dbname=netology_homework user=homeworker password=qwerty123'


def create_db():
    with psycopg2.connect(PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute(
                'create table student (id serial PRIMARY KEY, name character varying(100) NOT NULL, gpa numeric(10,2))')
            cur.execute('create table course (id serial PRIMARY KEY, name character varying(100) NOT NULL)')
            cur.execute('create table student_course (id serial PRIMARY KEY, student_id integer, course_id integer)')


# create_db()


def get_students(course_id):
    with psycopg2.connect(PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute('select student.id, student.name, student_course.course_id, course.name from student join student_course \
            on student.id = student_course.student_id join course on course.id = student_course.course_id \
            where course.id = %s', (course_id,))
            return cur.fetchall()


print(get_students(1))


def add_student(student):
    with psycopg2.connect(PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute('select * from student where student.name = %s AND student.birth = %s AND student.gpa = %s',
                        (student['name'], student['birth'], student['gpa'],))
            student_is_in = cur.fetchone()
            if student_is_in:
                print('Такой студент уже есть')
            else:
                cur.execute('insert into student (name, gpa, birth) values (%s, %s, %s) returning id',
                            (student['name'], student['gpa'], student['birth']))
                print('created id:', cur.fetchone()[0])


def add_students(course, students):
    with psycopg2.connect(PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute('select * from course where course.name = %s', (course['name'],))
            course_is_in = cur.fetchone()
            if course_is_in:
                print('Такой курс уже есть')
                course_id = course_is_in[0]
            else:
                cur.execute('insert into course (name) values (%s)', (course['name'],))
                cur.execute('select * from course where course.name = %s', (course['name'],))
                new_course = cur.fetchone()
                course_id = new_course[0]
            for student in students:
                cur.execute('select * from student where student.name = %s AND student.birth = %s AND student.gpa = %s',
                            (student['name'], student['birth'], student['gpa'],))
                student_is_in = cur.fetchone()
                if student_is_in:
                    print('Такой студент уже есть')
                else:
                    cur.execute('insert into student (name, gpa, birth) values (%s, %s, %s) returning id',
                                (student['name'], student['gpa'], student['birth']))
                    print('created id:', cur.fetchone()[0])

                cur.execute('select * from student where student.name = %s AND student.birth = %s AND student.gpa = %s',
                            (student['name'], student['birth'], student['gpa'],))
                std = cur.fetchone()
                cur.execute('select * from student_course where student_course.student_id = %s \
                             AND student_course.course_id = %s', (std[0], course_id,))
                stunden_course_is_in = cur.fetchone()
                if stunden_course_is_in:
                    print('Такая запись уже есть')
                else:
                    cur.execute('insert into student_course (student_id, course_id) values (%s, %s)',
                                (std[0], course_id,))


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

course = {
    'name': 'PY-21'
}

add_students(course, students)

student = {
    'name': 'Test777  Test55',
    'gpa': 5.88,
    'birth': '12.08.1999'
}

add_student(student)


def get_student(student_id):
    with psycopg2.connect(PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute('select student.name from student where student.id = %s', (student_id,))
            return cur.fetchone()


print(get_student(2))
