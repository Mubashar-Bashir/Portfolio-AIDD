# Epoch Creator Skill

This skill creates and manages development epochs with proper governance controls.

## Purpose
- Generate epoch configuration files
- Enforce permission boundaries
- Maintain constitutional compliance
- Automate epoch transitions

## Parameters
- `epoch_name`: Name of the epoch (e.g., "Frontend_Epoch")
- `epoch_goal`: Goal of the epoch (e.g., "Stable frontend primitives")
- `allowed_actions`: Actions permitted in this epoch
- `forbidden_actions`: Actions prohibited in this epoch
- `exit_conditions`: Conditions to exit this epoch
- `constitution_version`: Version of constitution to comply with
- `human_approval_required`: Whether human approval is needed

## Usage
```bash
/sp.epoch.create --name "Backend_Contract_Epoch" --goal "Define API contracts" --allowed-actions "define,create,mock" --forbidden-actions "connect,live,integrate" --exit-conditions "schemas_validated,mocks_operational"
```

## Output
Creates epoch configuration file in `.specify/epochs/` directory with proper isolation rules.