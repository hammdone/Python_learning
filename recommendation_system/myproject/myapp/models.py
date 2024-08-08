from django.db import models

class UserInteraction(models.Model):
    user_id = models.IntegerField()
    vendor_id = models.IntegerField()

    class Meta:
        db_table = 'user_interactions'

class VendorCluster(models.Model):
    cluster_id = models.IntegerField()
    vendor_id = models.IntegerField()

    class Meta:
        db_table = 'vendor_clusters'
