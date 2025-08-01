from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='shop_images/', blank=True, null=True)


    class Meta:
        unique_together = ('user', 'shop')

    def __str__(self):
        return f"{self.user.username} likes {self.shop.name}"
