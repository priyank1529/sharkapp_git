from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# from stdimage.models import StdImageField
# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    objects = CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email


class Base(models.Model):
    create = models.DateTimeField("Created", auto_now_add=True)
    modified = models.DateTimeField("Modified", auto_now=True)
    active = models.BooleanField("Active", default=True)

    class Meta:
        abstract: bool = True


# class Services(Base):
#     icons = (
#         ("lni-cog", "Engrenagem"),
#         ("lni-stats-up", "Grafico"),
#         ("lni-users", "Usuários"),
#         ("lni-layers", "Design"),
#         ("lni-mobile", "Mobile"),
#         ("lni-rocket", "Foguete"),
#     )
#     service = models.CharField("Service", max_length=100)
#     description = models.TextField("Description", max_length=100)
#     icon = models.CharField("Icon", max_length=12, choices=icons)

#     class Meta:
#         verbose_name = 'Service'
#         verbose_name_plural = "Services"


#     def __str__(self) -> str:
#         return str(self.service)

    

#     class Profission(Base):
#        profission = models.CharField("Profission", max_length=100)

#        class Meta:
#         verbose_name = 'Profission'
#         verbose_name_plural = 'Profissionals'

#         def __str__(self) -> str:
#             return str(self.profission)


# class Team(Base):
#     name = models.CharField("Name", max_length=100)
#     profission = models.ForeignKey('Profission', verbose_name='Profission',
#                                    on_delete=models.CASCADE)
#     description = models.TextField("Description", max_length=200)
#     image = models.ImageField("Image", upload_to='team')
#     facebook = models.CharField('Facebook', max_length=100, default='#')
#     twitter = models.CharField('Twitter', max_length=100, default='#')
#     instagram = models.CharField('Instagram', max_length=100, default='#')

#     class Meta:
#         verbose_name = 'Employee'
#         verbose_name_plural = 'Teams'


#     def __str__(self) -> str:
#         return str(self.name)



class Sharks(Base):
    shark_name=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    shark_image=models.ImageField(upload_to='team',blank=True,null=True)
    net_worth=models.DecimalField(max_digits=15,decimal_places=2)

    def __str__(self):
        return self.shark_name
class Pitcher(Base):
      pitcher=models.CharField(max_length=100)
      def __str__(self):
         self.pitcher
class Pitcher_company(Base):
    company_name=models.CharField(max_length=100)
    contestants=models.ForeignKey(Pitcher,on_delete=models.CASCADE)
    ask_amount=models.DecimalField(max_digits=15,decimal_places=2)
    equity_in_percentage=models.FloatField(blank=True,null=True)
    valuation=models.DecimalField(max_digits=15,decimal_places=2)
    is_deal_approve=models.BooleanField(default=False)
    def __str__(self):
         self.company_name





