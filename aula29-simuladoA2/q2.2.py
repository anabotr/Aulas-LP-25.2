#### Questão 2 - refatoramento

from abc import ABC, abstractmethod

class BaseReport(ABC):
    def __init__(self, data):
        self.data = data
        self.last_export = None

    @abstractmethod
    def generate(self, detailed = False) -> str :...
    
    
class SalesReport(BaseReport):
    def generate(self, detailed : bool = False) -> str:
        print("Gerando relatório de vendas. A empresa... (texto do relatório)")
        content = f"Vendas: {self.data}"
        if detailed:
            content += " (detalhado)"
        return content
    
class InventoryReport(BaseReport):
    def generate(self, detailed = False) -> str:
        print("Gerando relatório de estoque. A empresa... (texto do relatório)")
        content = f"Estoque: {self.data}"
        if detailed:
            content += " (detalhado)"
        return content
    
class ReportService:
    fmts = {"pdf": "[PDF]", "csv": "[CSV]"}
    channels = {"email": "e-mail", "slack": "Slack"}

    def __init__(self, report : str):
        self.report = report
    
    @classmethod
    def add_fmt(cls, fmt : tuple):
        if fmt[0] not in cls.fmts:
            cls.fmts[fmt[0]] = fmt[1]
        
    def export(self, fmt : str ="pdf"):
        content = self.report.generate()
        if fmt not in self.__class__.fmts:
            raise ValueError("Formato nao suportado")
        else:
            blob = (self.__class__.fmts[fmt] + content).encode("utf-8") 
            self.report.last_export = blob
            return blob
    
    @classmethod
    def add_channel(cls, channel : tuple) -> None:
        if channel[0] not in cls.channels:
            cls.channels[channel[0]] = channel[1]

    def send(self, channel, target) -> None:
        payload = self.report.last_export
        if payload is None:
            raise RuntimeError("Relatório não exportado antes do envio")
        
        if channel not in self.__class__.channels:
            raise ValueError("Canal nao suportado")
        else:
            print(f"Enviando {self.__class__.channels[channel]} para {target}: {payload[:30]}...")

class email_sender(ABC):
    @abstractmethod
    def send_email(self, payload, address): ...

class slack_sender(ABC):
    @abstractmethod
    def send_slack(self, payload, channel): ...

class sms_sender(ABC):
    @abstractmethod
    def send_sms(self, payload, phone): ...
    
class Communicator(email_sender, slack_sender, sms_sender):
    pass


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
    