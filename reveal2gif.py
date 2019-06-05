import  os, sys, time
import random, argparse
import datetime
import imageio
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


VERSION = "0.2"
BANNER = """
{0} v. {1} - reveal2gif

by BongoKnight
""".format(sys.argv[0],VERSION)

GECKO_PATH = ''

def pause(min=2,max=5):
    return round(random.uniform(min,max),1)


def log(msg):    return msg


def get_page(driver,path):
    driver.get('file://' +  str(path))

    print('[*] Loading file')
    time.sleep(pause(2,3))

def make_screenshot(driver,path):
    ts = time.time()
    print("Screen saved in %s at %f" % (path, ts))
    driver.save_screenshot(path + "/" + str(int(ts)) + "slide.png")

def navigate(driver,path,key=""):
    actions = driver.find_element_by_css_selector("body")
    if key != None:
        for letter in key :
            make_screenshot(driver,path)
            if letter == "D":
                actions.send_keys(Keys.DOWN)
            elif letter == "U":
                actions.send_keys(Keys.UP)
            elif letter == "R":
                actions.send_keys(Keys.RIGHT)            
            elif letter == "L":
                actions.send_keys(Keys.LEFT)
            time.sleep(1)
    else:
        while True:
            elem = driver.find_element_by_css_selector(".navigate-right")
            make_screenshot(driver,path)
            if elem != None and elem.is_enabled():
                elem.send_keys(Keys.RIGHT)
                print("Saving a slide : " + str(driver.current_url))
                time.sleep(1)

            else:
                time.sleep(1)
                break


            



def make_gif(path, duration):
    
    filenames = [each for each in os.listdir(path) if each.endswith('slide.png')]
    images = []
    for filename in filenames:
        images.append(imageio.imread(path + "/" + filename))
    output_file = path + "/" + 'Slides.gif'
    imageio.mimsave(output_file, images, duration=duration)

def clean(path):
    filenames = [each for each in os.listdir(path) if each.endswith('slide.png')]
    for filename in filenames:
        os.remove(path + "/" + filename)

def parse_args():

    parser = argparse.ArgumentParser(description='Built a gif from the specified RevealJS presentation.')
    parser.add_argument('-p', '--path', metavar='REVEALPATH', type=str, help='Path to presentation')
    parser.add_argument('-o', '--out', metavar='OUTPUTPATH', type=str, help='Path to store gif and temporary png.')
    parser.add_argument('-k', '--key', metavar='KEY', type=str, help='Key to press : a string of R(ight) L(eft) U(p) D(own) for exemple RRRDD')
    parser.add_argument('-d','--driver-path', metavar='EXECUTABLE', type=str, help='Path to geckodriver executable')
    parser.add_argument('-q', '--headless', action='store_true', help='Run browser in headless mode. No browser window will be shown.')
    args = parser.parse_args(args=None if len(sys.argv) > 1 else ['--help'])

    return args


def main():

    print(BANNER)
    args = parse_args()
    outputpath = args.out
    path = args.path 
    key = args.key
    if not path or not outputpath:
        print('[!] Error: Reveal slides path and output directory must be provided')
        sys.exit(0)
    elif not os.path.isfile(path):
        print('[!] Error: Reveal slides not found')
        sys.exit(0)
    elif not os.path.isdir(outputpath):
        print("[!] Error: output directory doesn't exist")
        sys.exit(0)
    
    else:
        options = Options()
        if args.headless: options.add_argument("--headless")
        driver_path = args.driver_path if args.driver_path  else GECKO_PATH
        if not driver_path:
            print('\n[!] Error: the path to the geckodriver executable file must be provided')
            print('Geckodriver executables can be downloaded from https://github.com/mozilla/geckodriver/releases')
            sys.exit(0)
    print("* Saving GIF in %s" % outputpath)
    print("* Getting Slides in %s" % path)
    driver = webdriver.Firefox(executable_path=driver_path,options=options)
    start = time.time()
    get_page(driver,path)
    navigate(driver,outputpath,key)
    make_gif(outputpath,3)
    clean(outputpath)
    driver.quit()
    end = time.time()



    print('Create a GIF in %.2f' % (end-start))


if __name__ == '__main__':
    main()

