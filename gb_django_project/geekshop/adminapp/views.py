from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, reverse
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from adminapp.forms import ShopUserAdminForm, ProductEditForm, ProductCategoryEditForm
from django.http import HttpResponseRedirect
from authapp.forms import ShopUserRegisterForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


# Create your views here.

# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin:user_read'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     content = {
#         'update_form': user_form
#     }
#     return render(request, 'adminapp/user_update.html', content)


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:user_read')
    form_class = ShopUserRegisterForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     content = {
#         'objects': users_list
#     }
#     return render(request, 'adminapp/users.html', content)


class UsersListView(ListView):
    paginate_by = 1
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         user_form = ShopUserAdminForm(request.POST, request.FILES, instance=edit_user)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin:user_read'))
#     else:
#         user_form = ShopUserAdminForm(instance=edit_user)
#
#     content = {
#         'update_form': user_form
#     }
#
#     return render(request, 'adminapp/user_update.html', content)


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:user_read')
    form_class = ShopUserAdminForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     user_item = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == "POST":
#         if user_item.is_active:
#             user_item.is_active = False
#         else:
#             user_item.is_active = True
#         user_item.save()
#         return HttpResponseRedirect(reverse('admin:user_read'))
#
#     content = {
#         'user_to_delete': user_item
#     }
#
#     return render(request, 'adminapp/user_delete.html', content)


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin:user_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.success_url)

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     if request.method == 'POST':
#         form = ProductCategoryEditForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin:category_read'))
#     else:
#         update_form = ProductCategoryEditForm()
#
#     content = {
#         'form': update_form
#     }
#     return render(request, 'adminapp/category_update.html', content)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:category_read')
    # fields = '__all__'
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     categories_list = ProductCategory.objects.all().order_by('-is_active')
#     content = {
#         'objects': categories_list
#     }
#     return render(request, 'adminapp/categories.html', content)


class ProductCategoryListView(ListView):
    paginate_by = 1
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         update_form = ProductCategoryEditForm(request.POST, instance=edit_category)
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('admin:category_read'))
#     else:
#         update_form = ProductCategoryEditForm(instance=edit_category)
#
#     content = {
#         'update_form': update_form
#     }
#     return render(request, 'adminapp/category_update.html', content)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:category_read')
    # fields = '__all__'
    form_class = ProductCategoryEditForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'редактирование категории'
    #     return context
    #
    # def get_success_url(self):
    #     self.object = self.get_object()
    # def get_queryset(self):
    #     return ProductCategory.objects.get(pk=self.kwargs['pk'])

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         if category_item.is_active:
#             category_item.is_active = False
#         else:
#             category_item.is_active = True
#         category_item.save()
#         return HttpResponseRedirect(reverse('admin:category_read'))
#
#     content = {
#         'category_to_delete': category_item
#     }
#     return render(request, 'adminapp/category_delete.html', content)


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:category_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.success_url)

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('admin:products', args=[pk]))
#     else:
#         product_form = ProductEditForm()
#
#     content = {
#         'update_form': product_form,
#         'category': category_item
#     }
#
#     return render(request, 'adminapp/product_update.html', content)

class ProductCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/product_update.html'
    form_class = ProductEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_pk = self.get_object().pk
        context['category'] = category_pk
        return context

    def get_success_url(self):
        category_pk = self.get_object().pk
        # print(f' HERE IS = {category_pk}')
        return reverse_lazy('admin:products', args=[category_pk])

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# class ProductCreateView(CreateView):
#     model = Product
#     template_name = 'adminapp/product_update.html'
#     form_class = ProductEditForm
#
#     def get_success_url(self):
#         category_pk = self.get_object().category.pk
#         return reverse_lazy('admin:products', args=[category_pk])
#
#     # def get_context_data(self, *, object_list=None, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['category'] = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
#     #     return context
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk):
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category=category_item).order_by('-is_active')
#     content = {
#         'objects': products_list,
#         'category': category_item
#     }
#     return render(request, 'adminapp/products.html', content)


class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        products_list = Product.objects.filter(category=category)
        context['category'] = category
        context['object_list'] = products_list
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     edit_product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         update_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('admin:products', args=[edit_product.category_id]))
#     else:
#         update_form = ProductEditForm(instance=edit_product)
#
#     content = {
#         'form': update_form,
#         'category': edit_product.category
#     }
#     return render(request, 'adminapp/product_update.html', content)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    form_class = ProductEditForm

    # def get_queryset(self):
    #     return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_pk = self.get_object().category.pk
        context['category'] = category_pk
        return context

    def get_success_url(self):
        category_pk = self.get_object().category.pk
        return reverse_lazy('admin:products', args=[category_pk])

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# class ProductUpdateView(UpdateView):
#     model = Product
#     template_name = 'adminapp/product_update.html'
#     form_class = ProductEditForm
#
#     def get_success_url(self):
#         category_pk = self.get_object().category.pk
#         return reverse_lazy('admin:products', args=[category_pk])
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     edit_product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         if edit_product.is_active:
#             edit_product.is_active = False
#         else:
#             edit_product.is_active = True
#         edit_product.save()
#         return HttpResponseRedirect(reverse('admin:products', args=[edit_product.category_id]))
#
#     content = {
#         'product_to_delete': edit_product
#     }
#     return render(request, 'adminapp/product_delete.html', content)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    def get_success_url(self):
        category_pk = self.get_object().category.pk
        return reverse_lazy('admin:products', args=[category_pk])

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     content = {
#         'object': product_item
#     }
#     return render(request, 'adminapp/product_detail.html', content)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_detail.html'

    # success_url = reverse_lazy('admin:product_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
