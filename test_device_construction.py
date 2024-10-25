import numpy as np

import parameters as params
from devices import device_properties_dict
import device_construction
import visualization


device_properties = device_properties_dict[params.DEVICE_NAME]
xs = np.arange(start=device_properties["boundaries"][0], stop=device_properties["boundaries"][-1], step=params.X_STEP)
device = device_construction.get_device(xs, **device_properties)
visualization.plot_device(device)
