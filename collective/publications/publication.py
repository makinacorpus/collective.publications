from five import grok
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.directives import form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from collective.publications import MessageFactory as _

foncsi_collection = SimpleVocabulary(
    [SimpleTerm(value=u'dixquestions', title=u'10 questions'),
     SimpleTerm(value=u'researchreport', title=u'Research report'),
     SimpleTerm(value=u'thinking', title=u'Thinking'),]
    )

class IPublication(form.Schema):

    dcterm_abstract = RichText(
            title=_(u"Abstract"),
            description=_(u"A short summary of the content."),
            required=False,
        )

    dcterm_issue = schema.TextLine(
            title=_(u"Issue"),
            description=_(u"Publication issue."),
            required=False,
        )

    number_of_pages = schema.TextLine(
        title=_(u"Number of pages"),
        required=False,
        )
        
    dcterm_bibliographicCitation = schema.Int(
            title=_(u"Bibliographic citation"),
            required=False,
        )

    type_in_collection = schema.Choice(
            title=_(u"Type in collection"),
            description=_(u"Publication type in the collection."),
            vocabulary=foncsi_collection,
            required=False,
        )

    cover = NamedBlobImage(
            description=_(u"Cover picture."),
            required=False,
            title=_(u"Cover"),
    )

class View(grok.View):
    grok.context(IPublication)
    grok.require('zope2.View')

    grok.name('view')
