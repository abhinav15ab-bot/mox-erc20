from script.deploy import deploy,INITIAL_SUPPLY
import boa

RANDOM_USER = boa.env.generate_address("random_user")
def test_token_supply():
    snek_token = deploy()
    assert snek_token.totalSupply() == INITIAL_SUPPLY

