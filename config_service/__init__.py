from hydra import compose, initialize
from omegaconf import OmegaConf

# global initialization
initialize(version_base=None, config_path="../conf", job_name="verification_api")
nestle_config = compose(config_name="nestle")
rb_config = compose(config_name="rb")
# cfg = compose(config_name="config")