import json
import os 

############################################### SPELL DICTS ##########################################################
#               For every spell you make that hasnt already been added to the line 71 if                             # 
#              statement can you please add it otherwise it the program wont work for you                            #
#
# Base outline for spells:
#   NAME_SPELL: Name. 
#   CASTING_TIME: Time it takes to cast, 1 action , 2 bonus action. You have one action and one bonus action per round
#                 not counting movement
#   RANGE: How far the spell can travel measured in feet, 0ft spell you cast on yourself. 1 grid square is 5ft 
#   COMPONENTS: Verbal(V), Somatic(S), Material(M), {component}, if requires (M) put that at the end + material it
#               requires + 0 or 1, 0 wont be used up, 1 represents it will be. example: 'V','M ; lead, 0'
#   DURATION: 0 stands for instantanious, numb above 0 stand for rounds in battle that it will last.
#
#                                    Not allways present for every spell 
#
#   SAVING_THROW: {True or False depending if spell has a saving throw}{ability required(STR, DEX, CON, INT, WIS, CHA)}
#                  Leave second bit out if False.
#   DAMAGE_TYPE: {True or False depending if spell has a damage type}{damage type(Acid, Bludgeoning, Cold, Fire, Force
#                , Lightning, Necrotic, Piercing, Poison, Radiant, Slashing, Thunder, Disadvantage)}
#                Leave second bit out if False.
#   RESISTANCE_TYPE: {True or False depending if spell has a resistance type}{resistance type(Bludgeoning, Piercing,
#                     Slashing} Leave second bit out if False.
#   DAMAGE_INCREASE: Per x amount of levels {True or False depending if spell does damage}{dice start amount}
#                    {levels it increases at}.Leave last bits out if False.
#
#   If they have more than one value you need to make them into a list
#
#Template = ' ' : {'NAME_SPELL': ' ','CASTING_TIME': 0,'RANGE': 0, 'COMPONENTS': ' ','DURATION': 0,'SAVING_THROW': ' ',
#                 'DAMAGE_TYPE': ' ','RESISTANCE_TYPE',' ','DAMAGE_INCREASE' : ' '},
      

WIZARD_CANTRIPS = { '1' : {'NAME_SPELL': 'Acid Splash','CASTING_TIME': 1,'RANGE': 60, 'COMPONENTS': ['V','S'],
                           'DURATION': 0,'SAVING_THROW': [True,'DEX'], 'DAMAGE_TYPE': [True,'Acid'],'RESISTANCE_TYPE':False
                           ,'DAMAGE_INCREASE' : [True,'1d6', 5]},
                    '2': {'NAME_SPELL': 'Blade Ward','CASTING_TIME': 1, 'RANGE': 0, 'COMPONENTS': ['V','S'],
                          'DURATION': 1, 'SAVING_THROW': False, 'DAMAGE_TYPE': False, 'RESISTANCE_TYPE': [True,'Bludgeoning'
                          ,'Piercing','Slashing'], 'DAMAGE_INCREASE': False},
                    '3' : {'NAME_SPELL': 'Chill Touch','CASTING_TIME': 1,'RANGE': 120, 'COMPONENTS': ['V','S'], 'DURATION':
                           0, 'SAVING_THROW':False, 'DAMAGE_TYPE':[True, 'Disadvantage'], 'RESISTANCE_TYPE':False,
                           'DAMAGE_INCREASE':[True,'1d8',5]}
                    }


################################################################################################
def spell_load(spell, spell_store, filepath, bool_): 
    filePathNameExt = 'Class_Spells/' + filepath + '/' + spell_store + '.json'
    for oneCantrip in spell.keys():
        try:
            with open(filePathNameExt,'r') as f:
                sPS = json.load(f)
                if spell[oneCantrip]['NAME_SPELL'] in sPS[oneCantrip]['NAME_SPELL']:
                    return bool_ == False
                    
                else:
                    with open(filePathNameExt,'w') as f:
                        json.dump(spell, f, indent = 4)
                    return bool_ == False
        except:
            with open(filePathNameExt,'w') as f:
                        json.dump(spell, f, indent = 4)
            return bool_ == False
            
p = True
                    
while p == True:
    try:
        file = input('Please enter spell class i.e Sorcerer, Druid: > ')
        file = file[0].upper()+file[1:].lower()
        all_files = os.listdir("Class_Spells/" + file)
        print(f'LIST OF FILES ALREADY IN {file} folder:')
        for i in all_files:
            print(i)
    except Exception as e:
        print(f'error:{e}')
        break
    print('\n')
    open_or_append = int(input('do you want to open(1) or add spell list to files(2) > '))
    if open_or_append == 1:
        file_name_open = input('Please enter a file to open from the list >')
        with open('Class_Spells/'+file+'/'+file_name_open+'.json', 'r') as f:
            spellList =  json.load(f)
            for oneCantrip in spellList.keys():
                for i in spellList[oneCantrip]:
                    print(i,':', spellList[oneCantrip][i])
                print('\n')
                    
                
        break
    elif open_or_append == 2:
        file_name = input('''
    If you are appending to a spell list that
    already exists Please enter the name of the .json file
    --------------------------------------------------
    If you created a new list of spells please enter the
    name of a new file to store the spells in, NAME FORMAT EXAMPLES:
    WIZARD_CANTRIPS - WIZARD_SPELLS_LEVEL_1 * This should be the
    same name you gave the dictionary *
     > ''')
        spell_append = file_name.strip('.json')
        
        if spell_append == 'WIZARD_CANTRIPS':
            spell_dict = WIZARD_CANTRIPS
        
        
        p = spell_load(spell_dict, spell_append, file, p)



