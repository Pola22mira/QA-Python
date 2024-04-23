from smartphone import Smartphone
        
samsung1 = Smartphone('Samsung1', 'S11', '+79991234567')
samsung2 = Smartphone('Samsung2', 'S22', '+79993214567')
samsung3 = Smartphone('Samsung3', 'S33', '+71234567890')
samsung4 = Smartphone('Samsung4', 'S44', '+72345678901')
samsung5 = Smartphone('Samsung5', 'S55', '+73456789012')


catalog = [samsung1, samsung2, samsung3, samsung4, samsung5]
for example in catalog:
    example = example.printAllCatalog()
    
#или:
#catalog = [samsung1.printAllCatalog(), samsung2.printAllCatalog(), samsung3.printAllCatalog(), samsung4.printAllCatalog(), samsung5.printAllCatalog()]