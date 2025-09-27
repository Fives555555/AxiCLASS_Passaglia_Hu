#%%

#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from classy import Class
matplotlib.use('TkAgg')
plt.ion()

def compute_lcdm():
    cosmofid = {
    #####LCDM parameter####
    'H0':67.32117,
    # 'Omega_Lambda':0.68,    
    'omega_b':0.02238280,
    'N_ur': 2.046,
    'omega_cdm': 0.1201075,
    'N_ncdm': 1,
    'm_ncdm': 0.06,
    'T_ncdm': 0.7137658555036082, # (4/11)^(1/3)
    'YHe': 0.2454006,
    'tau_reio': 0.05430842,
    'n_s': 0.9660499,
    'A_s': 2.100549e-09,
    ################################
    'get_lyman_alpha_tilt_and_amplitude':'yes',
    'do_shooting':'yes',
    'k_output_values':'0.1',
    ########extra parameters########
    'modes': 's',
    'gauge': 'synchronous',
    'non linear':'halofit',
    # 'evolver':1,
    ####verbose###
    'input_verbose': 1,
    'background_verbose': 1,
    'thermodynamics_verbose': 1,
    'perturbations_verbose': 1,
    'transfer_verbose': 1,
    'primordial_verbose': 1,
    'harmonic_verbose': 1,
    'fourier_verbose': 1,
    'lensing_verbose': 1,
    'output_verbose': 1,
    }
    M = Class()
    M.set({'output': 'tCl,pCl,lCl,mPk', 'z_max_pk':4, 'P_k_max_h/Mpc':2 , 'lensing':'yes'})
    M.set(cosmofid)
    M.compute()
    cls = M.lensed_cl(2500)
    bg = M.get_background() # load background table
    pt = M.get_perturbations()
    return cls, bg, pt, M

def compute_ax_full(m_axion):
    cosmofid = {
    #####LCDM parameter####
    # 'compute_sigma8':'yes',
    'H0':67.32117,
    # 'Omega_Lambda':0.68,
    'omega_b':0.02238280,
    'N_ur': 2.046,
    'omega_cdm': 0.00001,#0.1201075,#0.00001,
    'N_ncdm': 1,
    'm_ncdm': 0.06,
    'T_ncdm': 0.7137658555036082, # (4/11)^(1/3)
    'YHe': 0.2454006,
    'tau_reio': 0.05430842,
    'n_s': 0.9660499,
    'A_s': 2.100549e-09,
    #######axion parameters#######
    'scf_potential': 'axionquad',
    'Omega_scf': 0.3,#0.005,
    #Also need to specify scf_param = phi_i, phi_ini_dot
    'scf_parameters': r'%g, %g, %g' % (m_axion, 0.1, 0.),
    'scf_tuning_index': 1,
    'axionquad_mass_is_log10': 'no',
    #####extra axion parameters#####
    #keep as is for fluid approx ##
    'scf_evolve_as_fluid':'yes',  ##if set to yes, will switch for fluid when threshold_scf_fluid_m_over_H is met
    'scf_evolve_like_axionCAMB':'no', ##fluid all the time in perts ## the option no is currently bugging, to be debug.
    'scf_evolve_as_fluid_PH':'yes', ##Whether to use to PH or original fluid approx.
    'threshold_scf_fluid_m_over_H':80, ##threshold_scf_fluid_m_over_H controls when to switch to fluid.
    'do_shooting':'no', ##controls shooting in general; e.g. theta_s
    'do_shooting_scf': 'no', ## necessary when log10_axion_ac & log10_fraction_axion_ac are chosen;
    'scf_has_perturbations': 'yes', ##for pedagogical purposes only
    'use_big_theta_scf': 'no', ##in perts with the fluid it is often more stable to follow the heat flux rather "Big Theta=(1+w)*Theta" than the velocity divergence "Theta".
    'use_delta_scf_over_1plusw': 'no',
    'attractor_ic_scf': 'no',##some specific IC for tracker potentials
    # 'use_ppf': 'no',##some alternative way of dealing with fluid approx instabilities;
    'k_output_values':'0.01',
    ################################
    'get_lyman_alpha_tilt_and_amplitude':'yes',
    'include_scf_in_delta_m':'yes', #do we include scf contribution to delta_m ? default is false, unless the potential is axionquad or axion with n=1
    'include_scf_in_delta_cb':'yes', #do we include scf contribution to delta_cb ? default is false
    'include_scf_in_growth_factor': 'no', #include the axion contribution to the growth factor? Useful only in output.
    ########extra parameters########
    'modes': 's',
    'gauge': 'synchronous',
    #'lensing':'yes',
    'non linear':'halofit',
    #'compute_phase_shift': 'no',
    'evolver':0,
    #################################
    ####verbose###
    'input_verbose': 1,
    'background_verbose': 10,
    'thermodynamics_verbose': 1,
    'perturbations_verbose': 1,
    'transfer_verbose': 1,
    'primordial_verbose': 1,
    'harmonic_verbose': 1,
    'fourier_verbose': 1,
    'lensing_verbose': 1,
    'output_verbose': 1,
    }
    M = Class()
    M.set({'output': 'tCl,pCl,lCl,mPk', 'z_max_pk':4, 'P_k_max_h/Mpc':2 , 'lensing':'yes'})
    M.set(cosmofid)
    M.compute()
    cls = M.lensed_cl(2500)
    bg = M.get_background()
    pt = M.get_perturbations()
    return cls, bg, pt, M


