#%%

#%% Perturbation variables non-zero
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
    # perturbations = M.get_perturbations()
    return cls, bg

def compute_ax(m_axion):
    cosmofid = {
    #####LCDM parameter####
    # 'compute_sigma8':'yes',
    'H0':67.32117,
    # 'Omega_Lambda':0.68,
    'omega_b':0.02238280,
    'N_ur': 2.046,
    'omega_cdm': 0.00001,
    'N_ncdm': 1,
    'm_ncdm': 0.06,
    'T_ncdm': 0.7137658555036082, # (4/11)^(1/3)
    'YHe': 0.2454006,
    'tau_reio': 0.05430842,
    'n_s': 0.9660499,
    'A_s': 2.100549e-09,
    #######axion parameters#######
    'scf_potential': 'axionquad',
    'Omega_scf': 0.3,
    #Also need to specify scf_param = phi_i, phi_ini_dot
    'scf_parameters': r'%g, %g, %g' % (m_axion, 0.1, 0.),
    'scf_tuning_index': 1,
    'axionquad_mass_is_log10': 'no',
    #####extra axion parameters#####
    #keep as is for fluid approx ##
    'scf_evolve_as_fluid':'yes',  ##if set to yes, will switch for fluid when threshold_scf_fluid_m_over_H is met
    'scf_evolve_like_axionCAMB':'yes', ##fluid all the time in perts ## the option no is currently bugging, to be debug.
    # 'scf_evolve_as_fluid_PH':'no', ##Whether to use to PH or original fluid approx.
    'threshold_scf_fluid_m_over_H':3, ##threshold_scf_fluid_m_over_H controls when to switch to fluid.
    'do_shooting':'yes', ##controls shooting in general; e.g. theta_s
    'do_shooting_scf': 'yes', ## necessary when log10_axion_ac & log10_fraction_axion_ac are chosen;
    'scf_has_perturbations': 'yes', ##for pedagogical purposes only
    'use_big_theta_scf': 'no', ##in perts with the fluid it is often more stable to follow the heat flux rather "Big Theta=(1+w)*Theta" than the velocity divergence "Theta".
    'use_delta_scf_over_1plusw': 'no',
    'attractor_ic_scf': 'no',##some specific IC for tracker potentials
    # 'use_ppf': 'no',##some alternative way of dealing with fluid approx instabilities;
    # 'k_output_values':'0.1',
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
    # 'evolver':1,
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
    return cls, bg

def lensed_output(M):
    ll = M['ell'][2:]
    clTT = M['tt'][2:]
    clEE = M['ee'][2:]
    clPP = M['pp'][2:]
    return ll, clTT, clEE, clPP


# TODO
# Note to self - in code: have uncommented the synchronous output sections, but left the print variable change in, also commented all printing and commented the switch delay for phi and delta phi.



#%% # LCDM
LCDM_cls, LCDM_bg = compute_lcdm()
lcdm_ll, lcdm_clTT, lcdm_clEE, lcdm_clPP = lensed_output(LCDM_cls)

#%% # m=1e-24, all DM
ax_24_cls, ax_24_bg = compute_ax(1e-24)
ax_24_ll, ax_24_clTT, ax_24_clEE, ax_24_clPP = lensed_output(ax_24_cls)

#%% # m=1e-25, all DM
ax_25_cls, ax_25_bg = compute_ax(1e-25)
ax_25_ll, ax_25_clTT, ax_25_clEE, ax_25_clPP = lensed_output(ax_25_cls)

#%% m=1e-26, all DM
ax_26_cls, ax_26_bg = compute_ax(1e-26)
ax_26_ll, ax_26_clTT, ax_26_clEE, ax_26_clPP = lensed_output(ax_26_cls)

#%% # m=5e-7, all DM
ax_7_cls, ax_7_bg = compute_ax(5e-7)#5e-7)
ax_7_ll, ax_7_clTT, ax_7_clEE, ax_7_clPP = lensed_output(ax_7_cls)


#%% TT power spectrum

fig_cls, ax_cls = plt.subplots()
ax_cls.set_xscale('log')
ax_cls.set_yscale('linear')
# ax_cls.set_xlim([2,2500])
ax_cls.set_xlabel(r'$\ell$')
ax_cls.set_ylabel(r'$[\ell(\ell+1)/2\pi]  C_\ell^\mathrm{TT}$')
ax_cls.plot(lcdm_ll,lcdm_clTT*lcdm_ll*(lcdm_ll+1)/2./np.pi,'r-', label=r'$\Lambda$CDM')
ax_cls.plot(ax_24_ll,ax_24_clTT*ax_24_ll*(ax_24_ll+1)/2./np.pi, label=r'$m=1x10^{-24}$ eV')
ax_cls.plot(ax_25_ll,ax_25_clTT*ax_25_ll*(ax_25_ll+1)/2./np.pi, label=r'$m=1x10^{-25}$ eV')
ax_cls.plot(ax_26_ll,ax_26_clTT*ax_26_ll*(ax_26_ll+1)/2./np.pi, label=r'$m=1x10^{-26}$ eV')
# ax_cls.plot(ax_7_ll,ax_7_clTT*ax_7_ll*(ax_7_ll+1)/2./np.pi, label=r'$m=1x10^{-7}$ eV')
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
ax_H.loglog(ax_24_bg['z'], ax_24_bg['H [1/Mpc]'], label=r'$m=1x10^{-24}$ eV')
ax_H.loglog(ax_25_bg['z'], ax_25_bg['H [1/Mpc]'], label=r'$m=1x10^{-25}$ eV')
ax_H.loglog(ax_26_bg['z'], ax_26_bg['H [1/Mpc]'], label=r'$m=1x10^{-26}$ eV')
# ax_H.loglog(ax_7_bg['z'], ax_7_bg['H [1/Mpc]'], label=r'$m=5x10^{-7}$ eV')
ax_H.legend()



fig_rho, ax_rho = plt.subplots()
ax_rho.set_xlabel(r'z')
ax_rho.set_ylabel(r'$\rho_{tot}$')
ax_rho.loglog(LCDM_bg['z'], LCDM_bg['(.)rho_tot'],'r-', label=r'$\Lambda$CDM')
ax_rho.loglog(ax_24_bg['z'], ax_24_bg['(.)rho_tot'], label=r'$m=1x10^{-24}$ eV')
ax_rho.loglog(ax_25_bg['z'], ax_25_bg['(.)rho_tot'], label=r'$m=1x10^{-25}$ eV')
ax_rho.loglog(ax_26_bg['z'], ax_26_bg['(.)rho_tot'], label=r'$m=1x10^{-26}$ eV')
# ax_rho.loglog(ax_7_bg['z'], ax_7_bg['(.)rho_tot'], label=r'$m=5x10^{-7}$ eV')
ax_rho.legend()





