
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from substring import matching_substring_pairs 


def plot_arc_diagram( string, plot_title="" ):
    slds = matching_substring_pairs(string)
    bews = map( lambda sld: (sld[0], sum(sld)+sld[1], sld[1]), slds )
    plot_arc_diagram_impl(bews, plot_title)

#  begin                                        end                 
# /                                            /
# ***********-----------O-----------***********
# |--width--|            \          |--width--|
#           |-inner rad-| \
# |-----outer radius----|  center

def plot_ring( ax, begin, end, width ):
    cx = 0.5*(begin + end)
    center = (cx, 0)
    outer_radius = cx - begin
    inner_radius = outer_radius - width

    mypie, _ = ax.pie([1], radius=outer_radius, colors=[(0.4,0.4, 1.0, 0.3)], center=center )
    plt.setp( mypie, width=width)

    return outer_radius

def plot_arc_diagram_impl( bews, plot_title ):
    fig, ax = plt.subplots(subplot_kw={'aspect': 'auto'})

    x_min = 0
    x_max = 0
    max_width = 0
    for bew in bews:
        x_max = max(x_max, bew[1])
        orad = plot_ring(ax, bew[0], bew[1], bew[2])
        max_width = max(max_width, orad)

    ax.set_xlim(x_min, x_max)
    ax.set_ylim( -max_width, max_width)

    plt.axis('off')

    title_obj = plt.title(plot_title, loc='left')
    plt.setp(title_obj, color=(0.0, 0.0, 0.0, 0.3)) 

    plt.savefig('output.png')
    plt.show()
