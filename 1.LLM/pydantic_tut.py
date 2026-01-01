'''pydanatic is a data validation and data parsing library for python, it ensures that the data you work with is correct, structured and type safe'''
from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name : str = "sagar"# here we are declaring that this is how schema should be
# and "sagar is default so if i am not puting anything in student object as name"
    age : Optional[int] = None# here i am puting a option that user dont neccesarily have to share thier age and defualt is NONE
    email: EmailStr # this only allows email as input
    cgpa : float = Field(gt = 0, lt =10 ,default = 5, description= "this feild tells about the students cgpa and how they have performed this sem")# this allowes you to set a default range 

# here i should give str but i am giving int so that i could see that this gives error
new_student = {"name":"sagar","email":"sagargwal34@gmail.com","cgpa": 7}
student = Student(**new_student)# ** is for unfolding the dictionary its like giving the dict itself
student_dict = dict(student)

print(student_dict)
# error output
# Input should be a valid string [type=string_type, input_value=32, input_type=int]
