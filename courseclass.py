import json

class Courses:
    def __init__(self, id, number, school, units, building, day, time, max_cap, instr_name, code, ge_list, status, final_exam, department, secType, title):
        self.id = id;
        self.number = number;
        self.school = school;
        self.units = units;
        self.building = building;
        self.day = day;
        self.time = time;
        self.max_cap = max_cap;
        self.instr_name = instr_name;
        self.code = code;
        self.ge_list = ge_list;
        self.status = status;
        self.final_exam = final_exam;
        self.department = department;
        self.secType = secType;
        self.title = title;

    def writeArray(self):
        formatted = "{ \n"
        formatted +=  f'     name: \"{self.id}\",\n     number: \"{self.number}\",\n     school: \"{self.school}\",\n     units: {self.units[0]},\
                            \n     building: \"{self.building}\",\n     time: \"{self.day} {self.time}\",\
                            \n     max_cap: {self.max_cap},\n     instructor: \"{self.instr_name}\",\
                            \n     code: \"{self.code}\",\n     ge_list: {self.ge_list},\n     status: \"{self.status}\",\n     final_exam: \"{self.final_exam}\",\
                            \n     department: \"{self.department}\",\n     secType: \"{self.secType}\",\n     title: \"{self.title}\"';
        formatted += "\n},\n";
        return formatted;
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)