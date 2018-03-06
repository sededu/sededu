# interactive backwater module written by Andrew J. Moodie
# see module and website for more information
# classroom module for this model can be found at 
# http://www.coastalsustainability.rice.edu/outreach/
# the model setup below is parameterized to the Lower Mississippi River
# as established by Nittrouer et al., 
# Spatial and temporal trends, GSAB, 2012


# IMPORT LIBLARIES
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widget
import channel, hydro, utils

# SET PARAMETERS
# def rootInit():
L = 1600e3 # length of domain
nx = 400 # number of nodes
dx = L / nx # width of cells
x = np.arange(0, L+1, dx) # define x-coordinates

start = 43 # pin-point to start eta from
S0 = 7e-5 # bed slope
eta = np.linspace(start, start - S0*(L), nx+1) # channel bed

mou = 0.75 # fraction of x channelized (i.e. mouth position)
mouIdx = int(mou*nx)
thet = 2 # plume spreading angle
RKs = np.array([0, 165, 368, 425, 505])
RKidxs = np.int_( (nx*mou) - np.round(RKs*1000/dx) )

B0 = 1100 # basic channel width
B = channel.set_B(B0, mou, thet, nx, dx) # channel width
S = channel.get_slope(eta, nx, dx) # bed slope at each node
H0 = 0 # 
Cf = 0.0047
Qwinit = 10000
Qw = Qwinit
Qwbf = 35000
Qwmax = 60000
Qwmin = 5000

H = hydro.get_backwater_dBdx(eta, S, B, H0, Cf, Qw, nx, dx)
Xs = hydro.find_backwaterregion(H, dx)
zed = 0.5 + hydro.get_backwater_dBdx(eta, S, B, H0, Cf, Qwbf, nx, dx)

nitt_bed, nitt_water = channel.load_nitt()
nitt_water_dict = [{'10,000 m$^3$/s':nitt_water.hdr.index('f5k_10k')},
                   {'20,000 m$^3$/s':nitt_water.hdr.index('f15k_20k')},
                   {'35,000 m$^3$/s':nitt_water.hdr.index('f30k_35k')}]
nitt_water_dict_idx = np.array( [ list(d.values()) for d in nitt_water_dict ] )
# nitt_water.seldata = nitt_water.data[:, [int(v) for v in nitt_water_dict.values()]]
nitt_water.seldata = nitt_water.data[:, nitt_water_dict_idx.flatten()]

# setup the figure
plt.rcParams['toolbar'] = 'None'
plt.rcParams['figure.figsize'] = 11, 7
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.075, bottom=0.5, top=0.95, right=0.95)
background_color = 'white'
ax.set_xlabel("distance from Head of Passes (km)")
ax.set_ylabel("elevation (m)")
plt.ylim(-50, 100)
plt.xlim(L/1000*0.25, L/1000-(L/1000*0.125))
# set(hand.ax, 'xTickLabels', cellfun(@num2str, num2cell(abs((cellfun(@str2num, (get(gca, 'XTickLabels')))) - (L/1000*mou))), 'UniformOutput', false))


# add plot elements
eta_line, = plt.plot(x/1000, eta, lw=2, color='black') # plot bed
zed_line = plt.plot(x[:mouIdx]/1000, eta[:mouIdx]+zed[:mouIdx], 'k--', lw=1.2) # plot levee
water_line, = plt.plot(x/1000, eta+H, lw=2, color='blue') # plot initial condition
ax.set_prop_cycle(plt.cycler('color', ['green', 'gold', 'red']))
nitt_water_line = plt.plot(np.tile((L/1000*mou - np.array(nitt_water.RK)).transpose(), (1,3)),
                           nitt_water.seldata, lw=1.5)
nitt_water_legend = ax.legend([l for l in nitt_water_line], 
                              [ str(list(d.keys())[0]) for d in nitt_water_dict ])
for l in nitt_water_line:
    l.set_visible(False)
nitt_water_legend.set_visible(False)
nitt_bed_line, = plt.plot(L/1000*mou - nitt_bed.data[:,0], nitt_bed.data[:,1],
                         '.', color='grey', visible=False)
Qw_val = plt.text(0.7, 0.9, "Qw = " + utils.format_number(Qw), transform=ax.transAxes)
Bw_val = plt.text(( (Xs[1]-Xs[0])/4 + Xs[0])/1000, 52, \
    "backwater from \n" + "RK " + str(L*mou/1000-round(Xs[0]/1000)) + " to " + str(L*mou/1000-round(Xs[1]/1000)), \
    horizontalalignment="center", backgroundcolor="white")
Bw_brack, = plt.plot(np.array([Xs[0], Xs[0], Xs[1], Xs[1]])/1000, np.array([36, 40, 40, 36]), 'k-', lw=1.2)


