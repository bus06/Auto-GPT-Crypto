"""This is a plugin to use Auto-GPT with Crypto."""
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict
from auto_gpt_plugin_template import AutoGPTPluginTemplate

# Crypto
import os
from web3 import Web3
from eth_abi.packed import encode_packed
from eth_abi.exceptions import DecodingError
import requests
import json
# Connect to the Ethereum network using Infura API endpoint

PromptGenerator = TypeVar("PromptGenerator")

infura_api = os.getenv('INFURA_API_KEY')
my_address = os.getenv('ETH_WALLET_ADDRESS')
private_key = os.getenv('ETH_WALLET_PRIVATE_KEY')
etherscan_api = os.getenv('ETHERSCAN_API_KEY')
network = os.getenv('ETH_NETWORK')


class Message(TypedDict):
    role: str
    content: str


class AutoGPTCryptoPlugin(AutoGPTPluginTemplate):
    """
    This is a plugin to use Auto-GPT with Crypto.
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-GPT-Crypto"
        self._version = "0.1.0"
        self._description = "This is a plugin for Auto-GPT-Crypto."

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        prompt.add_command(
            "Get My ETH Balance",
            "get_my_eth_balance",
            {},
            self.get_my_eth_balance
        ),
        prompt.add_command(
            "Get ETH Balance",
            "get_eth_balance",
            {
                "address": "<address>"
            },
            self.get_eth_balance
        ),
        # prompt.add_command(
        #     "Send ETH",
        #     "send_eth",
        #     {
        #         "recipient_address": "<recipient_address>",
        #         "amount": "<amount>"
        #     },
        #     self.send_eth
        # ),
        # prompt.add_command(
        #     "Purchase ERC-20 Token",
        #     "purchase_tokens",
        #     {
        #         "token_address": "<token_address>",
        #         "amount_in_eth": "<amount_in_eth>"
        #     },
        #     self.purchase_tokens
        # ),
        # prompt.add_command(
        #     "Get Token Balances",
        #     "get_token_balances",
        #     {
        #         "wallet_address": "<wallet_address>"
        #     },
        #     self.get_token_balances
        # ),
        # prompt.add_command(
        #     "Stake Tokens",
        #     "stake_tokens",
        #     {
        #         "token_address": "<token_address>",
        #         "staking_contract_address": "<staking_contract_address>",
        #         "amount": "<amount>"
        #     },
        #     self.stake_tokens
        # ),
        # prompt.add_command(
        #     "Send Tokens",
        #     "send_tokens",
        #     {
        #         "token_address": "<token_address>",
        #         "recipient_address": "<recipient_address>",
        #         "amount": "<amount>"
        #     },
        #     self.send_tokens
        # )
        return prompt

    def can_handle_post_prompt(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_prompt method.
        Returns:
            bool: True if the plugin can handle the post_prompt method."""
        return True

    def can_handle_on_response(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_response method.
        Returns:
            bool: True if the plugin can handle the on_response method."""
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        """This method is called when a response is received from the model."""
        pass

    def can_handle_on_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_planning method.
        Returns:
            bool: True if the plugin can handle the on_planning method."""
        return False

    def on_planning(
        self, prompt: PromptGenerator, messages: List[Message]
    ) -> Optional[str]:
        """This method is called before the planning chat completion is done.
        Args:
            prompt (PromptGenerator): The prompt generator.
            messages (List[str]): The list of messages.
        """
        pass

    def can_handle_post_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_planning method.
        Returns:
            bool: True if the plugin can handle the post_planning method."""
        return False

    def post_planning(self, response: str) -> str:
        """This method is called after the planning chat completion is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_instruction method.
        Returns:
            bool: True if the plugin can handle the pre_instruction method."""
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        """This method is called before the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            List[Message]: The resulting list of messages.
        """
        pass

    def can_handle_on_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_instruction method.
        Returns:
            bool: True if the plugin can handle the on_instruction method."""
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        """This method is called when the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            Optional[str]: The resulting message.
        """
        pass

    def can_handle_post_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_instruction method.
        Returns:
            bool: True if the plugin can handle the post_instruction method."""
        return False

    def post_instruction(self, response: str) -> str:
        """This method is called after the instruction chat is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_command method.
        Returns:
            bool: True if the plugin can handle the pre_command method."""
        return False

    def pre_command(
        self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """This method is called before the command is executed.
        Args:
            command_name (str): The command name.
            arguments (Dict[str, Any]): The arguments.
        Returns:
            Tuple[str, Dict[str, Any]]: The command name and the arguments.
        """
        pass

    def can_handle_post_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_command method.
        Returns:
            bool: True if the plugin can handle the post_command method."""
        return False

    def post_command(self, command_name: str, response: str) -> str:
        """This method is called after the command is executed.
        Args:
            command_name (str): The command name.
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_chat_completion(
        self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int
    ) -> bool:
        """This method is called to check that the plugin can
          handle the chat_completion method.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
          Returns:
              bool: True if the plugin can handle the chat_completion method."""
        return False

    def handle_chat_completion(
        self, messages: List[Message], model: str, temperature: float, max_tokens: int
    ) -> str:
        """This method is called when the chat completion is done.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
        Returns:
            str: The resulting response.
        """
        pass

    # Crypto

    def get_eth_balance(address: str) -> float:

        endpoint = f"https://{network}.infura.io/v3/{infura_api}"
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBalance",
            "params": [address, "latest"],
            "id": 1
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(endpoint, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            balance_wei = int(response.json()["result"], 16)
            balance_eth = balance_wei / 10 ** 18
            return f'{balance_eth} ETH'
        else:
            raise Exception(
                f"Failed to get ETH balance for {address}; status code {response.status_code}")

    def get_my_eth_balance(self) -> float:
        endpoint = f"https://{network}.infura.io/v3/{infura_api}"
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBalance",
            "params": [my_address, "latest"],
            "id": 1
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(endpoint, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            balance_wei = int(response.json()["result"], 16)
            balance_eth = balance_wei / 10 ** 18
            return f'{balance_eth} ETH'
        else:
            raise Exception(
                f"Failed to get ETH balance for {my_address}; status code {response.status_code}")

    # def send_eth(self, recipient_address: str, amount: float) -> str:
    #     try:
    #         # Convert amount to Wei
    #         amount_wei = w3.toWei(amount, 'ether')

    #         # Build transaction
    #         nonce = w3.eth.getTransactionCount(my_address)
    #         tx = {
    #             'nonce': nonce,
    #             'to': recipient_address,
    #             'value': amount_wei,
    #             'gas': 21000,
    #             'gasPrice': w3.toWei('50', 'gwei')
    #         }

    #         # Sign transaction
    #         signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)

    #         # Send transaction
    #         tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    #         return tx_hash.hex()

    #     except Exception as e:
    #         return f"An error occurred: {e}"

    # def purchase_tokens(token_address: str, amount_eth: float) -> str:
    #     # Set the Etherscan API key and endpoint
    #     api_endpoint = f'https://api.etherscan.io/api?module=contract&action=getabi&address={token_address}&apikey={etherscan_api}'

    #     # Send the API request to get the contract ABI
    #     try:
    #         response = requests.get(api_endpoint)
    #         response_json = response.json()
    #         if response_json['status'] != '1':
    #             return f"API error: {response_json['message']}"
    #         contract_abi = response_json['result']
    #     except Exception as e:
    #         return f"API request failed: {e}"

    #     # Convert amount to token units
    #     try:
    #         contract = w3.eth.contract(
    #             address=token_address, abi=contract_abi)
    #         token_decimals = contract.functions.decimals().call()
    #         amount_units = int(amount_eth * 10 ** token_decimals)
    #     except Exception as e:
    #         return f"Failed to convert amount to token units: {e}"

    #     # Build transaction data
    #     try:
    #         transfer_data = encode_abi(
    #             '(address,uint256)', (my_address, amount_units))
    #         tx_data = contract.functions.transfer(my_address, amount_units).buildTransaction({
    #             'nonce': w3.eth.getTransactionCount(w3.eth.accounts[0]),
    #             'gas': 200000,
    #             'gasPrice': w3.toWei('50', 'gwei'),
    #             'data': transfer_data
    #         })
    #     except Exception as e:
    #         return f"Failed to build transaction data: {e}"

    #     # Sign transaction
    #     try:
    #         signed_tx = w3.eth.account.sign_transaction(
    #             tx_data, private_key=private_key)
    #     except Exception as e:
    #         return f"Failed to sign transaction: {e}"

    #     # Send transaction
    #     try:
    #         tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    #     except Exception as e:
    #         return f"Failed to send transaction: {e}"

    #     # Get the token symbol
    #     try:
    #         token_symbol = contract.functions.symbol().call()
    #     except Exception as e:
    #         return f"Failed to get token symbol: {e}"

    #     return f"{amount_eth} ETH converted to {amount_units} {token_symbol} tokens and sent to {recipient_address}; transaction hash: {tx_hash.hex()}"

    # def get_token_balances(wallet_address: str) -> dict:
    #     # Set the Etherscan API key and endpoint
    #     api_endpoint = f'https://api.etherscan.io/api?module=account&action=tokentx&address={wallet_address}&startblock=0&endblock=999999999&sort=asc&apikey={etherscan_api}'

    #     # Send the API request
    #     try:
    #         response = requests.get(api_endpoint)
    #         response_json = response.json()
    #         if response_json['status'] != '1':
    #             return f"API error: {response_json['message']}"
    #     except Exception as e:
    #         return f"API request failed: {e}"

    #     # Parse the API response
    #     token_balances = {}
    #     for transfer in response_json['result']:
    #         token_address = transfer['contractAddress']
    #         token_symbol = transfer['tokenSymbol']
    #         token_decimals = int(transfer['tokenDecimal'])
    #         token_value = float(transfer['value']) / 10 ** token_decimals

    #         if token_address not in token_balances:
    #             token_balances[token_address] = {'symbol': token_symbol, 'balance': 0}

    #         if transfer['from'] == wallet_address:
    #             token_balances[token_address]['balance'] -= token_value
    #         elif transfer['to'] == wallet_address:
    #             token_balances[token_address]['balance'] += token_value

    #     # Remove tokens with zero balances
    #     token_balances = {k: v for k, v in token_balances.items() if v['balance'] != 0}

    #     return token_balances

    # def send_tokens(token_address: str, recipient_address: str, amount: float) -> str:
    #     api_endpoint = f'https://api.etherscan.io/api?module=contract&action=getabi&address={token_address}&apikey={etherscan_api}'

    #     # Send the API request to get the contract ABI
    #     try:
    #         response = requests.get(api_endpoint)
    #         response_json = response.json()
    #         if response_json['status'] != '1':
    #             return f"API error: {response_json['message']}"
    #         contract_abi = response_json['result']
    #     except Exception as e:
    #         return f"API request failed: {e}"

    #     # Convert amount to token units
    #     try:
    #         contract = w3.eth.contract(
    #             address=token_address, abi=contract_abi)
    #         token_decimals = contract.functions.decimals().call()
    #         amount_units = int(amount * 10 ** token_decimals)
    #     except Exception as e:
    #         return f"Failed to convert amount to token units: {e}"

    #     # Build transaction data
    #     try:
    #         transfer_data = encode_abi(
    #             '(address,uint256)', (recipient_address, amount_units))
    #         tx_data = contract.functions.transfer(recipient_address, amount_units).buildTransaction({
    #             'nonce': w3.eth.getTransactionCount(my_address),
    #             'gas': 200000,
    #             'gasPrice': w3.toWei('50', 'gwei'),
    #             'data': transfer_data
    #         })
    #     except Exception as e:
    #         return f"Failed to build transaction data: {e}"

    #     # Sign transaction
    #     try:
    #         signed_tx = w3.eth.account.sign_transaction(
    #             tx_data, private_key=private_key)
    #     except Exception as e:
    #         return f"Failed to sign transaction: {e}"

    #     # Send transaction
    #     try:
    #         tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    #     except Exception as e:
    #         return f"Failed to send transaction: {e}"

    #     # Get the token symbol
    #     try:
    #         token_symbol = contract.functions.symbol().call()
    #     except Exception as e:
    #         return f"Failed to get token symbol: {e}"

    #     return f"{amount} {token_symbol} tokens sent from {my_address} to {recipient_address}; transaction hash: {tx_hash.hex()}"

    # def stake_tokens(token_address: str, staking_contract_address: str, sender_address: str, amount: float) -> str:
    #     # Connect to Ethereum network
    #     w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

    #     # Set the Etherscan API key and endpoint
    #     api_key = 'YOUR_ETHERSCAN_API_KEY'
    #     api_endpoint = f'https://api.etherscan.io/api?module=contract&action=getabi&address={token_address}&apikey={api_key}'

    #     # Send the API request to get the contract ABI
    #     try:
    #         response = requests.get(api_endpoint)
    #         response_json = response.json()
    #         if response_json['status'] != '1':
    #             return f"API error: {response_json['message']}"
    #         contract_abi = response_json['result']
    #     except Exception as e:
    #         return f"API request failed: {e}"

    #     # Convert amount to token units
    #     try:
    #         contract = w3.eth.contract(
    #             address=token_address, abi=contract_abi)
    #         token_decimals = contract.functions.decimals().call()
    #         amount_units = int(amount * 10 ** token_decimals)
    #     except Exception as e:
    #         return f"Failed to convert amount to token units: {e}"

    #     # Build transaction data
    #     try:
    #         approve_data = encode_packed(['address', 'uint256'], [
    #                                     staking_contract_address, amount_units])
    #         contract.functions.approve(staking_contract_address, amount_units).buildTransaction({
    #             'from': sender_address,
    #             'nonce': w3.eth.getTransactionCount(sender_address),
    #             'gas': 200000,
    #             'gasPrice': w3.toWei('50', 'gwei'),
    #             'data': approve_data.hex()
    #         })
    #         stake_data = encode_packed(['uint256'], [amount_units])
    #         staking_contract = w3.eth.contract(
    #             address=staking_contract_address, abi=staking_contract_abi)
    #         tx_data = staking_contract.functions.stake(amount_units).buildTransaction({
    #             'from': sender_address,
    #             'nonce': w3.eth.getTransactionCount(sender_address),
    #             'gas': 200000,
    #             'gasPrice': w3.toWei('50', 'gwei'),
    #             'data': stake_data.hex()
    #         })
    #     except Exception as e:
    #         return f"Failed to build transaction data: {e}"

    #     # Sign transaction
    #     try:
    #         signed_tx = w3.eth.account.sign_transaction(
    #             tx_data, private_key=private_key)
    #     except Exception as e:
    #         return f"Failed to sign transaction: {e}"

    #     # Send transaction
    #     try:
    #         tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    #     except Exception as e:
    #         return f"Failed to send transaction: {e}"

    #     # Get the token symbol
    #     try:
    #         token_symbol = contract.functions.symbol().call()
    #     except Exception as e:
    #         return f"Failed to get token symbol: {e}"

    #     return f"{amount} {token_symbol} tokens staked in contract {staking_contract_address}; transaction hash: {tx_hash}"
