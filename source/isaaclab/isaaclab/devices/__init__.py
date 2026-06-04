# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Sub-package providing interfaces to different teleoperation devices.

Currently, the following categories of devices are supported:

* **Keyboard**: Standard keyboard with WASD and arrow keys.
* **Spacemouse**: 3D mouse with 6 degrees of freedom.
* **Gamepad**: Gamepad with 2D two joysticks and buttons. Example: Xbox controller.
* **OpenXR**: Uses hand tracking of index/thumb tip avg to drive the target pose. Gripping is done with pinching.
* **Haptikos + Quest**: Uses Haptikos exoskeleton hand tracking injected into OpenXR for teleoperation.
* **Haply**: Haptic device (Inverse3 + VerseGrip) with position, orientation tracking and force feedback.

All device interfaces inherit from the :class:`DeviceBase` class, which provides a
common interface for all devices. The device interface reads the input data when
the :meth:`DeviceBase.advance` method is called. It also provides the function :meth:`DeviceBase.add_callback`
to add user-defined callback functions to be called when a particular input is pressed from
the peripheral device.
"""

from .device_base import DeviceBase, DeviceCfg, DevicesCfg
from .retargeter_base import RetargeterBase, RetargeterCfg
from .teleop_device_factory import create_teleop_device

__all__ = [
    "DeviceBase",
    "DeviceCfg",
    "DevicesCfg",
    "HaptikosQuest",
    "HaplyDevice",
    "HaplyDeviceCfg",
    "ManusVive",
    "ManusViveCfg",
    "OpenXRDevice",
    "OpenXRDeviceCfg",
    "RetargeterBase",
    "RetargeterCfg",
    "Se2Gamepad",
    "Se2GamepadCfg",
    "Se2Keyboard",
    "Se2KeyboardCfg",
    "Se2SpaceMouse",
    "Se2SpaceMouseCfg",
    "Se3Gamepad",
    "Se3GamepadCfg",
    "Se3Keyboard",
    "Se3KeyboardCfg",
    "Se3SpaceMouse",
    "Se3SpaceMouseCfg",
    "create_teleop_device",
]


def __getattr__(name: str):
    if name in ["HaplyDevice", "HaplyDeviceCfg"]:
        from .haply import HaplyDevice, HaplyDeviceCfg

        return {"HaplyDevice": HaplyDevice, "HaplyDeviceCfg": HaplyDeviceCfg}[name]
    if name in ["Se2Gamepad", "Se2GamepadCfg", "Se3Gamepad", "Se3GamepadCfg"]:
        from .gamepad import Se2Gamepad, Se2GamepadCfg, Se3Gamepad, Se3GamepadCfg

        return {
            "Se2Gamepad": Se2Gamepad,
            "Se2GamepadCfg": Se2GamepadCfg,
            "Se3Gamepad": Se3Gamepad,
            "Se3GamepadCfg": Se3GamepadCfg,
        }[name]
    if name in ["Se2Keyboard", "Se2KeyboardCfg", "Se3Keyboard", "Se3KeyboardCfg"]:
        from .keyboard import Se2Keyboard, Se2KeyboardCfg, Se3Keyboard, Se3KeyboardCfg

        return {
            "Se2Keyboard": Se2Keyboard,
            "Se2KeyboardCfg": Se2KeyboardCfg,
            "Se3Keyboard": Se3Keyboard,
            "Se3KeyboardCfg": Se3KeyboardCfg,
        }[name]
    if name in ["Se2SpaceMouse", "Se2SpaceMouseCfg", "Se3SpaceMouse", "Se3SpaceMouseCfg"]:
        from .spacemouse import Se2SpaceMouse, Se2SpaceMouseCfg, Se3SpaceMouse, Se3SpaceMouseCfg

        return {
            "Se2SpaceMouse": Se2SpaceMouse,
            "Se2SpaceMouseCfg": Se2SpaceMouseCfg,
            "Se3SpaceMouse": Se3SpaceMouse,
            "Se3SpaceMouseCfg": Se3SpaceMouseCfg,
        }[name]
    if name == "HaptikosQuest":
        from .openxr.haptikos_quest import HaptikosQuest

        return HaptikosQuest
    if name in ["ManusVive", "ManusViveCfg"]:
        from .openxr.manus_vive import ManusVive, ManusViveCfg

        return {"ManusVive": ManusVive, "ManusViveCfg": ManusViveCfg}[name]
    if name in ["OpenXRDevice", "OpenXRDeviceCfg"]:
        from .openxr.openxr_device import OpenXRDevice, OpenXRDeviceCfg

        return {"OpenXRDevice": OpenXRDevice, "OpenXRDeviceCfg": OpenXRDeviceCfg}[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
