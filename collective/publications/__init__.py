from zope.i18nmessageid import MessageFactory

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('collective.publications')

# Override subjects fields in dexterity contents
# (see http://pypi.python.org/pypi/collective.z3cform.widgets#override-existing-fields)
from plone.app.dexterity.behaviors.metadata import ICategorization
from zope import schema as _schema


from plone.directives import form

form.widget(ICategorization['subjects'], 'collective.z3cform.widgets.token_input_widget.TokenInputFieldWidget')
_schema.getFields(ICategorization)['subjects'].index_name = 'Subject' 
