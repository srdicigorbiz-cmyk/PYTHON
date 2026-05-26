from abc import ABC, abstractmethod
class State(ABC):
    @abstractmethod
    def publish(self, document):
        pass
    @abstractmethod
    def rollback(self, document):
        pass
class Draft(State):
    def publish(self, document):
        document.allapot = ModerationState()
        return "A dokumentum Moderation allapotba kerult."
    def rollback(self, document):
        return "A dokumentum már Draft allapotban van."
class ModerationState(State):
    def publish(self, document):
        document.allapot = PublishState()
        return "A dokumentum Publish allapotba kerult"
    def rollback(self, document):
        document.allapot = Draft()
        return "A dokumentum Draft allapotba kerult"
class PublishState(State):
    def publish(self, document):
        return "A dokumentum mar publish allapotban van"
    def rollback(self, document):
        document.allapot = ModerationState()
        return "A dokumentum Moderation allapotba kerult"
class Dokument:
    def __init__(self):
        self.allapot = Draft()
    def publish(self):
        return self.allapot.publish(self)
    def rollback(self):
        return self.allapot.rollback(self)
    
dok = Dokument()
print(dok.publish())
print(dok.publish())
print(dok.publish())
print(dok.rollback())
print(dok.rollback())
print(dok.rollback())