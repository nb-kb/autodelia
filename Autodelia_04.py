# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 17:39:46 2024

@author: Duchess & K
"""

import time as time
import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
   
# clock that never resets, used to gather incrementing time and
# numerical time digits' places' loop intervals information
def secs():
    date = time.ctime()
    sec = int(date[18])
    eng = sec, date
    return eng

get_sec = secs()

###
# random numbergen
def rand(ranrange,factor):
    rand = random.randrange(1,ranrange)
    rng_output = rand*factor
    return rng_output
### 

# differentiates string time and integer time for finer comparisons
# and loop length control
globaltime = get_sec
gt0 = globaltime
gtint = gt0[0]
gtdate = gt0[1]
gt = [gtint, gtdate]

 # a way to stop the main loop for gameplay 
def sec_stopper(gt):

    step = False    

    # check globaltime
    if gt[1] < secs()[1]:        
        gt[1] = secs()[1]
        gt[0] = secs()[0]
        step = True

        
    return gt[0],step


# a way to check what tech the player has made it to
progress = [0,0,0,0,0,0,0,0,0,0]

# adds binary int flags raised during loop to determine progress
def progress_checker():
    total = 0
    i = 0
    for reso in resources[1:11]:
        if reso[1] > 0:
            progress[i] = 1
    for resource in progress:
        total += resource
        
        if total > 3:
            invert_total = total - 2
            inv_tot = invert_total
        else:
            inv_tot = 1
    
    return inv_tot, total

# era determines which populations and menus to show
# based on population list
era = -1

#a way to multiply gains by era without it ever equalling 0
absera = abs(era + 0.1 * 1)

# check the current amount of times the player has come around the
# main while loop    # also called 'Influence' in-game
loop = [0]

# changes to mod0 allow menus items to be added
# at faster or slower intervals
def option_cieling(mod0):
    
    # designed to be checked for menu option additions over time
    loop_counter_with_mod0 = [ loop[0] , mod0 ]
    cntr0 = loop_counter_with_mod0
    
    # takes into from cntr0
    counter0_divider = cntr0[0] / cntr0[1]
    cntr0_div = counter0_divider
    
    return int(cntr0_div + 2)

# loops to Influence
def loop_check():
    # calling loops 'Influence' for fun, maybe use it
    # later for something as the player gets more of it.
    return 'Influence: ', int(loop[0])



population = [
    
            'Class, Population, Rate',
            
              ['tribe',        0, 0,'form a tribe','living in your tribes','bushpeople','outer wilds'],
              ['village',      0, 0,'build a village','our villages','villagers','outer wilds'],
              ['town',         0, 0,'construct a new town','governing our towns','legates','outer wilds'],
              ['city',         0, 0,'conquer a city','their lives of luxury','nobles','outer wilds'],
              ['metropolis',   0, 0,'design a metropolis','uptopic lives','patricians','outer wilds'],
              ['country',      0, 0,'invade a country','acting as emissaries','viceroyals','outer wilds'],
              ['empire',       0, 0,'claim new boundaries for the empire','ruling your lands','royals','outer wilds'],
              ['cosmopolis',   0, 0,'assasinate royals of neighboring cosmopolii','operating in stealth','cyber-templar','outer wilds'],
              ['interplanetary empire', 0, 0,'colonize another planet','dominating planets','space captains','outer wilds'],
              ['intergalactic dynasty', 0, 0,'unleash galactic war','destroying stars','solar vassals','outer wilds'],
              
              # tutorial era (-1)
              ['camp', 1, 1,'form a camp','camping','outlanders','outer wilds']
              
              ]



# Class: Size
camp = population[-1]
tribe = population[1]
village = population[2]
town = population[3]
city = population[4]
metropolis = population[5]
country = population[6]
empire = population[7]
cosmopolis = population[8]
interplanetary = population[9]
intergalactic = population[10]



# Class: Rate
rt_camp = camp[2]
rt_tribe = tribe[2]
rt_village = village[2]
rt_town = town[2]
rt_city = city[2]
rt_metropolis = metropolis[2]
rt_country = country[2]
rt_empire = empire[2]
rt_cosmopolis = cosmopolis[2]
rt_interplanetary = interplanetary[2]
rt_intergalactic = intergalactic[2]

pop = population[era]
        
resources = [
    
          'Types, Qty, Rate, Perf. Present, Present, Identity, Locale',
            
            ['meat', 0,0,'search for game','chasing down wild animals','hunters','fields'],
            ['wood', 0,0,'take axe to tree','axing down the trees','lumberjacks','eerie, dark wood'],
            ['stone', 0,0,'break stone','slaving away','miners','mines'],
            ['money', 0,0,'strike a deal','accounting hedge funds','merchants','financial district'],
            ['metal', 0,0, 'craft fine weaponry','arming the soldiers','smiths','forge'],
            ['soldiers', 0,0,'forge alliances','conscripting fighters','emissaries','battlefield'],
            ['silica', 0,0,'design microchips','programming A.I.','engineers','machine cities'],
            ['energy', 0,0,'stabalize molecules','manipulating fusion','cyber templar','solar laboratory'],
            ['fuel', 0,0,'navigate asteroids','colonizing moons','space captains','uncharted space'],
            ['dysonspheres', 0,0,'construct mega-spheres','harvesting stars','solar vassals','pegasus galaxy'],
          
            # tutorial resource (-1)
            ['spirit:', 1,0,'meditate','finding higher self','yourself','subconscious']
          
          ]

procure = [
    
    'Procurement options',
    
    
    'Cultivate the Lands for',
    'Trade with Caravans for',
    'Go to the Market for',
    'Order Shipments of',
    '',
    '',
    '',
    '',
    'Synthesize Cubes of',
    'Terraform a Planet Specifically to Produce',
    
    # tutorial title
    'Hunt for',
    
    ]

# Types: Qty
spirit = resources[-1]
meat = resources[1]
wood = resources[2]
stone = resources[3]
money = resources[4]
metal = resources[5]
soldiers = resources[6]
silica = resources[7]
energy = resources[8]
fuel = resources[9]
dysonspheres = resources[10]

# Types: Rate
# rate = [
 
# "Resource Rates:",     
 
# meat[2],
# wood[2],
# stone[2],
# money[2],
# metal[2],
# soldiers[2],
# silica[2],
# energy[2],
# fuel[2],
# dysonspheres[2],

# ]

workers = ['workers',0]

struggle = 1

meat_used = 0

expansion = 0

deceased = 0

basic_controls = [
    
    f'{pop[4].capitalize()} Menu: 1-',
    
    f' Find other {pop[5].capitalize()}',
    f'{procure[era]} Food',
    'Take Axe to Tree',
    'Break Stone',
    'Conquer a New Land',
    'Hire Mercenaries',
    'Refine Ores',
    '',
    '',
    '',
    

    ]

work_delegation_controls = [
    
    f'{pop[5].capitalize()} Delegation: 1-',
    
    '(un)assign',
    '(un)assign',
    '(un)assign',
    '(un)assign',
    '(un)assign',
    '(un)assign',
    '(un)assign',
    '(un)assign',
    '(un)assign',
    '(un)assign',
    
    ]


commerce_controls = [
    
    # constructing these bonuses offers money, which can be used to buy soldiers
    'Commerce Menu: 1-',
    
    # maybe a list of things, chairs, doors, tables, etc. could be modified by another list
    # of traits such as material, or bonus pools.
    # linear increace to influence ++
    'wood + stone = furnishings ; influence +',
    
    # another list of hammers, drills, swords, etc, maybe with their own boost pools as well
    # make the game similar to a roguelike with different random upgrades to choose from
    # multiplicative increase to pop[2] eg. 1.025x or 2x
    'stone + metal = tools/weapons ; pop rate x',
    
    # make a list of transportation types, maybe fuel and metal can bring about bigger boosts
    # later on eg, boats, planes, carriages, into freighters, jets, and trains
    # linear increase to idle resource gain eg +20% wood gain or + 2%
    'wood + metal = transportation ; idle resource rates +',
    
    # secure the troops with more armor, different lists based on era may be useful
    # increase personal_struggle random range by a linear amount eg. pe_st += 15 or pe_st += 40
    'soldiers + metal = armor ; pe_st range +',
    
    'silica + solders = cyborgs ; increased item effectiveness +',
    
    'metal + fuel = modern transportation',
    
    'fuel + silica = living ships ; item effectiveness x',
    
    'dysonspheres + fuel = paradoxes ; pop gain x',
    
    ]

def loop_rewards0():
    for reso in resources[1:11]:
        gain0= reso[2]
        
        reso[1] += gain0*absera
        
        
    for pop in population[1:10]:

        gain1= pop[2]
        pop[1] += gain1*absera

def loop_reward_display():                
    if workers[1] > 0:
        loop_rewards0()
        print(f'\ncontributions of {pop[5]} to the {pop[0]}\n\n')
        
        for reso in resources[1:11]:
            if reso[2]>0:
                print(     f'{reso[5]} brought {reso[1]} {reso[0]}')
                
        if era != -1 and era != 1:
            recruits = population[era-1]
            
        else:
            recruits = pop
            
        for popu in population[1:11]:
            if popu[2]>0:
                print(     f'{popu[5]} found {popu[1]} new {recruits[5]}')
        
    else:
        print("\nno one works for you...\n")
        
def header():
    
    clear()
    
    print('AUTODELIA')
    print(tabs,tb,workers)
    print('')
    
#submenu
def submenu(rnge0, current_resources):
    
    # increment this to increase the amount of shown resources in the
    # submenu
    cu_re = current_resources + 1
    
    
    submenu_options = [
        
        'Submenu Options:',
                
         population[era],
        
         resources[rnge0:cu_re],
         
            
        ]

    su_op = submenu_options
    
    popu = su_op[1]
    reso = su_op[2]
    x = []
    for res in reso:
        x.append(res[0:2])
        
    submenu = popu[0:2], x
    

    return print(submenu, loop_check(),'\n'), 

# to turn menus into pages to flip through. append a 0 to the list for more tabs
tabs = [1,0,0,0]

# abstractions of the tabs[] configurations to plug in easier
menu = [1,0,0,0]
delegation = [0,1,0,0]
conquest = [0,0,1,0]
commerce = [0,0,0,1]

# numerator used to scan left and right of the tab bar
tb = [0]

def page_nav(act):

    if act == '[':
        tabs[tb[0]] -=1
        tb[0] -=1
        if abs(tb[0]) > len(tabs):
            tb[0] = -1
        tabs[tb[0]] +=1
        
    elif act == ']':
        tabs[tb[0]] -=1
        tb[0] += 1
        if tb[0] >= len(tabs):
            tb[0] = 0
        tabs[tb[0]] +=1


    if tabs == [1,0,0,0]:
        command = menu_tab()
    elif tabs == [0,1,0,0]:
        command = delegation_tab()     
    elif tabs == [0,0,1,0]:
        command = conquest_tab()
    elif tabs == [0,0,0,1]:
        command = commerce_tab()
        
    return command
       
# Control Menu
def menu_tab():
    # tabs = [1,0] 
    
    # defining the for loop option range to only increment
    # if the loop is a number divisible by 5
    option_range = option_cieling(5)
    opt_rnge = option_range
    if opt_rnge > 9:
        opt_rnge = 9
        
    header()  
    print(basic_controls[0] + f'{opt_rnge-1}')
    print('')
    
    i = 1

    for option in basic_controls[1:opt_rnge]:
        print(f'     {i}: {option}')
        i+=1

    

    
    prog = progress_checker()
        
    
    break_length = len(basic_controls)-i
    
    menu_break = '\n'*break_length
    print(menu_break)    
    submenu(prog[0],prog[1])
    print("'[' or ']' for more options")
    
    command = input(f'\nUse 0-9 on the keyboard to manage your {pop[0]}!\n')
    
    clear()
    
      
    return command


def delegation_tab():
    # tabs = [0,1]
    
    # defining the for loop option range to only increment
    # if the loop is a number divisible by 10
    option_range = option_cieling(10)
    opt_rnge = option_range
    if opt_rnge > 11:
        opt_rnge = 11
    
    header()  
    print(work_delegation_controls[0] + f'{opt_rnge -1}')
    print('')
    
    i = 1
    res = [pop[2]]
    jobs = [pop[5]]
    for reso in resources[1:opt_rnge]:
        numerators = reso[2]
        job = reso[5]
        jobs.append(job)
        res.append(numerators)
        
    for option in work_delegation_controls[1:opt_rnge]:
        
        
            print(f'     {i}: {option}', f'{jobs[i-1]} ({res[i-1]})')
            i+=1    
    
        
        # print(f'{i}: {option}',i, f'{resources[i]}')
        # i+=1
        
        
    prog = progress_checker()
       
    break_length = len(basic_controls)-i
    menu_break = '\n'*break_length

    print(menu_break)    
    submenu(prog[0],prog[1])
    print("'[' or ']' for more options")
    

    command = input(f'\nUse 0-9 on the keyboard to command your {pop[5]}!\n')
    
    clear()
         
    return command
    

def delegate_workers(resource):
    
    rate = resource[2]
    prog = progress_checker()
        
    header()
    print(f'Work Delegation: add/remove\n{tabs} {tb} {workers}\n\nUnemployed inhabitants: {pop[1]}\n\
\n{resource[5]} currently {resource[4]}: {resource[2]}\n')

    print('\n'*3)
    submenu(prog[0],prog[1])
    
    work_delegations = input(f'employ/fire {resource[5]}: \n\namount: ')
    
    wo_de = work_delegations
    
    try:
        wo_de = int(wo_de)
    except:
        ValueError
    
    if wo_de == '':
        print("AUTODELIA\n")
    elif type(wo_de) == int:
        
    
        clear()
        
        if  workers[1] + wo_de <= loop[0]:
            if pop[1] >= wo_de or rate >= wo_de:
                compare_pop = pop[1]
                compare_rate = rate
                
                
                compare_pop -= wo_de
                compare_rate += wo_de
                
    
                
                if compare_pop < 0:
                    
                    rate += pop[1]
                    workers[1] += pop[1]
                    pop[1] -= pop[1]
    
                    
                elif compare_rate < 0:
    
                    pop[1] += rate                
                    workers[1] -= rate
                    rate -= rate
                    
                else:
                    
                    pop[1] -= wo_de
                    workers[1] += wo_de                
                    rate += wo_de
    
                
                compare_pop += wo_de
                compare_rate -= wo_de
                
                resource[2] = rate
                
                pop[1] = pop[1]
                
                if pop[1] > compare_pop:
                    print('AUTODELIA\n\n')
                    print(f'[{pop[0]}: {pop[1]}] +{abs(wo_de)} unemployed {pop[5]}')
                    print(f'[{resource[0]} rate: {resource[2]}] {wo_de} {resource[5]}')
                    print('')
                    print(f'{abs(wo_de)} {resource[5]} recalled!')
           
                    print(f'The {resource[5]} are returning from {resource[4]} in the {resource[6]}!')
                    
                    
                elif pop[1] < compare_pop:
                    print('AUTODELIA\n\n')
                    print(f'[{pop[0]}: {pop[1]}] {abs(wo_de)} {pop[5]} employed!')
                    print(f'[{resource[0]} rate: {resource[2]}] +{wo_de} {resource[5]}')
                    print('')
                    print(f'{wo_de} {resource[5]} hired!')
                    print(f'You delegated some {resource[5]} to {resource[3]} in the {resource[6]}!')
                else:
                    print('idk chief...')
                    print('pop[1]',pop[1],'| worker_delegation',wo_de)
                    print('compare_pop',compare_pop,'| compare_rate',rate)
                    
    
                input('\n[enter]\n')
            
        else:
            print('AUTODELIA\n\n')
            input("Not enough Influence!\n[enter]\n")
                
def conquest_tab():
    
    header()
    print('Conquest Menu:')
    print('')
    
    i=-1
    for conq in conquests:
        if era >= i:
            i+=1
            
            print(conq[1])
            print('')
            
    prog = progress_checker()
    
    print('\n'*1*(7-i))
    submenu(prog[0], prog[1])
    
    print("'[' or ']' for more options")
    
  
    command = input(f'\nyour {pop[5]} are busy with {pop[4]}!\n')
    
    clear()
         
    return command

def commerce_tab():
    
    header()
    
    print(commerce_controls[0] + str(len(commerce_controls)))
    print('')
    i=1
    for good in commerce_controls[1::]:
        print(i,good)
        i+=1

    print('\n'*2)
    prog = progress_checker()
    
    submenu(prog[0],prog[1])
    
    command = input('\nnothing to see here...yet...\n[enter]\n')
    
    return command


def insight_rewards():
    header()
    insight = rand(3,1)
    loop[0] += insight
    print(loop_check(),'+',insight,'\n')
    
    gains = [
        
        'Gains Select:',
        
        'with your insights...',
        'into foresight...',
        'beyond the physical...'
        
        ]
    
    input(f'\nyour plans broaden; your awareness increases {gains[insight]}\n[enter]\n')
    command = page_nav(act)
    
    return command

def searching_rewards(pop):

    base = pop[0]
    acting = pop[4]
    agents = pop[5]
    theatre = pop[6]
    
    header()

    newcomers = pe_st
    pop[1] += newcomers
    
    loop[0] += 1
    
    loop_rewards0()
    loop_reward_display()
    
    print(f'you found {newcomers} {agents} for the {base} while {acting} in the {theatre}!')
    input('\n[enter]\n')
    command = menu_tab()
    
    return command
    
    
def procurement_rewards(resource0,has_cost,resource1,factor):
    # this is a branching function that allows for rewarding the player for things
    # meat,Flase,None if requireing nothing else OR something like wood,True,stone
    
    header()
    
    prog = progress_checker()
    
    resource0[1] += pe_st
    
    if has_cost == False and resource1 == None:
        
        print('...')
        
    elif has_cost == True:
        
        resource0
        
        
    submenu(prog[0],prog[1])
    
    
    
    
    
    
###
#Randomizer lists for varied gameplay flavor texts
###

tribe_facilities = [
    
    'Facilities:',
    
    'poop hole',
    'teepee',
    'small fire',
    'straw blanket... sex... maybe?',
    'the local cave you think is nice',
    
    ]

spoils = [
    
    'Spoils:',
    
    'head of the chieftan',
    "enemy tribe's poop hole",
    'necklaces made of teeth... for everyone!',
    'goats for... sexual purposes?',
    'some domesticated animals... the goats again...',
    
    'Next 5:',
    '',
    
    
    ]

searching = [
    
    'Search Options:',
    
    'searching for others stranded in the wilderness...',
    'scouting enemy territory for survivors...',
    'figures approach from the distance...',
    'you give up the search temporarily...',
    'getting lost...',
    'scanning the horizon for signs of life...',
    
    
    'AUTODELIA',
             
             ]

hunting = [
    
    'Hunt Options:',
    
    'coating yourself in mud...',
    'stalking the night...',
    'imitating mating calls...',
    'wearing animal pelts...',
    'cornering the local wildlife...',
    'realizing hope is lost...',
    
    'AUTODELIA',
             
             ]

animal = [
    
    'Animals:',
    
    'zebra',
    'goat',
    'deer',
    'mammoth',
    'fat chickens',
    'caribouuUU',
    'synthesized meat cubes',
    '',
    ''
    
    
    ]

lumbering = [
    
    'Lumber Options:',
    
    'searching for the best trees...',
    'sapping for that sweet, sweet syrup...',
    'taking an extra long lunch...',
    'exploring deeper into the dark woods...',
    'hauling lumber back to the tribe...',
    'eating the ripe fruit fresh off the branch...',
    
    
    'AUTODELIA',
    
    ]

land_grab = [
    
    'Land Grab Options:',
    
    'conquering local dam...',
    'building new teepees, farther from eachother...',
    'pulling out the stumps of fell trees...',
    'blood seeps into the soil...',
    'gathering wood for torches, and resin for torches...',
    'sharpening what little weapons we have...',
    'AUTODELIA',
    
    ]

benefit = [
    
    'Expansion benefit Options:',
    
    'A wave of immigrants moved in!...',
    'Travelling Shamans want to help our people...',
    'Scouts noticed in the shadows of the canopy...',
    'Blood seeps into the soil...',
    "'But sir, I JUST crucified him!...'"
    
    ]

attacking = [
    
    'Attack Options:',
    
    'mercilessly attacking the nearest tribe...',
    'wiping out all survivors...',
    'losing good sapiens...',
    'clashing in battles of wits and boundaries...',
    'getting bested, then gaining the upper hand, then getting bested, then gai...',
    'taking 10 paces backwards...',
    'AUTODELIA',
             
             ]

mining = [
    
    "Mining Options:",
    
    "looking for a warm, dark cave to explore...",
    "stumbling upon an amethyst geode...",
    "showing off your new diamond ring...",
    "asking friends for help... they decline...",
    "extracting copper with your pickaxe... the pointy end...",
    "entering a cavern full of bioluminescent fungi...",
    "AUTODELIA"
    
    ]

stalling = [
    
   " Stalling Options:",
   
   "watching the sunrise...",
   "getting lost in thought...",
   "imagining a future of total conquest...",
   "picturing the growth of the empire...",
   "ignoring good advice...",
   "taking bad avice...",
   "AUTODELIA"
   
    ]

def load(load_list):
    clear()
    # loading_elipses()           
    print('AUTODELIA\n')            
    print(f'\n{load_list[rand(7,1)]}\n')

def fallback():
    clear()
    print("AUTODELIA\n\ni don't think i've learned how to do that yet...")
    input('\n[enter]\n')
    
    command = page_nav(act)
    
    return command


"""
game start
game start
game start

