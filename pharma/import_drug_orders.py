''' import_drug_orders.py '''


''' ImportDrugOrders '''
class ImportDrugOrders:
    def __init__(self, con, meta):
        ## database connection
        self.con = con

        ## table structure
        self.meta = meta

    def process_orders(self, orders):
        for order in orders:
            print(order[7])
            '''
            insert_stmt = insert(meta.tables['pcc_drugorders']).values(
                jazz_id=contact['id'],
                type=contact['type'],
                last_name=contact['last_name'],
                first_name=contact['first_name'],
                email=contact['email']
            )
            '''
