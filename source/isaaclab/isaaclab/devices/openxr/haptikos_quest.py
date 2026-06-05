# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Haptikos and Quest for teleoperation and interaction."""

from __future__ import annotations

from .openxr_device import OpenXRDevice


class HaptikosQuest(OpenXRDevice):
    """Haptikos exoskeleton hand tracking through OpenXR.

    The Haptikos Isaac Teleop plugin (`IsaacTeleop Haptikos Plugin <https://github.com/Haptikostech/IsaacTeleop/tree/haptikos-plugin/src/plugins/haptikos>`_) runs separately. It reads controller poses and hand tracking data
    from the Haptikos App, combines them, and injects left and right hand joint poses into the
    OpenXR runtime as hand tracker data.

    The Haptikos plugin currently supports Linux and has been tested with Meta Quest headsets.
    Other OpenXR headsets with controllers may also work.

    To use this device with Haptikos hand tracking, the following components need to be active:

    * Haptikos App.
    * Haptikos exoskeletons.
    * A Meta Quest/OpenXR headset and controllers.
    * Controllers mounted on the exoskeletons.
    * The Haptikos Isaac Teleop plugin executable.

    The Haptikos ROBOTICS API (`Haptikos API <https://github.com/Haptikostech/HaptikosAPI>`_) must be
    downloaded and installed separately.
    The headset controllers must be attached to the Haptikos exoskeletons using the included mount.
    Orientation calibration aligns the Haptikos glove forward direction with the HMD forward direction.
    """
