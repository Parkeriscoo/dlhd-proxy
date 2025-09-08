import reflex as rx
import os


proxy_content = os.environ.get("PROXY_CONTENT", "TRUE").upper() == "TRUE"
socks5 = os.environ.get("SOCKS5", "")
timezone = os.environ.get("TZ", "UTC")
guide_update = os.environ.get("GUIDE_UPDATE", "03:00")

print(f"PROXY_CONTENT: {proxy_content}\nSOCKS5: {socks5}\nTZ: {timezone}\nGUIDE_UPDATE: {guide_update}")

config = rx.Config(
    app_name="dlhd_proxy",
    proxy_content=proxy_content,
    socks5=socks5,
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)

config.timezone = timezone
config.guide_update = guide_update