def compute_ax_efa(m_axion, switch):
    cosmofid = {
    #####LCDM parameter####
    # 'compute_sigma8':'yes',
    'H0':67.32117,
    # 'Omega_Lambda':0.68,
    'omega_b':0.02238280,
    'N_ur': 2.046,
    'omega_cdm': 0.00001,#0.1201075,#0.00001,
    'N_ncdm': 1,
    'm_ncdm': 0.06,
    'T_ncdm': 0.7137658555036082, # (4/11)^(1/3)
    'YHe': 0.2454006,
    'tau_reio': 0.05430842,
    'n_s': 0.9660499,
    'A_s': 2.100549e-09,
    #######axion parameters#######
    'scf_potential': 'axionquad',
    'Omega_scf': 0.3,#0.005,
    #Also need to specify scf_param = phi_i, phi_ini_dot
    'scf_parameters': r'%g, %g, %g' % (m_axion, 0.1, 0.),
    'scf_tuning_index': 1,
    'axionquad_mass_is_log10': 'no',
    #####extra axion parameters#####
    #keep as is for fluid approx ##
    'scf_evolve_as_fluid':'yes',  ##if set to yes, will switch for fluid when threshold_scf_fluid_m_over_H is met
    'scf_evolve_like_axionCAMB':'no', ##fluid all the time in perts ## the option no is currently bugging, to be debug.
    'scf_evolve_as_fluid_PH':'yes', ##Whether to use to PH or original fluid approx.
    'threshold_scf_fluid_m_over_H':switch, ##threshold_scf_fluid_m_over_H controls when to switch to fluid.
    'do_shooting':'no', ##controls shooting in general; e.g. theta_s
    'do_shooting_scf': 'no', ## necessary when log10_axion_ac & log10_fraction_axion_ac are chosen;
    'scf_has_perturbations': 'yes', ##for pedagogical purposes only
    'use_big_theta_scf': 'no', ##in peyesrts with the fluid it is often more stable to follow the heat flux rather "Big Theta=(1+w)*Theta" than the velocity divergence "Theta".
    'use_delta_scf_over_1plusw': 'no',
    'attractor_ic_scf': 'no',##some specific IC for tracker potentials
    # 'use_ppf': 'no',##some alternative way of dealing with fluid approx instabilities;
    'k_output_values':'0.01',
    ################################
    'get_lyman_alpha_tilt_and_amplitude':'yes',
    'include_scf_in_delta_m':'yes', #do we include scf contribution to delta_m ? default is false, unless the potential is axionquad or axion with n=1
    'include_scf_in_delta_cb':'yes', #do we include scf contribution to delta_cb ? default is false
    'include_scf_in_growth_factor': 'no', #include the axion contribution to the growth factor? Useful only in output.
    ########extra parameters########
    'modes': 's',
    'gauge': 'synchronous',
    #'lensing':'yes',
    'non linear':'halofit',
    #'compute_phase_shift': 'no',
    'evolver':0,
    #################################
    ####verbose###
    'input_verbose': 1,
    'background_verbose': 10,
    'thermodynamics_verbose': 1,
    'perturbations_verbose': 1,
    'transfer_verbose': 1,
    'primordial_verbose': 1,
    'harmonic_verbose': 1,
    'fourier_verbose': 1,
    'lensing_verbose': 1,
    'output_verbose': 1,
    }
    M = Class()
    M.set({'output': 'tCl,pCl,lCl,mPk', 'z_max_pk':4, 'P_k_max_h/Mpc':2 , 'lensing':'yes'})
    M.set(cosmofid)
    M.compute()
    cls = M.lensed_cl(2500)
    bg = M.get_background()
    pt = M.get_perturbations()
    return cls, bg, pt, M

