class Model(object):
    services = {
                 'email': {'number': 1000, 'price': 2,},
                 'sms': {'number': 1000, 'price': 10,},
                 'voice': {'number': 1000, 'price': 15,},
}
class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')
    def list_pricing(self, services):
        for svc in services:
            print("For" , Model.services[svc]['number'],svc, "message you pay $", Model.services[svc]['price'])

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))
class Client(object):
    controller = Controller()
    print("Services Provided:")
    controller.get_services()
    print("Pricing for Services:")
    controller.get_pricing()


# General


class Model(object):
    def logic(self):
        data = 'Got it!'
        print("Model: Crunching data as per business logic")
        return data
    
class View(object):
    def update(self, data):
        print("View: Updating the view with results: ", data)
        
class Controller(object):
    def __init__(self):
        self.model = Model()   
        self.view = View()
    def interface(self):
        print("Controller: Relayed the Client asks")
        data = self.model.logic()
        self.view.update(data)
        
class Client(object):
    print("Client: asks for certain information")
    controller = Controller()
    controller.interface()