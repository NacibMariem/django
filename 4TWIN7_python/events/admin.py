from django.contrib import admin , messages
from .models import Event,Participation 
# Register your models here.
class ParticipantFilter(admin.SimpleListFilter):
    title = 'Participants'
    parameter_name = 'NombreParticipants'
    
    def lookups(self, request, model_admin):
        return (
            ('0' ,('No Participants')),
            ('more' ,('There are Participants'))
        )
    def queryset(self, request, queryset):
        if self.value() =='0':
            return queryset.filter(NombreParticipants__exact=0)
        if self.value() =='more':
            return queryset.filter(NombreParticipants__gt=0)
            
class ParticipationInline(admin.StackedInline): #we can use TabularInline (tableau ) ou stackInline
        model = Participation
        extra = 1
        classes = ['collapse']
        can_delete = True
        readonly_fields = ('datePart',)

def set_state(ModelAdmin,request,queryset):
    rows = queryset.update(State= True)
    if(rows ==1):
        msg ="One event was"
    else:
        msg = f"{rows} events were"
    messages.success(request, message='%s successfully accepted' % msg)

set_state.short_description = "Accept" # elle sera afficher fel liste state sinon state sera affiché par defaut

class EventAdmin(admin.ModelAdmin):
    def unset_state(self, request ,queryset):
        rows_filter = queryset.filter(State= False)
        if rows_filter.count() > 0:
            messages.error(request,message=f"{rows_filter.count()} are already refused")
        else:
            rows =queryset.update(State=False)
            if(rows==1):
                msg = "One event was "
            else:
                msg = f"{rows} events were"
            messages.success(request, message='%s successfully accepted' % msg)
    unset_state.short_description = "Refuse"
    actions = [set_state,"unset_state"]
    actions_on_bottom = True
    actions_on_top = True
    inlines=[
        ParticipationInline
    ]
    
    list_per_page = 20

    list_display =(
        'Title',
        'Category',
        'State', #liste affiché dans la table evnt
    )
    list_filter=(
        'Category',
        'State',
        'NombreParticipants'
    )
    ordering = ('Title',)
    search_fields=[
        'Title',
        'Category'
    ]
    readonly_fields=('CreatedAt','UpdatedAt')
    autocomplete_fields=['Organizer']
    fieldsets = (
        (
            'State',
            {
                'fields': ('State',)
            }
        ),
        (
            'About',
            {
                'classes': ('collapse',),
                'fields': (
                    'Title',
                    'ImageEvent',
                    'Category',
                    'Organizer',   
                    'NombreParticipants',
                    'Description',
                ),
            }
        ),
        (
            'Dates',
            {
                'fields': (
                    (
                        'DateEvent',
                        'CreatedAt',
                    ),
                )
            }
        ),
    )
admin.site.register(Event,EventAdmin)
admin.site.register(Participation)