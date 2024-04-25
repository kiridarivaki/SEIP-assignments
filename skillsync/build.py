#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.pycharm")
use_plugin("python.install_dependencies")


name = "skillsync"
default_task = "publish"


@init
def set_properties(project):
    project.depends_on("pytest")
    project.depends_on("pytest-mock")
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property("dir_source_unittest_python", "src/unittest/python")

    project.set_property("coverage_threshold_warn", 70)  # Coverage warning threshold
    project.set_property("coverage_fail_on_thresholds", False)  # Do not fail on missing threshold
    project.set_property("coverage_break_build", False)  # Prevent build failure due to coverage   

