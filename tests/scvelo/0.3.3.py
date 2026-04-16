# Based on https://scvelo.readthedocs.io/en/stable/getting_started.html

print("importing packages...")
import scvelo as scv
import scanpy as sc
print("done")

scv.settings.verbosity = 3  # show errors(0), warnings(1), info(2), hints(3)
scv.settings.presenter_view = True  # set max width size for presenter view
scv.set_figure_params('scvelo')  # for beautified visualization

if __name__ == '__main__':
	print("loading dataset")
	adata = scv.datasets.pancreas()
	print("done")

	print("filter_and_normalize...")
	scv.pp.filter_and_normalize(adata, min_shared_counts=20)
	print("done")

	print("neighbors and moments...")
	sc.pp.neighbors(adata, n_pcs=30, n_neighbors=30)
	scv.pp.moments(adata, n_pcs=None, n_neighbors=None)
	print("done")

	# to test dynamical mode
	# scv.tl.recover_dynamics()

	# default mode = 'steady_state'
	print("velocity...")
	scv.tl.velocity(adata, mode='steady_state')
	scv.tl.velocity_graph(adata, n_jobs=1)
	scv.tl.velocity_pseudotime(adata)
	print("done")

	print("velocity_confidence...")
	scv.tl.velocity_confidence(adata)
	print("done")
