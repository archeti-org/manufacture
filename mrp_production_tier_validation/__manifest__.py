# Copyright 2021 ArcheTI
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Manufacturing Order Tier Validation",
    "summary": "Extends the functionality of Manufacturing Order to "
    "support a tier validation process.",
    "version": "14.0.1.0.0",
    "category": "Manufacture",
    "website": "https://github.com/OCA/manufacture",
    "author": "ArcheTI, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["mrp", "base_tier_validation"],
    "data": ["views/mrp_production_views.xml"],
}
