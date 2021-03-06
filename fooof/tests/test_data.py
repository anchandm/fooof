"""Tests for the FOOOF data objects."""

from fooof.core.info import get_obj_desc

from fooof.data import *

###################################################################################################
###################################################################################################

def test_fooof_settings():

    settings = FOOOFSettings([], None, None, None, None)
    assert settings

    # Check that the object has the correct fields, given the object description
    settings_fields = get_obj_desc()['settings']
    for field in settings_fields:
        getattr(settings, field)
    assert True

def test_fooof_results():

    results = FOOOFResults([], [], None, None, [])
    assert results

    # Check that the object has the correct fields, given the object description
    results_fields = get_obj_desc()['results']
    for field in results_fields:
        getattr(results, field.strip('_'))
    assert True

def test_syn_params():

    syn_params = SynParams([1, 1], [10, 1, 1], 0.05)
    assert syn_params

    # Check that the object has the correct fields
    for field in ['aperiodic_params', 'gaussian_params', 'nlv']:
        getattr(syn_params, field)
    assert True
