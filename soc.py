import requests, json
import courseclass

 # Write your query or mutation here




def generateCourses(depart):
    body = {'query': 'query { \
        schedule(year:2023, quarter: "Spring", department: "'+depart+'", section_type: "LEC" ) \
                {course{\
                    department\
                    id\
                    school\
                    units\
                    number\
                    ge_list\
                    title\
                    }\
                meetings {\
                    building \
                    days \
                    time} \
                instructors{\
                    name\
                    } \
                section{ \
                    code\
                    type\
                    }\
                max_capacity \
                restrictions \
                status \
                final_exam\
                } \
            }'}
    headers ={"Content-Type": "application/json"}
    response = requests.post("https://api.peterportal.org/graphql", data=json.dumps(body), headers=headers)
    dpt_courses = response.json();
    return dpt_courses;


def json_extract(json_courses, course_list, department):
    all_courses = json_courses.get("data").get("schedule");
    for course in all_courses:
        if course:
            
            course_info = course.get("course");
            meetings = course.get("meetings")[0];
            instr_name = course.get("instructors")[0].get("name");
            section_code = course.get("section").get("code");
            secType = course.get("section").get("type");
            if course_info:
                id = course_info.get("id");
                title = (course_info.get("title"));
                school = course_info.get("school");
                units = course_info.get("units");
                number = course_info.get("number");
                ge_list = course_info.get("ge_list");
            if meetings:
                building = meetings.get("building");
                days = meetings.get("days");
                time = meetings.get("time");
            max_cap = course.get("max_capacity");
            status = course.get("staus");
            final_exam = course.get("final_exam");
            new_course = courseclass.Courses(id, number, school, units, building, days, time, max_cap, instr_name, section_code, ge_list, status, final_exam, department, secType, title);
            #print(new_course.toJSON());
            course_list.append(new_course);
    
    return course_list;






    
if __name__ == "__main__":
    departments = ["AC ENG", "AFAM", "ANATOMY",  "ANTHRO", "ARABIC", "ARMN", "ART", "ART HIS", "ARTS", "ARTSHUM", "ASIANAM", "BANA", 
"BATS", "BIO SCI", "BIOCHEM", "BME", "CBE", "CEM", "CHC/LAT", "CHEM", "CHINESE", "CLASSIC", "CLT&THY", "COGS", "COM LIT", 
"COMPSCI", "CRITISM", "CRM/LAW", "CSE", "DANCE", "DATA", "DEV BIO", "DRAMA", "EARTHSS", "EAS", "ECO EVO", "ECON", "ECPS",
"EDUC", "EECS", "EHS", "ENGLISH", "ENGR", "ENGRCEE", "ENGRMAE", "EPIDEM", "EURO ST", "FIN", "FLM&MDA", "FRENCH", "GDIM", 
"GEN&SEX", "GERMAN", "GLBL ME", "GLBLCLT", "GREEK", "HEBREW", "HINDI", "HISTORY", "HUMAN", "HUMARTS", "I&C SCI", "IN4MATX", "INNO",  
"INTL ST", "IRAN", "ITALIAN", "JAPANSE", "KOREAN", "LATIN", "LIT JRN", "LPS", "LSCI", "M&MG", "MATH","MGMT EP", "MGMT FE", "MGMT HC", "MGMTMBA", "MOL BIO", "MSE", "MUSIC", "NET SYS", "NEURBIO", "NUR SCI", "PED GEN", 
 "PERSIAN", "PHARM", "PHILOS", "PHMD", "PHRMSCI", "PHY SCI", "PHYSICS", "PHYSIO", "PLASTIC", "POL SCI",
  "PORTUG", "PSCI",  "PSYCH", "PUB POL", "PUBHLTH", "REL STD", "ROTC", "RUSSIAN", "SOC SCI", "SOCECOL", "SOCIOL", "SPANISH", "SPPS",
    "STATS", "SWE", "TAGALOG", "TOX", "UCDC", "UNI AFF", "UNI STU", "UPPP", "VIETMSE", "VIS STD", "WRITING"]
    course_list = [];
    # dpt_courses = generateCourses("PUBHLTH");
    # print(dpt_courses);
    # json_extract(dpt_courses, course_list);


    # for courses in course_list:
    #     courses.writeString();

    for depart in departments:
        dpt_courses = generateCourses(depart);
        print(depart);
        json_extract(dpt_courses, course_list, depart);
    
    f = open("socarray.txt", "a")
        
    for courses in course_list:
        f.write(courses.writeArray());
        #clean_json = json.dumps(course_list);
    f.close();
    #print(clean_json);