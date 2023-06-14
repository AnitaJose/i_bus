from django.db import models

# Create your models here.


class CollegeBranch(models.Model):
    """Model for cc_data table."""

    branch_name = models.CharField(max_length=250)

    def __str__(self):
        return self.branch_name

    class Meta:
        """Override the table name."""

        db_table = 'college_branch'
