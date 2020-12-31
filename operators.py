#  ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
from bpy.types import Operator


class SEANBLEND_OT_Disable(Operator):
    """Disables the addon in blender preferences"""
    bl_label = "Disable Add-on"
    bl_description = "Disables the addon in blender preferences"
    bl_idname = "seanblend.disable"

    def execute(self, context):
        bpy.ops.preferences.addon_disable(module="SeanBlend_Add-on")
        return {"FINISHED"}

class SEANBLEND_OT_Remove(Operator):
    """Removes the addon in blender preferences"""
    bl_label = "Remove Add-on (Blender might crash)"
    bl_description = "Removes the addon in blender preferences (risk of Blender crashing)"
    bl_idname = "seanblend.remove"

    def execute(self, context):
        bpy.ops.preferences.addon_remove(module="SeanBlend_Add-on")
        return {"FINISHED"}


classes = (
    SEANBLEND_OT_Disable,
    SEANBLEND_OT_Remove,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)