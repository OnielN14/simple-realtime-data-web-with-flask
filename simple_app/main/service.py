from .schema import ToDo

class ToDoService:
    def __init__(self):
        self.model = ToDo()

    def create(self, req):
        self.model.create(req)
        

    def update(self, req):
        # self.model.update(req)
        print(req)
        return req

    def delete(self, req):
        # self.model.delete(req)
        print(req)
        return req

    def retrieve(self):
        return self.model.retrieve()