import matplotlib as mpl
from cycler import cycler


#########################################################
# Figure layout defaults
#########################################################
fcp_params = {'ax_edge_color'        : '#ffffff',
              'ax_face_color'        : '#eaeaea',
              'ax_fig_ws'            : 50,
              'ax_leg_fig_ws'        : 0,
              'ax_leg_ws'            : 20,
              'ax_label_pad'         : 4,
              'ax_size'              : [400,400],  # [width, height]
              'bp_divider_color'     : '#bbbbbb',
              'bp_fill_color'        : '#ffffff',
              'bp_label_size'        : 25,
              'bp_label_edge_color'  : '#666666',
              'bp_label_fill_color'  : '#ffffff',
              'bp_label_font_size'   : 13,
              'bp_label_text_color'  : '#666666',
              'bp_label_text_style'  : 'normal',
              'bp_label_text_weight' : 'normal',
              'bp_name_font_size'    : 12,
              'bp_name_text_color'  : '#666666',
              'bp_name_text_style'  : 'normal',
              'bp_name_text_weight' : 'normal',
              'bp_name_ws'           : 0,
              'col_padding'          : 30,
              'cols'                 : 1,
              'dpi'                  : 100,
              'fig_ax_ws'            : 80,
              'fig_edge_color'       : '#ffffff',
              'fig_face_color'       : '#ffffff',
              'fig_title_ws'         : 10,
              'grid_major_color'     : '#ffffff',
              'grid_major_linestyle' : '-',
              'grid_minor_color'     : '#ffffff',
              'grid_minor_linestyle' : 'dotted',
              'label_font_size'      : 14,
              'label_style'          : 'italic',
              'label_weight'         : 'bold',
              'leg_bkgrd'            : 'white',
              'leg_border'           : 'white',
              'leg_fig_ws'           : 10,
              'leg_font_size'        : 12,
              'leg_items'            : [],
              'leg_points'           : 1,
              'leg_title'            : '',
              'line_width'           : 1,
              'marker_size'          : 7,
              'marker_type'          : 'o',
              'rc_label_edge_color'  : '#aaaaaa',
              'rc_label_fill_color'  : '#969ab3',
              'rc_label_font_size'   : 14,
              'rc_label_text_color'  : '#ffffff',
              'rc_label_text_style'  : 'normal',
              'rc_label_text_weight' : 'bold',
              'rc_label_size'        : 25,
              'rc_label_ws'          : 10,
              'row_padding'          : 30,
              'rows'                 : 1,
              'tick_major_color'     : '#ffffff',
              'tick_minor_color'     : '#ffffff',
              'tick_font_size'       : 12,
              'tick_label_color'     : '#000000',
              'tick_length'          : 4,
              'tick_width'           : 1.5,
              'title_ax_ws'          : 20,
              'title_h'              : 40,
              'title_fill_color'     : '#ffffff',
              'title_font_size'      : 18,
              'title_edge_color'     : '#ffffff',
              'title_text_color'     : '#333333',
              'title_text_style'     : 'bold',
              }

#########################################################
# New color schemes
#########################################################

palette = [(0.2980, 0.4471, 0.6902),
           (0.7686, 0.3059, 0.3216),
           (0.3333, 0.6588, 0.4078),
           (0.5059, 0.4471, 0.698),
           (0.3922, 0.7098, 0.8039),
           (0.8000, 0.7255, 0.4549),
           (0.9812, 0.5554, 0.3874),
           (0.5543, 0.6271, 0.7960),
           (0.6537, 0.8470, 0.3282),
           (0.9986, 0.8509, 0.1849),
           (0.7020, 0.7019, 0.7019),
           (0.5529, 0.8275, 0.7803),
           (0.7491, 0.7337, 0.8525),
           (0.9787, 0.5072, 0.4566),
           (0.6941, 0.4824, 0.6157),
           (0.9529, 0.749 , 0.3569),
           (0.1961, 0.3922, 0.2235),
           (0.2392, 0.3333, 0.4667),
           (0.8706, 0.4588, 0.1529),
           (0.3451, 0.5137, 0.5059),
           (0.7647, 0.1686, 0.3922),
           (0.3412, 0.1961, 0.3059),
           (0.5804, 0.5373, 0.4588),
           (0.6157, 0.7961, 0.8784),
           (0.4353, 0.4353, 0.4353),
           (0.6941, 0.4824, 0.6157),
           (0.9529, 0.749 , 0.3569),
           (0.1961, 0.3922, 0.2235),
           (0.2392, 0.3333, 0.4667),
           (0.8706, 0.4588, 0.1529),
           (0.3451, 0.5137, 0.5059),
           (0.7647, 0.1686, 0.3922),
           (0.3412, 0.1961, 0.3059),
           (0.5804, 0.5373, 0.4588),
           (0.6157, 0.7961, 0.8784),
           (0.4353, 0.4353, 0.4353)
          ]

