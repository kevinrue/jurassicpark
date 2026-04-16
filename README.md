<img src="www/jurassic_gut.png" width=200 align="right">

<br/>
<br/>
<br/>

# Jurassic Park

<p align="right">Logo credits: <a href="https://www.imm.ox.ac.uk/news/wimm-day-2025" >MRC WIMM Image Competition 2025</a></p>

This repository creates and tests environments for [velociraptor](https://github.com/kevinrue/velociraptor).

## Developer setup

Use the GitHub Actions workflows as the source of truth for setup and test commands:
`.github/workflows/create-test-upload-ubuntu.yml`,
`.github/workflows/create-test-upload-macos.yml`, and
`.github/workflows/create-test-upload-windows.yml`.

Core pinned dependencies (cross-OS parity target):

- `scvelo==0.3.3`
- `anndata==0.11.4`
- `scipy==1.15.2`
- `zarr==2.18.7`

### Windows (pyenv-win + PowerShell)

```powershell
pyenv install 3.13.5
pyenv shell 3.13.5
python -m pip install scvelo==0.3.3 anndata==0.11.4 scipy==1.15.2 zarr==2.18.7 tqdm ipywidgets
python tests/scvelo/0.3.3.py
```

### Linux/macOS (pyenv + pyenv-virtualenv)

```bash
pyenv install 3.13.5
pyenv virtualenv 3.13.5 jurassicpark-env
pyenv activate jurassicpark-env
python -m pip install scvelo==0.3.3 anndata==0.11.4 scipy==1.15.2 zarr==2.18.7 tqdm ipywidgets
python tests/scvelo/0.3.3.py
```

## Codex/Copilot usage in this repo

- Repository-wide agent guidance lives in `.github/copilot-instructions.md`.
- Add new version checks under `tests/scvelo/` using the current naming style.
- Treat files under `outputs/` as temporary backups, not standards inputs.
