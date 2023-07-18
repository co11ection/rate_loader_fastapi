from tortoise import fields, models


class InsuranceRate(models.Model):
    cargo_type = fields.CharField(max_length=255)
    rate = fields.FloatField()
    date = fields.DateField(auto_now_add=True)
