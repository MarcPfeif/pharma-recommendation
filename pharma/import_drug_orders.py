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
                admission_date=order[7],
                reorder=order[8],
                order_date=order[9],
                MAR_start_date=order[10],
                MAR_end_date=order[11],
                order_hold_start_date=order[12],
                order_hold_end_date=order[13],
                discontinued_date=order[14],
                order_created_by=order[15],
                order_created_date=order[16],
                order_created_by_user_long_name=order[17],
                order_revision_by=order[18],
                order_revision_by_date=order[19],
                physician_id=order[20],
                physician_first_name=order[21],
                physician_last_name=order[22],
                PRN=order[23],
                pharmacy_name=order[24],
                order_category_id=order[25],
                order_category=order[26],
                order_type_id=order[27],
                order_type=order[28],
                communication_method=order[29],
                order_description=order[30],
                related_generic=order[31],
                advanced_directive=order[32],
                pharmacy_medication_name=order[33],
                strength=order[34],
                strength_UOM=order[35],
                form=order[36],
                dose=order[37],
                diet_supplement=order[38],
                diet_type_id=order[39],
                diet_texture=order[40],
                fluid_consistency=order[41],
                route_of_admin=order[42],
                quantity_to_administer=order[43],
                directions=order[44],
                related_diagnoses=order[45],
                indications_for_use=order[46],
                nurse_admin_notes=order[47],
                wt_vital=order[48],
                resp_vital=order[49],
                BPV_vital=order[50],
                temp_vital=order[51],
                pulse_vital=order[52],
                BS_vital=order[53],
                O2_vital=order[54],
                ht_vital=order[55],
                facility_id=order[56],
                vitals_description=order[57],
                value=order[58],
                BP_vitals_description=order[59],
                BP_value=order[60],
                BPD_diastolic_value=order[61],
                facility_name=order[62],
                allergy=order[63],
                NCSP_pho_phys_order=order[64],
            )
            self.con.execute(insert_stmt)
