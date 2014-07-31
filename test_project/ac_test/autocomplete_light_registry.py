import autocomplete_light

from ac_test.models import Ingredient

# class PersonAutocomplete(autocomplete_light.AutocompleteModelBase):
#     search_fields = ['^first_name', 'last_name']
# autocomplete_light.register(Person, PersonAutocomplete)


# class CASAutocomplete(autocomplete_light.AutocompleteModelBase):
#     search_fields = ['cas', 'name']
#     #choices = GHSIngredient.objects.all()
#     
# #     def choices_for_request(self):
# #         return super(CASAutocomplete, self).choices_for_request().exclude(name=self.request.GET['name'])
#     
# # autocomplete_light.register(CASAutocomplete,
# #                             choices = GHSIngredient.objects.all())
# 
# autocomplete_light.register(GHSIngredient, CASAutocomplete)


class IngredientAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['cas', 'name']
    model = Ingredient

#    choices = Ingredient.objects.all()
      
autocomplete_light.register(IngredientAutocomplete)

# autocomplete_light.register(GHSIngredient,
#                             search_fields = ['cas', 'name'],
#                             widget_attrs = {
#                                 'class': 'modern-style',
#                             })