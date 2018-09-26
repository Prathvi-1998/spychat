class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.is_online=True
        self.current_status_message = None


spy=Spy('Prathvi','Mr',19,3.0)
friend1 = Spy('Ankit','mr',22,3.0)
friend2 = Spy('yuvraj','mr',24,4.0)
friend3 = Spy('shivam','mr',19,2.0)
friend = [friend1,friend2,friend3]
