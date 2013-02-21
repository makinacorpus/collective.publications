from zope.i18nmessageid import MessageFactory

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('collective.publications')

# Override subjects fields in dexterity contents
# (see http://pypi.python.org/pypi/collective.z3cform.widgets#override-existing-fields)

from plone.autoform.interfaces import WIDGETS_KEY
from plone.directives.form.schema import TEMP_KEY
from plone.app.dexterity.behaviors.metadata import ICategorization
from zope import schema as _schema

_directives_values = ICategorization.queryTaggedValue(TEMP_KEY)
_directives_values.setdefault(WIDGETS_KEY, {})
_directives_values[WIDGETS_KEY]['subjects'] = 'collective.z3cform.widgets.token_input_widget.TokenInputFieldWidget'
_schema.getFields(ICategorization)['subjects'].index_name = 'Subject' 
