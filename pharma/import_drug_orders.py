''' import_drug_orders.py '''


''' ImportDrugOrders '''
class ImportDrugOrders:
    def __init__(self, con, meta):
        ## database connection
        self.con = con

        ## table structure
        self.meta = meta

    def process_orders(self, orders):
        pass