def lensed_output(M):
    ll = M['ell'][2:]
    clTT = M['tt'][2:]
    clEE = M['ee'][2:]
    clPP = M['pp'][2:]
    return ll, clTT, clEE, clPP

def matter_power(M, kk):
    Pk = [] # P(k) in (Mpc/h)**3
    h = M.h() # get reduced Hubble for conversions to 1/Mpc
    for k in kk:
        Pk.append(M.pk(k*h,0.)*h**3) # function .pk(k,z)
    return Pk



#%%

# want to get the evolution of rho, delta , phi , delta phi, matter power spectrum and TT power spectrum (this is below)

#%% # LCDM
LCDM_cls, LCDM_bg, LCDM_pt, LCDM_M = compute_lcdm()
lcdm_ll, lcdm_clTT, lcdm_clEE, lcdm_clPP = lensed_output(LCDM_cls)
#%%
np.save('LCDM_cls.npy', LCDM_cls)
np.save('LCDM_bg.npy', LCDM_bg)
np.save('LCDM_pt.npy', LCDM_pt)

#%% # m=1e-28 EFA N=3
ax_28E_cls3, ax_28E_bg3, ax_28E_pt3, ax_28_M3 = compute_ax_efa(1e-28, 3)
ax_28E_ll3, ax_28E_clTT3, ax_28E_clEE3, ax_28E_clPP3 = lensed_output(ax_28E_cls3)
#%%
np.save('ax_28E_cls3.npy', ax_28E_cls3)
np.save('ax_28E_bg3.npy', ax_28E_bg3)
np.save('ax_28E_pt3.npy', ax_28E_pt3)

#%% # m=1e-28 EFA N=10
ax_28E_cls10, ax_28E_bg10, ax_28E_pt10, ax_28_M10 = compute_ax_efa(1e-28, 10)
ax_28E_ll10, ax_28E_clTT10, ax_28E_clEE10, ax_28E_clPP10 = lensed_output(ax_28E_cls10)
#%%
np.save('ax_28E_cls10.npy', ax_28E_cls10)
np.save('ax_28E_bg10.npy', ax_28E_bg10)
np.save('ax_28E_pt10.npy', ax_28E_pt10)

#%% # m=1e-28 EFA N=30
ax_28E_cls30, ax_28E_bg30, ax_28E_pt30, ax_28_M30 = compute_ax_efa(1e-28, 30)
ax_28E_ll30, ax_28E_clTT30, ax_28E_clEE30, ax_28E_clPP30 = lensed_output(ax_28E_cls30)
#%%
np.save('ax_28E_cls30.npy', ax_28E_cls30)
np.save('ax_28E_bg30.npy', ax_28E_bg30)
np.save('ax_28E_pt30.npy', ax_28E_pt30)


