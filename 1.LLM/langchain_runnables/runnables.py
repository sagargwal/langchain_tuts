class nalkiprompt():
    def __init__(self,template,input_variable):
        self.template = template
        self.input_varible = input_variable
    
    def format(self,input_dict):
        return self.template.format(**input_dict)


prompt = nalkiprompt(
    template = "mera naam {name} hai,mae {age} saal ka hu",
    input_variable= ["haldwani","bageshwar"]
)
result = prompt.format({"name": "sagar","age" : "25"})

print(result)