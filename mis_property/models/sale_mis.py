# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class PropertySaleMIS(models.Model):
    _name = 'property.sale.mis'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sale MIS'

    _sql_constraints = [
        ('unique_name', 'unique(name)',
         "SO Number must be Unique!"),
    ]

    name = fields.Char(string="SO Number", required=True, index=True)
    company_group = fields.Char(string="Group", required=True)
    class_price = fields.Char(string="Class for Price")
    rs_date = fields.Date(string="RS Date", required=True)
    rs_year = fields.Integer(string="RS Year", store=True, compute="_get_rs_date")
    rs_month = fields.Integer(string="RS Month", store=True, compute="_get_rs_date")
    so_type = fields.Char(string="SO Type")
    customer_name = fields.Char(string="Customer Name", required=True, index=True)
    dp_percent = fields.Float(string="DP", help="In Percent", group_operator="avg")
    dp_terms = fields.Integer(string="DP Term", help="No. of Months", group_operator="avg")
    full_dp_schedule_date = fields.Date(string="Full DP (Schedule Date)")
    actual_full_dp_date = fields.Date(string="Full DP (Actual Date)")
    tcp = fields.Float(string="TCP", help="Total Contract Price", group_operator="sum")
    ntcp = fields.Float(string="NTCP", help="Net Total Contract Price", group_operator="sum")
    mcc = fields.Float(string="MCC", group_operator="sum")
    vat = fields.Float(string="VAT", group_operator="sum")
    ntcp_m = fields.Float(string="NTCP in M", help="In Million", store=True, compute="_get_ntcp_m", group_operator="sum")
    dp_amount = fields.Float(string="DP Amount", group_operator="sum")
    la_amount = fields.Float(string="LA Amount", group_operator="sum")
    be_code = fields.Char(string="BE Code", help="Project or BE Code", required=True, index=True)
    project_name = fields.Char(string="Project Name", required=True, index=True)
    block_lot = fields.Char(string="Block/Lot", required=True)
    lot_area = fields.Float(string="Lot Area")
    unit_type = fields.Char(string="Unit Type")
    house_status = fields.Char(string="House/Unit Status")
    house_model = fields.Char(string="House Model")
    floor_area = fields.Float(string="Floor Area")
    house_series = fields.Char(string="House Series", help="House Series for Profiling")
    financing_type = fields.Char(string="Financing Type")
    brand = fields.Char(string="Brand")
    brand_group = fields.Char(string="Brand Group")
    division_group = fields.Char(string="Division Group")
    sub_division = fields.Char(string="Sub-Division")
    count_number = fields.Integer(string="Count No.")
    condo_cost = fields.Float(string="Lot/Condo Cost", group_operator="sum")
    tcp_m = fields.Float(string="TCP in M", help="In Million", store=True, compute="_get_tcp_m", group_operator="sum")
    island = fields.Char(string="Island")
    cluster_i = fields.Char(string="Cluster 1")
    cluster_ii = fields.Char(string="Cluster 2")
    cluster_iii = fields.Char(string="Cluster 3")
    region = fields.Char(string="Region")
    province = fields.Char(string="Province")
    city = fields.Char(string="City")
    legal_class_city = fields.Char(string="Legal Class City")
    city_class = fields.Char(string="City Class")
    group_a = fields.Char(string="Group A")
    group_b = fields.Char(string="Group B")
    tcp_sqm = fields.Float(string="TCP per Sqm", store=True, compute="_get_tcp_sqm", group_operator="sum")
    # Not Sure if still Needed
    qtr_reporting = fields.Char(string="Qtr Reporting")
    # What is the Purpose?
    grouping_new = fields.Char(string="New Grouping")
    tcp_sqm_new = fields.Float(string="TCP per Sqm (New)", group_operator="sum")
    # Weird sample data
    condo_class = fields.Char(string="Condo Class")
    x_bool = fields.Boolean(string="X (boolean)")
    employment = fields.Char(string="Employment")
    condo_category = fields.Char(string="Condo Category")
    house_ncp = fields.Float(string="House NCP", group_operator="sum")
    lot_ncp = fields.Float(string="Lot NCP", group_operator="sum")
    house_ncp_m = fields.Float(string="House NCP in M", store=True, compute="_get_house_ncp_m", group_operator="sum")
    lot_ncp_m = fields.Float(string="Lot NCP in M", store=True, compute="_get_lot_ncp_m", group_operator="sum")
    house_tcp = fields.Float(string="House TCP", group_operator="sum")
    lot_tcp = fields.Float(string="Lot TCP", group_operator="sum")
    house_tcp_m = fields.Float(string="House TCP in M", store=True, compute="_get_house_tcp_m", group_operator="sum")
    lot_tcp_m = fields.Float(string="Lot TCP in M", store=True, compute="_get_lot_tcp_m", group_operator="sum")
    house_tcp_sqm = fields.Float(string="House TCP per Sqm", store=True, compute="_get_house_tcp_sqm", group_operator="sum")
    lot_tcp_sqm = fields.Float(string="Lot TCP per Sqm", store=True, compute="_get_lot_tcp_sqm", group_operator="sum")

    @api.depends('tcp')
    def _get_tcp_m(self):
        for r in self:
            r.tcp_m = r.tcp > 0 and r.tcp / 1000000.00 or 0

    @api.depends('ntcp')
    def _get_ntcp_m(self):
        for r in self:
            r.ntcp_m = r.ntcp > 0 and r.ntcp / 1000000.00 or 0

    @api.depends('tcp', 'lot_area', 'floor_area')
    def _get_tcp_sqm(self):
        for r in self:
            r.tcp_sqm = (r.tcp > 0 and (r.lot_area + r.floor_area) > 0) and r.tcp / (r.lot_area + r.floor_area) or 0

    @api.depends('lot_ncp')
    def _get_lot_ncp_m(self):
        for r in self:
            r.lot_ncp_m = r.lot_ncp > 0 and r.lot_ncp / 1000000.00 or 0

    @api.depends('house_ncp')
    def _get_house_ncp_m(self):
        for r in self:
            r.house_ncp_m = r.house_ncp > 0 and r.house_ncp / 1000000.00 or 0

    @api.depends('lot_tcp')
    def _get_lot_tcp_m(self):
        for r in self:
            r.lot_tcp_m = r.lot_tcp > 0 and r.lot_tcp / 1000000.00 or 0

    @api.depends('house_tcp')
    def _get_house_tcp_m(self):
        for r in self:
            r.house_tcp_m = r.house_tcp > 0 and r.house_tcp / 1000000.00 or 0

    @api.depends('house_tcp', 'floor_area')
    def _get_house_tcp_sqm(self):
        for r in self:
            r.house_tcp_sqm = (r.house_tcp > 0 and r.floor_area > 0) and r.house_tcp / r.floor_area or 0

    @api.depends('lot_tcp', 'lot_area')
    def _get_lot_tcp_sqm(self):
        for r in self:
            r.lot_tcp_sqm = (r.lot_tcp > 0 and r.lot_area > 0) and r.lot_tcp / r.lot_area or 0

    @api.depends('rs_date')
    def _get_rs_date(self):
        for r in self:
            if r.rs_date:
                r.rs_year = r.rs_date.year
                r.rs_month = r.rs_date.month
            else:
                r.rs_year = 0
                r.rs_month = 0

