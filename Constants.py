


#On va sauter mercedes pour faire la suite et on revient plus tard 

#On va mettre egalement opel de coté et voir la suite 

#  {'ID.6', 'ID.4', 'ID.Buzz Cargo', 'Golf', 'Bus', 'Fox', 'Cross Touran', 'Bora', 'Cross Golf', 'Caddy',
#    'Eos', 'Golf Variant', 'Golf Cabriolet', 'Golf Sportsvan', 'ID Buzz', 'ID.5',
#    'Arteon', 'Golf Plus', 'CC', 'e-Golf', 'Crafter', 'Beetle', 'Golf GTD', 'Golf GTE',
#      'Grand California', 'Atlas', 'ID.3', 'Golf R', 'Amarok', 'Coccinelle', 'Golf GTI'}

dict_Marques_Names={
'audi':'Audi','bmw':'BMW', 'ford':'Ford','mercedes-benz':'Mercedes-Benz','opel':'Opel',
 'volkswagen':'Volkswagen','renault':'Renault','honda':'Honda',
 'hummer':'HUMMER','hyundai':'Hyundai','kia':'Kia','land-rover':'Land Rover','lexus':'Lexus','mazda':'Mazda','mini':'MINI','mitsubishi':'Mitsubishi','nissan':'Nissan',
 'peugeot':'Peugeot','skoda':'Skoda','suzuki':'Suzuki','toyota':'Toyota','volvo':'Volvo'
}


