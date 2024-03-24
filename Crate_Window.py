import maya.cmds as cs
from functools import partial
import importlib

import Crate_Generator
importlib.reload(Crate_Generator)
# Make a new window

def ui_window():
    
    width_value = 1.00;
    depth_value = 1.00;
    spacing_value = 0.1;
    num_boards_value = 2;
    
    def get_slider_value(slider_name, *args):
        return float("{:.2f}".format(cs.floatSlider(slider_name, q=True, v=True)))
        
    def set_slider_value(slider_name, new_value, *args):
        cs.floatSlider(slider_name, edit=True, value=new_value)
        
    def get_text_field_value(field_name, *args):
        return float(cs.textField(field_name, q=True, tx=True))
    
    def set_text_field_value(field_name, new_text, *args):
        cs.textField(field_name, edit=True, text=new_text)
        
    def set_field_to_slider(field_name, slider_name, *args):
        val = get_text_field_value(field_name)
        set_slider_value(slider_name, val)
        
    def set_slider_to_field(slider_name, field_name, *args):
        new_text = get_slider_value(slider_name)
        set_text_field_value(field_name, new_text)
        
    def create_new_crate(_):
        x_width = get_text_field_value(width_text_field)
        z_depth = get_text_field_value(depth_text_field)
        spacing = get_text_field_value(spacing_text_field)
        num_boards = get_text_field_value(num_boards_text_field)
        Crate_Generator.create_crate(x_width, z_depth, spacing, int(num_boards))
    
        
    window = cs.window(title='Crate Generator', widthHeight=(200, 200))
    m_layout = cs.columnLayout(adjustableColumn=True)    
    #top row
    cs.rowLayout(numberOfColumns=3, adjustableColumn=2)
    cs.text(label='width')
    width_text_field = cs.textField()
    width_slider = cs.floatSlider()
    cs.textField(width_text_field, edit=True, text=width_value, cc=partial(set_field_to_slider, width_text_field, width_slider))
    cs.floatSlider(width_slider, min=0.01, max=50, value=width_value, step=0.01, edit=True, dc=partial(set_slider_to_field, width_slider, width_text_field))
    #second row
    cs.setParent(m_layout)
    cs.rowLayout(numberOfColumns=3, adjustableColumn=2)
    cs.text(label='depth')
    depth_text_field = cs.textField()
    depth_slider = cs.floatSlider()
    cs.textField(depth_text_field, edit=True, text=depth_value, cc=partial(set_field_to_slider, depth_text_field, depth_slider))
    cs.floatSlider(depth_slider, min=0.01, max=50, value=depth_value, step=0.01, edit=True, dc=partial(set_slider_to_field, depth_slider, depth_text_field))
    #third row
    cs.setParent(m_layout)
    cs.rowLayout(numberOfColumns=3, adjustableColumn=2)
    cs.text(label='spacing')
    spacing_text_field = cs.textField()
    spacing_slider = cs.floatSlider()
    cs.textField(spacing_text_field, edit=True, text=spacing_value, cc=partial(set_field_to_slider, spacing_text_field, spacing_slider))
    cs.floatSlider(spacing_slider, min=0.01, max=5.0, value=spacing_value, step=0.1, edit=True, dc=partial(set_slider_to_field, spacing_slider, spacing_text_field))
    #fourth row
    cs.setParent(m_layout)
    cs.rowLayout(numberOfColumns=2, adjustableColumn=2)
    cs.text(label='number of boards (min 2)')
    num_boards_text_field = cs.textField()
    cs.textField(num_boards_text_field, edit=True, text=num_boards_value)

    #crate button
    cs.setParent(m_layout)
    cs.button(label='create crate', c=partial(create_new_crate))
    cs.showWindow(window)


#ui_window()