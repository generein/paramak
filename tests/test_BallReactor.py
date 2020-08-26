import os
import unittest
from pathlib import Path

import pytest

import paramak


class test_BallReactor(unittest.TestCase):
    def test_BallReactor_creation_with_narrow_divertor(self):
        """creates blanket from parametric shape and checks a solid is created"""

        test_reactor = paramak.BallReactor(
            inner_bore_radial_thickness=50,
            inboard_tf_leg_radial_thickness=200,
            center_column_shield_radial_thickness=50,
            divertor_radial_thickness=50,
            inner_plasma_gap_radial_thickness=150,
            plasma_radial_thickness=100,
            outer_plasma_gap_radial_thickness=50,
            firstwall_radial_thickness=50,
            blanket_radial_thickness=100,
            blanket_rear_wall_radial_thickness=10,
            elongation=2,
            triangularity=0.55,
            number_of_tf_coils=16,
        )

        test_reactor.export_stp()

        assert len(test_reactor.shapes_and_components) == 7

    def test_BallReactor_creation_with_wide_divertor(self):
        """creates blanket from parametric shape and checks a solid is created"""

        test_reactor = paramak.BallReactor(
            inner_bore_radial_thickness=50,
            inboard_tf_leg_radial_thickness=200,
            center_column_shield_radial_thickness=50,
            divertor_radial_thickness=172.5,
            inner_plasma_gap_radial_thickness=150,
            plasma_radial_thickness=100,
            outer_plasma_gap_radial_thickness=50,
            firstwall_radial_thickness=50,
            blanket_radial_thickness=100,
            blanket_rear_wall_radial_thickness=10,
            elongation=2,
            triangularity=0.55,
            number_of_tf_coils=16,
        )

        test_reactor.export_stp()

        assert len(test_reactor.shapes_and_components) == 7

    def test_BallReactor_svg_creation(self):
        os.system("rm test_ballreactor_image.svg")

        test_reactor = paramak.BallReactor(
            inner_bore_radial_thickness=50,
            inboard_tf_leg_radial_thickness=50,
            center_column_shield_radial_thickness=50,
            divertor_radial_thickness=100,
            inner_plasma_gap_radial_thickness=50,
            plasma_radial_thickness=200,
            outer_plasma_gap_radial_thickness=50,
            firstwall_radial_thickness=50,
            blanket_radial_thickness=100,
            blanket_rear_wall_radial_thickness=50,
            elongation=2,
            triangularity=0.55,
            number_of_tf_coils=16,
        )
        test_reactor.export_svg("test_ballreactor_image.svg")

        assert Path("test_ballreactor_image.svg").exists() is True
        os.system("rm test_ballreactor_image.svg")

    def test_BallReactor_with_pf_coils(self):
        test_reactor = paramak.BallReactor(
            inner_bore_radial_thickness=10,
            inboard_tf_leg_radial_thickness=30,
            center_column_shield_radial_thickness=60,
            divertor_radial_thickness=50,
            inner_plasma_gap_radial_thickness=30,
            plasma_radial_thickness=300,
            outer_plasma_gap_radial_thickness=30,
            firstwall_radial_thickness=30,
            blanket_radial_thickness=30,
            blanket_rear_wall_radial_thickness=30,
            elongation=2,
            triangularity=0.55,
            number_of_tf_coils=16,
            rotation_angle=180,
            pf_coil_radial_thicknesses=[50, 50, 50, 50],
            pf_coil_vertical_thicknesses=[50, 50, 50, 50],
            pf_coil_to_rear_blanket_radial_gap=50,
            pf_coil_to_tf_coil_radial_gap=50,
        )
        test_reactor.export_stp()
        assert len(test_reactor.shapes_and_components) == 11

    def test_BallReactor_with_pf_and_tf_coils(self):
        test_reactor = paramak.BallReactor(
            inner_bore_radial_thickness=10,
            inboard_tf_leg_radial_thickness=30,
            center_column_shield_radial_thickness=60,
            divertor_radial_thickness=50,
            inner_plasma_gap_radial_thickness=30,
            plasma_radial_thickness=300,
            outer_plasma_gap_radial_thickness=30,
            firstwall_radial_thickness=30,
            blanket_radial_thickness=30,
            blanket_rear_wall_radial_thickness=30,
            elongation=2,
            triangularity=0.55,
            number_of_tf_coils=16,
            rotation_angle=180,
            pf_coil_radial_thicknesses=[50, 50, 50, 50],
            pf_coil_vertical_thicknesses=[50, 50, 50, 50],
            pf_coil_to_rear_blanket_radial_gap=50,
            pf_coil_to_tf_coil_radial_gap=50,
            outboard_tf_coil_radial_thickness=50,
            tf_coil_poloidal_thickness=50,
        )
        test_reactor.export_stp()
        assert len(test_reactor.shapes_and_components) == 12

    def test_BallReactor_with_pf_and_tf_coils_export_physical_groups(self):
        test_reactor = paramak.BallReactor(
            inner_bore_radial_thickness=10,
            inboard_tf_leg_radial_thickness=30,
            center_column_shield_radial_thickness=60,
            divertor_radial_thickness=50,
            inner_plasma_gap_radial_thickness=30,
            plasma_radial_thickness=300,
            outer_plasma_gap_radial_thickness=30,
            firstwall_radial_thickness=30,
            blanket_radial_thickness=30,
            blanket_rear_wall_radial_thickness=30,
            elongation=2,
            triangularity=0.55,
            number_of_tf_coils=16,
            rotation_angle=180,
            pf_coil_radial_thicknesses=[50, 50, 50, 50],
            pf_coil_vertical_thicknesses=[50, 50, 50, 50],
            pf_coil_to_rear_blanket_radial_gap=50,
            pf_coil_to_tf_coil_radial_gap=50,
            outboard_tf_coil_radial_thickness=50,
            tf_coil_poloidal_thickness=50,
        )
        test_reactor.export_physical_groups()

    def test_SingleNullBallReactor_with_pf_and_tf_coils(self):
        test_reactor = paramak.SingleNullBallReactor(
            inner_bore_radial_thickness=10,
            inboard_tf_leg_radial_thickness=30,
            center_column_shield_radial_thickness=60,
            divertor_radial_thickness=50,
            inner_plasma_gap_radial_thickness=30,
            plasma_radial_thickness=300,
            outer_plasma_gap_radial_thickness=30,
            firstwall_radial_thickness=30,
            blanket_radial_thickness=30,
            blanket_rear_wall_radial_thickness=30,
            elongation=2,
            triangularity=0.55,
            number_of_tf_coils=16,
            rotation_angle=270,
            pf_coil_radial_thicknesses=[50, 50, 50, 50],
            pf_coil_vertical_thicknesses=[50, 50, 50, 50],
            pf_coil_to_rear_blanket_radial_gap=50,
            pf_coil_to_tf_coil_radial_gap=50,
            outboard_tf_coil_radial_thickness=100,
            tf_coil_poloidal_thickness=50,
            divertor_position="lower"
        )
        assert len(test_reactor.shapes_and_components) == 12

    def test_single_null_ball_reactor_divertor_lower(self):
        test_reactor = paramak.SingleNullBallReactor(
            inner_bore_radial_thickness=10,
            inboard_tf_leg_radial_thickness=30,
            center_column_shield_radial_thickness=60,
            divertor_radial_thickness=50,
            inner_plasma_gap_radial_thickness=30,
            plasma_radial_thickness=300,
            outer_plasma_gap_radial_thickness=30,
            firstwall_radial_thickness=30,
            blanket_radial_thickness=30,
            blanket_rear_wall_radial_thickness=30,
            elongation=2,
            triangularity=0.55,
            number_of_tf_coils=16,
            divertor_position="lower"
        )

        assert len(test_reactor.shapes_and_components) == 7

    def test_single_null_ball_reactor_divertor_upper(self):
        test_reactor = paramak.SingleNullBallReactor(
            inner_bore_radial_thickness=10,
            inboard_tf_leg_radial_thickness=30,
            center_column_shield_radial_thickness=60,
            divertor_radial_thickness=50,
            inner_plasma_gap_radial_thickness=30,
            plasma_radial_thickness=300,
            outer_plasma_gap_radial_thickness=30,
            firstwall_radial_thickness=30,
            blanket_radial_thickness=30,
            blanket_rear_wall_radial_thickness=30,
            elongation=2,
            triangularity=0.55,
            number_of_tf_coils=16,
            divertor_position="upper"
        )

        assert len(test_reactor.shapes_and_components) == 7
