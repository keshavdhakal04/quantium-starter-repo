from dash.testing.application_runners import import_app

def test_header_present(dash_duo):
    """Verify that the header is present in the app."""
    app = import_app("dashApp")
    dash_duo.start_server(app)
    
    # Wait for the H1 and check its content
    header = dash_duo.wait_for_element("h1", timeout=10)
    assert header.text == "Pink Morsel Sales Visualiser"

def test_visualisation_present(dash_duo):
    """Verify that the sales graph is present."""
    app = import_app("dashApp")
    dash_duo.start_server(app)
    
    # We wait for the graph container. If it's found, the test passes.
    # This avoids the is_displayed() race condition.
    graph = dash_duo.wait_for_element("#sales-graph", timeout=10)
    assert graph is not None

def test_region_picker_present(dash_duo):
    """Verify that the region picker is present."""
    app = import_app("dashApp")
    dash_duo.start_server(app)
    
    # Wait for the radio items/picker by ID
    picker = dash_duo.wait_for_element("#region-picker", timeout=10)
    assert picker is not None