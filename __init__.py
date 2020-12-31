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

bl_info = {
    "name":        "SeanBlend_Add-on",
    "description": "A add-on made by SeanBlend",
    "author":      "Sean Huang",
    "version":     (0, 0, 1),
    "blender":     (2, 80, 0),
    "location":    "",
    "warning":     "",
    "doc_url":     "https://github.com/Tools-With-Code/SeanBlend_Add-on",
    "tracker_url": "https://github.com/Tools-With-Code/SeanBlend_Add-on/issues",
    "category":    "SeanBlend"
}

from . import props, operators, ui

modules = (
    props,
    operators,
    ui
)

def register():
    for mod in modules:
        mod.register()

def unregister():
    for mod in modules:
        mod.unregister()