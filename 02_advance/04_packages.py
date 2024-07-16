# Packages --> is a container for multiple modules
# It's simply a folder which contains multople modules and-
# by creating a file named __init__.py, python automatically knows that it's a package.
# The real example of package that we use here, is the ecommerce package which-
# is located in: 02_advance > ecommerce


# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()


# from ecommerce.shipping import calc_shipping
# calc_shipping()


from ecommerce import shipping
shipping.calc_shipping()