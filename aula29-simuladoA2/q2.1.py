#### Questão 2 - identificação de problemas


class BaseReport:
    def __init__(self, data):
        self.data = data
        self.last_export = None

    #Aqui, se viola o SRP, generate não apenas gera o relatório como também o imprime
    #Além disso, o OCP está quebrado, obriga subclasses a reescreverem o método, criando 
    # comportamentos divergentes.
    def generate(self):
        print("Gerando relatório base. A empresa... (texto do relatório)")
        return str(self.data)
    
    
class SalesReport(BaseReport):
    #aqui, se quebra o LSP: generate recebe mais de um parâmetro no filho, e isso quebra o programa
    # ao atribuir BaseReport a um objeto do tipo SalesReport. 
    #Além disso, a classe base printa, e algumas das outras não, causando inconsistências
    def generate(self, detailed=False):
        print("Gerando relatório de vendas. A empresa... (texto do relatório)")
        content = f"Vendas: {self.data}"
        if detailed:
            content += " (detalhado)"
        print(content)
        return content
    
class InventoryReport(BaseReport):
    def generate(self):
        print("Gerando relatório de estoque. A empresa... (texto do relatório)")
        return f"Estoque: {self.data}"
    
#Cada filho de BaseReport tem um tipo de retorno para a mesma coisa: um relatório
#Alguns retornam printando, outros por string, isso quebra o princípio de Liskov também. 
    
class ReportService:
    def __init__(self, report):
        self.report = report
        
    #Aqui, o OCP foi violado, porque um novo formato não pode ser adicionado sem a mudança da classe
    def export(self, fmt="pdf"):
        content = self.report.generate()
        if fmt == "pdf":
            blob = ("[PDF]" + content).encode("utf-8")
        elif fmt == "csv":
            blob = ("[CSV]" + content).encode("utf-8")  
        else:
            raise ValueError("Formato nao suportado")
        self.report.last_export = blob
        return blob
    
    def send(self, channel, target):
        #Aqui, se quebra o SRP, porque a função para enviar verifica se o report existe
        if self.report.last_export is None:
            self.export("pdf")
        payload = self.report.last_export
        if channel == "email":
            print(f"Enviando e-mail para {target}: {payload[:30]}...")
        elif channel == "slack":
            print(f"Postando no Slack #{target}: {payload[:30]}...")
        else:
            raise ValueError("Canal nao suportado")

class Communicator:
    #Aqui, é quebrado o ISP, há funções sem necessidade na classe, o que é inútil e deixa a OO ruim
    def send_email(self, payload, address):
        raise NotImplementedError
    def send_slack(self, payload, channel):
        raise NotImplementedError
    def send_sms(self, payload, phone):
        raise NotImplementedError


def main():
        sales = SalesReport(data=[10, 20, 30])
        service = ReportService(sales)
        blob = service.export(fmt="pdf")
        service.send(channel="email", target="financeiro@empresa.com")
        inv = InventoryReport(data={"SKU1": 5, "SKU2": 2})
        service2 = ReportService(inv)
        service2.export(fmt="csv")
        service2.send(channel="slack", target="relatorios")


if __name__ == "__main__":
    main()
    
#S: principio de responsabilidade unica
#O: Open closed
#L: Liskov - filhos e pais podem ser trocados
#I: Interfaces separadas, são os adjetivos de uma classe