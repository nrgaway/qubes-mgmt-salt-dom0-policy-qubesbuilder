#!yamlscript
# -*- coding: utf-8 -*-
# vim: set syntax=yaml ts=2 sw=2 sts=2 et :

##
# policy-qubesbuilder.absent
# ==========================
#
# [WORK IN PROGRESS]
# [NOT IMPLEMENTED]
#
# Remove qubesbuilder rpc policies
#
# Execute:
#   qubesctl state.sls policy-qubesbuilder.absent
##

# --- Dom0 --------------------------------------------------------------------
$if  __grains__['virtual'] == 'Qubes':
  /etc/qubes-rpc/qubesbuilder.AttachDisk:
    file:
      - absent

  /etc/qubes-rpc/qubesbuilder.ExportDisk:
    file:
      - absent

  /etc/qubes-rpc/policy/qubesbuilder.AttachDisk:
    file:
      - absent

  /etc/qubes-rpc/policy/qubesbuilder.ExportDisk:
    file:
      - absent

# --- AppVM -------------------------------------------------------------------
$if __grains__['virtual_subtype'] == 'Xen PV DomU':
  /etc/qubes-rpc/qubesbuilder.CopyTemplateBack:
    file:
      - absent

  /etc/qubes-rpc/policy/qubesbuilder.CopyTemplateBack:
    file:
      - absent

