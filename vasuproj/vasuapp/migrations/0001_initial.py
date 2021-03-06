# Generated by Django 2.1.3 on 2018-12-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=64)),
                ('esal', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StaffingMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Eno', models.CharField(max_length=64, unique=True)),
                ('Ename', models.CharField(max_length=64)),
                ('DMName', models.CharField(default='Dummy Manager', max_length=64, null=True)),
                ('BudgetArea', models.CharField(default='Dummy Area', max_length=64, null=True)),
                ('IBMMailID', models.CharField(default='Dummy@in.ibm.com', max_length=64, null=True)),
                ('OfficeNumber', models.CharField(default='080-417-72392', max_length=64, null=True)),
                ('MobileNumber', models.CharField(default='999999999', max_length=64, null=True)),
                ('ClientMailID', models.CharField(default='Anthem@Anthem.com', max_length=64, null=True)),
            ],
        ),
    ]