#%% # m=1e-28 Full (N=80)
ax_28F_cls, ax_28F_bg, ax_28F_pt, ax_28F_M = compute_ax_full(1e-28)
ax_28F_ll, ax_28F_clTT, ax_28F_clEE, ax_28F_clPP = lensed_output(ax_28F_cls)
#%%
np.save('ax_28F_cls.npy', ax_28F_cls)
np.save('ax_28F_bg.npy', ax_28F_bg)
np.save('ax_28F_pt.npy', ax_28F_pt)



#%%  How to save and import a dictionary
# import numpy as np

# # Save
# dictionary = {'hello':'world'}
# np.save('my_file.npy', dictionary) 

# # Load
# read_dictionary = np.load('my_file.npy',allow_pickle='TRUE').item()
# print(read_dictionary['hello']) # displays "world"


#%% Keys

# BG keys - call bg['a']:
# (['z', 'proper time [Gyr]', 'conf. time [Mpc]', 'H [1/Mpc]', 'comov. dist.', 'ang.diam.dist.', 'lum. dist.', 'comov.snd.hrz.', '(.)rho_g', '(.)rho_b', '(.)rho_cdm', '(.)rho_ncdm[0]', '(.)p_ncdm[0]', '(.)rho_lambda', '(.)rho_ur', '(.)rho_crit', '(.)rho_scf', '(.)Omega_scf', '(.)p_scf', '(.)p_prime_scf', '(.)w_scf', '(.)dw_scf', 'phi_scf', "phi'_scf", 'V_scf', "V'_scf", "V''_scf", '(.)rho_tot', '(.)p_tot', '(.)p_tot_prime', 'gr.fac. D', 'gr.fac. f'])

# PT keys - call ax_28_pt['scalar'][k_value]['a'] (MUST HAVE K OUTPUT VALUE):
# (['a', 'tau [Mpc]', 'delta_g', 'theta_g', 'shear_g', 'pol0_g', 'pol1_g', 'pol2_g', 'delta_b', 'theta_b', 'psi', 'phi', 'delta_ur', 'theta_ur', 'shear_ur', 'delta_cdm', 'theta_cdm', 'delta_ncdm[0]', 'theta_ncdm[0]', 'shear_ncdm[0]', 'cs2_ncdm[0]', 'delta_phi_scf', 'delta_phi_over_phi_scf', 'delta_phi_prime_scf', 'delta_scf', 'theta_scf'])

#%% Phi - irrelevant for PH approx

# fig_phi, ax_phi = plt.subplots()
# ax_phi.set_xscale('log')
# ax_phi.plot(ax_28E_bg3['conf. time [Mpc]'], ax_28E_bg3['phi_scf'], linestyle='solid', label=r'PH EFA, N=3')
# ax_phi.plot(ax_28E_bg10['conf. time [Mpc]'], ax_28E_bg10['phi_scf'], linestyle='dotted', label=r'PH EFA, N=10')
# ax_phi.plot(ax_28E_bg30['conf. time [Mpc]'], ax_28E_bg30['phi_scf'],linestyle='dashdot', label=r'PH EFA, N=30')
# ax_phi.plot(ax_28F_bg['conf. time [Mpc]'], ax_28F_bg['phi_scf'], linestyle='dashed', label=r'Exact evolution')
# ax_phi.set_xlabel(r'$\eta$ [Mpc]')
# ax_phi.set_ylabel(r'$\phi$');
# ax_phi.set_xlim([5e1, 2e4]);
# ax_phi.legend()

#%% Delta phi

# fig_delphi, ax_delphi = plt.subplots()
# ax_delphi.set_xscale('log')
# ax_delphi.plot(ax_28E_pt['scalar'][0]['tau [Mpc]'], ax_28E_pt['scalar'][0]['delta_phi_scf'], label='PH EFA')
# ax_delphi.plot(ax_28F_pt['scalar'][0]['tau [Mpc]'], ax_28F_pt['scalar'][0]['delta_phi_scf'], label='Exact evolution')
# ax_delphi.set_xlabel(r'$\eta$ [Mpc]')
# ax_delphi.set_ylabel(r'$\delta\phi$');
# ax_delphi.set_xlim([5e1, 2e4]);
# ax_delphi.legend()

