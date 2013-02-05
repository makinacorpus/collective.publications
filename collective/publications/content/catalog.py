#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'

from five import grok
from collective import dexteritytextindexer
from collective.dexteritytextindexer.utils import searchable
from plone.indexer import indexer
from plone.dexterity.interfaces import IDexterityContent
from plone.app.dexterity.behaviors.metadata import IDublinCore
from collective.publications.content.publication import IPublication

from collective.publications.utils import magicstring

@indexer(IPublication)
def pagesIndexer(obj):
    return obj.pages
grok.global_adapter(pagesIndexer, name="pages_count")

@indexer(IPublication)
def issueIndexer(obj):
    return obj.dcterm_issue
grok.global_adapter(issueIndexer, name="dcterm_issue")

@indexer(IPublication)
def creatorsIndexer(obj):
    creators = [magicstring(a) for a in IDublinCore(obj).creators]
    return creators
grok.global_adapter(creatorsIndexer, name="creatorsIndexer")

searchable(IDublinCore, 'title')
searchable(IDublinCore, 'description')

class MySearchableTextExtender(grok.Adapter):
    grok.context(IDexterityContent)
    grok.name('MCIPublication')
    grok.implements(dexteritytextindexer.IDynamicTextIndexExtender)

    def __init__(self, context):
        self.context = context

    def __call__(self):
        """Extend the searchable text with a custom string"""
        ret = []
        content = [
            getattr(self.context, 'title', ''),
            getattr(self.context, 'description', ''),
            getattr(self.context, 'subject', ''),]
        if getattr(self.context, 'portal_type', '') in ['publication']:
            content.extend([
                getattr(self.context, 'dcterm_issue', ''),]) 
        for i in content:
            if isinstance(i, (list, tuple)):
                i = ' '.join(i)
            if isinstance(i, basestring):
                i = i.strip()
            if i and (not i in ret):
                ret.append(i)
        ret = ' '.join(ret)
        return ret


