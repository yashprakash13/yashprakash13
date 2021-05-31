import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width':1920, 'height': 800})
    await page.goto('https://medium.com/@ipom')
    await page.screenshot({'path': 'medium_profile_screenshot.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
