# Copyright (c) ONNX Project Contributors

# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import numpy as np

from onnx.reference.ops._op import OpRunUnaryNum


class Softplus(OpRunUnaryNum):
    def _run(self, X):
        tmp = np.asarray(np.exp(X), dtype=X.dtype)
        tmp += 1
        np.log(tmp, out=tmp)
        return (tmp,)
