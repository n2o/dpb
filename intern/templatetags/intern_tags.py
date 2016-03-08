from django import template

register = template.Library()


@register.filter(is_safe=True)
def sizify(value):
    """
    Simple kb/mb/gb size snippet for templates:
    
    {{ product.file.size|sizify }}
    """
    #value = ing(value)
    if value < 512000:
        value = value / 1024.0
        ext = 'KB'
    elif value < 4194304000:
        value = value / 1048576.0
        ext = 'MB'
    else:
        value = value / 1073741824.0
        ext = 'GB'
    return '%s %s' % (str(round(value, 2)), ext)


@register.filter(is_safe=True)
def faAttachment(extension):
    """
    Add fontawesome icon if found. Else return normal extension as string.
    :param extension: file extension
    :return: matching fontawesome icon as string
    """
    if extension == 'pdf':
        return "<i class='fa fa-file-pdf-o fa-lg'></i>"
    elif extension == 'jpg' or extension == 'png':
        return "<i class='fa fa-picture-o fa-lg'></i>"
    elif extension == 'doc' or extension == 'docx':
        return "<i class='fa fa-file-word-o fa-lg'></i>"
    elif extension == 'xls' or extension == 'xlsx':
        return "<i class='fa fa-file-excel-o fa-lg'></i>"
    else:
        return extension


@register.filter(is_safe=True)
def houseDetails(value, text):
    if value:
        return """<div class="row">
            <div class="col-md-4">
              {0}
            </div>
            <div class="col-md-8">
              {1}
            </div>
          </div>
        """.format(text, value)
    else:
        return ""


@register.filter(is_safe=True)
def houseDetailsLink(value, text):
    if value:
        return """<span style='margin-right: 1em;'>
                  <a href='{1}'>
                    {0}
                  </a>
              </span>
        """.format(text, value)
    else:
        return ""


@register.filter(is_safe=True)
def form_item(val):
    return """
        <div class="form-group">
            {1}
            {0}
            {2}
        </div>""".format(val.errors, val.label_tag(), val)


@register.filter(is_safe=True)
def form_checkbox(val):
    return """
        <div class="checkbox">
            {0}
            <label>
            {2} {3}
            </label>
        </div>""".format(val.errors, val.label_tag(), val, val.label)
