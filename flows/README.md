# Flows

Package for CLI flows. A "flow" is a way to split the CLI into different sub components depending on the desired action. Hypothetical example: `legit config` might be a valid command, which acts entirely differently from `legit validate`. One would trigger a `config` flow while the other would trigger a `validate` flow.