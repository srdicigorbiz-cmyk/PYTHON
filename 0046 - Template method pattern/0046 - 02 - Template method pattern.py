from abc import ABC, abstractmethod
class Jelentes(ABC):
    def fejlec(self):
        return "--- Fejléc ---"
    def lablec(self):
        return "--- Lábléc ---"
    @abstractmethod
    def tartalom(self):
        pass
    def keszit(self):
        print(self.fejlec())
        print(self.tartalom())
        return(self.lablec())
    
class PdfJelentes(Jelentes):
    def tartalom(self):
        return "ez egy pdf"
class ExcelJelentes(Jelentes):
    def tartalom(self):
        return "ez egy excel"
    
pdf = PdfJelentes()
excel = ExcelJelentes()
print(pdf.keszit())
print(excel.keszit())