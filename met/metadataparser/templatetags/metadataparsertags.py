from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

register = template.Library()


@register.inclusion_tag('metadataparser/bootstrap_form.html')
def bootstrap_form(form, cancel_link, delete_link=None):
    return {'form': form,
            'cancel_link': cancel_link,
            'delete_link': delete_link}


@register.inclusion_tag('metadataparser/tag_entities_list.html')
def entities_list(federation, entities, page, entity_type=None):

    paginator = Paginator(entities, 25)

    try:
        entities_page = paginator.page(page)
    except PageNotAnInteger:
        entities_page = paginator.page(1)
    except EmptyPage:
        entities_page = paginator.page(paginator.num_pages)

    if entity_type:
        append_url = '&entity_type=%s' % entity_type
    else:
        append_url = ''

    return {'federation': federation,
            'entity_type': entity_type,
            'append_url': append_url,
            'entities': entities_page}
