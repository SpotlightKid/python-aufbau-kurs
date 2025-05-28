from a import cfg as cfg_a
from b import cfg as cfg_b

assert cfg_a is cfg_b, "Config instances are not the same"
cfg_a.foo = 42
assert cfg_b.foo == 42, "cfg_b does not have same state as cfg_a"
print(cfg_b)
