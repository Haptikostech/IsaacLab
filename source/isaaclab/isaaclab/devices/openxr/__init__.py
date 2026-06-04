# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""OpenXR devices for teleoperation and interaction."""

from .xr_cfg import XrAnchorRotationMode, XrCfg, remove_camera_configs

__all__ = [
    "HaptikosQuest",
    "ManusVive",
    "ManusViveCfg",
    "OpenXRDevice",
    "OpenXRDeviceCfg",
    "XrAnchorRotationMode",
    "XrCfg",
    "remove_camera_configs",
]


def __getattr__(name: str):
    if name == "HaptikosQuest":
        from .haptikos_quest import HaptikosQuest

        return HaptikosQuest
    if name in ["ManusVive", "ManusViveCfg"]:
        from .manus_vive import ManusVive, ManusViveCfg

        return {"ManusVive": ManusVive, "ManusViveCfg": ManusViveCfg}[name]
    if name in ["OpenXRDevice", "OpenXRDeviceCfg"]:
        from .openxr_device import OpenXRDevice, OpenXRDeviceCfg

        return {"OpenXRDevice": OpenXRDevice, "OpenXRDeviceCfg": OpenXRDeviceCfg}[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
