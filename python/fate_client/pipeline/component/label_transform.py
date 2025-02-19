#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from pipeline.param.label_transform_param import LabelTransformParam
from pipeline.component.component_base import Component
from pipeline.interface import Input
from pipeline.interface import Output
from pipeline.utils.logger import LOGGER


class LabelTransform(Component, LabelTransformParam):
    def __init__(self, **kwargs):
        Component.__init__(self, **kwargs)

        #print (self.name)
        LOGGER.debug(f"{self.name} component created")
        new_kwargs = self.erase_component_base_param(**kwargs)

        LabelTransformParam.__init__(self, **new_kwargs)

        self.input = Input(self.name)
        self.output = Output(self.name, data_type='single', has_model=True)
        self._module_name = "LabelTransform"
