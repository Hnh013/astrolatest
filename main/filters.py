import django_filters
from django_filters import CharFilter, NumberFilter
from .models import *


class AstroFilter(django_filters.FilterSet):
	
	profile = CharFilter(field_name="profile", lookup_expr='icontains')
	skill = CharFilter(field_name="skill", lookup_expr='icontains')
	language = CharFilter(field_name="language", lookup_expr='icontains')
	experience = NumberFilter(field_name="experience", lookup_expr='gte')
	location = CharFilter(field_name="location", lookup_expr='icontains')
	class Meta:
		model = Astro_Profile
		fields = '__all__'
		exclude = ['about']