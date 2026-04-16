# Copilot Instructions For Jurassic Park

## Project Scope

- This repository creates and tests Python environments for velociraptor.
- Keep the current mixed R project layout intact. Do not propose converting this repo into a Python package unless explicitly requested.

## Canonical Source Of Truth

- Treat `.github/workflows/create-test-upload-ubuntu.yml`, `.github/workflows/create-test-upload-macos.yml`, and `.github/workflows/create-test-upload-windows.yml` as the canonical sources for setup, dependency pins, and test commands.
- Ignore files under `outputs/` for standards decisions. They are temporary backups, not policy inputs.

## Dependency Policy

- Keep cross-OS parity where possible for core pins.
- Current baseline pins used in CI are:
  - `scvelo==0.3.3`
  - `anndata==0.11.4`
  - `scipy==1.15.2`
  - `zarr==2.18.7`
- Do not change these pins unless explicitly asked.
- If a dependency update is requested, explain OS impact and update Linux/macOS and Windows install commands together when feasible.

## Test Conventions

- Primary smoke test target is `tests/scvelo/0.3.3.py`.
- Version-specific test scripts belong in `tests/scvelo/` and should follow the existing naming pattern (for example `0.3.2.py`, `0.3.2-dynamical.py`).
- Prefer small, explicit script additions over broad refactors.

## Command Style

- On Linux/macOS, follow the pyenv + pyenv-virtualenv flow in CI.
- On Windows, follow the pyenv-win shell flow in CI.
- When documenting or proposing local commands, mirror CI command structure and pin set.

## Editing Guidance

- Keep changes minimal and scoped to the user request.
- Avoid introducing tooling config files (formatters/linters/type-checking frameworks) unless explicitly requested.
- Preserve existing CI behavior and comments unless a change is requested.
