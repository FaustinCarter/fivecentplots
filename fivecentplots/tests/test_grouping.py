
import pytest
import fivecentplots as fcp
import pandas as pd
import numpy as np
import os, sys, pdb
import fivecentplots.utilities as utl
import inspect
osjoin = os.path.join
st = pdb.set_trace

MASTER = osjoin(os.path.dirname(fcp.__file__), 'tests', 'test_images', 'grouping.py')

# Sample data
df1 = pd.read_csv(osjoin(os.path.dirname(fcp.__file__), 'tests', 'fake_data.csv'))
df2 = pd.read_csv(osjoin(os.path.dirname(fcp.__file__), 'tests', 'fake_data_box.csv'))

# Set theme
# fcp.set_theme('gray')
# fcp.set_theme('white')

# Other
SHOW = False


def make_all():
    """
    Remake all test master images
    """

    members = inspect.getmembers(sys.modules[__name__])
    members = [f for f in members if 'test_' in f[0]]
    for member in members:
        print('Running %s...' % member[0], end='')
        member[1](master=True)
        print('done!')


def test_legend_single(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'legend_single_master') if master else 'legend_single'

    # Make the plot
    fcp.plot(df=df1, x='Voltage', y='I [A]', legend='Die',
             filter='Substrate=="Si" & Target Wavelength==450 & Boost Level==0.2 & Temperature [C]==25',
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_legend_multiple(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'legend_multiple_master') if master else 'legend_multiple'

    # Make the plot
    fcp.plot(df=df1, x='Voltage', y='I [A]', legend=['Die', 'Substrate'],
             filter='Target Wavelength==450 & Boost Level==0.2 & Temperature [C]==25',
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_legend_multiple_xy(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'legend_multiple_xy_master') if master else 'legend_multiple_xy'

    # Make the plot
    fcp.plot(df=df1, x='Voltage', y=['I [A]', 'Voltage'], lines=False,
             filter='Substrate=="Si" & Target Wavelength==450 & Boost Level==0.2',
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_legend_secondary_none(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'legend_secondary_none') if master else 'legend_secondary_none'

    # Make the plot
    fcp.plot(df1, x='Voltage', y=['Voltage', 'I [A]'], twin_x=True,
             filter='Substrate=="Si" & Target Wavelength==450 & Boost Level==0.2 & Temperature [C]==25 & Die=="(-1,2)"',
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_legend_secondary_axis(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'legend_secondary_axis') if master else 'legend_secondary_axis'

    # Make the plot
    fcp.plot(df1, x='Voltage', y=['Voltage', 'I [A]'], twin_x=True, legend=True,
             filter='Substrate=="Si" & Target Wavelength==450 & Boost Level==0.2 & Temperature [C]==25 & Die=="(-1,2)"',
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_legend_secondary_column(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'legend_secondary_column_master') if master else 'legend_secondary_column'

    # Make the plot
    fcp.plot(df1, x='Voltage', y=['Voltage', 'I [A]'], twin_x=True, legend='Die',
             filter='Substrate=="Si" & Target Wavelength==450 & Boost Level==0.2 & Temperature [C]==25 & Die=="(-1,2)"',
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_groups_none(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'groups_none_master') if master else 'groups_none'

    # Make the plot
    fcp.plot(df=df1, x='Voltage', y='I [A]', legend='Temperature [C]',
             filter='Substrate=="Si" & Target Wavelength==450 & Boost Level==0.2',
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_groups_enabled(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'groups_enabled_master') if master else 'groups_enabled'

    # Make the plot
    fcp.plot(df=df1, x='Voltage', y='I [A]', groups='Die', legend='Temperature [C]',
             filter='Substrate=="Si" & Target Wavelength==450 & Boost Level==0.2',
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_groups_enabled2(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'groups_enabled2_master') if master else 'groups_enabled2'

    # Make the plot
    fcp.plot(df=df1, x='Voltage', y='I [A]', groups=['Die', 'Temperature [C]'],
             filter='Substrate=="Si" & Target Wavelength==450 & Boost Level==0.2',
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_groups_boxplot(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'groups_boxplot_master') if master else 'groups_boxplot'

    # Make the plot
    df_box = pd.read_csv(osjoin(os.path.dirname(fcp.__file__), 'tests', 'fake_data_box.csv'))
    fcp.boxplot(df=df_box, y='Value', groups=['Batch', 'Sample'], legend='Region',
                filename=name + '.png', inline=False, jitter=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_groups_row_col(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'groups_row_col_master') if master else 'groups_row_col'

    # Make the plot
    fcp.plot(df=df1, x='Voltage', y='I [A]', legend='Die', col='Boost Level', row='Temperature [C]',          ax_size=[225, 225],
             filter='Substrate=="Si" & Target Wavelength==450', label_rc_font_size=14,
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_groups_wrap_column(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'groups_wrap_column_master') if master else 'groups_wrap_column'

    # Make the plot
    fcp.plot(df=df1, x='Voltage', y='I [A]', legend='Die', wrap=['Temperature [C]', 'Boost Level'],
             ax_size=[225, 225], filter='Substrate=="Si" & Target Wavelength==450',
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_groups_wrap_column_ncol(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'groups_wrap_column_ncol_master') if master else 'groups_wrap_column_ncol'

    # Make the plot
    fcp.plot(df=df1, x='Voltage', y='I [A]', legend='Die', wrap=['Temperature [C]', 'Boost Level'],
             ax_size=[225, 225], filter='Substrate=="Si" & Target Wavelength==450', ncol=2,
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_groups_wrap_names(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'groups_wrap_names_master') if master else 'groups_wrap_names'

    # Make the plot
    fcp.plot(df=df1, x='Voltage', y=['I Set', 'I [A]'], legend='Die', wrap='y',
             groups=['Boost Level', 'Temperature [C]'], ax_size=[325, 325],
             filter='Substrate=="Si" & Target Wavelength==450',
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_groups_wrap_names_no_sharing(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'groups_wrap_names-no-sharing_master') if master else 'groups_wrap_names-no-sharing'

    # Make the plot
    fcp.plot(df=df1, x='Voltage', y=['I Set', 'I [A]'], legend='Die', wrap='y',
             groups=['Boost Level', 'Temperature [C]'], ax_size=[525, 170],
             filter='Substrate=="Si" & Target Wavelength==450', ncol=1, ws_row=0,
             separate_labels=False, separate_ticks=False,
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        compare = utl.img_compare(name + '.png', osjoin(MASTER, name + '_master.png'))
        if remove:
            os.remove(name + '.png')

        assert not compare


def test_figure(master=False, remove=True, show=False):

    name = osjoin(MASTER, 'figure_master') if master else 'figure'

    # Make the plot
    fcp.plot(df=df1, x='Voltage', y='I [A]', fig_groups='Die', wrap=['Temperature [C]', 'Boost Level'],
             ax_size=[225, 225], filter='Substrate=="Si" & Target Wavelength==450',
             filename=name + '.png', inline=False)

    # Compare with master
    if master:
        return
    elif show:
        os.startfile(osjoin(MASTER, name + '_master.png'))
        os.startfile(name + '.png')
    else:
        for i in range(0, 3):
            tag = ' (%s)' % (i+1) if i > 0 else ''
            compare = utl.img_compare(name + tag + '.png', osjoin(MASTER, name + tag + '_master.png'))
            if remove:
                os.remove(name + tag + '.png')

            assert not compare


if __name__ == '__main__':
    pass