Auto_models={

'audi' : {  '100': '100', '200': '200', '50': '50', '80': '80', '90': '90', 'A1': 'a1',
             'A2': 'a2','A3': 'a3', 'A4': 'a4', 'A4 allroad': 'a4-allroad', 'A5': 'a5','A6': 'a6',
             'A6 allroad': 'a6-allroad', 'A7': 'a7', 'A8': 'a8', 'Allroad': 'allroad', 'Cabriolet': 'cabriolet', 
             'Coupe': 'coupe', 'e-tron': 'e-tron', 'e-tron GT': 'e-tron-gt', 'Q1': 'q1', 'Q2': 'q2', 'Q3': 'q3',
             'Q4 e-tron': 'q4-e-tron', 'Q5': 'q5', 'Q6': 'q6', 'Q7': 'q7', 'Q8': 'q8', 'Q8 e-tron': 'q8-e-tron',
             'QUATTRO': 'quattro', 'R8': 'r8', 'RS': 'rs', 'RS e-tron GT': 'rs-e-tron-gt', 'RS Q3': 'rs-q3', 
             'RS Q5': 'rs-q5', 'RS Q8': 'rs-q8', 'RS2': 'rs2', 'RS3': 'rs3', 'RS4': 'rs4', 'RS5': 'rs5',
            'RS6': 'rs6', 'RS7': 'rs7', 'S1': 's1', 'S2': 's2', 'S3': 's3', 'S4': 's4', 'S5': 's5',
            'S6': 's6', 'S7': 's7', 'S8': 's8', 'SQ2': 'sq2', 'SQ3': 'sq3', 'SQ5': 'sq5', 'SQ6': 'sq6',
             'SQ7': 'sq7', 'SQ8': 'sq8', 'SQ8 e-tron': 'sq9', 'TT': 'tt', 'TT-RS': 'tt-rs', 'TTS': 'tts', 'V8': 'v8'},



'bmw' : {
    '2002': '2002', 'Autres': 'autres', 'i3': 'i3', 'i4': 'i4', 'i5': 'i5', 'i7': 'i7',
    'i8': 'i8', 'iX': 'ix', 'iX1': 'ix1', 'iX2': 'ix2',
    'iX3': 'ix3', 'iX4': 'ix4', 'Série 1 (tous)': 'serie-1-(tous)', '114': '114', '116': '116', 
    '118': '118', '120': '120', '123': '123', '125': '125', '128': '128',
    '130': '130', '135': '135', '140': '140', 'Série 2 (tous)': 'serie-2-(tous)', '214': '214', 
    '216': '216', '218': '218', '220': '220', '223': '223', '225': '225',
    '228': '228', '230': '230', '235': '235', 'S240': 's240', 'Série 3 (tous)': 'serie-3-(tous)', 
    '315': '315', '316': '316', '318': '318', '320': '320', '323': '323',
    '324': '324', '325': '325', '328': '328', '330': '330', '335': '335',
    '340': '340', 'Active Hybrid 3': 'active-hybrid-3', 'Série 4 (tous)': 'serie-4-(tous)', '418': '418', 
    '420': '420', '425': '425', '428': '428', '430': '430', '435': '435',
    '440': '440', 'Série 5 (tous)': 'serie-5-(tous)', '518': '518', '520': '520', '523': '523', 
    '524': '524', '525': '525', '528': '528', '530': '530', '535': '535',
    '540': '540', '545': '545', '550': '550', 'Active Hybrid 5': 'active-hybrid-5', 'Série 6 (tous)': 'serie-6-(tous)', 
    '620': '620', '628': '628', '630': '630', '633': '633', '635': '635',
    '640': '640', '645': '645', '650': '650', 'Série 7 (tous)': 'serie-7-(tous)', '725': '725', 
    '728': '728', '730': '730', '732': '732', '735': '735', '740': '740',
    '745': '745', '750': '750', '760': '760', 'Active Hybrid 7': 'active-hybrid-7', 'Série 8 (tous)': 'serie-8-(tous)', 
    '830': '830', '840': '840', '850': '850', 'Série M (tous)': 'serie-m-(tous)', '1er M Coupé': '1er-m-coupé',
    'M1': 'm1', 'M2': 'm2', 'M3': 'm3', 'M4': 'm4', 'M5': 'm5',
    'M550': 'm550', 'M6': 'm6', 'M8': 'm8', 'M850': 'm850', 'Série X (tous)': 'serie-x-(tous)',
    'Active Hybrid X6': 'active-hybrid-x6', 'X1': 'x1', 'X2': 'x2', 'X2 M': 'x2-m', 'X3': 'x3',
    'X3 M': 'x3-m', 'X4': 'x4', 'X4 M': 'x4-m', 'X5': 'x5', 'X5 M': 'x5-m',
    'X6': 'x6', 'X6 M': 'x6-m', 'X7': 'x7', 'X7 M': 'x7-m', 'XM': 'xm',
    'Série Z (tous)': 'serie-z-(tous)', 'Z1': 'z1', 'Z3': 'z3', 'Z3 M': 'z3-m', 'Z4': 'z4', 
    'Z4 M': 'z4-m', 'Z8': 'z8'
},



'ford': {
    'Aerostar': 'aerostar', 'B-MAX': 'b-max', 'Bronco': 'bronco', 'C-MAX': 'c-max', 'Capri': 'capri', 
    'Connect Elkto': 'connect-elkto', 'Consul': 'consul', 'Cougar': 'cougar', 'Courier': 'courier', 'Crown': 'crown', 
    'Customline': 'customline', 'Econoline': 'econoline', 'Econovan': 'econovan', 'EcoSport': 'ecosport', 'Edge': 'edge', 
    'Escape': 'escape', 'Escort': 'escort', 'Excursion': 'excursion', 'Expedition': 'expedition', 'Explorer': 'explorer', 
    'Express': 'express', 'F 1': 'f-1', 'F 100': 'f-100', 'F 150': 'f-150', 'F 250': 'f-250', 'F 350': 'f-350', 
    'F 360': 'f-360', 'F 450': 'f-450', 'F 550': 'f-550', 'F 650': 'f-650', 'F Super Duty': 'f-super-duty', 
    'Fairlane': 'fairlane', 'Falcon': 'falcon', 'Fiesta': 'fiesta', 'Flex': 'flex', 'Focus': 'focus', 
    'Focus C-Max': 'focus-c-max', 'Focus CC': 'focus-cc', 'Freestar': 'freestar', 'Freestyle': 'freestyle', 'Fusion': 'fusion', 
    'Galaxy': 'galaxy', 'Grant Torino': 'grant-torino', 'Granada': 'granada', 'Grand C-Max': 'grand-c-max', 'Grand Tourneo': 'grand-tourneo', 
    'GT': 'gt', 'Ka/Ka+': 'ka%2Fka+', 'Kuga': 'kuga', 'M': 'm', 'Maverick': 'maverick', 'Mercury': 'mercury', 
    'Mondeo': 'mondeo', 'Mustang': 'mustang', 'Mustang Mach-E': 'mustang-mach-e', 'Oreon': 'oreon', 'Prob': 'prob', 
    'Puma': 'puma', 'Ranger (tous)': 'ranger-(tous)', 'Ranger': 'ranger', 'Ranger Raptor': 'ranger-raptor', 'RS 200': 'rs-200', 
    'S-Max': 's-max', 'Scorpio': 'scorpio', 'Sierra': 'sierra', 'Sportka': 'sportka', 'Streetka': 'streetka', 
    'Taunus': 'taunus', 'Taurus': 'taurus', 'Thunderbird': 'thunderbird', 'Torino': 'torino', 'Tourneo (tous)': 'tourneo-(tous)', 
    'Tourneo': 'tourneo', 'Tourneo Connect': 'tourneo-connect', 'Tourneo Courier': 'tourneo-courier', 'Tourneo Custom': 'tourneo-custom', 
    'Transit (tous)': 'transit-(tous)', 'E-Transit': 'e-transit', 'Transit': 'transit', 'Transit Bus': 'transit-bus', 
    'Transit Connect': 'transit-connect', 'Transit Courier': 'transit-courier', 'Transit Custom': 'transit-custom', 'Windstar': 'windstar', 
    'Autres': 'autres'
},



'mercedes-benz' : {
    '170': '170', '180': '180', '190': '190', '200': '200', '208': '208', '210/310': '210-310',
    '220': '220', '230': '230', '240': '240', '250': '250', '260': '260', '270': '270', '280': '280',
    '300': '300', '308': '308', '320': '320', '350': '350', '416': '416', '420': '420', '450': '450',
    '500': '500', '560': '560', '600': '600', 'Actros': 'actros', 'AMG GT': 'amg-gt', 'Atego': 'atego',
    'CE (tous)': 'ce-(tous)', 'CE 200': 'ce-200', 'CE 220': 'ce-220', 'CE 230': 'ce-230', 'CE 280': 'ce-280', 'CE 300': 'ce-300',
    'Citan': 'citan', 'CL 160': 'cl-160', 'CL 180': 'cl-180', 'CL 200': 'cl-200', 'CL 220': 'cl-220', 'CL 230': 'cl-230', 'CL 320': 'cl-320',
    'CL 420': 'cl-420', 'CL 500': 'cl-500', 'CL 55 AMG': 'cl-55-amg', 'CL 600': 'cl-600', 'CL 63 AMG': 'cl-63-amg', 'CL 65 AMG': 'cl-65-amg',
    'CLA (tous)': 'cla-(tous)', 'CLA 180': 'cla-180', 'CLA 200': 'cla-200', 'CLA 220': 'cla-220', 'CLA 250': 'cla-250', 'CLA 35 AMG': 'cla-35-amg',
    'CLA 45 AMG': 'cla-45-amg', 'Classe A(tous)': 'classe-a-(tous)', 'A 150': 'a-150', 'A 160': 'a-160', 'A 170': 'a-170', 'A 180': 'a-180', 'A 190': 'a-190',
    'A 200': 'a-200', 'A 210': 'a-210', 'A 220': 'a-220', 'A 250': 'a-250', 'A 35 AMG': 'a-35-amg', 'A 45 AMG': 'a-45-amg', 'Classe B (tous)': 'classe-b-(tous)',
    'B 150': 'b-150', 'B 160': 'b-160', 'B 170': 'b-170', 'B 180': 'b-180', 'B 200': 'b-200', 'B 220': 'b-220', 'B 250': 'b-250', 'B Electric Drive': 'b-electric-drive',
    'Classe C (tous)': 'classe-c-(tous)', 'C 180': 'c-180', 'C 200': 'c-200', 'C 220': 'c-220', 'C 230': 'c-230', 'C 240': 'c-240', 'C 250': 'c-250', 'C 270': 'c-270',
    'C 280': 'c-280', 'C 300': 'c-300', 'C 32 AMG': 'c-32-amg', 'C 320': 'c-320', 'C 350': 'c-350', 'C 36 AMG': 'c-36-amg', 'C 400': 'c-400', 'C 43 AMG': 'c-43-amg',
    'C 450': 'c-450', 'C 55 AMG': 'c-55-amg', 'C 63 AMG': 'c-63-amg', 'Classe E (tous)': 'classe-e-(tous)', 'E 200': 'e-200', 'E 220': 'e-220', 'E 230': 'e-230', 'E 240': 'e-240',
    'E 250': 'e-250',    'E 260': 'e-260', 'E 270': 'e-270', 'E 280': 'e-280', 'E 290': 'e-290', 'E 300': 'e-300', 'E 320': 'e-320',
    'E 350': 'e-350', 'E 36 AMG': 'e-36-amg', 'E 400': 'e-400', 'E 420': 'e-420', 'E 43 AMG': 'e-43-amg',
    'E 430': 'e-430', 'E 450': 'e-450', 'E 50 AMG': 'e-50-amg', 'E 500': 'e-500', 'E 53 AMG': 'e-53-amg',
    'E 55 AMG': 'e-55-amg', 'E 550': 'e-550', 'F 60 AMG': 'f-60-amg', 'E 63 AMG': 'e-63-amg',
    'Classe EQ(tous)': 'classe-eq-(tous)', 'EQA': 'eqa', 'EQA 250': 'eqa-250', 'EQA 300': 'eqa-300', 'EQA 350': 'eqa-350',
    'EQB 250': 'eqb-250', 'EQB 300': 'eqb-300', 'EQB 350': 'eqb-350', 'EQC 400': 'eqc-400',
    'EQE 300': 'eqe-300', 'EQE 350': 'eqe-350', 'EQE 43': 'eqe-43', 'EQE 500': 'eqe-500', 'EQE 53': 'eqe-53',
    'EQE SUV': 'eqe-suv', 'EQS': 'eqs', 'FOS SUV': 'fos-suv', 'EQS SUV': 'eqs-suv', 'EQT': 'eqt',
    'EQV 250': 'eqv-250', 'EQV 300': 'eqv-300', 'Classe G(tous)': 'classe-g-(tous)', 'G': 'g',
    'G 230': 'g-230', 'G 240': 'g-240', 'G 250': 'g-250', 'G 270': 'g-270', 'G 280': 'g-280', 'G 290': 'g-290',
    'G 300': 'g-300', 'G 320': 'g-320', 'G 350': 'g-350', 'G 400': 'g-400', 'G 500': 'g-500', 'G 55 AMG': 'g-55-amg',
    'G 63 AMG': 'g-63-amg', 'G 65 AMG': 'g-65-amg', 'G 650': 'g-650', 'Classe M (tous)': 'classe-m-(tous)',
    'ML 230': 'ml-230', 'ML 250': 'ml-250', 'ML 270': 'ml-270', 'ML 280': 'ml-280', 'ML 300': 'ml-300',
    'ML 320': 'ml-320', 'ML 350': 'ml-350', 'ML 400': 'ml-400', 'ML 420': 'ml-420', 'ML 430': 'ml-430',
    'ML 450': 'ml-450', 'ML 500': 'ml-500', 'ML 55 AMG': 'ml-55-amg', 'ML 63 AMG': 'ml-63-amg',
    'Classe R(tous)': 'classe-r-(tous)', 'R 280': 'r-280', 'R 300': 'r-300', 'R 320': 'r-320', 'R 350': 'r-350',
    'R 500': 'r-500', 'R 63 AMG': 'r-63-amg', 'Classe S(tous)': 'classe-s-(tous)', 'S 250': 's-250', 'S 260': 's-260',
    'S 280': 's-280', 'S 300': 's-300', 'S 320': 's-320', 'S 350': 's-350', 'S 380': 's-380', 'S 400': 's-400',
    'S 420': 's-420', 'S 430': 's-430', 'S 450': 's-450', 'S 500': 's-500', 'S 55 AMG': 's-55-amg',
    'S 550': 's-550', 'S 560': 's-560', 'S 560 E': 's-560-e', 'S 580': 's-580', 'S 600': 's-600',
    'S 63 AMG': 's-63-amg', 'S 65 AMG': 's-65-amg', 'S 650': 's-650', 'S 680': 's-680', 'Classe T': 'classe-t',
    'Classe V (tous)': 'classe-v-(tous)', 'V': 'v', 'V 200': 'v-200', 'V 220': 'v-220', 'V 230': 'v-230',
    'V 250': 'v-250', 'V 280': 'v-280', 'V 300': 'v-300', 'Classe X (tous)': 'classe-x-(tous)', 'X 220': 'x-220',
    'X 250': 'x-250', 'X 350': 'x-350', 'CLC': 'clc', 'CLE': 'cle', 'CLE 200': 'cle-200', 'CLE 220': 'cle-220',
    'CLE 300': 'cle-300', 'CLE 450': 'cle-450', 'CLE 53 AMG': 'cle-53-amg', 'CLK (tous)': 'clk-(tous)',
    'CLK': 'clk', 'CLK 200': 'clk-200', 'CLK 220': 'clk-220', 'CLK 230': 'clk-230', 'CLK 240': 'clk-240',
    'CLK 270': 'clk-270', 'CLK 280': 'clk-280', 'CLK 320': 'clk-320', 'CLK 350': 'clk-350', 'CLK 430': 'clk-430',
    'CLK 500': 'clk-500', 'CLK 55 AMG': 'clk-55-amg', 'CLK 63 AMG': 'clk-63-amg', 'CLS(tous)': 'cls-(tous)',
    'CLS': 'cls', 'CLS 220': 'cls-220', 'CLS 250': 'cls-250', 'CLS 280': 'cls-280', 'CLS 300': 'cls-300',
    'CLS 320': 'cls-320', 'CLS 350': 'cls-350', 'CLS 400': 'cls-400', 'CLS 450': 'cls-450', 'CLS 500': 'cls-500',
    'CLS 53 AMG': 'cls-53-amg', 'CLS 55 AMG': 'cls-55-amg', 'CLS 63 AMG': 'cls-63-amg', 'GL (tous)': 'gl-(tous)',
    'GL 320': 'gl-320', 'GL 350': 'gl-350', 'GL 400': 'gl-400', 'GL 420': 'gl-420', 'GL 450': 'gl-450',
    'GL 500': 'gl-500', 'GL 55 AMG': 'gl-55-amg', 'GL 63 AMG': 'gl-63-amg', 'GLA (tous)': 'gla-(tous)',
    'GLA 180': 'gla-180', 'GLA 200': 'gla-200', 'GLA 220': 'gla-220', 'GLA 250': 'gla-250', 'GLA 35 AMG': 'gla-35-amg',
    'GLA 45 AMG': 'gla-45-amg', 'GLB (tous)': 'glb-(tous)', 'GLB 180': 'glb-180', 'GLB 200': 'glb-200',
    'GLB 220': 'glb-220', 'GLB 250': 'glb-250', 'GLB 35 AMG': 'glb-35-amg', 'GLC(tous)': 'glc-(tous)',
    'GLC 200': 'glc-200', 'GLC 220': 'glc-220', 'GLC 250': 'glc-250', 'GLC 300': 'glc-300', 'GLC 350': 'glc-350',
    'GLC 400': 'glc-400', 'GLC 43 AMG': 'glc-43-amg', 'GLC 450': 'glc-450', 'GLC 63 AMG': 'glc-63-amg',
    'GLE (tous)': 'gle-(tous)', 'GLE 250': 'gle-250', 'GLE 300': 'gle-300', 'GLE 350': 'gle-350', 'GLE 400': 'gle-400',
    'GLE 43 AMG': 'gle-43-amg', 'GLE 450': 'gle-450', 'GLE 500': 'gle-500', 'GLE 53 AMG': 'gle-53-amg',
    'GLE 580': 'gle-580', 'GLE 63 AMG': 'gle-63-amg', 'GLK (tous)': 'glk-(tous)', 'GLK 200': 'glk-200',
    'GLK 220': 'glk-220', 'GLK 250': 'glk-250', 'GLK 280': 'glk-280', 'GLK 300': 'glk-300', 'GLK 320': 'glk-320',
    'GLK 350': 'glk-350', 'GLS (tous)': 'gls-(tous)', 'GLS 350': 'gls-350', 'GLS 400': 'gls-400', 'GLS 450': 'gls-450',
    'GLS 500': 'gls-500', 'GLS 580': 'gls-580', 'GLS 600': 'gls-600', 'GLS 63 AMG': 'gls-63-amg', 'Marco Polo': 'marco-polo',
    'Maybach GLS': 'maybach-gls', 'Maybach S-Klasse': 'maybach-s-klasse', 'MB 100': 'mb-100', 'SL(tous)': 'sl-(tous)',
    'SL 230': 'sl-230', 'SL 250': 'sl-250', 'SL 280': 'sl-280', 'SL 300': 'sl-300', 'SL 320': 'sl-320',
    'SL 350': 'sl-350', 'SL 380': 'sl-380', 'SL 400': 'sl-400', 'SL 420': 'sl-420', 'SL 43 AMG': 'sl-43-amg',
    'SL 450': 'sl-450', 'SL 500': 'sl-500', 'SL 55 AMG': 'sl-55-amg', 'SL 560': 'sl-560', 'SL 60 AMG': 'sl-60-amg',
    'SL 600': 'sl-600', 'SL 63 AMG': 'sl-63-amg', 'SL 65 AMG': 'sl-65-amg', 'SL 70 AMG': 'sl-70-amg', 'SL 73 AMG': 'sl-73-amg',
    'SLC (tous)': 'slc-(tous)', 'SLC 180': 'slc-180', 'SLC 200': 'slc-200', 'SLC 250': 'slc-250', 'SLC 280': 'slc-280',
    'SLC 300': 'slc-300', 'SLC 350': 'slc-350', 'SLC 380': 'slc-380', 'SLC 43 AMG': 'slc-43-amg', 'SLC 450': 'slc-450',
    'SLC 500': 'slc-500', 'SLK (tous)': 'slk-(tous)', 'SLK': 'slk', 'SLK 200': 'slk-200', 'SLK 230': 'slk-230',
    'SLK 250': 'slk-250', 'SLK 280': 'slk-280', 'SLK 300': 'slk-300', 'SLK 32 AMG': 'slk-32-amg', 'SLK 320': 'slk-320',
    'SLK 350': 'slk-350', 'SLK 55 AMG': 'slk-55-amg', 'SLR': 'slr', 'SLS': 'sls', 'Sprinter': 'sprinter',
    'T1': 't-1', 'T2': 't-2', 'Vaneo': 'vaneo', 'Vario': 'vario', 'Viano': 'viano', 'Vito': 'vito',
    'W 114/115 Strich-Acht': 'w-114-115-strich-acht', 'Autres': 'autres'

},



'opel' : {
    'Ampera': 'ampera', 'Ampera-E': 'ampera-e', 'Antara': 'antara', 'Arena': 'arena', 'Ascona': 'ascona',
    'Astra': 'astra', 'Calibra': 'calibra', 'Campo': 'campo', 'Cascada': 'cascada', 'Combo': 'combo',
    'Combo Life': 'combo-life', 'Combo-e': 'combo-e', 'Combo-e Life': 'combo-e-life', 'Commodore': 'commodore',
    'Corsa': 'corsa', 'Corsa-e': 'corsa-e', 'Crossland': 'crossland', 'Crossland X': 'crossland-x',
    'Diplomat': 'diplomat', 'Frontera': 'frontera', 'Grandland': 'grandland', 'Grandland X': 'grandland-x',
    'GT': 'gt', 'Insignia': 'insignia', 'Kadett': 'kadett', 'Karl': 'karl', 'Manta': 'manta', 'Meriva': 'meriva',
    'Mokka': 'mokka', 'Mokka X': 'mokka-x', 'Mokka-E': 'mokka-e', 'Monterey': 'monterey', 'Monza': 'monza',
    'Movano': 'movano', 'Movano-e': 'movano-e', 'Omega': 'omega', 'Pick Up Sportscap': 'pick-up-sportscap',
    'Rekord': 'rekord', 'Rocks-e': 'rocks-e', 'Senator': 'senator', 'Signum': 'signum', 'Sintra': 'sintra',
    'Speedster': 'speedster', 'Tigra': 'tigra', 'Vectra': 'vectra', 'Vivaro': 'vivaro', 'Vivaro-e': 'vivaro-e',
    'Zafira': 'zafira', 'Zafira Life': 'zafira-life', 'Zafira Tourer': 'zafira-tourer', 'Autres': 'autres'
},




'volkswagen' : {
    '181': '181', 'Amarok': 'amarok', 'Anfibio': 'anfibio', 'Arteon': 'arteon', 'Atlas': 'atlas',
    'Beetle': 'beetle', 'Bora': 'bora', 'Buggy': 'buggy', 'Bus': 'bus', 'Caddy': 'caddy',
    'CC': 'cc', 'Coccinelle': 'coccinelle', 'Corrado': 'corrado', 'Crafter': 'crafter', 'Cross Touran': 'cross-touran',
    'Derby': 'derby', 'Eos': 'eos', 'Escarabajo': 'escarabajo', 'Fox': 'fox', 'Golf(tous)': 'golf-(tous)',
    'Cross Golf': 'cross-golf', 'e-Golf': 'e-golf', 'Golf': 'golf', 'Golf Cabriolet': 'golf-cabriolet', 'Golf GTD': 'golf-gtd',
    'Golf GTE': 'golf-gte', 'Golf GTI': 'golf-gti', 'Golf Plus': 'golf-plus', 'Golf R': 'golf-r', 'Golf Sportsvan': 'golf-sportsvan',
    'Golf Variant': 'golf-variant',
      'Grand California': 'grand-california',
     'ID.Buzz (tous)': 'id.-buzz-(tous)', 'ID Buzz': 'id.-buzz',
    'ID.Buzz Cargo': 'id.-buzz-cargo', 'ID.3': 'id.3', 'ID.4': 'id.4', 'ID.5': 'id.5', 'ID.6': 'id.6', 'ID.7': 'id.7',
    'lltis': 'lltis', 'Jetta': 'jetta', 'Käfer': 'käfer', 'Karmann Ghia': 'karmann-ghia', 'Kever': 'kever',
    'L80': 'l80', 'LT': 'lt', 'Lupo': 'lupo', 'Maggiolino': 'maggiolino', 'New Beetle': 'new-beetle',
    'Passat (tous)': 'passat-(tous)', 'Passat': 'passat', 'Passat Alltrack': 'passat-alltrack', 'Passat CC': 'passat-cc',
    'Passat Variant': 'passat-variant', 'Phaeton': 'phaeton', 
    'Pointer': 'pointer', 'Polo (tous)': 'polo-(tous)',
    'Polo': 'polo', 'Polo Cross': 'polo-cross', 'Polo GTI': 'polo-gti', 'Polo Plus': 'polo-plus', 'Polo R WRC': 'polo-r-wrc',
    'Polo Sedan': 'polo-sedan', 'Polo Variant': 'polo-variant', 'Routan': 'routan', 'Santana': 'santana', 'Scirocco': 'scirocco',
    'Sharan': 'sharan', 'T-Cross': 't-cross', 'T-Roc': 't-roc', 'T1': 't1', 'T2': 't2', 'T3 (tous)': 't3-(tous)',
    'T3': 't3', 'T3 Blue Star': 't3-blue-star', 'T3 California': 't3-california', 'T3 Caravelle': 't3-caravelle',
    'T3 Kombi': 't3-kombi', 'T3 Multivan': 't3-multivan', 'T3 White Star': 't3-white-star', 'T4(tous)': 't4-(tous)',
    'T4': 't4', 'T4 Allstar': 't4-allstar', 'T4 California': 't4-california', 'T4 Caravelle': 't4-caravelle', 'T4 Kombi': 't4-kombi',
    'T4 Multivan': 't4-multivan', 'T5 (tous)': 't5-(tous)', 'T5': 't5', 'T5 California': 't5-california',
    'T5 Caravelle': 't5-caravelle', 'T5 Kombi': 't5-kombi', 'T5 Multivan': 't5-multivan', 'T5 Shuttle': 't5-shuttle',
    'T5 Transporter': 't5-transporter', 'T6 (tous)': 't6-(tous)', 'T6 California': 't6-california', 'T6 Caravelle': 't6-caravelle',
    'T6 Kombi': 't6-kombi', 'T6 Multivan': 't6-multivan', 'T6 Transporter': 't6-transporter', '6.1': '6-1',
    'T6.1 California': 't6-1-california', 'T6.1 Caravelle': 't6-1-caravelle', 'T6.1 Kombi': 't6-1-kombi', 'T6.1 Multivan': 't6-1-multivan',
    'T6.1 Transporter': 't6-1-transporter', 'T7 Multivan': 't7-multivan', 'Taigo': 'taigo', 'Taro': 'taro',
    'Tiguan (tous)': 'tiguan-(tous)', 'Tiguan': 'tiguan', 'Tiguan Allspace': 'tiguan-allspace', 'Touareg': 'touareg',
    'Touran': 'touran', 'Transporter': 'transporter', 'up!': 'up', 'Vento': 'vento', 'Viloran': 'viloran',
    'XL1': 'xl1', 'Autres': 'autres'
}
,


'renault':{
  'Alaskan':'alaskan', 'Alpine A110':'alpine-a110', 'Alpine A310':'alpine-a310', 'Alpine A610':'alpine-a610', 'Alpine V6':'alpine-v6', 'Arkana':'arkana', 'Austral':'austral', 'Avantime':'avantime', 'Captur':'captur', 'Clio':'clio', 'Coupe':'coupe', 'Duster':'duster', 'Espace':'espace', 'Express':'express', 'Fluence':'fluence',
    'Fluence Z.E.':'fluence-z.e.', 'Fuego':'fuego', 'Grand Espace':'grand-espace', 'Grand Modus':'grand-modus', 'Grand Scenic':'grand-scenic', 'Kadjar':'kadjar', 'Kangoo':'kangoo', 'Kangoo E-TECH':'kangoo-e-tech', 'Kangoo Z.E.':'kangoo-z.e.', 'Koleos':'koleos', 'Laguna':'laguna', 'Latitude':'latitude', 'Logan':'logan', 'Mascott':'mascott', 'Master':'master',
    'Megane':'megane', 'Megane E-Tech':'megane-e-tech', 'Messenger':'messenger', 'Modus':'modus', 'P 1400':'p-1400', 'R 11':'r-11', 'R 14':'r-14', 'R 18':'r-18', 'R 19':'r-19', 'R 20':'r-20', 'R 21':'r-21', 'R 25':'r-25', 'R 30':'r-30', 'R4':'r-4', 'R5':'r-5',
    'R6':'r-6', 'R9':'r-9', 'Rafale':'rafale', 'Rapid':'rapid', 'Safrane':'safrane', 'Sandero':'sandero', 'Sandero Stepway':'sandero-stepway', 'Scenic':'scenic', 'Spider':'spider', 'Super 5':'super-5', 'Symbol':'symbol', 'Talisman':'talisman', 'Trafic':'trafic', 'Twingo':'twingo', 'Twizy':'twizy',
    'Vel Satis':'vel-satis', 'Wind':'Wind', 'ZOE':'zoe', 'Autres':'autres'
},

'honda':{
    'Accord':'accord', 'Ascot':'ascot', 'Avancier':'avancier', 'Beat':'beat', 'Capa':'capa', 'City':'city', 'Civic':'civic', 'Clarity':'clarity', 'Concerto':'concerto', 'CR-V':'cr-v', 'CR-Z':'cr-z', 'Crosstour':'crosstour', 'CRX':'crx', 'e':'e', 'e:Ny1':'e%3Any',
    'Element':'element', 'Fit':'fit', 'FR-V':'fr-v', 'HR-V':'hr-v', 'Insight':'insight', 'Inspire':'inspire', 'Integra':'integra', 'Jazz':'jazz', 'Legend':'legend', 'Life':'life', 'Logo':'logo', 'Mobilio':'mobilio', 'NSX':'nsx', 'Odyssey':'odyssey', 'Orthia':'orthia',
    'Partner':'partner', 'Pilot':'pilot', 'Prelude':'prelude', 'Quintet':'quintet', 'Ridgeline':'ridgeline', 'S 2000':'s-2000', 'Saber':'saber', 'Sabre':'sabre', 'Shuttle':'shuttle', 'Sm-x':'sm-x', 'Stepwgn':'stepwgn', 'Stream':'stream', 'Torneo':'torneo', 'ZR-V':'zr-v', 'Autres':'autres'
},

'hummer':{'H1':'h1','H2':'h2','H3':'h3','Autres':'autres'},

'hyundai':{
 'ACCENT':'accent', 'Atos':'atos', 'AVENTE':'avente', 'AZERA':'azera', 'BAYON':'bayon', 'Coupe':'coupe', 'CRETA':'creta', 'ELANTRA':'elantra', 'Equus':'equus', 'Excel':'excel', 'Galloper':'galloper', 'Genesis':'genesis', 'Genesis Coupe':'genesis-coupe', 'Getz':'getz', 'Grace':'grace',
    'Grand Santa Fe':'grand-santa-fe', 'GRANDEUR':'grandeur', 'H 100':'h-100', 'H 200':'h-200', 'H 300':'h-300', 'H 350':'h-350', 'H-1':'h-1', 'Highway':'highway', 'i10':'i10', 'i20':'i20', 'i30':'i30', 'i40':'i40', 'i50':'i50', 'i800':'i800', 'IONIQ':'ioniq',
    'IONIQ 5':'ioniq-5', 'IONIQ 6':'ioniq-6', 'iX20':'ix20', 'iX35':'ix35', 'iX55':'ix55', 'KONA':'kona', 'Lantra':'lantra', 'Matrix':'matrix', 'NEXO':'nexo', 'NF':'nf', 'PALISADE':'palisade', 'Pony':'pony', 'Porter':'porter', 'S-Coupe':'s-coupe', 'SANTA FE':'santa-fe',
    'Santamo':'santamo', 'Satellite':'satellite', 'Solaris':'solaris', 'SONATA':'sonata', 'Sonica':'sonica', 'Starex':'starex', 'STARIA':'staria', 'Stellar':'stellar', 'Terracan':'terracan', 'Tiburon':'tiburon', 'Trajet':'trajet', 'TUCSON':'tucson', 'VELOSTER':'veloster', 'Veracruz':'veracruz', 'Verna':'verna',
    'XG 250':'xg-250', 'XG 30':'xg-30', 'XG 350':'xg-350', 'Autres':'autres'
},

'kia':{
    'Besta': 'besta', 'Carens': 'carens', 'Carnival': 'carnival', "Ceed/ cee'd": "ceed-cee'd", "Ceed SW / cee'd SW": "ceed-sw-cee'd-sw", 
    'Cerato': 'cerato', 'Clarus': 'clarus', 'e-Niro': 'e-niro', 'Elan': 'elan', 'EV6': 'ev6', 'EV9': 'ev9', 'Joice': 'joice', 
    'K2500': 'k2500', 'K2700': 'k2700', 'K2900': 'k2900', 'Leo': 'leo', 'Magentis': 'magentis', 'Mentor': 'mentor', 'Mohave/Borrego': 'mohave-borrego', 
    'Niro': 'niro', 'Opirus': 'opirus', 'Optima': 'optima', 'Picanto': 'picanto', 'Pregio': 'pregio', 'Pride': 'pride', "ProCeed / pro_cee'd": "proceed-pro-cee'd", 
    'Retona': 'retona', 'Rio': 'rio', 'Roadster': 'roadster', 'Rocsta': 'rocsta', 'Sephia': 'sephia', 'Shuma': 'shuma', 'Sorento': 'sorento', 
    'Soul': 'soul', 'Spectra': 'spectra', 'Sportage': 'sportage', 'Stinger': 'stinger', 'Stonic': 'stonic', 'Venga': 'venga', 'XCeed': 'xceed', 'Autres': 'autres'
},

'land-rover':{
    'Defender': 'defender', 'Discovery': 'discovery', 'Discovery Sport': 'discovery-sport', 'Freelander': 'freelander', 'LRX': 'lrx', 
    'Range Rover': 'range-rover', 'Range Rover Evoque': 'range-rover-evoque', 'Range Rover Sport': 'range-rover-sport', 'Range Rover Velar': 'range-rover-velar', 
    'Series': 'series', 'Autres': 'autres'
},

'lexus':{
    'CT 200h': 'ct-200h', 'ES (tous)': 'es-tous', 'ES 300': 'es-300', 'ES 330': 'es-330', 'ES 350': 'es-350', 
    'GS (tous)': 'gs-tous', 'GS 200t': 'gs-200t', 'GS 250': 'gs-250', 'GS 300': 'gs-300', 'GS 350': 'gs-350', 
    'GS 430': 'gs-430', 'GS 450h': 'gs-450h', 'GS 460': 'gs-460', 'GS F': 'gs-f', 'GX (tous)': 'gx-tous', 
    'GX460': 'gx460', 'GX470': 'gx470', 'IS (tous)': 'is-tous', 'IS 200': 'is-200', 'IS 220d': 'is-220d', 
    'IS 250': 'is-250', 'IS 3.00': 'is-3.00', 'IS 350': 'is-350', 'IS F': 'is-f', 'LBX': 'lbx', 
    'LC (tous)': 'lc-tous', 'LC 500': 'lc-500', 'LC 500h': 'lc-500h', 'LC F': 'lc-f', 'LFA': 'lfa', 
    'LS (tous)': 'ls-tous', 'LS 400': 'ls-400', 'LS 430': 'ls-430', 'LS 460': 'ls-460', 'LS 500': 'ls-500', 
    'LS 600': 'ls-600', 'LX (tous)': 'lx-tous', 'LX 450d': 'lx-450d', 'LX.470': 'lx-470', 'LX 500d': 'lx-500d', 
    'LX 570': 'lx-570', 'LX 600': 'lx-600', 'NX (tous)': 'nx-tous', 'NX 200t': 'nx-200t', 'NX 300': 'nx-300', 
    'NX 300h': 'nx-300h', 'NX 350h': 'nx-350h', 'NX 450h+': 'nx-450h+', 'RC (tous)': 'rc-tous', 'RC 200t': 'rc-200t', 
    'RC 300h': 'rc-300h', 'RC 350': 'rc-350', 'RC F': 'rc-f', 'RX (tous)': 'rx-tous', 'RX 200t': 'rx-200t', 
    'RX 300': 'rx-300', 'RX 330': 'rx-330', 'RX 350': 'rx-350', 'RX 350h': 'rx-350h', 'RX 400': 'rx-400', 
    'RX 450h': 'rx-450h', 'RX 500h': 'rx-500h', 'RZ': 'rz', 'SC (tous)': 'sc-tous', 'SC 400': 'sc-400', 
    'SC 430': 'sc-430', 'UX (tous)': 'ux-tous', 'UX 200': 'ux-200', 'UX 250h': 'ux-250h', 'UX 300e': 'ux-300e', 
    'UX 300h': 'ux-300h', 'Autres': 'autres'
},

'mazda':{
    '121': '121', '2': '2', '3': '3', '323': '323', '5': '5', '6': '6', '626': '626', '929': '929', 
    'Atenza': 'atenza', 'Axela': 'axela', 'B Series': 'b-series', 'Bongo': 'bongo', 'BT-50': 'bt-50', 
    'Capella': 'capella', 'CX-3': 'cx-3', 'CX-30': 'cx-30', 'CX-5': 'cx-5', 'CX-60': 'cx-60', 
    'CX-7': 'cx-7', 'CX-80': 'cx-80', 'CX-9': 'cx-9', 'Demio': 'demio', 'E Series': 'e-series', 
    'Familia': 'familia', 'Millenia': 'millenia', 'MPV': 'mpv', 'MX-3': 'mx-3', 'MX-30': 'mx-30', 
    'MX-5': 'mx-5', 'MX-6': 'mx-6', 'Pick Up': 'pick-up', 'Premacy': 'premacy', 'Protege': 'protege', 
    'RX-7': 'rx-7', 'RX-8': 'rx-8', 'RX-9': 'rx-9', 'Tribute': 'tribute', 'Xedos': 'xedos', 'Autres': 'autres'
},

'mini':{
   
    "1000": "1000","1300": "1300","3/5 Portes": "3-5-portes","Cooper": "cooper","Cooper D": "cooper-d", "Cooper S": "cooper-s", "Cooper SD": "cooper-sd",
    "Cooper SE": "cooper-se", "John Cooper Works": "john-cooper-works","One": "one","One D": "one-d","Clubvan": "clubvan","Gamme Cabrio (tous)": "gamme-cabrio-(tous)",
     "Cooper Cabrio": "cooper-cabrio","Cooper D Cabrio": "cooper-d-cabrio","Cooper S Cabrio": "cooper-s-cabrio","Cooper SD Cabrio": "cooper-sd-cabrio", "John Cooper Works Cabrio": "john-cooper-works-cabrio",
    "One Cabrio": "one-cabrio","Gamme Clubman (tous)": "gamme-clubman-(tous)","Cooper Clubman": "cooper-clubman","Cooper D Clubman": "cooper-d-clubman","Cooper S Clubman": "cooper-s-clubman",
    "Cooper SD Clubman": "cooper-sd-clubman","John Cooper Works Clubman": "john-cooper-works-clubman","One Clubman": "one-clubman","One D Clubman": "one-d-clubman","Gamme Countryman (tous)": "gamme-countryman-(tous)",
   "Cooper Countryman": "cooper-countryman","Cooper D Countryman": "cooper-d-countryman","Cooper S Countryman": "cooper-s-countryman","Cooper SD Countryman": "cooper-sd-countryman",
    "Cooper SE Countryman": "cooper-se-countryman","John Cooper Works Countryman": "john-cooper-works-countryman","One Countryman": "one-countryman","uew/uno": "uew-uno",
    "Gamme Coupe (tous)": "gamme-coupe-(tous)", "Cooper Coupe": "cooper-coupe","Cooper D Coupe": "cooper-d-coupe","Cooper S Coupe": "cooper-s-coupe","Cooper SD Coupe": "cooper-sd-coupe",
   "John Cooper Works Coupe": "john-cooper-works-coupe","Gamme Paceman (tous)": "gamme-paceman-(tous)","Cooper D Paceman": "cooper-d-paceman","Cooper Paceman": "cooper-paceman", "Cooper S Paceman": "cooper-s-paceman",
    "Cooper SD Paceman": "cooper-sd-paceman","John Cooper Works Paceman": "john-cooper-works-paceman","Gamme Roadster (tous)": "gamme-roadster-(tous)","Cooper Roadster": "cooper-roadster", "Cooper S Roadster": "cooper-s-roadster",
    "Cooper SD Roadster": "cooper-sd-roadster","John Cooper Works Roadster": "john-cooper-works-roadster","Autres": "autres"
  
    },


'mitsubishi':{ "3000 GT": "3000-gt","400": "400","Airtrek": "airtrek","ASX": "asx","Attrage": "attrage", "Canter": "canter", "Carisma": "carisma",
    "Chariot": "chariot","Colt": "colt","Cordia": "cordia","Cosmos": "cosmos","Delica": "delica","Diamante": "diamante","DINGO": "dingo","Dion": "dion",
    "Eclipse": "eclipse","Eclipse Cross": "eclipse-cross", "FTO": "fto","Galant": "galant" ,   "Galloper": "galloper", "Grandis": "grandis","I-MiEV": "i-miev",
   "L200": "l200","L300": "l300","L400": "l400","Lancer": "lancer", "Legnum": "legnum", "Libero": "libero","Mirage": "mirage","Montero": "montero", "Outlander": "outlander",
    "Pajero": "pajero","Pajero Pinin": "pajero-pinin","Pajero Sport": "pajero-sport","PICK UP": "pick-up","RVR": "rvr", "Santamo": "santamo","Sapporo": "sapporo","Shogun": "shogun",
     "Sigma": "sigma", "Space Gear": "space-gear","Space Runner": "space-runner","Space Star": "space-star","Space Wagon": "space-wagon", "Starion": "starion", "Tredia": "tredia",
    "Autres": "autres"
    },


'nissan':{
      "100 NX": "100-nx", "200 SX": "200-sx", "280 ZX": "280-zx", "300 ZX": "300-zx", "350Z": "350z", "370Z": "370z", "AD": "ad",
    "Almera": "almera", "Almera Tino": "almera-tino", "Altima": "altima", "Ariya": "ariya", "Armada": "armada", "Avenir": "avenir", "Bassara": "bassara",
    "Bluebird": "bluebird", "Cabstar": "cabstar", "Cargo": "cargo", "Cedric": "cedric", "Cefiro": "cefiro", "Cherry": "cherry", "Cube": "cube",
    "Datsun": "datsun", "E-NV200": "e-nv200", "Elgrand": "elgrand", "Evalia": "evalia", "Expert": "expert", "Figaro": "figaro", "Frontier": "frontier",
    "Gloria": "gloria", "GT-R": "gt-r", "Interstar": "interstar", "Juke": "juke", "King Cab": "king-cab", "Kubistar": "kubistar", "Laurel": "laurel",
    "Leat": "leat", "Liberty": "liberty", "March": "march", "Maxima": "maxima", "Micra": "micra", "Murano": "murano", "Navara": "navara",
    "Note": "note", "NP300": "np300", "NV200": "nv200", "NV250": "nv250", "NV300": "nv300", "NV400": "nv400", "Pathfinder": "pathfinder",
    "Patrol": "patrol", "Pick Up": "pick-up", "Pixo": "pixo", "Prairie": "prairie", "Presage": "presage", "Presea": "presea", "Primastar": "primastar",
    "Primera": "primera", "Pulsar": "pulsar", "Qashqai": "qashqai", "Qashqai+2": "qashqai-plus-2", "Quest": "quest", "R Nessa": "r-nessa", "Rogue": "rogue",
    "Safari": "safari", "Sentra": "sentra", "Serena": "serena", "Silvia": "silvia", "Skyline": "skyline", "Stagea": "stagea", "Stanza": "stanza",
    "Sunny": "sunny", "Teana": "teana", "Terrano": "terrano", "Tiida": "tiida", "Titan": "titan", "Townstar": "townstar", "Townstar EV": "townstar-ev",
    "Trade": "trade", "Urvan": "urvan", "Vanette": "vanette", "Wingroad": "wingroad", "X-Trail": "x-trail", "Autres": "autres"

},


'peugeot':{
   
    "1007": "1007", "104": "104", "106": "106", "107": "107", "108": "108", "2008": "2008", "204": "204",
    "205": "205", "206": "206", "207": "207", "208": "208", "3008": "3008", "301": "301", "304": "304",
    "305": "305", "306": "306", "307": "307", "308": "308", "309": "309", "4007": "4007", "4008": "4008",
    "404": "404", "405": "405", "406": "406", "407": "407", "408": "408", "5008": "5008", "504": "504",
    "505": "505", "508": "508", "604": "604", "605": "605", "607": "607", "806": "806", "807": "807",
    "Bipper": "bipper", "Boxer": "boxer", "Camper": "camper", "e-2008": "e-2008", "e-208": "e-208", "e-Expert": "e-expert", "e-Rifter": "e-rifter",
    "Expert": "expert", "iOn": "ion", "J5": "j5", "J9": "j9", "Partner": "partner", "Ranch": "ranch", "RCZ": "rcz",
    "Rifter": "rifter", "Traveller": "traveller", "Autres": "autres"
},


'skoda':{
    "105": "105", "120": "120", "130": "130", "135": "135", "Citigo": "citigo", "Enyaq": "enyaq", "Fabia": "fabia",
    "Favorit": "favorit", "Felicia": "felicia", "Forman": "forman", "Kamiq": "kamiq", "Karoq": "karoq", "Kodiaq": "kodiaq",
    "Octavia": "octavia", "Pick-up": "pick-up", "Praktik": "praktik", "Rapid/Spaceback": "rapid-spaceback", "Roomster": "roomster", "Scala": "scala",
    "Snowman": "snowman", "Superb": "superb", "Yeti": "yeti", "Autres": "autres"
},


'suzuki': {
    "Across": "across", "Alto": "alto", "Baleno": "baleno", "Cappuccino": "cappuccino", "Carry": "carry", 
    "Celerio": "celerio", "Escudo": "escudo", "Grand Vitara": "grand-vitara", "Ignis": "ignis", "IK-2": "ik-2", 
    "Jimmy": "jimmy", "Kizashi": "kizashi", "Liana": "liana", "LJ 80": "lj-80", "Maruti": "maruti", 
    "S-Cross": "s-cross", "SA 310": "sa-310", "Samurai": "samurai", "Santana": "santana", "SJ 410": "sj-410", 
    "SJ 413": "sj-413", "SJ Samurai": "sj-samurai", "Splash": "splash", "Super-Carry": "super-carry", 
    "Swace": "swace", "Swift": "swift", "SX4": "sx4", "SX4 S-Cross": "sx4-s-cross", "Vitara": "vitara", 
    "Wagon R+": "wagon-r-plus", "X-90": "x-90", "XL-7": "xl-7", "Autres": "autres"
},

'tesla' : {
    "Cybertruck": "cybertruck", "Model 3": "model-3", "Model S": "model-s", "Model X": "model-x", 
    "Model Y": "model-y", "Autres": "autres"
},

'toyota' : {
    "4-Runner": "4-runner", "Allion": "allion", "Alphard": "alphard", "Altezza": "altezza", "Aristo": "aristo", 
    "Auris": "auris", "Avalon": "avalon", "Avensis": "avensis", "Avensis Verso": "avensis-verso", "Aygo": "aygo", 
    "Aygo X": "aygo-x", "BB": "bb", "Belta": "belta", "bZ4X": "bz4x", "C-HR": "c-hr", "Caldina": "caldina", 
    "Cami": "cami", "Camry": "camry", "Carina": "carina", "Celica": "celica", "Chaser": "chaser", 
    "Coaster": "coaster", "Corolla": "corolla", "Corolla Cross": "corolla-cross", "Corolla Verso": "corolla-verso", 
    "Corona": "corona", "Corsa": "corsa", "Cressida": "cressida", "Cresta": "cresta", "Crown": "crown", 
    "Duet": "duet", "Dyna": "dyna", "Estima": "estima", "FJ Cruiser": "fj-cruiser", "FJ40": "fj40", 
    "Fortuner": "fortuner", "Fun Cruiser": "fun-cruiser", "Funcargo": "funcargo", "Gaia": "gaia", "GR86": "gr86", 
    "GT86": "gt86", "Harrier": "harrier", "HDJ": "hdj", "Hiace": "hiace", "Highlander": "highlander", 
    "Hilux": "hilux", "Ipsum": "ipsum", "iQ": "iq", "Ist": "ist", "KJ": "kj", 
    "Land Cruiser": "land-cruiser", "Land Cruiser Prado": "land-cruiser-prado", "Lite-Ace": "lite-ace", 
    "Mark II": "mark-ii", "Mark X": "mark-x", "Matrix": "matrix", "Mirai": "mirai", "Model F": "model-f", 
    "MR 2": "mr-2", "Nadia": "nadia", "Noah": "noah", "Opa": "opa", "Paseo": "paseo", 
    "Passo": "passo", "Pick up": "pick-up", "Picnic": "picnic", "Platz": "platz", "Premio": "premio", 
    "Previa": "previa", "Prius": "prius", "Prius+": "prius-plus", "Proace": "proace", "Proace City": "proace-city", 
    "Ractis": "ractis", "Raum": "raum", "RAV 4": "rav-4", "Sequoia": "sequoia", "Sienna": "sienna", 
    "Solara": "solara", "Sprinter": "sprinter", "Starlet": "starlet", "Supra": "supra", "Tacoma": "tacoma", 
    "Tercel": "tercel", "Town Ace": "town-ace", "Tundra": "tundra", "Urban Cruiser": "urban-cruiser", 
    "Venza": "venza", "Verossa": "verossa", "Verso": "verso", "Verso-S": "verso-s", "Vista": "vista", 
    "Vitz": "vitz", "Voxy": "voxy", "Will": "will", "Windom": "windom", "Wish": "wish", 
    "Yaris": "yaris", "Yaris Cross": "yaris-cross", "Autres": "autres"
},

'volvo' : {
    "240": "240", "244": "244", "245": "245", "262": "262", "264": "264", 
    "265": "265", "340": "340", "360": "360", "440": "440", "460": "460", 
    "480": "480", "740": "740", "744": "744", "745": "745", "760": "760", 
    "764": "764", "780": "780", "850": "850", "855": "855", "940": "940", 
    "944": "944", "945": "945", "960": "960", "965": "965", "Amazon": "amazon", 
    "C30": "c30", "C40": "c40", "C70": "c70", "EC40": "ec40", "EX30": "ex30", 
    "EX40": "ex40", "EX90": "ex90", "P1800": "p1800", "Polar": "polar", "PV544": "pv544", 
    "S40": "s40", "S60": "s60", "S60 Cross Country": "s60-cross-country", "S70": "s70", 
    "S80": "s80", "S90": "s90", "V40": "v40", "V40 Cross Country": "v40-cross-country", 
    "V50": "v50", "V60": "v60", "V60 Cross Country": "v60-cross-country", "V70": "v70", 
    "V90": "v90", "V90 Cross Country": "v90-cross-country", "XC40": "xc40", "XC60": "xc60", 
    "XC70": "xc70", "XC90": "xc90", "Autres": "autres"
}






}



AllModels = [[i, j] for i in Auto_models.keys() for j in Auto_models[i].keys()]

# print(AllModels.index(['volkswagen','Grand California']))
print(len(AllModels))

# 0 * * * * /root/ScrappingApp/OasisScrapping/watchdog.sh

# IBM code 16c46d3d57abb704c543bc81b94a9704