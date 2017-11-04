import importlib.util


def check_module(module_name):
    """
    Checks if module can be imported without actually
    importing it
    """
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print('Module: {} not found'.format(module_name))
        return None
    else:
        print('Module: {} can be imported'.format(module_name))
        return module_spec


def import_module_from_spec(module_spec):
    """
    import the module via the passed in module specification
    Returns the newly imported module
    """
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


def import_source(module_name):
    module_file_path = module_name.__file__
    module_name = module_name.__name__

    module_spec = importlib.util.spec_from_file_location(
        module_name, module_file_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    print(dir(module))

    msg = 'The {module_name} module has the following methods:' \
          ' {methods}'
    print(msg.format(module_name=module_name,
                     methods=dir(module)))


if __name__ == '__main__':
    module_spec = check_module('fake_module')
    module_spec = check_module('collections')
    if module_spec:
        module = import_module_from_spec(module_spec)
        print(dir(module))

    import logging
    import_source(logging)