# add slider
widget_color = 'lightgoldenrodyellow'
ax_Qw = plt.axes([0.075, 0.35, 0.525, 0.05], facecolor=widget_color)
slide_Qw = utils.MinMaxSlider(ax_Qw, 'water discharge (m$^3$/s)', Qwmin, Qwmax, 
    valinit=Qwinit, valstep=500, transform=ax.transAxes)


# add gui table
ax_overTable = plt.axes([0.20, 0.1, 0.5, 0.1], frameon=False, xticks=[], yticks=[])
tabData = [['0', '0', False], ['0', '0', False],
           ['0', '0', False], ['0', '0', False],
           ['0', '0', False]];
tabRowName = ['Head of Passes (RK 0)', 'New Orleans (RK 165)', 'Baton Rouge (RK 368)',
              'St. Francisville (RK 425)', 'Old River Diversion (RK 505)']
tabColName = ['flow depth (m)', 'stage (m)', 'over levee?'];
overTable = plt.table(cellText=tabData, rowLabels=tabRowName,
                      colLabels=tabColName, colWidths=[0.3, 0.2, 0.2],
                      loc="center")
overTable.scale(1, 1.5) # xscale, yscale
[ overTable._cells[(c, 0)]._text.set_text(utils.format_table(HRK)) 
    for c, HRK in zip(np.arange(1,6), H[RKidxs]) ] # insert flow depth values
[ overTable._cells[(c, 1)]._text.set_text(utils.format_table(StRK)) 
    for c, StRK in zip(np.arange(1,6), H[RKidxs]+eta[RKidxs]) ] # insert stage values
[ overTable._cells[(c, 2)]._text.set_text(str(ObRK)) 
    for c, ObRK in zip(np.arange(1,6), 
    H[RKidxs]+eta[RKidxs] > eta[RKidxs]+zed[RKidxs]) ] # insert flow depth values
    

# add gui buttons
chk_data_ax = plt.axes([0.7, 0.3, 0.15, 0.15], facecolor=background_color)
chk_data_dict = {'show water lines':'wl', 'show thalweg':'tw'}
chk_data = widget.CheckButtons(chk_data_ax, chk_data_dict,
                                            (False, False))

btn_reset_ax = plt.axes([0.8, 0.01, 0.1, 0.04])
btn_reset = widget.Button(btn_reset_ax, 'Reset', color=widget_color, hovercolor='0.975')


def update(val):
    # read values from the sliders
    Qw = slide_Qw.val
    H = hydro.get_backwater_dBdx(eta, S, B, H0, Cf, Qw, nx, dx)
    Xs = hydro.find_backwaterregion(H, dx)
    
    water_line.set_ydata(eta+H)
    Qw_val.set_text("Qw = " + utils.format_number(Qw))
    Bw_val.set_text("backwater from \n" + "RK " + str(L*mou/1000-round(Xs[0]/1000)) + \
        " to " + str(L*mou/1000-round(Xs[1]/1000)))
    Bw_val.set_x(((Xs[1]-Xs[0])/4 + Xs[0])/1000)
    Bw_brack.set_xdata(np.array([Xs[0], Xs[0], Xs[1], Xs[1]])/1000)

    # update table
    [ overTable._cells[(c, 0)]._text.set_text(utils.format_table(HRK)) 
    for c, HRK in zip(np.arange(1,6), H[RKidxs]) ] # insert flow depth values
    [ overTable._cells[(c, 1)]._text.set_text(utils.format_table(StRK)) 
        for c, StRK in zip(np.arange(1,6), H[RKidxs]+eta[RKidxs]) ] # insert stage values
    [ overTable._cells[(c, 2)]._text.set_text(str(ObRK)) 
        for c, ObRK in zip(np.arange(1,6), 
        H[RKidxs]+eta[RKidxs] > eta[RKidxs]+zed[RKidxs]) ] # insert flow depth values
    fig.canvas.draw_idle()


def reset(event):
    slide_Qw.reset()
    chk_data_status = chk_data.get_status()
    for cb in [i for i, x in enumerate(chk_data_status) if x]:
        chk_data.set_active(cb)
    fig.canvas.draw_idle()


def draw_nitt(label):
    chk_val = chk_data_dict[label]
    if chk_val == 'wl':
        for wl in nitt_water_line:
            wl.set_visible(not wl.get_visible())
        nitt_water_legend.set_visible(not nitt_water_legend.get_visible())
    elif chk_val == 'tw':
        nitt_bed_line.set_visible(not nitt_bed_line.get_visible())
    fig.canvas.draw_idle()


# connect widgets
slide_Qw.on_changed(update)
chk_data.on_clicked(draw_nitt)
btn_reset.on_clicked(reset)


# show the results
plt.show()


# if __name__ == '__main__':
#     # app = QApplication(sys.argv)
#     root = rootInit()
#     # root.show()
#     # sys.exit(app.exec_())