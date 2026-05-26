class RegiAdatbazis:
    def db_connect(self, host):
        return f"Kapcsolódva: {host}"
    
    def db_query(self, sql):
        return f"Eredmény: {sql}"

class Adapter:
    def __init__(self, oldsys):
        self.oldsys=oldsys
    def kapcsolod(self, host):
        return self.oldsys.db_connect(host)
    def lekerdezes(self, sql):
        return self.oldsys.db_query(sql)

def kapcs(sys, host):
    return sys.kapcsolod(host)
def leker(sys, sql):
    return sys.lekerdezes(sql)

regi= RegiAdatbazis()
adapter = Adapter(regi)
print(kapcs(adapter, "1 allomas"))
print(leker(adapter, "sql bazis"))
