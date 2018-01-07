#coding:utf-8
import telebot
import config
from config import *
import requests,json
import random
import os
requests.packages.urllib3.disable_warnings()

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start","hello","hi","help"])
def start(message):
    bot.send_message(message.chat.id, "Hello, I\'m Telegram Bot. \n"
                                            "The list of commands are:\n"
                                            "/help - list of commands\n"
                                            "/cats - get random cat and have fun\n"
                                            "/rates - get actual exchange rates\n"
                                            "/zcash - get actual ZCash Balance\n"
                                            "/tw - TeamViewer Status\n"    
                                            #"/monstatus - Monitoring Status \n"
                                            "/monstopall - Stop All Monitoring \n"
                                            "\n"                
                                            "-----------NiceHash-----------\n"
                                            "/speed - worker's actual speed \n"
                                            "/uptime - worker's uptime \n"                                                                                
                                            "/nice - get your Nicehash balance \n"
                                            "/nice_monstart - Start Monitoring \n"
                                            "/nice_monstop - Stop Monitoring \n"
                                            "\n"
                                            "-----------NanoPool_ZEC-----------\n"                                        				                            
                                            #"/zec_hashrate - get workers speed \n"
                                            #"/zec_avghash  - get AVG speed \n"
   		                            "/zec_monstop - Stop Monitoring \n"					                
 		                            "/zec_monstart - Start Monitoring \n"
                                            "\n"
                                            "-----------NanoPool_XFX-----------\n"                                                                                  
                                            #"/xfx_hashrate - get workers speed \n"
                                            #"/xfx_avghash  - get AVG speed \n"
                                            "/xfx_monstop - Stop Monitoring \n"                                 
                                            "/xfx_monstart - Start Monitoring \n"
                                            "\n"
                                            "-----------NanoPool_SAPHIRE-----------\n"                                                                               
                                            #"/saph_hashrate - get workers speed \n"
                                            #"/saph_avghash  - get AVG speed \n"
                                            "/saph_monstop - Stop Monitoring \n"                                 
                                            "/saph_monstart - Start Monitoring \n"
                                            )


@bot.message_handler(commands=["zec_monstop"])
def zecmonstop(message):
    os.system("crontab -l | sed '/^[^#].*zecnanomonitor.*/s/^/#/' | crontab -")
    bot.send_message(message.chat.id, "Zec Monitoring Stopped")


@bot.message_handler(commands=["zec_monstart"])
def zecmonstart(message):
    os.system("crontab -l | sed '/^#.*zecnanomonitor.*/s/^#//' | crontab -")
    bot.send_message(message.chat.id, "Zec Monitoring Started")


@bot.message_handler(commands=["xfx_monstop"])
def zecmonstop(message):
    os.system("crontab -l | sed '/^[^#].*xfxnanomonitor.*/s/^/#/' | crontab -")
    bot.send_message(message.chat.id, "Zec Monitoring Stopped")


@bot.message_handler(commands=["xfx_monstart"])
def zecmonstart(message):
    os.system("crontab -l | sed '/^#.*xfxnanomonitor.*/s/^#//' | crontab -")
    bot.send_message(message.chat.id, "Zec Monitoring Started")



@bot.message_handler(commands=["saph_monstop"])
def zecmonstop(message):
    os.system("crontab -l | sed '/^[^#].*saphirenanomon.*/s/^/#/' | crontab -")
    bot.send_message(message.chat.id, "Zec Monitoring Stopped")


@bot.message_handler(commands=["saph_monstart"])
def zecmonstart(message):
    os.system("crontab -l | sed '/^#.*saphirenanomon.*/s/^#//' | crontab -")
    bot.send_message(message.chat.id, "Zec Monitoring Started")



@bot.message_handler(commands=["nicemonstop"])
def nicemonstop(message):
    os.system("crontab -l | sed '/^[^#].*nicehash.*/s/^/#/' | crontab -")
    bot.send_message(message.chat.id, "Nice Monitoring Stopped")


@bot.message_handler(commands=["nicemonstart"])
def nicemonstart(message):
    os.system("crontab -l | sed '/^#.*nicehash.*/s/^#//' | crontab -")
    bot.send_message(message.chat.id, "Nice Monitoring Started")


@bot.message_handler(commands=["nicemonstop"])
def nicemonstop(message):
    os.system("crontab -l | sed '/^[^#].*nicehash.*/s/^/#/' | crontab -")
    os.system("crontab -l | sed '/^[^#].*saphirenanomon.*/s/^/#/' | crontab -")
    os.system("crontab -l | sed '/^[^#].*xfxnanomonitor.*/s/^/#/' | crontab -")
    os.system("crontab -l | sed '/^#.*zecnanomonitor.*/s/^#//' | crontab -")
    bot.send_message(message.chat.id, "ALL Monitoring Disabled !")