"""

clear()
# Start Screen
input("AUTODELIA\n\
\n\
Welcome to Autodelia: an incremental tyranny simulator\n\
where even though you start from nothing, you will eventually\n\
hold the universe in your hand.\
\n\
\n\
WIP\n\
\n[enter]\n")

clear()


# begin input loop
act = menu_tab()

while True:
    
    # Conquests

    conquests = [
        
        ['camps',   f'     allied camps: {camp[2]}\n     {camp[5]}: {camp[1]}'],
        ['tribes',  f'     allied tribes: {tribe[2]}\n     {tribe[5]}: {tribe[1]}'],
        ['villages',f'     allied villages: {village[2]}\n     {village[5]}: {village[1]}'],
        ['towns',   f'     allied towns: {town[2]}\n     {town[5]}: {town[1]}'],
        ['cities',  f'     conquered cities: {city[2]}\n     {city[5]}: {city[1]}'],
        
        ['metropolii',     f'     allied metropolii: {metropolis[2]}\n     {metropolis[5]}: {metropolis[1]}'],
        ['countries',      f'     allied countries: {country[2]}\n     {country[5]}: {country[1]}'],
        ['empires',        f'     conquered nations: {empire[2]}\n     {empire[5]}: {empire[1]}'],
        ['cosmopolii',     f'     allied cosmopolii: {cosmopolis[2]}\n     {cosmopolis[5]}: {cosmopolis[1]}'],
        
        ['interplanetary empires',     f'    off world colonies: {interplanetary[2]}\n     {interplanetary[5]}: {interplanetary[1]}'],
        ['intergalactic dynasties',    f'    galaxies under your control: {intergalactic[2]}\n     {intergalactic[5]}: {intergalactic[1]}'],
        
        ]
    
    pop = population[era]
       
    gtint = sec_stopper(gt)[0]
    step = sec_stopper(gt)[1]  
    
  # a silly way of giving the player a little agency
    personal_struggles = rand(loop[0]+4,1)

    pe_st = personal_struggles + struggle
    
            
            
    # a way to check tabs input and value changing 
    if act == '[' or act == ']':
        act = page_nav(act)
        
    """
    0 - STALLING; ALL MENUS
    """
    
    if act == '0':
        
    # control 0 menu tab; gain 1-3 influence, loads stalling list            
        if step == True:
            load(stalling)
        
        if gtint == 0:
            
          act = insight_rewards()
          
          
    # 1 - SEARCH(MENU_TAB)
    #     ASSIGN MEAT RATE(DELEGATION_TAB)
    elif act == '1':
        
        if tabs == menu:
            
            if step == True:
                
                load(searching)
                
            if gtint == 1:
                
                act = searching_rewards(pop)
                
                
        if tabs == delegation:
            
            delegate_workers(pop)                  
            act = delegation_tab()    
            
        if tabs == conquest:
            act = fallback()
            
        if tabs == commerce:
            act = fallback()
            
    elif act == '2':
        
        if tabs == menu:
            
            if step == True:
                
                load(hunting)
                
            if gtint == 2:
                
                act = procurement_rewards(meat)
            
            
    elif act == '[' or act == ']':
        act = page_nav(act)
        
    else:
        act = fallback()
                        

