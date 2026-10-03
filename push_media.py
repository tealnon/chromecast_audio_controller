import time
import pychromecast
from zeroconf import Zeroconf

target_ip = "TARGET DEVICE IP"
print(f"[*] Initializing local mDNS and scanning for {target_ip}...")

zconf = Zeroconf()
try:
    services, browser = pychromecast.discovery.discover_chromecasts()
    pychromecast.discovery.stop_discovery(browser)
    
    cast_info = next((s for s in services if s.host == target_ip), None)
    
    if not cast_info:
        print(f"[-] Error: No Cast service found on {target_ip}.")
    else:
        print(f"[+] Target found. Establishing secure session...")
        cast = pychromecast.get_chromecast_from_cast_info(cast_info, zconf)
        cast.wait()
        
        mc = cast.media_controller
        audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        
        print("[*] Playing test audio stream...")
        mc.play_media(audio_url, "audio/mp3")
        mc.block_until_active()
        
        input("[*] Streaming active. Press Enter in the terminal to stop...")
        mc.stop()
        print("[+] Playback stopped cleanly.")
finally:
    zconf.close()