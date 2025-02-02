from orbitModeling import *
from load_star_database import load_star_database
from load_planet_database import load_planet_database
import vpython as vp
import time
from setup_master_database import setup_master_database
setup_master_database()
list_of_planets = load_planet_database()

def Jacob(time_increment):
    '''
    --------------------------------------------------------------------------------
    This is a function to test the GUI:
    - Input the time to simulate the orbit: works well inside a loop when incrementing the time variable
    - Outputs a list containing the earth and mars's 3d coordinates
    - The distances are in Km, which means very large values (we will porbably be moving to astronomical units (AU) later for that reason).
    - The angles are in radians as requested
    --------------------------------------------------------------------------------
    '''
    # Earth = planet(5.972 * math.pow(10, 24), 149598262.00, 0.017, 147098291.00, 365.25636, 0, -0.196535244, 1.796767421, 1.749518042, Sun)
    # Mars = planet(5.972 * math.pow(10, 24), 227943823.5, 0.093, 206655215, 687.0106875, 0.032288591, 0.865308761, 5.865019079, 0.7309438907, Sun)
    list_of_planets[0].simulate_orbit(time_increment)
    list_of_planets[1].simulate_orbit(time_increment)
    results = [list_of_planets[1].xPos, list_of_planets[1].yPos, list_of_planets[1].zPos, list_of_planets[0].xPos, list_of_planets[0].yPos, list_of_planets[0].zPos]
    return results


def display():
    vp.scene.append_to_title('\n')
    vp.button(text="credits", bind=showat, pos=vp.scene.title_anchor)
    vp.scene.append_to_caption('\n')
    vp.button(text="Pause", bind=Pause)
    vp.scene.append_to_caption('\n')
    t = vp.slider(min=-20000, max=20000, value=1, length=675, bind=setyear)
    vp.scene.append_to_caption('\n')
    print("B")
    celestpos = Jacob(t.value)
    # makes the sun shine
    vp.sphere(color=vp.color.yellow, emissive=True)
    vp.local_light(pos=vp.vector(0, 0, 0), color=vp.color.yellow)
    # creates the visual representation of the planets
    earth = vp.sphere(texture=vp.textures.earth,
                      pos=vp.vector(celestpos[0] / 10000000, celestpos[1] / 10000000, celestpos[2] / 10000000),
                      make_trail=True, trail_type="points", interval=10, retain=25)
    mars = vp.sphere(color=vp.vector(1, 0, 0),
                     pos=vp.vector(celestpos[3] / 10000000, celestpos[4] / 10000000, celestpos[5] / 10000000),
                     make_trail=True, trail_type="points", interval=10, retain=25)
    #    venus = vp.sphere(color = vp.vector(1,1,.8), pos = vp.vector(celestpos[0] / 10000000,celestpos[0] / 10000000,celestpos[0] / 10000000), make_trail=True, trail_type="points", interval=10, retain=10)
    #    mercury = vp.sphere(color = vp.vector(.3,.3,.3), pos = vp.vector(celestpos[0] / 10000000,celestpos[0] / 10000000,celestpos[0] / 10000000), make_trail=True, trail_type="points", interval=10, retain=5)
    #    moon = vp.sphere(color = vp.vector(.3,.3,.3), pos = vp.vector(Moon.xPos / 10000000, Moon.yPos / 10000000,0))
    vp.scene.append_to_caption('\n')
    sl = vp.slider(min=-20, max=20, value=1, length=675, bind=setspeed)
    while True:
        while pause == False:

            celestpos = Jacob(sl.value)
            # simulates motion
            #            Moon.simulate_orbit(i, 0)
            #            Earth.simulate_orbit(t, 0)
            #            Venus.simulate_orbit(t, 0)
            #            Mercury.simulate_orbit(t, 0)
            earth.pos = vp.vector(celestpos[0] / 10000000, celestpos[1] / 10000000, celestpos[2] / 10000000)
            mars.pos = vp.vector(celestpos[3] / 10000000, celestpos[4] / 10000000, celestpos[5] / 10000000)
            #            venus.pos = vp.vector(Venus.xPos / 10000000,Venus.yPos / 10000000,0)
            #            mercury.pos = vp.vector(Mercury.xPos / 10000000, Mercury.yPos / 10000000,0)
            #       moon.pos = vp.vector(Moon.xPos / 10000000, Moon.yPos / 10000000,0)
            if (sl.value > 0):
                t.value += 1
                time.sleep(0.01)
            else:
                t.value -= 1
                time.sleep(.01)


def display_at(date):
    # insert planets
    Sun = star(1.989 * math.pow(10, 30))
    Earth = planet(5.972 * math.pow(10, 24), 149598262.00, 0.017, 147098291.00, 365.25636, Sun)
    Venus = planet(5.972 * math.pow(10, 24), 108209475.00, 0.007, 107476170.00, 224.7057127, Sun)
    Mercury = planet(5.972 * math.pow(10, 24), 57909227.00, 0.206, 46001009.00, 87.95373149, Sun)
    #    Moon = satellite(7.34767 * math.pow(10, 22), 384400, Earth)
    celestpos = Jacob(date,list_of_planets)

    # makes the sun shine,
    vp.sphere(color=vp.color.yellow, emissive=True)
    vp.local_light(pos=vp.vector(0, 0, 0), color=vp.color.yellow)
    # creates the visual representation of the planets
    earth = vp.sphere(texture=vp.textures.earth,
                      pos=vp.vector(celestpos[0] / 10000000, celestpos[1] / 10000000, celestpos[2] / 10000000),
                      make_trail=True, trail_type="points", interval=10, retain=25)
    mars = vp.sphere(color=vp.vector(1, 0, 0),
                     pos=vp.vector(celestpos[3] / 10000000, celestpos[4] / 10000000, celestpos[5] / 10000000),
                     make_trail=True, trail_type="points", interval=10, retain=25)


def showat():
    global day
    display_at(day)


def setspeed(s):
    speed = s


def setday(d):
    global day
    day = d


def setmonth(m):
    month = d


def setyear(y):
    year = y


pause = False

t = 0

day = 0


def Pause(a):
    global pause
    pause = not pause




vp.scene.width = 800
vp.scene.height = 800
vp.scene.range = 1.3
vp.scene.title = "ANTIKYTHERA\n"

vp.button(text="display", bind=display, pos=vp.scene.title_anchor)
vp.scene.append_to_title('\n')
vp.button(text="display at", bind=showat, pos=vp.scene.title_anchor)
vp.scene.append_to_title('\n')
vp.winput(bind=setday, pos=vp.scene.title_anchor)
vp.winput(bind=setmonth, pos=vp.scene.title_anchor)
vp.winput(bind=setyear, pos=vp.scene.title_anchor)
vp.scene.append_to_title('\n')
print("A")
