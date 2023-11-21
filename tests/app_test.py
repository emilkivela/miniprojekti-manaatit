def test_opening_ref_creation_page(client):
    response = client.get("/new")
    assert b"Author" in response.data
