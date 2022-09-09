from omegaconf import OmegaConf
from config_service import nestle_config, rb_config

print(OmegaConf.to_yaml(nestle_config))
print("###############################")
print(OmegaConf.to_yaml(rb_config))

