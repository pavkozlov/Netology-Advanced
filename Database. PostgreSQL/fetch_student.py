import psycopg2

PARAMS = '''dbname=netology_homework 
            user=homeworker 
            password=qwerty123'''


def create_db():
    with psycopg2.connect(PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute('''create table if not exists student (
                        id serial PRIMARY KEY,
                        name character varying(100) NOT NULL,
                        gpa numeric(10,2),
                        birth timestamp with time zone)''')
            cur.execute('''create table if not exists course (
                        id serial PRIMARY KEY,
                        name character varying(100) NOT NULL)''')
            cur.execute('''create table if not exists student_course (
                        id integer,
                        student_id integer references student(id) ON DELETE CASCADE,
                        course_id integer references course(id) ON DELETE CASCADE)''')


def get_students(course_id):
    with psycopg2.connect(PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute('select student.id, student.name, student_course.course_id, course.name from student join student_course \
                        on student.id = student_course.student_id join course on course.id = student_course.course_id \
                        where course.id = %s', (course_id,))
            return cur.fetchall()


def add_student(student):
    with psycopg2.connect(PARAMS) as conn:
        with conn.cursor() as cur:
            command_for_add_student(cur, student)


def command_for_add_student(cursor, student):
    cursor.execute('insert into student (name, gpa, birth) values (%s, %s, %s) RETURNING id',
                   (student['name'], student['gpa'], student['birth']))
    return cursor.fetchone()[0]


def add_students(course_id, students):
    with psycopg2.connect(PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute('select * from course where course.id = %s', (course_id,))
            course_in_list = cur.fetchone()
            if course_in_list:
                course_id = course_in_list[0]
                for student in students:
                    id = command_for_add_student(cur, student)
                    cur.execute('insert into student_course (student_id, course_id) values (%s, %s)',
                                (id, course_id,))
            else:
                raise Exception('Нет такого курса')


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

test_student = {
    'name': 'Test777  Test55',
    'gpa': 5.88,
    'birth': '12.08.1999'
}


def get_student(student_id):
    with psycopg2.connect(PARAMS) as conn:
        with conn.cursor() as cur:
            cur.execute('select student.name from student where student.id = %s', (student_id,))
            return cur.fetchone()


if __name__ == '__main__':
    create_db()

    add_student(test_student)
    add_students(88, students)

    get_by_course = get_students(3)

    get_by_id = get_student(2)
