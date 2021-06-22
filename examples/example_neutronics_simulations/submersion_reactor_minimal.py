"""This is a minimal example that obtains the particle flux in each component
for a parametric submersion reactor"""

import neutronics_material_maker as nmm
import openmc
import paramak


def make_model_and_simulate():
    """Makes a neutronics Reactor model and simulates the flux"""

    # makes the 3d geometry from input parameters
    my_reactor = paramak.SubmersionTokamak(
        inner_bore_radial_thickness=30,
        inboard_tf_leg_radial_thickness=30,
        center_column_shield_radial_thickness=30,
        divertor_radial_thickness=80,
        inner_plasma_gap_radial_thickness=50,
        plasma_radial_thickness=200,
        outer_plasma_gap_radial_thickness=50,
        firstwall_radial_thickness=30,
        blanket_rear_wall_radial_thickness=30,
        rotation_angle=180,
        support_radial_thickness=50,
        inboard_blanket_radial_thickness=30,
        outboard_blanket_radial_thickness=30,
        elongation=2.75,
        triangularity=0.5,
    )

    # this can just be set as a string as temperature is needed for this
    # material
    flibe = nmm.Material.from_library(name='FLiBe', temperature=773.15)

    source = openmc.Source()
    # sets the location of the source to x=0 y=0 z=0
    source.space = openmc.stats.Point((my_reactor.major_radius, 0, 0))
    # sets the direction to isotropic
    source.angle = openmc.stats.Isotropic()
    # sets the energy distribution to 100% 14MeV neutrons
    source.energy = openmc.stats.Discrete([14e6], [1])

    # makes the neutronics model from the geometry and material allocations
    neutronics_model = paramak.NeutronicsModel(
        geometry=my_reactor,
        source=source,
        materials={
            'inboard_tf_coils_mat': 'eurofer',
            'center_column_shield_mat': 'eurofer',
            'divertor_mat': 'eurofer',
            'firstwall_mat': 'eurofer',
            'blanket_rear_wall_mat': 'eurofer',
            'blanket_mat': flibe,
            'supports_mat': 'eurofer'},
        cell_tallies=['flux'],
        simulation_batches=5,
        simulation_particles_per_batch=1e4,
    )

    # simulate the neutronics model
    neutronics_model.simulate()
    print(neutronics_model.results)


if __name__ == "__main__":
    make_model_and_simulate()
