import scvelo as scv
import scanpy as sc

scv.settings.verbosity = 3  # show errors(0), warnings(1), info(2), hints(3)
scv.settings.presenter_view = True  # set max width size for presenter view
scv.set_figure_params('scvelo')  # for beautified visualization

if __name__ == '__main__':
	adata = scv.datasets.pancreas()
	
	scv.pp.filter_genes(adata, min_shared_counts=20)
	scv.pp.normalize_per_cell(adata)
	scv.pp.filter_genes_dispersion(adata, n_top_genes=2000)
	scv.pp.log1p(adata)
	
	scv.pp.filter_and_normalize(adata, min_shared_counts=20, n_top_genes=2000)
	sc.pp.neighbors(adata, n_pcs=30, n_neighbors=30)
	scv.pp.moments(adata, n_pcs=None, n_neighbors=None)
	
	scv.tl.recover_dynamics(adata)
	
	scv.tl.velocity(adata, mode='dynamical')
	scv.tl.velocity_graph(adata)
	scv.tl.velocity_pseudotime(adata)
	
	scv.tl.latent_time(adata)
	
	scv.tl.velocity_confidence(adata)
