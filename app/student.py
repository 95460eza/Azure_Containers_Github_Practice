import json


class Student:
    def __init__(self, request, redis_db) -> None:
        self.request = request
        self.redis = redis_db
        self.students = []
        self.ID = "Id"
        self.FIRST_NAME = "First name"
        self.LAST_NAME = "Last name"
        self.BIRTHDAY = "Date of Birth"
        self.COURSE = "Course"

    def get_values(self):
        self.id = str(self.request.form.getlist(self.ID)[0])
        self.first_name = self.request.form.getlist(self.FIRST_NAME)[0]
        self.last_name = self.request.form.getlist(self.LAST_NAME)[0]
        self.birthday = self.request.form.getlist(self.BIRTHDAY)[0]
        #self.birthday = '1970-09-15'
        # Validate birthday format
        # try:
        #     # Attempt to parse the birthday string into a datetime object
        #     birthday_date = datetime.strptime(self.birthday, "%Y-%m-%d")
        # except ValueError:
        #     # If parsing fails, raise an error indicating incorrect format
        #     raise ValueError("Invalid birthday format. Please provide the date in YYYY-MM-DD format.")
        self.course = self.request.form.getlist(self.COURSE)[0]

        self.INFO = {
            self.FIRST_NAME: self.first_name,
            self.LAST_NAME: self.last_name,
            self.BIRTHDAY: self.birthday,
            self.COURSE: self.course,
        }

    def __hmset__(self):
        self.redis.hmset(self.id, self.INFO)

    def __hmget__(self, id, value):
        return self.redis.hmget(id, value)

    def get_ids(self):
        return self.redis.keys("*")

    def student_id_exist(self):
        res = self.redis.hgetall(self.id)
        if res:
            return True
        else:
            return False

    def record_student(self):
        if not self.student_id_exist():
            self.__hmset__()
            return None
        else:
            return "error"

    def get_all_students(self):
        ids = self.get_ids()
        for id in ids:
            student = {}
            student[self.ID] = id.decode("utf-8")
            student[self.FIRST_NAME] = self.__hmget__(id, self.FIRST_NAME)[0].decode("utf-8")
            student[self.LAST_NAME] = self.__hmget__(id, self.LAST_NAME)[0].decode( "utf-8" )
            student[self.BIRTHDAY] = self.__hmget__(id, self.BIRTHDAY)[0].decode( "utf-8" )
            student[self.COURSE] = self.__hmget__(id, self.COURSE)[0].decode("utf-8" )
            self.students.append(student)
        return self.students