#%% Rho

fig_rho, ax_rho = plt.subplots()
ax_rho.set_xscale('log')
ax_rho.set_yscale('log')
ax_rho.plot(ax_28E_bg3['conf. time [Mpc]'], ax_28E_bg3['(.)rho_scf'], linestyle='solid', label=r'PH EFA, N=3')
ax_rho.plot(ax_28E_bg10['conf. time [Mpc]'], ax_28E_bg10['(.)rho_scf'], linestyle='dotted', label=r'PH EFA, N=10')
ax_rho.plot(ax_28E_bg30['conf. time [Mpc]'], ax_28E_bg30['(.)rho_scf'], linestyle='dashdot', label=r'PH EFA, N=30')
ax_rho.plot(ax_28F_bg['conf. time [Mpc]'], ax_28F_bg['(.)rho_scf'], linestyle='dashed', label=r'Exact evolution')
ax_rho.set_xlabel(r'$\eta$ [Mpc]')
ax_rho.set_ylabel(r'$\rho$');
ax_rho.set_xlim([5e1, 2e4]);
ax_rho.legend()

#%% Delta

fig_del, ax_del = plt.subplots()
ax_del.set_xscale('log')
ax_del.set_yscale('log')
ax_del.plot(ax_28E_pt3['scalar'][0]['tau [Mpc]'], abs(ax_28E_pt3['scalar'][0]['delta_scf']), linestyle='solid', label=r'PH EFA, N=3')
ax_del.plot(ax_28E_pt10['scalar'][0]['tau [Mpc]'], abs(ax_28E_pt10['scalar'][0]['delta_scf']), linestyle='dotted', label=r'PH EFA, N=10')
ax_del.plot(ax_28E_pt30['scalar'][0]['tau [Mpc]'], abs(ax_28E_pt30['scalar'][0]['delta_scf']), linestyle='dashdot', label=r'PH EFA, N=30')
ax_del.plot(ax_28F_pt['scalar'][0]['tau [Mpc]'], abs(ax_28F_pt['scalar'][0]['delta_scf']), linestyle='dashed', label=r'Exact evolution')
ax_del.set_xlabel(r'$\eta$ [Mpc]')
ax_del.set_ylabel(r'$\delta$');
ax_del.set_xlim([5e1, 2e4]);
ax_del.legend()

#%% Linear matter power spectrum

kk = np.logspace(-4,np.log10(3),1000) # k in h/Mpc
LCDM_Pk = matter_power(LCDM_M, kk)
ax_28_Pk3 = matter_power(ax_28_M3, kk)
ax_28_Pk10 = matter_power(ax_28_M10, kk)
ax_28_Pk30 = matter_power(ax_28_M30, kk)
# ax_28_PkF = matter_power(ax_28F_M, kk)

fig_pk, ax_pk = plt.subplots()
ax_pk.set_xscale('log')
ax_pk.set_yscale('log')
ax_pk.plot(kk, LCDM_Pk, label=r'$\Lambda$CDM')
ax_pk.plot(kk, ax_28_Pk3, label=r'PH EFA, N=3')
# ax_pk.plot(kk, ax_28_Pk10, label=r'PH EFA, N=10')
# ax_pk.plot(kk, ax_28_Pk30, label=r'PH EFA, N=30')
# ax_pk.plot(kk, ax_28_PkF, linestyle='dashed', label=r'Exact evolution')
ax_pk.set_xlim(kk[0],kk[-1])
ax_pk.set_xlabel(r'$k \,\,\,\, [h/\mathrm{Mpc}]$')
ax_pk.set_ylabel(r'$P(k) \,\,\,\, [\mathrm{Mpc}/h]^3$')
ax_pk.legend()



#%% TT power spectrum

