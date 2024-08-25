"""Models for the core app."""

from django.db import models


# Create your models here.
class Item(models.Model):
    """Model for an item that can be ordered."""

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="")
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.title)


class Category(models.Model):
    """Model for a category of items."""

    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)


class Order(models.Model):
    """Model for an order."""

    items = models.ManyToManyField(Item, through="OrderItem")
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order: {self.id}"


class OrderItem(models.Model):
    """Model for an item in an order."""

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Address(models.Model):
    """Model for an address."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return self.address


class Payment(models.Model):
    """Model for a payment."""

    stripe_charge_id = models.CharField(max_length=100)
    order = models.ForeignKey(Order, related_name="payment", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stripe_charge_id


class UserProfile(models.Model):
    """Model for a user profile."""

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=100)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    """Model for a coupon."""

    code = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.code


class Refund(models.Model):
    """Model for a refund."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


class Contact(models.Model):
    """Model for a contact form."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class OrderReview(models.Model):
    """Model for a review of an order."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.name


class GlobalCounter(models.Model):
    """Model for a global counter."""

    count = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def increment(self):
        """Increment the counter."""
        self.count += 1
        self.save()

    def __str__(self):
        return f"Global Counter: {self.count}"

    class Meta:
        verbose_name = "Global Counter"
        verbose_name_plural = "Global Counters"
