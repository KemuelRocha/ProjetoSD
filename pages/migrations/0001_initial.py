# Generated by Django 4.0.1 on 2022-03-29 15:04

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telefone', models.CharField(max_length=12)),
                ('tipo_usuario', models.CharField(choices=[('pessoa', 'Pessoa'), ('profissional', 'Profissional'), ('empresa', 'Empresa')], max_length=12)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('cnpj', models.IntegerField(primary_key=True, serialize=False)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(choices=[('BA', 'Bahia'), ('PE', 'Pernambuco')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('cpf', models.IntegerField(primary_key=True, serialize=False)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=255, verbose_name='Área do serviço')),
                ('valorDiaria', models.FloatField(null=True)),
                ('valorHora', models.FloatField(null=True)),
                ('periodo', models.CharField(choices=[('Hora', 'Pagamento por hora'), ('Dia', 'Pagamento por dia')], max_length=4)),
                ('profissional', models.ManyToManyField(to='pages.Profissional')),
            ],
        ),
        migrations.CreateModel(
            name='EmpXServ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiencia', models.IntegerField()),
                ('avaliacao', models.IntegerField()),
                ('empresa_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.empresa')),
                ('serv_pk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.servico')),
            ],
        ),
        migrations.CreateModel(
            name='ContratoPessXProf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('duracaoHora', models.IntegerField()),
                ('pessoa_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.pessoa')),
                ('prof_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.profissional')),
            ],
        ),
        migrations.CreateModel(
            name='ContratoEmpXProf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('duracaoHora', models.IntegerField()),
                ('empresa_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.empresa')),
                ('profissional_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.profissional')),
            ],
        ),
        migrations.CreateModel(
            name='ContratoEmpXPess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('duracaoHora', models.IntegerField()),
                ('empresa_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.empresa')),
                ('pessoa_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='endereco',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.endereco'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
