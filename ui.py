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
from bpy.types import Panel


class SEANBLEND_PT_SeanBlendAddon(Panel):
    bl_label = "SeanBlend"
    bl_idname = "SEANBLEND_PT_SeanBlendAddon"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        settings = context.scene.idname

class SEANBLEND_PT_Settings(Panel):
    bl_label = "Settings"
    bl_idname = "SEANBLEND_PT_Settings"
    bl_parent_id = "SEANBLEND_PT_SeanBlendAddon"

    def draw(self, context):
        layout = self.layout
        settings = context.scene.idname

        layout.operator("seanblend.disable")
        layout.operator("seanblend.remove")


classes = (
    SEANBLEND_PT_SeanBlendAddon,
    SEANBLEND_PT_Settings,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)