@bot.message_handler(commands=["tw"])
def teamviewer(message):

    resp = requests.get('https://webapi.teamviewer.com/api/v1/devices?groupid=g110554507' , headers={'Authorization': 'Bearer 2658988-8XhttiQW8GCcs5UoDjJg'})
    stats = json.loads(resp.text)

    output = ""
    for device in stats['devices']:
        output = output + str(device['alias']) +"\n" + str(device['online_state']) + "\n" + "-----------------\n"

    bot.send_message(message.chat.id, "TeamViewer Status\n"
                                "-----------------\n")
    bot.send_message(message.chat.id, output)


@bot.message_handler(commands=["speed"])
def speed(message):
    stats = getStats()
    a = ""
    list1 = []
    for worker in stats["result"]["workers"]:
        a = "Worker " + str(worker[0]) + " Speed = " + str(worker[1].get("a"))
        list1.append(a)
    list1.sort()
    output = ""
    for i in list1:
        output = output + str(i) + "\n"
    bot.send_message(message.chat.id, output)



@bot.message_handler(commands=["zec_hashrate"])
def zec_hashrate():
    value = "Zec"



@bot.message_handler(commands=["hashrate"])
def hashrate(message):
    stats = nanoStats()
    a = ""
    list1 = []
    for worker in stats['data']:
        a = "Worker " + str(worker['id']) + " HashRate = " + str(worker['hashrate'])
        list1.append(a)
    list1.sort()
    output = ""
    for i in list1:
        output = output + str(i) + "\n"
    bot.send_message(message.chat.id, output)


@bot.message_handler(commands=["avghash"])
def avghash(message):
    stats = getHash()
    o = "AVG HasRate at NanoPool:"
    s = ""
    a = "now = " + str(stats['data']['hashrate'])
    b = "h1 = " + str(stats['data']['avgHashrate']['h1'])
    c = "h3 = " + str(stats['data']['avgHashrate']['h3'])
    d = "h6 = " + str(stats['data']['avgHashrate']['h6'])
    e = "h12 = " + str(stats['data']['avgHashrate']['h12'])
    f = "h24 = " + str(stats['data']['avgHashrate']['h24'])
    list1 = [o, s, a, b, c, d, e, f]
    output = ""
    for i in list1:
        output = output + str(i) + "\n"
    bot.send_message(message.chat.id, output)


@bot.message_handler(commands=["uptime"])
def uptime(message):
    stats = getStats()
    a = ""
    list2 = []
    for worker in stats["result"]["workers"]:
        a = "Worker " + str(worker[0]) + " Uptime = " + str(worker[2]) + " min"
        list2.append(a)
    list2.sort()
    output = ""
    for i in list2:
        output = output + str(i) + "\n"
    bot.send_message(message.chat.id, output)


@bot.message_handler(commands=["ratebtc"])
def ratebtc(message):
    ratebtc = btcrate()
    bot.send_message(message.chat.id, "1 BTC = $ " + str(ratebtc))


@bot.message_handler(commands=["ratezec"])
def ratezec(message):
    ratezec = zecrate()
    bot.send_message(message.chat.id, "1 ZEC = $ " + str(ratezec))

@bot.message_handler(commands=["rateeth"])
def rateeth(message):
    rateeth = ethrate()
    bot.send_message(message.chat.id, "1 ETH = $ " + str(rateeth))



@bot.message_handler(commands=["rates","rateall"])
def rates(message):
    rateeth = ethrate()
    ratebtc = btcrate()
    ratezec = zecrate()
    bot.send_message(message.chat.id, "1 BTC = $ " + str(ratebtc) + "\n"
                                      "1 ZEC = $ " + str(ratezec) + "\n"
                                      "1 ETH = $ " + str(rateeth))

@bot.message_handler(commands=["profit"])
def profitability(message):
    profitability = profit()
    profitbtc = "%.4f" % (profitability)
    ratebtc = btcrate()
    profitusd = "%.2f" % (ratebtc * profitability)
    bot.send_message(message.chat.id, "Profitability  " + str(profitbtc) + " BTC/day\n "
                                       "                     " + str(profitusd) + " USD/day")


@bot.message_handler(commands=["nice"])
def nicehash(message):
    nicebtc = btcnice()
    ratebtc = btcrate()
    usd = "%.2f" % (nicebtc * ratebtc)
    bot.send_message(message.chat.id, "NiceHash Balance:\n"
                                    "BTC = " + str(nicebtc) +"\n"
                                    "USD = $ " + str(usd))

