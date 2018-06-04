from django.contrib import admin
from .models import Post
from .models import Medico
from .models import Especialidade

admin.site.register(Post)
admin.site.register(Medico)
admin.site.register(Especialidade)
