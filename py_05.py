# variable d'environnement
import os

var_env = os.environ.get("HOME", "")
print(var_env)