jmp_spectral = mpl.colors.LinearSegmentedColormap(
              'my_cmap',
               {
                'blue':  ((0.0000, 0.3098, 0.3098),
                          (0.0420, 0.4392, 0.4392),
                          (0.0830, 0.6235, 0.6235),
                          (0.1250, 0.8156, 0.8156),
                          (0.1670, 1.0000, 1.0000),
                          (0.2080, 1.0000, 1.0000),
                          (0.2500, 1.0000, 1.0000),
                          (0.2920, 0.8588, 0.8588),
                          (0.3330, 0.7215, 0.7215),
                          (0.3750, 0.5882, 0.5882),
                          (0.4170, 0.4274, 0.4274),
                          (0.4580, 0.0000, 0.0000),
                          (0.5000, 0.0000, 0.0000),
                          (0.5420, 0.0000, 0.0000),
                          (0.5830, 0.0000, 0.0000),
                          (0.6250, 0.0000, 0.0000),
                          (0.6670, 0.0000, 0.0000),
                          (0.7080, 0.0000, 0.0000),
                          (0.7500, 0.0000, 0.0000),
                          (0.7920, 0.0039, 0.0039),
                          (0.8330, 0.0078, 0.0078),
                          (0.8750, 0.0196, 0.0196),
                          (0.9170, 0.0392, 0.0392),
                          (0.9580, 0.0392, 0.0392),
                          (1.0000, 0.1294, 0.1294)),
                'red':   ((0.0000, 0.3098, 0.3098),
                          (0.0420, 0.4392, 0.4392),
                          (0.0830, 0.4705, 0.4705),
                          (0.1250, 0.3686, 0.3686),
                          (0.1670, 0.1529, 0.1529),
                          (0.2080, 0.1372, 0.1372),
                          (0.2500, 0.0000, 0.0000),
                          (0.2920, 0.0000, 0.0000),
                          (0.3330, 0.0000, 0.0000),
                          (0.3750, 0.0000, 0.0000),
                          (0.4170, 0.0000, 0.0000),
                          (0.4580, 0.0000, 0.0000),
                          (0.5000, 0.0000, 0.0000),
                          (0.5420, 0.2431, 0.2431),
                          (0.5830, 0.4862, 0.4862),
                          (0.6250, 0.7254, 0.7254),
                          (0.6670, 0.8745, 0.8745),
                          (0.7080, 0.8941, 0.8941),
                          (0.7500, 0.9098, 0.9098),
                          (0.7920, 0.9294, 0.9294),
                          (0.8330, 0.9529, 0.9529),
                          (0.8750, 0.9764, 0.9764),
                          (0.9170, 0.9921, 0.9921),
                          (0.9580, 0.9450, 0.9450),
                          (1.0000, 0.6196, 0.6196)),
                'green': ((0.0000, 0.0627, 0.0628),
                          (0.0420, 0.0117, 0.0117),
                          (0.0830, 0.0000, 0.0000),
                          (0.1250, 0.0000, 0.0000),
                          (0.1670, 0.0078, 0.0078),
                          (0.2080, 0.2666, 0.2666),
                          (0.2500, 0.4000, 0.4000),
                          (0.2920, 0.5568, 0.5568),
                          (0.3330, 0.6509, 0.6509),
                          (0.3750, 0.7058, 0.7058),
                          (0.4170, 0.7647, 0.7647),
                          (0.4580, 0.8274, 0.8274),
                          (0.5000, 0.8901, 0.8901),
                          (0.5420, 0.9450, 0.9450),
                          (0.5830, 0.8784, 0.8784),
                          (0.6250, 0.8705, 0.8705),
                          (0.6670, 0.8274, 0.8274),
                          (0.7080, 0.7176, 0.7176),
                          (0.7500, 0.6078, 0.6078),
                          (0.7920, 0.4901, 0.4901),
                          (0.8330, 0.3725, 0.3725),
                          (0.8750, 0.2470, 0.2470),
                          (0.9170, 0.1254, 0.1254),
                          (0.9580, 0.0392, 0.0392),
                          (1.0000, 0.1294, 0.1294))
               },
               256
              )

