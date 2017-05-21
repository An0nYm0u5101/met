#################################################################
# MET v2 Metadate Explorer Tool
#
# This Software is Open Source. See License: https://github.com/TERENA/met/blob/master/LICENSE.md
# Copyright (c) 2012, TERENA All rights reserved.
#
# This Software is based on MET v1 developed for TERENA by Yaco Sistemas, http://www.yaco.es/
# MET v2 was developed for TERENA by Tamim Ziai, DAASI International GmbH, http://www.daasi.de
# Current version of MET has been revised for performance improvements by Andrea Biancini,
# Consortium GARR, http://www.garr.it
#########################################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _

class EntityType(models.Model):
    name = models.CharField(blank=False, max_length=20, unique=True,
                            verbose_name=_(u'Name'), db_index=True)

    xmlname = models.CharField(blank=False, max_length=20, unique=True,
                            verbose_name=_(u'Name in XML'), db_index=True)

    def __unicode__(self):
        return self.name
