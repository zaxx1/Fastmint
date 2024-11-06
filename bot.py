import requests
import json
import os
import urllib.parse
from colorama import *
from datetime import datetime, timedelta
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class Fastmint:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'api.chaingn.org',
            'Origin': 'https://chaingn.org',
            'Pragma': 'no-cache',
            'Referer': 'https://chaingn.org/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Fastmint - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    def load_data(self, query: str):
        query_params = urllib.parse.parse_qs(query)
        user_data_json = query_params.get('user', [None])[0]

        if user_data_json:
            user_data = json.loads(urllib.parse.unquote(user_data_json))
            username = user_data.get('username', 'unknown')
            user_id = user_data.get('id')
            return user_id, username
        else:
            raise ValueError("User data not found in query.")

    def login(self, query: str):
        url = 'https://api.chaingn.org/auth/login'
        data = json.dumps({'OAuth': query})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result['sessionToken']
        else:
            return None
    
    def user(self, token: str):
        url = 'https://api.chaingn.org/user'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def wallets(self, token: str):
        url = 'https://api.chaingn.org/wallets'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def daily_visits(self, token: str):
        url = 'https://api.chaingn.org/user/daily_visits'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def refferal_info(self, token: str):
        url = 'https://api.chaingn.org/referral/info'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def claim_refferal(self, token: str):
        url = 'https://api.chaingn.org/referral/claim'
        data = {}
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, json=data)
        if response.status_code == 200:
            return True
        else:
            return False
        
    def start_farm(self, token: str, id: str):
        url = 'https://api.chaingn.org/wallet/farm'
        data = json.dumps({'id': id})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def claim_farm(self, token: str, id: str):
        url = 'https://api.chaingn.org/wallet/claim'
        data = json.dumps({'id': id})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def upgarde_info(self, token: str):
        url = 'https://api.chaingn.org/wallets/info'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def farming_upgarde(self, token: str, id: str):
        url = 'https://api.chaingn.org/wallet/upgrade'
        data = json.dumps({'id': id})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None

    def sub_tasks(self, token: str):
        url = 'https://api.chaingn.org/sub_tasks'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result['tasks']
        else:
            return None

    def check_tasks(self, token: str, recource_id: str):
        url = 'https://api.chaingn.org/sub_task'
        data = json.dumps({'recourceId': recource_id})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None

    def claim_tasks(self, token: str, task_id: str):
        url = 'https://api.chaingn.org/sub_task/claim'
        data = json.dumps({'id': task_id})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.put(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def fmc_wallets(self, token: str):
        url = 'https://api.chaingn.org/wallets/external'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def create_mnemonic(self, token: str):
        url = 'https://api.chaingn.org/wallet/external'
        data = {}
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, json=data)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def save_mnemonic(self, user_id, username, address, mnemonic):
        with open('mnemonic.txt', 'a') as file:
            file.write(
                f"Telegram ID: {user_id} - Username: {username} - address: {address} - mnemonic: {mnemonic}\n"
            )
        
    def create_wallet(self, token: str, mnemonic: str):
        url = 'https://api.chaingn.org/wallet/external'
        data = json.dumps({'mnemonic':mnemonic})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def question(self):
        while True:
            choice = input("1. Run Auto Create Wallet\n2. Only Run Bot\nChoose [1 or 2] -> ").strip()
            if choice == "1":
                create_fmc = True
                farming_upgrade = False
                break
            elif choice == "2":
                create_fmc = False
                while True:
                    farming_upgrade = input("Upgrade Farming Account Level? [y/n] -> ").strip().lower()
                    if farming_upgrade in ["y", "n"]:
                        farming_upgrade = farming_upgrade == "y"
                        break
                    else:
                        print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose '1' or '2'.{Style.RESET_ALL}")
        
        return create_fmc, farming_upgrade

    def process_query(self, query: str, create_fmc: bool, farming_upgrade: bool):
        user_id, username = self.load_data(query)
        token = self.login(query)
        if not token:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Token Is None {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return

        if create_fmc:
            fmc_wallet = self.fmc_wallets(token)
            if not fmc_wallet:
                self.log(f"{Fore.MAGENTA+Style.BRIGHT}ID: {Fore.WHITE+Style.BRIGHT}{user_id}{Style.RESET_ALL}")
                time.sleep(1)
                self.log(f"{Fore.MAGENTA+Style.BRIGHT}Username: {Fore.WHITE+Style.BRIGHT}{username}{Style.RESET_ALL}")
                time.sleep(1)
                self.log(f"{Fore.MAGENTA+Style.BRIGHT}FMC Wallet: {Fore.RED+Style.BRIGHT}FMC Wallet has not been created yet.{Style.RESET_ALL}")
                time.sleep(1)

                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}FMC Wallet: {Fore.YELLOW+Style.BRIGHT}Creating Mnemonic.....{Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
                time.sleep(2)

                create_mnemonic = self.create_mnemonic(token)
                if create_mnemonic:
                    mnemonic = create_mnemonic['mnemonic']
                    self.log(f"{Fore.MAGENTA+Style.BRIGHT}Wallet Status: {Fore.GREEN+Style.BRIGHT}Mnemonic Created Successfully{Style.RESET_ALL}")
                    time.sleep(1)

                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}Wallet Status: {Fore.YELLOW+Style.BRIGHT}Creating Address.....{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                    create_wallet = self.create_wallet(token, mnemonic)
                    if create_wallet:
                        self.log(f"{Fore.MAGENTA+Style.BRIGHT}Wallet Status: {Fore.GREEN+Style.BRIGHT}Address Created Successfully{Style.RESET_ALL}")
                        time.sleep(1)

                        print(
                            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}Wallet Status: {Fore.YELLOW+Style.BRIGHT}Saving Address n Mnemonic.....{Style.RESET_ALL}",
                            end="\r",
                            flush=True
                        )
                        time.sleep(2)

                        fmc_wallet = self.fmc_wallets(token)
                        for wallet in fmc_wallet:

                            address = wallet['address']
                            self.save_mnemonic(user_id, username, address, mnemonic)
                            self.log(f"{Fore.MAGENTA+Style.BRIGHT}Wallet Status: {Fore.GREEN+Style.BRIGHT}Address n Mnemonic Saved Successfully{Style.RESET_ALL}")

                    else:
                        self.log(f"{Fore.MAGENTA+Style.BRIGHT}Wallet Status: {Fore.RED+Style.BRIGHT}Failed to Create Address{Style.RESET_ALL}")
                        time.sleep(1)

                else:
                    self.log(f"{Fore.MAGENTA+Style.BRIGHT}Wallet Status: {Fore.GREEN+Style.BRIGHT}Failed to Create Mnemonic{Style.RESET_ALL}")
                    time.sleep(1)

            else:
                for fmc in fmc_wallet:
                    if fmc:
                        self.log(f"{Fore.MAGENTA+Style.BRIGHT}ID: {Fore.WHITE+Style.BRIGHT}{user_id}{Style.RESET_ALL}")
                        time.sleep(1)
                        self.log(f"{Fore.MAGENTA+Style.BRIGHT}Username: {Fore.WHITE+Style.BRIGHT}{username}{Style.RESET_ALL}")
                        time.sleep(1)
                        self.log(f"{Fore.MAGENTA+Style.BRIGHT}FMC Wallet: {Fore.GREEN+Style.BRIGHT}Already Created{Style.RESET_ALL}")
                        time.sleep(1)
                        self.log(f"{Fore.MAGENTA+Style.BRIGHT}Address: {Fore.WHITE+Style.BRIGHT}{fmc['address']}{Style.RESET_ALL}")
                        time.sleep(1)
                        self.log(f"{Fore.MAGENTA+Style.BRIGHT}Balance: {Fore.WHITE+Style.BRIGHT}{fmc['balance']}{Style.RESET_ALL}")
                        time.sleep(1)

        else:
            user = self.user(token)
            if not user:
                return

            wallets = self.wallets(token)
            if not wallets:
                return

            for wallet in wallets:
                if wallet:
                    id = wallet['id']
                    current_level = wallet['level']

                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {user['firstName']} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {wallet['balance']} MT {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Farming{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} Level {current_level} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                    time.sleep(2)

                    visits = self.daily_visits(token)
                    if visits and 'visits' in visits:
                        visit = [visit for visit in visits['visits'] if visit['isCompleted']]
                        
                        if visit:
                            last_visit = max(visit, key=lambda x: x['day'])
                            if last_visit['isCompleted'] and last_visit:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Rewards{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {last_visit['rewardMnt']} MT {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Streak{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {last_visit['day']} Day {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )

                    refferal = self.refferal_info(token)
                    if refferal and refferal['membersCount'] != 0:
                        reward = refferal['rewardMnt']
                        if reward > 0:
                            claim = self.claim_refferal(token)
                            if claim:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}" 
                                    f"{Fore.WHITE+Style.BRIGHT} {reward} MT {Style.RESET_ALL}" 
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} Isn't Reward to Claim {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Count Is None {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                        )
            
                    farm_date = wallet['startFarmDate']
                    if farm_date is None:
                        start = self.start_farm(token, id)
                        if start:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                            )

                    if farm_date:
                        farm_date_utc = datetime.fromisoformat(farm_date.replace('Z', '+00:00'))
                        farm_date_wib = farm_date_utc.astimezone(wib)
                        claim_time = (farm_date_wib + timedelta(hours=6)).strftime('%x %X %Z')

                        claim = self.claim_farm(token, id)
                        if claim:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}" 
                                f"{Fore.WHITE+Style.BRIGHT} {wallet['info']['reward']} MT {Style.RESET_ALL}" 
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                            )

                            start = self.start_farm(token, id)
                            if start:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} Not Time to Claim {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}" 
                                f"{Fore.WHITE+Style.BRIGHT} {claim_time} {Style.RESET_ALL}" 
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                            )

                    if farming_upgrade:
                        farming_account = self.upgarde_info(token)
                        if farming_account:
                            next_level = current_level + 1

                            if next_level <= len(farming_account):
                                item = farming_account[next_level - 1]

                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} Upgrade to Level {next_level} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Profit{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {item['reward']} MT/Claim {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Cost{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {item['cost']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                time.sleep(1)

                                if wallet['balance'] >= item['cost']:
                                    upgrade_farm = self.farming_upgarde(token, id)
                                    if upgrade_farm:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                            f"{Fore.GREEN+Style.BRIGHT} Is Upgraded {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                            f"{Fore.RED+Style.BRIGHT} Isn't Upgraded {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT} Isn't Upgraded {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} Balance Not Enough {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT} Upgarde Is Reached Max Level {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Upgrade Is Skipped {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )

                    MAX_CHECKS = 1
                    tasks = self.sub_tasks(token)
                    while tasks:
                        for task in tasks:
                            recource_id = task.get('recourceId')
                            task_id = task.get('id')
                            title = task.get('title', 'Unknown')
                            done = task.get('done', False)
                            claimed = task.get('claimed', False)

                            checks_done = task.get('checks_done', 0)

                            if not claimed:
                                if not done:
                                    if checks_done < MAX_CHECKS:
                                        check = self.check_tasks(token, recource_id)
                                        task['checks_done'] = checks_done + 1

                                        if check:
                                            self.log(
                                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                                f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                                f"{Fore.GREEN+Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                            )
                                            
                                            tasks = self.sub_tasks(token)
                                            break
                                        else:
                                            self.log(
                                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                                f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                                f"{Fore.RED+Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                            )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                            f"{Fore.YELLOW+Style.BRIGHT}Skipped after {MAX_CHECKS} attempts{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )

                                if task.get('done', False) and task_id is not None:
                                    claim = self.claim_tasks(token, task_id)
                                    if claim:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                            f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {task.get('reward', 0)} MT {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                            f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )
                        else:
                            break


    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            create_fmc, farming_upgrade = self.question()

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query, create_fmc, farming_upgrade)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        time.sleep(3)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Fastmint - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    fastmint = Fastmint()
    fastmint.main()