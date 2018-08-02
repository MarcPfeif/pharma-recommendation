''' import_drug_orders.py '''

from sqlalchemy.dialects.postgresql import insert


''' ImportDrugOrders '''
class ImportDrugOrders:
    def __init__(self, con, meta):
        ## database connection
        self.con = con

        ## table structure
        self.meta = meta

    def process_orders(self, orders):
        for order in orders:
            insert_stmt = insert(self.meta.tables['pcc_drugorders']).values(
                pcc_drug_order_id=order[0],
                client_id=order[1],
                phys_order_id=order[2],
                patient_number=order[3],
                patient_first_name=order[4],
                patient_last_name=order[5],
                current_census_id=order[6],
                admission_date=order[7]
            )
            '''
            reorder=order[8],
            MAR_start_date=order[9],
            MAR_end_date=order[10],
            order_hold_start_date=order[11],
            order_hold_end_date=order[12],
            discontinued_date=order[13],
            order_created_by=order[14],
            order_created_date=order[15],
            order_created_by_user_long_name=order[16],
            order_revision_by=order[17],
            order_revision_by_date=order[18],
            physician_id=order[19],
            physician_first_name=order[20],
            physician_last_name=order[21],
            PRN=order[22],
            pharmacy_name=order[23],
            order_category_id=order[24],
            order_category=order[25],
            order_type_id=order[26],
            order_type=order[27],
            communication_method=order[28],
            order_description=order[29],
            related_generic=order[30],
            advanced_directive=order[31],
            pharmacy_medication_name=order[32],
            strength=order[33],
            strength_UOM=order[34],
            form=order[35],
            dose=order[36],
            diet_supplement=order[37],
            diet_type_id=order[38],
            diet_texture=order[39],
            fluid_consistency=order[40],
            route_of_admin=order[41],
            quantity_to_administer=order[42],
            directions=order[43],
            related_diagnoses=order[44],
            indications_for_use=order[45],
            nurse_admin_notes=order[46],
            wt_vital=order[47],
            resp_vital=order[48],
            BPV_vital=order[49],
            temp_vital=order[50],
            pulse_vital=order[51],
            BS_vital=order[52],
            O2_vital=order[53],
            ht_vital=order[54],
            facility_id=order[55],
            vitals_description=order[56],
            value=order[57],
            BPD_value=order[58],
            BPD_diastolic_value=order[59],
            facility_name=order[60],
            allergy=order[61],
            NCSP_pho_phys_order=order[62],
            '''
            self.con.execute(insert_stmt)
