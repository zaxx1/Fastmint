import aiohttp
import asyncio
import json
import os
from colorama import *
from datetime import datetime, timedelta
import pytz

wib = pytz.timezone('Asia/Jakarta')

class Fastmint:
    def __init__(self) -> None:
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
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Fastmint App - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    async def login(self, query: str, retries=3):
        url = 'https://api.chaingn.org/auth/login'
        data = json.dumps({'OAuth': query})
        headers = {
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        result = await response.json()
                        if result and result['sessionToken']:
                            return result['sessionToken']
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
    
    async def user(self, token: str, retries=3):
        url = 'https://api.chaingn.org/user'
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def wallets(self, token: str, retries=3):
        url = 'https://api.chaingn.org/wallets'
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def daily_visits(self, token: str, retries=3):
        url = 'https://api.chaingn.org/user/daily_visits'
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def refferal_info(self, token: str, retries=3):
        url = 'https://api.chaingn.org/referral/info'
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def claim_refferal(self, token: str, retries=3):
        url = 'https://api.chaingn.org/referral/claim'
        data = {}
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, json=data) as response:
                        response.raise_for_status()
                        return True
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def start_farm(self, token: str, id: str, retries=3):
        url = 'https://api.chaingn.org/wallet/farm'
        data = json.dumps({'id': id})
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def claim_farm(self, token: str, id: str, retries=3):
        url = 'https://api.chaingn.org/wallet/claim'
        data = json.dumps({'id': id})
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def upgarde_info(self, token: str, retries=3):
        url = 'https://api.chaingn.org/wallets/info'
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def farming_upgarde(self, token: str, id: str, retries=3):
        url = 'https://api.chaingn.org/wallet/upgrade'
        data = json.dumps({'id': id})
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None

    async def sub_tasks(self, token: str, retries=3):
        url = 'https://api.chaingn.org/sub_tasks'
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None

    async def check_tasks(self, token: str, recource_id: str, retries=3):
        url = 'https://api.chaingn.org/sub_task'
        data = json.dumps({'recourceId':recource_id})
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        result = await response.json()
                        if response.status == 200:
                            return result
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None

    async def claim_tasks(self, token: str, task_id: int, retries=3):
        url = 'https://api.chaingn.org/sub_task/claim'
        data = json.dumps({'id':task_id})
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.put(url, headers=headers, data=data) as response:
                        result = await response.json()
                        if response.status == 200:
                            return result
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    def question(self):
        while True:
            farming_upgrade = input("Upgrade Farming Account Level? [y/n] -> ").strip().lower()
            if farming_upgrade in ["y", "n"]:
                farming_upgrade = farming_upgrade == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")
        
        return farming_upgrade

    async def process_query(self, query: str, farming_upgrade: bool):
        token = await self.login(query)
        if not token:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Token Is None {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        user = await self.user(token)
        if not user:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} User Data Is None {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        if user:
            wallets = await self.wallets(token)
            if not wallets:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Wallet Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                return
        
            if wallets:
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

                        visits = await self.daily_visits(token)
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

                        refferal = await self.refferal_info(token)
                        if refferal and refferal['membersCount'] != 0:
                            reward = refferal['rewardMnt']
                            if reward > 0:
                                claim = await self.claim_refferal(token)
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
                                    f"{Fore.YELLOW+Style.BRIGHT} Not Available Reward {Style.RESET_ALL}"
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
                            start = await self.start_farm(token, id)
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

                            farm_date = wallet['startFarmDate']

                        if farm_date:
                            now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
                            claim_utc = datetime.strptime(farm_date, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.utc) + timedelta(hours=6)
                            claim_wib = claim_utc.astimezone(wib).strftime('%x %X %Z')

                            if now_utc >= claim_utc:
                                claim = await self.claim_farm(token, id)
                                if claim and claim['id']:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}" 
                                        f"{Fore.WHITE+Style.BRIGHT} {wallet['info']['reward']} MT {Style.RESET_ALL}" 
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                                    )

                                    start = await self.start_farm(token, id)
                                    if start and start['id']:
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
                                        f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                                    )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT} Not Time to Claim {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}" 
                                    f"{Fore.WHITE+Style.BRIGHT} {claim_wib} {Style.RESET_ALL}" 
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                                )

                        if farming_upgrade:
                            farming_account = await self.upgarde_info(token)
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

                                    if wallet['balance'] >= item['cost']:
                                        upgrade_farm = await self.farming_upgarde(token, id)
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
                                        f"{Fore.YELLOW+Style.BRIGHT} Reached Max Level {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} Upgrade Is Skipped {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )

                        tasks = await self.sub_tasks(token)
                        if tasks:
                            for task in tasks['tasks']:
                                recource_id = task['recourceId']
                                task_id = task.get('id', None)
                                is_done = task['done']
                                is_claimed = task['claimed']

                                if task and not is_done and not is_claimed:
                                    check = await self.check_tasks(token, recource_id)
                                    if check and check['id']:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                            f"{Fore.GREEN+Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )

                                        tasks = await self.sub_tasks(token)
                                        for task in tasks['tasks']:
                                            task_id = task.get('id', None)

                                            if task and task_id is not None:

                                                claim = await self.claim_tasks(token, task_id)
                                                if claim and claim['id']:
                                                    self.log(
                                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                                        f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                                        f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                                        f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                                        f"{Fore.WHITE+Style.BRIGHT} {task['reward']} MT {Style.RESET_ALL}"
                                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                                    )
                                                else:
                                                    self.log(
                                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                                        f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                                        f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                                    )
                                            else:
                                                continue
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                            f"{Fore.RED+Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )

                                elif task and is_done and not is_claimed:
                                    if task_id is not None:
                                        claim = await self.claim_tasks(token, task_id)
                                        if claim and claim['id']:
                                            self.log(
                                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                                f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                                f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                                f"{Fore.WHITE+Style.BRIGHT} {task['reward']} MT {Style.RESET_ALL}"
                                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                            )
                                        else:
                                            self.log(
                                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                                f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                                f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                            )
                                    else:
                                        continue

                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )

    async def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            farming_upgrade = self.question()

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
                        await self.process_query(query, farming_upgrade)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        await asyncio.sleep(3)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    await asyncio.sleep(1)
                    seconds -= 1

        except FileNotFoundError:
            self.log(f"{Fore.RED}File 'query.txt' tidak ditemukan.{Style.RESET_ALL}")
            return
        except Exception as e:
            self.log(f"{Fore.RED+Style.BRIGHT}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        bot = Fastmint()
        asyncio.run(bot.main())
    except KeyboardInterrupt:
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
            f"{Fore.RED + Style.BRIGHT}[ EXIT ] Fastmint App - BOT{Style.RESET_ALL}                                       "                              
        )