####################################################
# Default marker scheme
####################################################
markers = ['o', '+', 's', 'x', 'd', 'Z', '^', 'Y', 'v', '\infty', '\#', '<',
           u'\u2B21', u'\u263A', '>', u'\u29C6', '\$', u'\u2B14', u'\u2B1A',
           u'\u25A6', u'\u229E', u'\u22A0', u'\u22A1', u'\u20DF', '\gamma',
           '\sigma', '\star']

####################################################
# Matplotlib default overrides
####################################################

rcParams = {'agg.path.chunksize': 0,
            'animation.avconv_args': [''],
            'animation.avconv_path': 'avconv',
            'animation.bitrate': -1,
            'animation.codec': 'mpeg4',
            'animation.convert_args': [''],
            'animation.convert_path': 'convert',
            'animation.ffmpeg_args': [''],
            'animation.ffmpeg_path': 'ffmpeg',
            'animation.frame_format': 'png',
            'animation.mencoder_args': [''],
            'animation.mencoder_path': 'mencoder',
            'animation.writer': 'ffmpeg',
            'axes.axisbelow': True,
            'axes.prop_cycle': cycler('color', palette),
            'axes.edgecolor': '#ffffff',
            'axes.facecolor': '#eaeaea',
            'axes.formatter.limits': [-4, 4],
            'axes.formatter.use_locale': False,
            'axes.formatter.use_mathtext': True,
            'axes.formatter.useoffset': True,
            'axes.grid': True,
            'axes.grid.which': 'major',
            'axes.hold': True,
            'axes.labelcolor': 'k',
            'axes.labelsize': 14.0,
            'axes.labelweight': 'bold',
            'axes.linewidth': 1.0,
            'axes.titlesize': 16.0,
            'axes.titleweight': 'normal',
            'axes.unicode_minus': True,
            'axes.xmargin': 0.0,
            'axes.ymargin': 0.0,
            'axes3d.grid': True,
            'backend': 'Qt4Agg',
            'backend.qt4': 'PyQt4',
            'backend.qt5': 'PyQt5',
            'backend_fallback': True,
            'contour.negative_linestyle': 'dashed',
            'docstring.hardcopy': False,
            'examples.directory': '',
            'figure.autolayout': False,
            'figure.dpi': 80.0,
            'figure.edgecolor': 'w',
            'figure.facecolor': '1.0',
            'figure.figsize': [7.0,7.0],
            'figure.frameon': True,
            'figure.max_open_warning': 20,
            'figure.subplot.bottom': 0.1,
            'figure.subplot.hspace': 0.2,
            'figure.subplot.left': 0.125,
            'figure.subplot.right': 0.9,
            'figure.subplot.top': 0.9,
            'figure.subplot.wspace': 0.2,
            'font.cursive': ['Apple Chancery',
                             'Textile',
                             'Zapf Chancery',
                             'Sand',
                             'cursive'],
            'font.family': ['sans-serif'],
            'font.fantasy': ['Comic Sans MS',
                             'Chicago',
                             'Charcoal',
                             'ImpactWestern',
                             'fantasy'],
            'font.monospace': ['Bitstream Vera Sans Mono',
                               'DejaVu Sans Mono',
                               'Andale Mono',
                               'Nimbus Mono L',
                               'Courier New',
                               'Courier',
                               'Fixed',
                               'Terminal',
                               'monospace'],
            'font.sans-serif': ['Arial',
                                'Bitstream Vera Sans',
                                'Lucida Grande',
                                'Verdana',
                                'Geneva',
                                'Lucid',
                                'Helvetica',
                                'Avant Garde',
                                'sans-serif'],
            'font.serif': ['Bitstream Vera Serif',
                           'DejaVu Serif',
                           'New Century Schoolbook',
                           'Century Schoolbook L',
                           'Utopia',
                           'ITC Bookman',
                           'Bookman',
                           'Nimbus Roman No9 L',
                           'Times New Roman',
                           'Times',
                           'Palatino',
                           'Charter',
                           'serif'],
            'font.size': 12.5,
            'font.stretch': 'normal',
            'font.style': 'normal',
            'font.variant': 'normal',
            'font.weight': 'normal',
            'grid.alpha': 1.0,
            'grid.color': '#ffffff',
            'grid.linestyle': '-',
            'grid.linewidth': 1.5,
            'image.aspect': 'equal',
            'image.cmap': 'jet',
            'image.interpolation': 'bilinear',
            'image.lut': 256,
            'image.origin': 'upper',
            'image.resample': False,
            'interactive': True,
            'keymap.all_axes': ['a'],
            'keymap.back': ['left', 'c', 'backspace'],
            'keymap.forward': ['right', 'v'],
            'keymap.fullscreen': ['f', 'ctrl+f'],
            'keymap.grid': ['g'],
            'keymap.home': ['h', 'r', 'home'],
            'keymap.pan': ['p'],
            'keymap.quit': ['ctrl+w', 'cmd+w'],
            'keymap.save': ['s', 'ctrl+s'],
            'keymap.xscale': ['k', 'L'],
            'keymap.yscale': ['l'],
            'keymap.zoom': ['o'],
            'legend.borderaxespad': 0.5,
            'legend.borderpad': 0.4,
            'legend.columnspacing': 2.0,
            'legend.fancybox': False,
            'legend.fontsize': 'large',
            'legend.frameon': True,
            'legend.handleheight': 0.7,
            'legend.handlelength': 2.0,
            'legend.handletextpad': 0.8,
            'legend.isaxes': True,
            'legend.labelspacing': 0.5,
            'legend.loc': 'upper right',
            'legend.markerscale': 1.0,
            'legend.numpoints': 2,
            'legend.scatterpoints': 3,
            'legend.shadow': False,
            'lines.antialiased': True,
            'lines.color': 'b',
            'lines.dash_capstyle': 'butt',
            'lines.dash_joinstyle': 'round',
            'lines.linestyle': '-',
            'lines.linewidth': 1.5,
            'lines.marker': 'None',
            'lines.markeredgewidth': 0.5,
            'lines.markersize': 6.0,
            'lines.solid_capstyle': 'projecting',
            'lines.solid_joinstyle': 'round',
            'mathtext.bf': 'serif:bold',
            'mathtext.cal': 'cursive',
            'mathtext.default': 'regular',
            'mathtext.fallback_to_cm': True,
            'mathtext.fontset': 'cm',
            'mathtext.it': 'serif:italic',
            'mathtext.rm': 'serif',
            'mathtext.sf': 'sans\\-serif',
            'mathtext.tt': 'monospace',
            'patch.antialiased': True,
            'patch.edgecolor': 'k',
            'patch.facecolor': 'b',
            'patch.linewidth': 1.0,
            'path.effects': [],
            'path.simplify': True,
            'path.simplify_threshold': 0.1111111111111111,
            'path.sketch': None,
            'path.snap': True,
            'pdf.compression': 6,
            'pdf.fonttype': 3,
            'pdf.inheritcolor': False,
            'pdf.use14corefonts': False,
            'pgf.debug': False,
            'pgf.preamble': [''],
            'pgf.rcfonts': True,
            'pgf.texsystem': 'xelatex',
            'plugins.directory': '.matplotlib_plugins',
            'polaraxes.grid': True,
            'ps.distiller.res': 6000,
            'ps.fonttype': 3,
            'ps.papersize': 'letter',
            'ps.useafm': False,
            'ps.usedistiller': False,
            'savefig.bbox': None,
            'savefig.directory': '~',
            'savefig.dpi': 100.0,
            'savefig.edgecolor': 'w',
            'savefig.facecolor': 'w',
            'savefig.format': 'png',
            'savefig.frameon': True,
            'savefig.jpeg_quality': 95,
            'savefig.orientation': 'portrait',
            'savefig.pad_inches': 0.1,
            'savefig.transparent': False,
            'svg.fonttype': 'path',
            'svg.image_inline': True,
            'svg.image_noscale': False,
            'text.antialiased': True,
            'text.color': 'k',
            'text.dvipnghack': None,
            'text.hinting': True,
            'text.hinting_factor': 8,
            'text.latex.preamble': [''],
            'text.latex.preview': False,
            'text.latex.unicode': False,
            'text.usetex': False,
            'timezone': 'UTC',
            'toolbar': 'toolbar2',
            'verbose.fileo': 'sys.stdout',
            'verbose.level': 'silent',
            'webagg.open_in_browser': True,
            'webagg.port': 8988,
            'webagg.port_retries': 50,
            'xtick.color': '.15',
            'xtick.direction': 'in',
            'xtick.labelsize': 'medium',
            'xtick.major.pad': 4.0,
            'xtick.major.size': 4.0,
            'xtick.major.width': 0,
            'xtick.minor.pad': 4.0,
            'xtick.minor.size': 2.0,
            'xtick.minor.width': 0,
            'ytick.color': '.15',
            'ytick.direction': 'in',
            'ytick.labelsize': 'medium',
            'ytick.major.pad': 4.0,
            'ytick.major.size': 4.0,
            'ytick.major.width': 0,
            'ytick.minor.pad': 4.0,
            'ytick.minor.size': 2.0,
            'ytick.minor.width': 0,
          }
mpl.rcParams.update(rcParams)


