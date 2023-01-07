import pyautogui as pag
from time import sleep

mediapath = "D:/_projects/python/websap/media"

def pulseSecureConnection():
    print("Connecting to Pulse Secure...")

    systemTray = pag.locateCenterOnScreen(f"{mediapath}/system-tray.png", confidence=0.9)
    pag.moveTo(systemTray.x, systemTray.y, 0.5)
    pag.click()

    sleep(2)
    connectionComplete = pag.locateCenterOnScreen(f"{mediapath}/connection-complete.png", confidence=0.9)

    if connectionComplete:
        print("connected to pulse secure")

    elif type(connectionComplete) != "NoneType":
        pulseSecure = pag.locateCenterOnScreen(f"{mediapath}/pulse-secure.png", confidence=0.9)
        pag.moveTo(pulseSecure.x, pulseSecure.y, 0.5)
        pag.click(button="right")

        sleep(1)
        vpnConnection = pag.locateCenterOnScreen(f"{mediapath}/vpn-connection.png", confidence=0.9)
        pag.moveTo(vpnConnection.x, vpnConnection.y, 0.5)
        pag.click()

        sleep(1)
        vpnConnectButton = pag.locateCenterOnScreen(f"{mediapath}/vpn-connect-button.png", confidence=0.9)
        pag.moveTo(vpnConnectButton.x, vpnConnectButton.y, 0.5)
        pag.click()

        sleep(15)
        proceedButton = pag.locateCenterOnScreen(f"{mediapath}/proceed.png", confidence=0.9)
        pag.moveTo(proceedButton.x, proceedButton.y, 0.5)
        pag.click()

        sleep(15)
        print("Successfully connected to Pulse Secure!")


def loginToWebsap(driver):
    print("Logging in to Websap...")

    driver.maximize_window()
    driver.get("http://cciwebsap.cci.tr/account/newlogin")

    # Logging in using credentials
    driver.find_element("xpath", "//input[@name='UserName']").send_keys("DPKMF001")
    driver.find_element("xpath", "//input[@name='Password']").send_keys("Roar@357")
    driver.find_element("xpath", "//button[@id='btnLogin']").click()

    print("Websap Login Complete.")
