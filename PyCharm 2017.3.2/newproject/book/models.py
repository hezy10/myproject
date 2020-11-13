from django.db import models

# Create your models here.
class Book(models.Model):
    '''当前的模型定义的是一个书籍表'''
    bookname = models.CharField(max_length=20,verbose_name='书籍名字')

    def __str__(self):
        '''
        这是魔法方法，用于后台管理站点需要展示的数据，必须返回的是字符串类型
        :return:
        '''
        return self.bookname
#
# 1、在model中添加模型类，注意继承于models.Model
# 2、按照将来在数据库中的字段以及类型，在模型类中进行定义
# 3、涉及新建或者修改或者删除的操作，必须先生成迁移文件 python manage.py makemigrations
# 4、执行迁移文件，将项目中的数据映射到数据库中


class RoleInfo(models.Model):
    rolename = models.CharField(max_length=20,verbose_name='角色名字')
    gender = models.SmallIntegerField(verbose_name='性别')
    # 外键关系，一对多关系，关系外键写在从表身上
    book = models.ForeignKey(Book)

    def __str__(self):
        return self.rolename



