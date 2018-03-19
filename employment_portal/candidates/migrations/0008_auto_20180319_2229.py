# Generated by Django 2.0.1 on 2018-03-19 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0007_auto_20180318_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 3, 19, 22, 29, 21, 638660)),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills_choices_1',
            field=models.CharField(choices=[('Java', 'Java'), ('C', 'C'), ('Python', 'Python'), ('C#', 'C#'), ('Visual Basic .NET', 'Visual Basic .NET'), ('PHP', 'PHP'), ('JavaScript', 'JavaScript'), ('Delphi/Object Pascal', 'Delphi/Object Pascal'), ('Ruby', 'Ruby'), ('SQL', 'SQL'), ('Visual Basic', 'Visual Basic'), ('PL/SQL', 'PL/SQL'), ('Assembly language', 'Assembly language'), ('Swift', 'Swift'), ('Perl', 'Perl'), ('Go', 'Go'), ('MATLAB', 'MATLAB'), ('Content management', 'Content management'), ('Data presentation', 'Data presentation'), ('Database administration', 'Database administration'), ('Middleware and integration software', 'Middleware and integration software'), ('Mobile development', 'Mobile development'), ('Network and information security', 'Network and information security'), ('Software engineering', 'Software engineering'), ('Software management', 'Storage systems and management'), ('Tech support', 'Tech support'), ('User interface design', 'User interface design'), ('UI/UX', 'UI/UX'), ('Web architecture and development framework', 'Web architecture and development framework')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills_choices_10',
            field=models.CharField(choices=[('Java', 'Java'), ('C', 'C'), ('Python', 'Python'), ('C#', 'C#'), ('Visual Basic .NET', 'Visual Basic .NET'), ('PHP', 'PHP'), ('JavaScript', 'JavaScript'), ('Delphi/Object Pascal', 'Delphi/Object Pascal'), ('Ruby', 'Ruby'), ('SQL', 'SQL'), ('Visual Basic', 'Visual Basic'), ('PL/SQL', 'PL/SQL'), ('Assembly language', 'Assembly language'), ('Swift', 'Swift'), ('Perl', 'Perl'), ('Go', 'Go'), ('MATLAB', 'MATLAB'), ('Content management', 'Content management'), ('Data presentation', 'Data presentation'), ('Database administration', 'Database administration'), ('Middleware and integration software', 'Middleware and integration software'), ('Mobile development', 'Mobile development'), ('Network and information security', 'Network and information security'), ('Software engineering', 'Software engineering'), ('Software management', 'Storage systems and management'), ('Tech support', 'Tech support'), ('User interface design', 'User interface design'), ('UI/UX', 'UI/UX'), ('Web architecture and development framework', 'Web architecture and development framework')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills_choices_2',
            field=models.CharField(choices=[('Java', 'Java'), ('C', 'C'), ('Python', 'Python'), ('C#', 'C#'), ('Visual Basic .NET', 'Visual Basic .NET'), ('PHP', 'PHP'), ('JavaScript', 'JavaScript'), ('Delphi/Object Pascal', 'Delphi/Object Pascal'), ('Ruby', 'Ruby'), ('SQL', 'SQL'), ('Visual Basic', 'Visual Basic'), ('PL/SQL', 'PL/SQL'), ('Assembly language', 'Assembly language'), ('Swift', 'Swift'), ('Perl', 'Perl'), ('Go', 'Go'), ('MATLAB', 'MATLAB'), ('Content management', 'Content management'), ('Data presentation', 'Data presentation'), ('Database administration', 'Database administration'), ('Middleware and integration software', 'Middleware and integration software'), ('Mobile development', 'Mobile development'), ('Network and information security', 'Network and information security'), ('Software engineering', 'Software engineering'), ('Software management', 'Storage systems and management'), ('Tech support', 'Tech support'), ('User interface design', 'User interface design'), ('UI/UX', 'UI/UX'), ('Web architecture and development framework', 'Web architecture and development framework')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills_choices_3',
            field=models.CharField(choices=[('Java', 'Java'), ('C', 'C'), ('Python', 'Python'), ('C#', 'C#'), ('Visual Basic .NET', 'Visual Basic .NET'), ('PHP', 'PHP'), ('JavaScript', 'JavaScript'), ('Delphi/Object Pascal', 'Delphi/Object Pascal'), ('Ruby', 'Ruby'), ('SQL', 'SQL'), ('Visual Basic', 'Visual Basic'), ('PL/SQL', 'PL/SQL'), ('Assembly language', 'Assembly language'), ('Swift', 'Swift'), ('Perl', 'Perl'), ('Go', 'Go'), ('MATLAB', 'MATLAB'), ('Content management', 'Content management'), ('Data presentation', 'Data presentation'), ('Database administration', 'Database administration'), ('Middleware and integration software', 'Middleware and integration software'), ('Mobile development', 'Mobile development'), ('Network and information security', 'Network and information security'), ('Software engineering', 'Software engineering'), ('Software management', 'Storage systems and management'), ('Tech support', 'Tech support'), ('User interface design', 'User interface design'), ('UI/UX', 'UI/UX'), ('Web architecture and development framework', 'Web architecture and development framework')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills_choices_4',
            field=models.CharField(choices=[('Java', 'Java'), ('C', 'C'), ('Python', 'Python'), ('C#', 'C#'), ('Visual Basic .NET', 'Visual Basic .NET'), ('PHP', 'PHP'), ('JavaScript', 'JavaScript'), ('Delphi/Object Pascal', 'Delphi/Object Pascal'), ('Ruby', 'Ruby'), ('SQL', 'SQL'), ('Visual Basic', 'Visual Basic'), ('PL/SQL', 'PL/SQL'), ('Assembly language', 'Assembly language'), ('Swift', 'Swift'), ('Perl', 'Perl'), ('Go', 'Go'), ('MATLAB', 'MATLAB'), ('Content management', 'Content management'), ('Data presentation', 'Data presentation'), ('Database administration', 'Database administration'), ('Middleware and integration software', 'Middleware and integration software'), ('Mobile development', 'Mobile development'), ('Network and information security', 'Network and information security'), ('Software engineering', 'Software engineering'), ('Software management', 'Storage systems and management'), ('Tech support', 'Tech support'), ('User interface design', 'User interface design'), ('UI/UX', 'UI/UX'), ('Web architecture and development framework', 'Web architecture and development framework')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills_choices_5',
            field=models.CharField(choices=[('Java', 'Java'), ('C', 'C'), ('Python', 'Python'), ('C#', 'C#'), ('Visual Basic .NET', 'Visual Basic .NET'), ('PHP', 'PHP'), ('JavaScript', 'JavaScript'), ('Delphi/Object Pascal', 'Delphi/Object Pascal'), ('Ruby', 'Ruby'), ('SQL', 'SQL'), ('Visual Basic', 'Visual Basic'), ('PL/SQL', 'PL/SQL'), ('Assembly language', 'Assembly language'), ('Swift', 'Swift'), ('Perl', 'Perl'), ('Go', 'Go'), ('MATLAB', 'MATLAB'), ('Content management', 'Content management'), ('Data presentation', 'Data presentation'), ('Database administration', 'Database administration'), ('Middleware and integration software', 'Middleware and integration software'), ('Mobile development', 'Mobile development'), ('Network and information security', 'Network and information security'), ('Software engineering', 'Software engineering'), ('Software management', 'Storage systems and management'), ('Tech support', 'Tech support'), ('User interface design', 'User interface design'), ('UI/UX', 'UI/UX'), ('Web architecture and development framework', 'Web architecture and development framework')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills_choices_6',
            field=models.CharField(choices=[('Java', 'Java'), ('C', 'C'), ('Python', 'Python'), ('C#', 'C#'), ('Visual Basic .NET', 'Visual Basic .NET'), ('PHP', 'PHP'), ('JavaScript', 'JavaScript'), ('Delphi/Object Pascal', 'Delphi/Object Pascal'), ('Ruby', 'Ruby'), ('SQL', 'SQL'), ('Visual Basic', 'Visual Basic'), ('PL/SQL', 'PL/SQL'), ('Assembly language', 'Assembly language'), ('Swift', 'Swift'), ('Perl', 'Perl'), ('Go', 'Go'), ('MATLAB', 'MATLAB'), ('Content management', 'Content management'), ('Data presentation', 'Data presentation'), ('Database administration', 'Database administration'), ('Middleware and integration software', 'Middleware and integration software'), ('Mobile development', 'Mobile development'), ('Network and information security', 'Network and information security'), ('Software engineering', 'Software engineering'), ('Software management', 'Storage systems and management'), ('Tech support', 'Tech support'), ('User interface design', 'User interface design'), ('UI/UX', 'UI/UX'), ('Web architecture and development framework', 'Web architecture and development framework')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills_choices_7',
            field=models.CharField(choices=[('Java', 'Java'), ('C', 'C'), ('Python', 'Python'), ('C#', 'C#'), ('Visual Basic .NET', 'Visual Basic .NET'), ('PHP', 'PHP'), ('JavaScript', 'JavaScript'), ('Delphi/Object Pascal', 'Delphi/Object Pascal'), ('Ruby', 'Ruby'), ('SQL', 'SQL'), ('Visual Basic', 'Visual Basic'), ('PL/SQL', 'PL/SQL'), ('Assembly language', 'Assembly language'), ('Swift', 'Swift'), ('Perl', 'Perl'), ('Go', 'Go'), ('MATLAB', 'MATLAB'), ('Content management', 'Content management'), ('Data presentation', 'Data presentation'), ('Database administration', 'Database administration'), ('Middleware and integration software', 'Middleware and integration software'), ('Mobile development', 'Mobile development'), ('Network and information security', 'Network and information security'), ('Software engineering', 'Software engineering'), ('Software management', 'Storage systems and management'), ('Tech support', 'Tech support'), ('User interface design', 'User interface design'), ('UI/UX', 'UI/UX'), ('Web architecture and development framework', 'Web architecture and development framework')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills_choices_8',
            field=models.CharField(choices=[('Java', 'Java'), ('C', 'C'), ('Python', 'Python'), ('C#', 'C#'), ('Visual Basic .NET', 'Visual Basic .NET'), ('PHP', 'PHP'), ('JavaScript', 'JavaScript'), ('Delphi/Object Pascal', 'Delphi/Object Pascal'), ('Ruby', 'Ruby'), ('SQL', 'SQL'), ('Visual Basic', 'Visual Basic'), ('PL/SQL', 'PL/SQL'), ('Assembly language', 'Assembly language'), ('Swift', 'Swift'), ('Perl', 'Perl'), ('Go', 'Go'), ('MATLAB', 'MATLAB'), ('Content management', 'Content management'), ('Data presentation', 'Data presentation'), ('Database administration', 'Database administration'), ('Middleware and integration software', 'Middleware and integration software'), ('Mobile development', 'Mobile development'), ('Network and information security', 'Network and information security'), ('Software engineering', 'Software engineering'), ('Software management', 'Storage systems and management'), ('Tech support', 'Tech support'), ('User interface design', 'User interface design'), ('UI/UX', 'UI/UX'), ('Web architecture and development framework', 'Web architecture and development framework')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills_choices_9',
            field=models.CharField(choices=[('Java', 'Java'), ('C', 'C'), ('Python', 'Python'), ('C#', 'C#'), ('Visual Basic .NET', 'Visual Basic .NET'), ('PHP', 'PHP'), ('JavaScript', 'JavaScript'), ('Delphi/Object Pascal', 'Delphi/Object Pascal'), ('Ruby', 'Ruby'), ('SQL', 'SQL'), ('Visual Basic', 'Visual Basic'), ('PL/SQL', 'PL/SQL'), ('Assembly language', 'Assembly language'), ('Swift', 'Swift'), ('Perl', 'Perl'), ('Go', 'Go'), ('MATLAB', 'MATLAB'), ('Content management', 'Content management'), ('Data presentation', 'Data presentation'), ('Database administration', 'Database administration'), ('Middleware and integration software', 'Middleware and integration software'), ('Mobile development', 'Mobile development'), ('Network and information security', 'Network and information security'), ('Software engineering', 'Software engineering'), ('Software management', 'Storage systems and management'), ('Tech support', 'Tech support'), ('User interface design', 'User interface design'), ('UI/UX', 'UI/UX'), ('Web architecture and development framework', 'Web architecture and development framework')], max_length=100, null=True),
        ),
    ]
