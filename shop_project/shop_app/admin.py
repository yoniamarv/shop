from django.contrib import admin
from shop_app.models import Product, Customer, Comment, Maillot, Question, Response, CommentResponse

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Comment)
admin.site.register(Maillot)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(CommentResponse)
