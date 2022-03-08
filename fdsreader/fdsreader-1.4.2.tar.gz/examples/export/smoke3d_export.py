import os
import fdsreader as fds
import fdsreader.export


def main():
    base_path = "C:\\Users\\janv1\\Documents\\Unreal Projects\\VRSmokeVis"
    case = "Apartment"
    sim = fds.Simulation(os.path.join(base_path, "fds_data", case))

    for smoke in sim.smoke_3d:
        fds.export.export_smoke_raw(smoke, os.path.join(base_path, "fds_post", case, "smoke", smoke.quantity.name.replace(' ', '_').lower()), 'F')


if __name__ == "__main__":
    main()