@bot.message_handler(commands=["block"])
def blockchain(message):
    btc = btcblock()
    ratebtc = btcrate()
    usd = "%.2f" % (btc * ratebtc)
    #ratezec = " 1 ZEC = $ " + str(rateformat)
    bot.send_message(message.chat.id, "BlockChain Balance:\n"
                                    "BTC = " + str(btc) +"\n"
                                    "USD = $ " + str(usd))

@bot.message_handler(commands=["zcash"])
def zcash(message):
    payments = getZec()
    zecfull = 0

    for data in payments['data']:
        zecfull += float(data['amount'])

    zec = zecfull - 5.0551
    #print zec
    ratezec = float(zecrate())
    #print ratezec
    usd = "%.2f" % (zec * ratezec)
    #usd = (zec * ratezec)
    #print usd

    bot.send_message(message.chat.id, "ZCash Balance:\n"
                                    "------------------------\n"                                   
                                    "ZEC = " + str(zec) +"\n"
                                    "USD = $ " + str(usd) +"\n"
                                    "------------------------\n"                    
                                    "1 ZEC = $ " + str(ratezec))


@bot.message_handler(commands=["balance"])
def balance(message):
    btc = btcblock()
    nicebtc = btcnice()
    ratebtc = btcrate()
    btcfull = nicebtc + btc
    usd = "%.2f" % (btcfull * ratebtc)
    bot.send_message(message.chat.id, "Total Balance:\n"
                                     "BTC = " + str(btcfull) + "\n"
                                     "USD = $ " + str(usd))


@bot.message_handler(commands=["cats"])
def cats(message):
    query = str(random.randint(1, 99))
    link = 'http://thecatapi.com/api/images/get?format=src&type=gif&random=' + query
    bot.send_photo(message.chat.id, photo=link)



def getStats():
    # query the nicehash API and check worker's status
    url = 'https://api.nicehash.com/api'

    params = dict(
        method='stats.provider.workers',
        addr=btcAddress,
        algo=24
        )

    resp = requests.get(url=url, params=params)
    stats = json.loads(resp.text)
    return stats

def btcrate():
    url = "https://blockchain.info/ticker"
    resp = requests.get(url=url)
    rate = json.loads(resp.text)
    btcrate = float(rate['USD']['last'])
    return btcrate


def zecrate():
    url = "https://api.cryptonator.com/api/ticker/zec-usd"
    resp = requests.get(url=url)
    rate = json.loads(resp.text)
    zecrate = "%.2f" % (float(rate['ticker']['price']))
    return zecrate

def ethrate():
    url = "https://api.cryptonator.com/api/ticker/eth-usd"
    resp = requests.get(url=url)
    rate = json.loads(resp.text)
    ethrate = "%.2f" % (float(rate['ticker']['price']))
    return ethrate

def btcnice():
    url = "https://api.nicehash.com/api?method=stats.provider&addr=" + btcAddress
    resp = requests.get(url=url)
    nicebalance = json.loads(resp.text)
    btcnice = nicebalance['result']['stats']
    balance = 0
    a = 0
    for i in btcnice:
        balance += float(btcnice[a]['balance'])
        a += 1
    return balance


def btcblock():
    url = "https://blockchain.info/q/addressbalance/" + btcAddress
    resp = requests.get(url=url)
    btcblock = float(resp.text) / 100000000
    return btcblock

def profit():
    url = 'https://api.nicehash.com/api'
    params = dict(
        method='stats.provider.ex',
        addr=btcAddress,
        )

    resp = requests.get(url=url, params=params)
    stats = json.loads(resp.text)

    profitability = float(stats['result']['current'][0]['profitability'])
    acceptedspeed = float(stats['result']['current'][0]['data'][0]['a'])
    profitbtcday = profitability * acceptedspeed
    return profitbtcday

def nanoStats():
    # query the nicehash API and check worker's status
    url = 'https://api.nanopool.org/v1/zec/workers/' + zecAddress

    resp = requests.get(url=url, verify=False)
    stats = json.loads(resp.text)
    return stats

def getHash():
    # query the nicehash API and check worker's status
    url = 'https://api.nanopool.org/v1/zec/user/' + zecAddress

    resp = requests.get(url=url, verify=False)
    stats = json.loads(resp.text)
    return stats

def getZec():
    # query the nicehash API and check worker's status
    url = 'https://api.nanopool.org/v1/zec/payments/' + zecAddress

    resp = requests.get(url=url, verify=False)
    stats = json.loads(resp.text)
    return stats


if __name__ == "__main__":
    bot.polling()

