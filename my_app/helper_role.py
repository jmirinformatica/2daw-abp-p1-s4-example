from flask import current_app
from flask_login import current_user
from flask_principal import identity_loaded, identity_changed, ActionNeed, RoleNeed, Permission, Identity, AnonymousIdentity
from enum import Enum

# Custom roles and actions
class Role(str, Enum):
    editor = "editor"
    viewer = "viewer"

class Action(str, Enum):
    edit = "create, update and delete"
    view = "list and read"

class HelperRole:

    #
    # Es poden protegir rutas a partir de les accions, com a routes_main.py
    # 
    # Primer es definiexen les accions que es poden fer
    edit_action_need = ActionNeed(Action.edit)
    view_action_need = ActionNeed(Action.view)
    # I després es creen els permisos a partir de les accions que 
    # es faran servir per protegir les rutes en forma d'anotacions 
    require_edit_permission = Permission(edit_action_need)
    require_view_permission = Permission(view_action_need)

    #
    # Tambe es poden protegir rutines a partir dels rols, com a routes_admin.py
    #
    # Primer es defineixen els rols que es poden tenir
    editor_role_need = RoleNeed(Role.editor)
    viewer_role_need = RoleNeed(Role.viewer)
    # I després es creen els permisos a partir dels rols que
    # es faran servir per protegir les rutes en forma d'anotacions
    require_editor_role = Permission(editor_role_need)
    require_viewer_role = Permission(viewer_role_need)

    @staticmethod
    def notify_identity_changed():
        if hasattr(current_user, 'email'):
            # és un usuari de veritat
            identity = Identity(current_user.email)
        else:
            # no s'ha autenticat, és un usuari anonim sense cap privilegi
            identity = AnonymousIdentity()
        
        identity_changed.send(current_app._get_current_object(), identity = identity)


# mètode que executa automaticament flask-principal quan s'ha carregat la identitat
@identity_loaded.connect
def on_identity_loaded(sender, identity):
    identity.user = current_user
    if hasattr(current_user, 'role'):
        if current_user.role == Role.editor:
            # Afegim que té el rol d'editor
            identity.provides.add(HelperRole.editor_role_need)
            # i que pot fer aquestes accions
            identity.provides.add(HelperRole.edit_action_need)
            identity.provides.add(HelperRole.view_action_need)
        elif current_user.role == Role.viewer:
            # Afegim que té el rol de viewer
            identity.provides.add(HelperRole.viewer_role_need)
            # i que pot fer aquestes accions
            identity.provides.add(HelperRole.view_action_need)
        else:
            current_app.logger.debug("Unkown role")