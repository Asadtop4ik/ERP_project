from rest_framework import permissions


class Manager1Permission(permissions.BasePermission):
    required_group = 'Manager1'

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and request.user.is_staff and
                request.user.has_perm('ERP_Project.view_brand')
        )


class Manager2Permission(permissions.BasePermission):
    required_group = 'Manager2'

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and
                request.user.is_staff and request.user.has_perm('ERP_Project.view_warehouse_product')
        )


class Manager3Permission(permissions.BasePermission):
    required_group = 'Manager3'

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and request.user.is_staff and
                request.user.has_perm('ERP_Project.view_filial')
        )


class CashierPermission(permissions.BasePermission):
    required_group = 'Cashier'

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and request.user.is_staff and
                request.user.has_perm('ERP_Project.view_customer')
        )


