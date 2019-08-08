class Empleado:
    def __init__(self):
        self.codigo=""
        self.nombre=""
        self.apellido=""
        self.salario_base=""
    def Calcular_retencion(self):
        re= (self.salario_base*0.1)
        return re
    def Mostar_nombrecompleto(self):
        print(self.nombre+" "+self.apellidos)

    def Calcular_salario_neto(self):
        auxtran =97.032
        salnet=self.salario_base+auxtran


emp=Empleado()
emp.codigo=float(input("Digite su codigo"))
emp.nombre=(input("Digite su nombre"))
emp.apellido=(input("Digite su apellido"))
emp.salario_base=float(input("Digite su salario"))


print(emp.Calcular_retencion())

