"""
Runs a pre-check of a staging area to identify issues that might cause the
snapshot or indexing processes to fail.
"""
import argparse
import sys
from hca.staging_area_validator import StagingAreaValidator


def _parse_args(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--staging-area', '-s',
                        required=True,
                        help='The Google Cloud Storage URL of the staging area. '
                             'Syntax is gs://<bucket>[/<path>].')
    parser.add_argument('--ignore-dangling-inputs', '-I',
                        action='store_true',
                        default=False,
                        help='Ignore errors caused by metadata files not found '
                             'in the staging area for input-only entities.')
    parser.add_argument('--no-json-validation', '-J',
                        action='store_false',
                        default=True,
                        dest='validate_json',
                        help='Do not validate JSON documents against their schema.')
    return parser.parse_args(argv)


if __name__ == '__main__':
    args = _parse_args(sys.argv[1:])
    adapter = StagingAreaValidator(
        staging_area=args.staging_area,
        ignore_dangling_inputs=args.ignore_dangling_inputs,
        validate_json=args.validate_json
    )
    sys.exit(adapter.main())
