import os
import logging
import yaml
from yacman import load_yaml
import eido
import sys
import peppy
from peppy import __version__ as peppy_version
import argparse

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

def _load_schema(path: str) -> dict:
    """
    Load in to memory the schemas we need to validate against.

    @param: - path - path to schemas
    """
    return load_yaml(path)
        
def _is_valid_namespace(path: str, name: str) -> bool:
    """
    Check if a given path is a valid namespace directory. Function
    Will check a given path for the following criteria:
        1. Is a folder
        2. Is not a "dot" file (e.g. .git)
    """
    criteria = [
        os.path.isdir(path),
        not name.startswith(".")
    ]
    return all(criteria)

# attentive programmers will notice that this is identical
# to the function above. I am keeping them separate as in
# the future there might exist separate criteria for a
# namespace v a projects
def _is_valid_project(path: str, name: str) -> bool:
    """
    Check if a given project name is a valid project
    directory. Will check a given project for the following
    criteria:
        1. Is a folder
        2. Is not a "dot" file (e.g. .git)
    """
    criteria = [
        os.path.isdir(path),
        not name.startswith(".")
    ]
    return all(criteria)

def _extract_project_file_name(path_to_proj: str) -> str:
    """
    Take a given path to a PEP/project inside a namespace and
    return the name of the PEP configuration file. The process
    is completed in the following steps:
        1. Look for a .pep.yaml file
            if exists -> check for config_file attribute
            else step two
        2. Look for project_config.yaml
            if exists -> return path
            else step 3
        3. If no .pep.yaml file with config_file attribute exists AND
           no porject_config.yaml file exists, then return None.
    """
    try:
        with open(f"{path_to_proj}/.pep.yaml", "r") as stream:
            _pephub_yaml = yaml.safe_load(stream)

        # check for config_file attribute
        if "config_file" in _pephub_yaml: 
            return _pephub_yaml["config_file"]
        else:
            # look for regular project_config.yaml 
            if not os.path.exists(f"{path_to_proj}/project_config.yaml"):
                raise ValueError(f"Cannot find project configuration file for {path_to_proj}. \
                                   Please include a project_config.yaml or .pep.yaml file. \
                                   See https://github.com/pepkit/pephub.databio.org for more information.")
            else: return "project_config.yaml"

    # catch no .pep.yaml exists
    except FileNotFoundError:
        if not os.path.exists(f"{path_to_proj}/project_config.yaml"):
            return None
        else: return "project_config.yaml"

def vwrap(p: peppy.Project, schema):
    """
    Validation wrapper function
    This little helper function just wraps the eido validate_project function
    to catch the exceptions raised and convert them into error reports.
    @param p peppy.Project object to validate
    @param schema Eido schema to validate against
    """
    return eido.validate_project(project=p, schema=schema, exclude_case=True)



def validate_peps(path_to_peps: str, path_to_schemas: str) -> None:  
    """
    Valdiate all PEPs inside a given PEP ata repository using eido

    @param: path_to_peps - Path to the PEP location
    @param: path_to_schemas = Path to the location of the schema file.

    """
    # fetch schemas to test
    schemas_to_test = _load_schema(path_to_schemas)
    
    # traverse directory
    for name in os.listdir(path_to_peps):
        # build a path to the namespace
        path_to_namespace = f"{path_to_peps}/{name}"
        logging.info(f"Validating namespace: {path_to_namespace}")

        if _is_valid_namespace(path_to_namespace, name):
            # traverse projects
            for proj in os.listdir(path_to_namespace):
                # build path to project
                path_to_proj = f"{path_to_namespace}/{proj}"
                logging.info(f"Validating projects in namespace: {path_to_namespace}")

                if _is_valid_project(path_to_proj, proj):
                    # extract config file
                    proj_config = f"{path_to_proj}/{_extract_project_file_name(path_to_proj)}"
                    proj = peppy.Project(proj_config)

                    for _, schema_data in schemas_to_test.items():
                        try:
                            vwrap(proj, schema_data["schema"])
                        except Exception as e:
                            logging.error(f"Error validating project {path_to_proj} against schema {schema_data['schema']}: {e}")
                            sys.exit(1)

                else:
                    raise ValueError(f"Invalid project found in PEP data directory: {path_to_proj}.")
        else:
            raise ValueError(f"Invalid namespace found in PEP data directory: {path_to_namespace}")

def build_argparser() -> argparse.ArgumentParser:
    """Build the argument parser for the script"""
    parser = argparse.ArgumentParser(description='Validate a PEP data directory')

    parser.add_argument('-s', '--schema', help='Path to schemas file (YAML).')
    parser.add_argument('-p', '--peps', help='Path to PEP data directory.')

    return parser

if __name__ == '__main__':
    parser = build_argparser()
    args = parser.parse_args()
    validate_peps(
        args.peps,
        args.schema
    )