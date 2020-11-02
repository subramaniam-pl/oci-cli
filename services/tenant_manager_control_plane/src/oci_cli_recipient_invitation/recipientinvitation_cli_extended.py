# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from services.tenant_manager_control_plane.src.oci_cli_recipient_invitation.generated import recipientinvitation_cli

recipientinvitation_cli.recipient_invitation_root_group.commands.pop(recipientinvitation_cli.recipient_invitation_group.name)
recipientinvitation_cli.recipient_invitation_root_group.add_command(recipientinvitation_cli.accept_recipient_invitation)
recipientinvitation_cli.recipient_invitation_root_group.add_command(recipientinvitation_cli.get_recipient_invitation)
recipientinvitation_cli.recipient_invitation_root_group.add_command(recipientinvitation_cli.ignore_recipient_invitation)
recipientinvitation_cli.recipient_invitation_root_group.add_command(recipientinvitation_cli.list_recipient_invitations)
recipientinvitation_cli.recipient_invitation_root_group.add_command(recipientinvitation_cli.update_recipient_invitation)
