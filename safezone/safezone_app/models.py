from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    regdate = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name


class Video(models.Model):
    fileNo = models.AutoField(primary_key=True, verbose_name='파일번호')
    filepath = models.CharField(max_length=100, verbose_name='파일 경로')
    filename = models.CharField(max_length=100, null=True, blank=True, verbose_name='파일명')
    regdate = models.DateField(default=models.DateField(auto_now_add=True), verbose_name='등록날짜')

    class Meta:
        db_table = 'upload_file'
        verbose_name = '업로드 파일'
        verbose_name_plural = '업로드 파일'

    def __str__(self):
        return f'파일번호: {self.fileNo}'
    
class Setting(models.Model):
    CAM_MODE_CHOICES = (
        (1, 'WebCam'),
        (2, 'USBCam'),
        (3, 'IPCam'),
    )

    ALARM_MODE_CHOICES = (
        (1, 'SMS문자메세지'),
        (2, '디스코드'),
        (3, '이메일'),
    )

    setno = models.AutoField(primary_key=True, verbose_name='설정번호')
    cammode = models.IntegerField(choices=CAM_MODE_CHOICES, verbose_name='카메라 모드')
    camIP = models.CharField(max_length=20, null=True, blank=True, verbose_name='카메라 IP')
    camport = models.IntegerField(null=True, blank=True, verbose_name='카메라 포트')
    alarmmode = models.CharField(choices=ALARM_MODE_CHOICES, max_length=20, verbose_name='알람 모드')
    alarmsend = models.CharField(max_length=30, verbose_name='알람 전송 대상')
    logpath = models.CharField(max_length=50, null=True, blank=True, verbose_name='로그 저장 경로')
    videorecordlength = models.IntegerField(null=True, blank=True, verbose_name='영상 저장 길이')

    class Meta:
        db_table = 'setting'
        verbose_name = '설정'
        verbose_name_plural = '설정'

    def __str__(self):
        return f'설정번호: {self.setno}'
    
class Event(models.Model):
    Violation_of_safety_rules = (
        (1, '안전모 미착용'),
        (2, '안전벨트 미착용'),
        (3, '안전화 미착용')
    )

    eventNo = models.AutoField(primary_key=True, verbose_name='메세지번호')
    eventtype = models.CharField(choices=Violation_of_safety_rules, max_length=20, verbose_name='위반 종류')
    eventtime = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name='위반 시간')

    class Meta:
        db_table = 'event'
        verbose_name = '이벤트'
        verbose_name_plural = '이벤트'

    def __str__(self):
        return f'메세지번호: {self.eventNo}'