fig_cls, ax_cls = plt.subplots()
ax_cls.set_xscale('log')
ax_cls.set_yscale('linear')
# ax_cls.set_xlim([2,2500])
ax_cls.set_xlabel(r'$\ell$')
ax_cls.set_ylabel(r'$[\ell(\ell+1)/2\pi]  C_\ell^\mathrm{TT}$')
ax_cls.plot(lcdm_ll,lcdm_clTT*lcdm_ll*(lcdm_ll+1)/2./np.pi,'r-', label=r'$\Lambda$CDM')
ax_cls.plot(ax_28E_ll3,ax_28E_clTT3*ax_28E_ll3*(ax_28E_ll3+1)/2./np.pi, label=r'PH EFA, N=3')
ax_cls.plot(ax_28E_ll10,ax_28E_clTT10*ax_28E_ll10*(ax_28E_ll10+1)/2./np.pi, label=r'PH EFA, N=10')
ax_cls.plot(ax_28E_ll30,ax_28E_clTT30*ax_28E_ll30*(ax_28E_ll30+1)/2./np.pi, label=r'PH EFA, N=30')
# ax_cls.plot(ax_28F_ll,ax_28F_clTT*ax_28F_ll*(ax_28F_ll+1)/2./np.pi, linestyle='dashed', label=r'Exact evolution')
ax_cls.legend()



#%% Background evolution

# bg keys: dict_keys(['z', 'proper time [Gyr]', 'conf. time [Mpc]', 'H [1/Mpc]', 'comov. dist.', 'ang.diam.dist.', 'lum. dist.', 'comov.snd.hrz.', '(.)rho_g', '(.)rho_b', '(.)rho_cdm', '(.)rho_ncdm[0]', '(.)p_ncdm[0]', '(.)rho_lambda', '(.)rho_ur', '(.)rho_crit', '(.)rho_tot', '(.)p_tot', '(.)p_tot_prime', 'gr.fac. D', 'gr.fac. f'])



# models = ['EdS','LCDM']
# cosmo = {}
# for M in models:
#     cosmo[M] = Class()
#     cosmo[M].set({'Omega_b':0.05})
#     if M=='EdS':
#         cosmo[M].set({'Omega_cdm':0.95})
#     elif M=='LCDM':
#         cosmo[M].set({'Omega_cdm':0.25})
#     cosmo[M].compute()
    
    
    
# distance_keys = ['lum. dist.','ang.diam.dist.','comov. dist.']
# texnames = {'lum. dist.':r'$d_L$','comov. dist.':r'$\chi$','ang.diam.dist.':r'$d_A$',}
# for M in models:
#     bg = cosmo[M].get_background()
#     print(bg.keys())
#     for key in distance_keys:
#         ls='--' if M=='EdS' else '-'
#         plt.loglog(bg['z'],bg[key]*cosmo[M].Hubble(0.),label=texnames[key],ls=ls)
# plt.xlim([0.08,10])
# plt.ylim([0.08,20])
# plt.xlabel(r'$z$')
# plt.ylabel(r'$\mathrm{distance}\quad (1/H_0)$')



fig_H, ax_H = plt.subplots()
# ax_H.set_xscale('log')
# ax_H.set_yscale('linear')
# ax_H.set_xlim([2,2500])
ax_H.set_xlabel(r'z')
ax_H.set_ylabel(r'H [1/Mpc]')
ax_H.loglog(LCDM_bg['z'], LCDM_bg['H [1/Mpc]'],'r-', label=r'$\Lambda$CDM')
ax_H.loglog(ax_28E_bg['z'], ax_28E_bg['H [1/Mpc]'], label=r'PH EFA $m=1x10^{-28}$ eV')

ax_H.legend()



fig_rho, ax_rho = plt.subplots()
ax_rho.set_xlabel(r'z')
ax_rho.set_ylabel(r'$\rho_{tot}$')
ax_rho.loglog(LCDM_bg['z'], LCDM_bg['(.)rho_tot'],'r-', label=r'$\Lambda$CDM')
ax_rho.loglog(ax_28E_bg['z'], ax_28E_bg['(.)rho_tot'], label=r'PH EFA $m=1x10^{-28}$ eV')

ax_rho.legend()





