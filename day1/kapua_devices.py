#
# Kapua device deletion utilities
# Author: Lisa Ong, NUS/ISS
#

import argparse
import random
from pprint import pprint

 # Generated python client
import swagger_client
from swagger_client.rest import ApiException

import kapua_config
import kapua_accounts

def list_devices(api_client, account_id):
    api_instance = swagger_client.DevicesApi(api_client)
    try:
        api_response = api_instance.device_simple_query(account_id)
        pprint(api_response)

    except ApiException as e:
        print(f'Exception when calling API: {e}')

def add_devices(api_client, account_id, device_names):
    # Step 1
    # Get a DevicesApi instance from the swagger_client
    #<YOUR CODE HERE>
    api_instance = swagger_client.DevicesApi(api_client)
    try:
        for device_name in device_names:
            # Step 2
            # Create a DeviceCreator request from the swagger_client to contain device information
            # Set client_id to the device_name
            # Set display_name to the device_name
            # Set other optional properties
            #<YOUR CODE HERE>
            DeviceCreator = {
                'clientId': device_name,
                'displayName' : device_name,
                'createBy' : 'Liang Faan' 
            }

            # Step 3
            # Pass the DeviceCreator request to the DevicesApi instance’s device_create method
            # Use account_id as the scope_id
            # <YOUR CODE HERE>
            api_response = api_instance.device_create(account_id, DeviceCreator)

            print(f'Created device: {api_response.display_name}')

    except ApiException as e:
        print(f'Exception when calling API: {e}')

def delete_devices(api_client, account_id, device_names):
    api_instance = swagger_client.DevicesApi(api_client)
    try:
        for device_name in device_names:    
            api_response = api_instance.device_simple_query(account_id,
                client_id=device_name)

            if len(api_response.items) > 0:
                api_instance.device_delete(account_id, api_response.items[0].id)
                print(f'Deleted device: {device_name}')
            else:
                print(f'Device {device_name} not found, skipping')

    except ApiException as e:
        print(f'Exception when calling API: {e}')

if __name__ == '__main__':

    # test values
    account_name = 'diec1'
    user_name = 'user1'

    parser = argparse.ArgumentParser(description='Automates creation of Kapua devices')
    parser.add_argument('--add', nargs='+', type=str, help='Adds one or more devices with the given names')
    parser.add_argument('--list', nargs='*', type=str, help='Lists all devices')
    parser.add_argument('--delete', nargs='+', type=str, help='Removes one or more devices with the given names')

    args = parser.parse_args()

    try:
        account_id = kapua_accounts.get_account_id(name=account_name)
        user_id = kapua_accounts.get_user_id(account_id=account_id, name=user_name)

        # create an API key
        api_key = kapua_accounts.add_user_key(account_id, user_id)
        print(f'Generated API KEY: {api_key}')
        api_client = kapua_config.get_api_client(api_key=api_key)

        if args.add is not None:
            add_devices(api_client, account_id, args.add)
        elif args.list is not None:
            list_devices(api_client, account_id)
        elif args.delete is not None:
            delete_devices(api_client, account_id, args.delete)

    finally:
        # cleanup the API keys (note: will delete all API KEYS)
        kapua_accounts.delete_user_keys(account_id, user_id)