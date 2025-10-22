import sys
import os
from entitysdk import Client, models
from entitysdk.token_manager import TokenManager
import os

'''
class TokenFromLaunchApi(TokenManager):

    def __init__(self, *, api_url, api_token, http_client):
        self._api_url = api_url
        self._api_token = api_token
        self._http_client = http_client

    def get_token(self) -> str:
        """Get the token from the task api."""
        self._http_client.get(f"{self._api_url}/{}")


class ApiClient(Client):

    def __init__(self, environment: str):

        http_client = httpx.Client()

        token_manager = TokenFromLaunchApi(
            api_url=os.environ["API_URL"],
            api_token=os.environ["API_TOKEN"],
            http_client=http_client,
        )

        super().__init__(environment=environment, token_manager=token_manager, http_client=http_client)
'''

def validate_morphology(client, entity_id) -> dict:
    morphology = client.get_entity(entity_type=models.CellMorphology, entity_id=entity_id)
    assert morphology.type == "cell_morphology"
    return {"entity_id": str(morphology.id)} 


if __name__ == "__main__":

    entity_id = sys.argv[1]

    #client = ApiClient(environment="staging")
    client = Client(environment="staging", token_manager=os.environ["ACCESS_TOKEN"])

    res = validate_morphology(client, entity_id)
    print(f"Success! {res}")
