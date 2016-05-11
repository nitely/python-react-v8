# -*- coding: utf-8 -*-

# Build examples without installing
# python-react-v8 or messing with sys.path


if __name__ == '__main__':
    import react
    react.set_up()

    from examples.simple import build
    from examples.flux import build as build_flux

    build.do_build()
    build_flux.do_build()
