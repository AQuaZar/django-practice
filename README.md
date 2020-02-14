# Notes:

The `migrate` command synchronizes database with the current models and existing migrations.

`admin.site.register(modelname)` to register in admin

We can configure view of each model in admin and add filtering functions.

**ORM** - Object-relational mapper

Custom model managers can be created by overwriting `models.Manager` class

Views could be implemented as Python objects instead of functions. Such class-based views have some advantages in some cases:

- Code related to HTTP methods(GET,POST,PUT) organized in separate methods.
- By using multiple inheritance could be created _mixins_
