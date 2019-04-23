import cobra
import numpy as np

def miFuncion():
	model = cobra.io.read_sbml_model("iMM904.xml")
	print "Ajustanto modelo segun datos experimentales=============="
	value=3.632
	model.reactions.get_by_id("EX_etoh_e").upper_bound=value+0.1*value 
	model.reactions.get_by_id("EX_etoh_e").lower_bound=value-0.1*value

	value=0.0123
	model.reactions.get_by_id("EX_succ_e").upper_bound=value+0.1*value 
	model.reactions.get_by_id("EX_succ_e").lower_bound=value-0.1*value

	value=0.0006
	model.reactions.get_by_id("EX_pyr_e").upper_bound=value+0.1*value 
	model.reactions.get_by_id("EX_pyr_e").lower_bound=value-0.1*value

	value=-3.002
	model.reactions.get_by_id("EX_glc__D_e").upper_bound=value+0.1*value 
	model.reactions.get_by_id("EX_glc__D_e").lower_bound=value-0.1*value

	solution=model.optimize()
	model.summary()
	print "Evaluando calidad de Prediccion=============="

	Vp= np.array([solution.fluxes['EX_glyc_e'],solution.fluxes['EX_ac_e'], solution.fluxes['EX_acald_e']])
	Vr= np.array([0.211,0.0078,0.0048])

	d= (Vr-Vp)/Vr

	Ecludian_norm = np.dot(d,d)

	print(Ecludian_norm)

  	return 1

if __name__ == "__main__":
    miFuncion()

