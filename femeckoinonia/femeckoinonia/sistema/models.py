from django.db import models

# Create your models here.
class Umec(models.Model):
    church = models.CharField(verbose_name='Igreja:',max_length=100)
    initials = models.CharField(verbose_name='Sigla',max_length=10,default='')
    address = models.CharField(verbose_name='Endereco:',max_length=200,default='')

    def __str__(self):
        return self.church

    class Meta:
        verbose_name = 'UMEC'
        verbose_name_plural = 'UMECs'


class BoardFemec(models.Model):

    OFFICE_CHOICES = (
        ('president', 'Presidente'),
        ('vice-president', 'Vice Presidente'),
        ('first-treasurer', '1 Tesoureiro(a)'),
        ('second-treasurer', '2 Tesoureiro(a)'),
        ('first-secretary', '1 Secretário(a)'),
        ('second-secretary', '2 Secretário(a)'),
        ('counselor', 'Conselheiro(a)'),
    )

    name = models.CharField(verbose_name='Nome',max_length=100)
    office = models.CharField(verbose_name='Cargo',
                            max_length=20,
                            choices=OFFICE_CHOICES)
    date = models.DateField(verbose_name='Data de Nascimento',
                            help_text='Preencha no formato: dia/mês/ano. Ex: 24/07/1993')
    fone = models.CharField(verbose_name='Telefone:',max_length=30, default='')
    email = models.CharField(verbose_name='Email:',max_length=50, default='')
    address = models.CharField(verbose_name='Endereco:',max_length=150, default='')
    

    def office_verbose(self):
        return dict(BoardFemec.OFFICE_CHOICES)[self.office]

    def __str__(self):
        return '%s (%s)' % (self.name, self.office_verbose)

    class Meta:
        verbose_name = 'Componente da diretoria'
        verbose_name_plural = 'Diretoria Femec'


class BoardUmec(models.Model):

    OFFICE_CHOICES = (
        ('president', 'Presidente'),
        ('vice-president', 'Vice Presidente'),
        ('first-treasurer', '1 Tesoureiro(a)'),
        ('second-treasurer', '2 Tesoureiro(a)'),
        ('first-secretary', '1 Secretário(a)'),
        ('second-secretary', '2 Secretário(a)'),
        ('counselor', 'Conselheiro(a)'),
    )

    name = models.CharField(verbose_name='Nome:',max_length=60)
    office = models.CharField(verbose_name='Cargo',
                            max_length=20,
                            choices=OFFICE_CHOICES)
    date = models.DateField(verbose_name='Data de Nascimento',
                            help_text='Preencha no formato: dia/mês/ano. Ex: 24/07/1993')
    fone = models.CharField(verbose_name='Telefone:',max_length=30, default='')
    email = models.CharField(verbose_name='Email:',max_length=30, default='')
    address = models.CharField(verbose_name='Endereco:',max_length=150, default='')

    def office_verbose(self):
        return dict(BoardUmec.OFFICE_CHOICES)[self.office]

    def __str__(self):
        return '%s (%s)' % (self.name, self.office_verbose)

    class Meta:
        verbose_name = 'Componente da diretoria'
        verbose_name_plural = 'Diretoria Umec'