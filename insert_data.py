from store.models import Product, ShoppingCart, ShoppingCartItem
from django.utils import timezone

data = [{
  "name": "Veal - Chops, Split, Frenched",
  "description": "Supplement Face Subcu/Fascia w Synth Sub, Perc",
  "price": 7877,
  "sale_start": "2022-02-15",
  "sale_end": "2021-12-12"
}, {
  "name": "Tea - Honey Green Tea",
  "description": "Revision of Infusion Dev in Hepatobil Duct, Extern Approach",
  "price": 32824,
  "sale_start": "2022-04-23",
  "sale_end": "2022-01-27"
}, {
  "name": "Cup - 3.5oz, Foam",
  "description": "Excision of Left Hypogastric Vein, Open Approach",
  "price": 44003,
  "sale_start": "2022-04-06",
  "sale_end": "2022-09-17"
}, {
  "name": "Pork - Sausage, Medium",
  "description": "Drainage of Right Shoulder Joint, Open Approach",
  "price": 16985,
  "sale_start": "2022-08-26",
  "sale_end": "2022-01-24"
}, {
  "name": "Pastry - Banana Muffin - Mini",
  "description": "Drainage of Left Nipple, External Approach",
  "price": 88503,
  "sale_start": "2022-01-18",
  "sale_end": "2022-09-01"
}, {
  "name": "Sugar - Crumb",
  "description": "Excision of Stomach, Percutaneous Endoscopic Approach, Vert",
  "price": 49599,
  "sale_start": "2022-11-14",
  "sale_end": "2021-12-06"
}, {
  "name": "Ice Cream - Chocolate",
  "description": "Irrigation of Nose using Irrigating Substance, Via Opening",
  "price": 47251,
  "sale_start": "2021-12-01",
  "sale_end": "2022-06-24"
}, {
  "name": "Chicken - Soup Base",
  "description": "Replacement of R Glenoid Cav with Autol Sub, Open Approach",
  "price": 31614,
  "sale_start": "2022-01-06",
  "sale_end": "2022-06-06"
}, {
  "name": "Wine - White, Chardonnay",
  "description": "Destruction of Lumbosacral Disc, Open Approach",
  "price": 32823,
  "sale_start": "2022-08-01",
  "sale_end": "2022-02-05"
}, {
  "name": "Rappini - Andy Boy",
  "description": "Removal of Radioact Elem from Pleura, Perc Endo Approach",
  "price": 41718,
  "sale_start": "2022-10-04",
  "sale_end": "2021-12-07"
}, {
  "name": "Muffin Batt - Carrot Spice",
  "description": "Hyperthermia of Pelvic Region",
  "price": 80697,
  "sale_start": "2022-05-03",
  "sale_end": "2022-10-08"
}, {
  "name": "Potatoes - Mini Red",
  "description": "Replace of L Knee Jt with Synth Sub, Uncement, Open Approach",
  "price": 90285,
  "sale_start": "2022-02-05",
  "sale_end": "2022-10-24"
}, {
  "name": "Trout Rainbow Whole",
  "description": "Laser Interstitial Thermal Therapy of Jejunum",
  "price": 81751,
  "sale_start": "2022-03-22",
  "sale_end": "2022-06-22"
}, {
  "name": "Leeks - Baby, White",
  "description": "Fusion of R Metatarsophal Jt with Ext Fix, Perc Approach",
  "price": 39566,
  "sale_start": "2022-09-06",
  "sale_end": "2022-08-15"
}, {
  "name": "V8 Splash Strawberry Kiwi",
  "description": "Bypass Innom Art to R Low Leg Art w Nonaut Sub, Open",
  "price": 21070,
  "sale_start": "2022-10-04",
  "sale_end": "2022-03-15"
}, {
  "name": "Canada Dry",
  "description": "Bypass R Kidney Pelvis to Bladder w Nonaut Sub, Perc Endo",
  "price": 96905,
  "sale_start": "2022-10-27",
  "sale_end": "2022-11-07"
}, {
  "name": "Nantucket Orange Juice",
  "description": "Repair Head, Percutaneous Endoscopic Approach",
  "price": 53900,
  "sale_start": "2022-07-03",
  "sale_end": "2022-10-29"
}, {
  "name": "Dried Cranberries",
  "description": "Occlusion of Trachea with Intraluminal Device, Open Approach",
  "price": 15357,
  "sale_start": "2022-04-04",
  "sale_end": "2023-01-17"
}, {
  "name": "Mix - Cappucino Cocktail",
  "description": "Restriction of L Foot Vein with Intralum Dev, Open Approach",
  "price": 90258,
  "sale_start": "2022-01-25",
  "sale_end": "2022-02-07"
}, {
  "name": "Icecream - Dstk Cml And Fdg",
  "description": "Fluoroscopy of Left Vertebral Artery using L Osm Contrast",
  "price": 57176,
  "sale_start": "2023-01-09",
  "sale_end": "2023-01-07"
}, {
  "name": "The Pop Shoppe - Root Beer",
  "description": "Restriction of Head Lymph with Extralum Dev, Open Approach",
  "price": 79784,
  "sale_start": "2023-01-12",
  "sale_end": "2022-02-17"
}, {
  "name": "Sprouts - Baby Pea Tendrils",
  "description": "Supplement L Subclav Art with Autol Sub, Open Approach",
  "price": 78151,
  "sale_start": "2023-01-09",
  "sale_end": "2022-11-30"
}, {
  "name": "Soup - Knorr, Chicken Noodle",
  "description": "Release Left Ureter, Open Approach",
  "price": 47349,
  "sale_start": "2022-03-24",
  "sale_end": "2022-02-10"
}, {
  "name": "Southern Comfort",
  "description": "Replace Buttock Skin w Synth Sub, Part Thick, Extern",
  "price": 95211,
  "sale_start": "2022-04-06",
  "sale_end": "2022-12-15"
}, {
  "name": "Tea - Herbal - 6 Asst",
  "description": "Bypass Inf Mesent Vein to Low Vein w Autol Sub, Perc Endo",
  "price": 2016,
  "sale_start": "2022-10-18",
  "sale_end": "2022-06-17"
}, {
  "name": "Veal - Provimi Inside",
  "description": "Insertion of Spacer into R Metatarsotars Jt, Perc Approach",
  "price": 13276,
  "sale_start": "2022-05-15",
  "sale_end": "2022-12-28"
}, {
  "name": "Beans - Fava, Canned",
  "description": "Bypass L Brach Vein to Up Vein with Synth Sub, Open Approach",
  "price": 7912,
  "sale_start": "2022-04-30",
  "sale_end": "2021-12-30"
}, {
  "name": "Ice Cream - Life Savers",
  "description": "Dressing Assessment",
  "price": 7598,
  "sale_start": "2022-11-06",
  "sale_end": "2022-10-17"
}, {
  "name": "Lettuce - Boston Bib",
  "description": "Plain Radiography of Abdomen and Pelvis",
  "price": 23223,
  "sale_start": "2022-09-29",
  "sale_end": "2022-03-15"
}, {
  "name": "Bacon Strip Precooked",
  "description": "Drainage of L Com Iliac Art with Drain Dev, Perc Approach",
  "price": 15853,
  "sale_start": "2022-02-27",
  "sale_end": "2022-12-10"
}, {
  "name": "Crab - Meat Combo",
  "description": "Insertion of Infusion Dev into L Peroneal Art, Perc Approach",
  "price": 6387,
  "sale_start": "2022-12-18",
  "sale_end": "2022-04-27"
}, {
  "name": "Tea Peppermint",
  "description": "Occlusion of Right Popliteal Artery, Perc Endo Approach",
  "price": 49845,
  "sale_start": "2022-04-08",
  "sale_end": "2022-01-25"
}, {
  "name": "Aromat Spice / Seasoning",
  "description": "Removal of Bandage on Right Upper Arm",
  "price": 46354,
  "sale_start": "2022-01-14",
  "sale_end": "2022-04-29"
}, {
  "name": "Beef - Short Ribs",
  "description": "Repair Nasal Turbinate, Endo",
  "price": 70599,
  "sale_start": "2022-01-26",
  "sale_end": "2022-12-06"
}, {
  "name": "Cheese - Le Cru Du Clocher",
  "description": "Bypass Stomach to Cutaneous, Open Approach",
  "price": 37482,
  "sale_start": "2022-06-23",
  "sale_end": "2022-01-06"
}, {
  "name": "Mix - Cocktail Ice Cream",
  "description": "Dilate of L Ext Iliac Vein with Intralum Dev, Open Approach",
  "price": 90915,
  "sale_start": "2022-11-06",
  "sale_end": "2022-06-29"
}, {
  "name": "Soup - Campbells, Minestrone",
  "description": "Removal of Infusion Dev from R Acromioclav Jt, Open Approach",
  "price": 33229,
  "sale_start": "2022-04-11",
  "sale_end": "2021-12-04"
}, {
  "name": "Muffin Mix - Carrot",
  "description": "Supplement Nasal Septum with Nonaut Sub, Perc Endo Approach",
  "price": 38146,
  "sale_start": "2022-03-18",
  "sale_end": "2022-01-17"
}, {
  "name": "Bread - French Baquette",
  "description": "Extirpation of Matter from L Hand Art, Bifurc, Open Approach",
  "price": 11642,
  "sale_start": "2022-04-14",
  "sale_end": "2023-01-24"
}, {
  "name": "Cheese - Grana Padano",
  "description": "Sys Nucl Med Therapy of Thyroid using Iodine 131",
  "price": 55641,
  "sale_start": "2022-07-28",
  "sale_end": "2021-12-27"
}, {
  "name": "Onions - Red Pearl",
  "description": "Removal of Spacer from Left Ankle Joint, Open Approach",
  "price": 52121,
  "sale_start": "2022-02-24",
  "sale_end": "2022-10-21"
}, {
  "name": "Beer - Muskoka Cream Ale",
  "description": "Excision of R Low Leg Subcu/Fascia, Open Approach, Diagn",
  "price": 20293,
  "sale_start": "2022-09-07",
  "sale_end": "2022-03-30"
}, {
  "name": "Dasheen",
  "description": "Bypass R Ureter to R Ureter with Autol Sub, Open Approach",
  "price": 99402,
  "sale_start": "2022-09-24",
  "sale_end": "2022-10-07"
}, {
  "name": "Coffee Decaf Colombian",
  "description": "Restriction of Small Intest with Intralum Dev, Open Approach",
  "price": 42486,
  "sale_start": "2022-03-18",
  "sale_end": "2022-11-12"
}, {
  "name": "Propel Sport Drink",
  "description": "Replacement of Left Scapula with Synth Sub, Perc Approach",
  "price": 20810,
  "sale_start": "2022-01-26",
  "sale_end": "2022-08-24"
}, {
  "name": "Cilantro / Coriander - Fresh",
  "description": "Dilate L Post Tib Art w 2 Intralum Dev, Perc Endo",
  "price": 12924,
  "sale_start": "2022-02-05",
  "sale_end": "2022-06-06"
}, {
  "name": "Scallops - Live In Shell",
  "description": "Replace of R Metacarpal with Autol Sub, Perc Endo Approach",
  "price": 55196,
  "sale_start": "2022-10-09",
  "sale_end": "2021-12-05"
}, {
  "name": "Sauce - Black Current, Dry Mix",
  "description": "Destruction of Cul-de-sac, Open Approach",
  "price": 76959,
  "sale_start": "2022-09-28",
  "sale_end": "2022-04-02"
}, {
  "name": "Cream - 10%",
  "description": "Excision of Right Peroneal Artery, Percutaneous Approach",
  "price": 24754,
  "sale_start": "2021-12-19",
  "sale_end": "2022-03-03"
}, {
  "name": "Sauce - Chili",
  "description": "Insert Card Rsync Pace Puls Gen in Abd Subcu/Fascia, Perc",
  "price": 13166,
  "sale_start": "2022-09-15",
  "sale_end": "2022-08-28"
}, {
  "name": "Turkey - Breast, Double",
  "description": "Immobilization of Right Inguinal Region using Brace",
  "price": 59125,
  "sale_start": "2022-05-16",
  "sale_end": "2022-10-16"
}, {
  "name": "Apron",
  "description": "Removal of Nonaut Sub from Trachea, Perc Endo Approach",
  "price": 7311,
  "sale_start": "2022-11-21",
  "sale_end": "2022-12-21"
}, {
  "name": "Jolt Cola - Red Eye",
  "description": "Repair Left Brachial Vein, Open Approach",
  "price": 90913,
  "sale_start": "2022-08-27",
  "sale_end": "2022-11-14"
}, {
  "name": "Cloves - Whole",
  "description": "Control Bleeding in Right Femoral Region, Open Approach",
  "price": 76065,
  "sale_start": "2022-06-19",
  "sale_end": "2022-07-11"
}, {
  "name": "Carrots - Purple, Organic",
  "description": "Replacement of R Ulnar Art with Autol Sub, Open Approach",
  "price": 91185,
  "sale_start": "2022-09-12",
  "sale_end": "2022-06-28"
}, {
  "name": "Icecream - Dstk Cml And Fdg",
  "description": "Insertion of Monitor Dev into Abd Aorta, Perc Endo Approach",
  "price": 58763,
  "sale_start": "2022-08-19",
  "sale_end": "2023-01-20"
}, {
  "name": "Beef Striploin Aaa",
  "description": "Reposition L Low Femur with Hybrid Ext Fix, Open Approach",
  "price": 35819,
  "sale_start": "2022-11-09",
  "sale_end": "2023-01-05"
}, {
  "name": "Chocolate Bar - Oh Henry",
  "description": "Insertion of Int Fix into L Rib, Perc Endo Approach",
  "price": 99755,
  "sale_start": "2023-01-27",
  "sale_end": "2022-10-01"
}, {
  "name": "Wine - Hardys Bankside Shiraz",
  "description": "Revise Nonaut Sub in L Temporomandib Jt, Perc Endo",
  "price": 71558,
  "sale_start": "2022-02-28",
  "sale_end": "2022-09-07"
}, {
  "name": "Green Tea Refresher",
  "description": "Excision of R Foot Subcu/Fascia, Open Approach, Diagn",
  "price": 9344,
  "sale_start": "2022-12-19",
  "sale_end": "2022-01-18"
}, {
  "name": "Country Roll",
  "description": "Excision of Left Internal Iliac Artery, Open Approach",
  "price": 19846,
  "sale_start": "2022-02-10",
  "sale_end": "2021-12-31"
}, {
  "name": "Garlic - Elephant",
  "description": "Supplement R Low Leg Subcu/Fascia w Autol Sub, Open",
  "price": 44175,
  "sale_start": "2022-04-12",
  "sale_end": "2023-01-02"
}, {
  "name": "Pasta - Elbows, Macaroni, Dry",
  "description": "Meds Mgmt for Substance Abuse Treatment, Methadone Maint",
  "price": 51035,
  "sale_start": "2022-07-24",
  "sale_end": "2022-03-15"
}, {
  "name": "Chips Potato Swt Chilli Sour",
  "description": "Muscle Perform Assess Neuro Low Back/LE w Oth Equip",
  "price": 70033,
  "sale_start": "2022-05-18",
  "sale_end": "2022-12-06"
}, {
  "name": "Papadam",
  "description": "Planar Nucl Med Imag of Thorax using Technetium 99m",
  "price": 71767,
  "sale_start": "2022-10-05",
  "sale_end": "2022-08-13"
}, {
  "name": "Lamb - Leg, Boneless",
  "description": "Restrict of L Verteb Vein with Extralum Dev, Open Approach",
  "price": 53299,
  "sale_start": "2022-08-23",
  "sale_end": "2022-01-25"
}, {
  "name": "Toamtoes 6x7 Select",
  "description": "Destruction of Right Epididymis, Percutaneous Approach",
  "price": 67133,
  "sale_start": "2022-12-23",
  "sale_end": "2022-03-15"
}, {
  "name": "Kiwi",
  "description": "Stereotactic Particulate Radiosurgery of Soft Palate",
  "price": 71722,
  "sale_start": "2022-08-10",
  "sale_end": "2022-10-08"
}, {
  "name": "Vinegar - Sherry",
  "description": "Removal of Autol Sub from Low Tendon, Open Approach",
  "price": 34933,
  "sale_start": "2022-10-01",
  "sale_end": "2023-01-01"
}, {
  "name": "Bread - Pita",
  "description": "Supplement Abdominal Wall with Synth Sub, Open Approach",
  "price": 9933,
  "sale_start": "2022-10-18",
  "sale_end": "2022-03-05"
}, {
  "name": "Veal - Chops, Split, Frenched",
  "description": "Release Left Ureter, Percutaneous Approach",
  "price": 36833,
  "sale_start": "2022-04-29",
  "sale_end": "2022-11-01"
}, {
  "name": "Wine - Delicato Merlot",
  "description": "Bypass L Foot Vein to Low Vein with Autol Vn, Open Approach",
  "price": 20875,
  "sale_start": "2022-02-28",
  "sale_end": "2023-01-10"
}, {
  "name": "Nestea - Ice Tea, Diet",
  "description": "Revision of Drainage Device in Left Lung, Open Approach",
  "price": 33640,
  "sale_start": "2022-08-04",
  "sale_end": "2022-05-27"
}, {
  "name": "Cranberry Foccacia",
  "description": "Supplement R Kidney Pelvis w Nonaut Sub, Perc Endo",
  "price": 98106,
  "sale_start": "2022-10-09",
  "sale_end": "2022-12-03"
}, {
  "name": "Appetizer - Southwestern",
  "description": "ROM & Jt Mobility Trmt Neuro Body w Assist Equip",
  "price": 35841,
  "sale_start": "2021-12-24",
  "sale_end": "2022-10-01"
}, {
  "name": "Wine - Sawmill Creek Autumn",
  "description": "Supplement Tricuspid Valve with Zooplastic, Open Approach",
  "price": 79200,
  "sale_start": "2022-01-21",
  "sale_end": "2023-01-12"
}, {
  "name": "Soup - Campbells, Lentil",
  "description": "Restrict Thor Aorta Asc w Extralum Dev, Perc Endo",
  "price": 47123,
  "sale_start": "2022-11-29",
  "sale_end": "2021-12-25"
}, {
  "name": "Versatainer Nc - 888",
  "description": "Drainage of Left Upper Lobe Bronchus with Drain Dev, Endo",
  "price": 87458,
  "sale_start": "2022-10-12",
  "sale_end": "2022-07-16"
}, {
  "name": "Pate - Liver",
  "description": "CT Scan of Pancreas using L Osm Contrast, Unenh, Enhance",
  "price": 84876,
  "sale_start": "2021-12-03",
  "sale_end": "2022-08-18"
}, {
  "name": "Yams",
  "description": "Remove Tissue Expander from Up Extrem Subcu/Fascia, Open",
  "price": 55032,
  "sale_start": "2022-09-18",
  "sale_end": "2021-12-11"
}, {
  "name": "Bag - Regular Kraft 20 Lb",
  "description": "Fluoroscopy of Right Knee using High Osmolar Contrast",
  "price": 69024,
  "sale_start": "2022-03-15",
  "sale_end": "2022-08-10"
}, {
  "name": "Nantucket Pine Orangebanana",
  "description": "Removal of Int Fix from R Finger Phalanx, Perc Endo Approach",
  "price": 31105,
  "sale_start": "2021-12-30",
  "sale_end": "2022-07-20"
}, {
  "name": "Plate - Foam, Bread And Butter",
  "description": "Removal of Drainage Device from Thymus, External Approach",
  "price": 82667,
  "sale_start": "2022-04-19",
  "sale_end": "2022-02-13"
}, {
  "name": "Trout - Hot Smkd, Dbl Fillet",
  "description": "Dilation of L Hand Art with 2 Drug-elut, Perc Endo Approach",
  "price": 71915,
  "sale_start": "2021-12-19",
  "sale_end": "2022-12-08"
}, {
  "name": "Cheese - Montery Jack",
  "description": "Bypass Left Atrium to L Pulm Art, Perc Endo Approach",
  "price": 72747,
  "sale_start": "2022-04-02",
  "sale_end": "2022-02-20"
}, {
  "name": "Bread - Multigrain",
  "description": "Muscles, Release",
  "price": 88836,
  "sale_start": "2022-12-05",
  "sale_end": "2022-05-27"
}, {
  "name": "Beef Ground Medium",
  "description": "Dilate of L Main Bronc with Intralum Dev, Perc Endo Approach",
  "price": 8014,
  "sale_start": "2022-01-01",
  "sale_end": "2023-01-28"
}, {
  "name": "Flour - Strong Pizza",
  "description": "Inspection of Thymus, Percutaneous Endoscopic Approach",
  "price": 27936,
  "sale_start": "2022-12-16",
  "sale_end": "2022-03-25"
}, {
  "name": "Devonshire Cream",
  "description": "Extirpation of Matter from Left Diaphragm, Perc Approach",
  "price": 38401,
  "sale_start": "2023-01-18",
  "sale_end": "2022-12-31"
}, {
  "name": "Carbonated Water - Strawberry",
  "description": "Supplement Cystic Duct with Synth Sub, Open Approach",
  "price": 38567,
  "sale_start": "2022-01-25",
  "sale_end": "2022-09-04"
}, {
  "name": "Creme De Cacao White",
  "description": "Monitoring of Venous Pressure, Portal, Percutaneous Approach",
  "price": 75017,
  "sale_start": "2022-12-24",
  "sale_end": "2022-02-22"
}, {
  "name": "Godiva White Chocolate",
  "description": "Replacement of R Int Iliac Art with Autol Sub, Open Approach",
  "price": 27181,
  "sale_start": "2022-05-01",
  "sale_end": "2022-10-13"
}, {
  "name": "Cookie Dough - Chocolate Chip",
  "description": "Revision of Nonaut Sub in R Ear, Perc Approach",
  "price": 77395,
  "sale_start": "2022-05-29",
  "sale_end": "2022-12-21"
}, {
  "name": "Banana Turning",
  "description": "Removal of Spacer from R Sternoclav Jt, Perc Endo Approach",
  "price": 56803,
  "sale_start": "2022-06-08",
  "sale_end": "2022-08-23"
}, {
  "name": "Wakami Seaweed",
  "description": "Drainage of Left Finger Phalanx, Percutaneous Approach",
  "price": 3385,
  "sale_start": "2023-01-05",
  "sale_end": "2022-11-18"
}, {
  "name": "Vermacelli - Sprinkles, Assorted",
  "description": "Fluoroscopy of Left Jugular Veins using Other Contrast",
  "price": 65473,
  "sale_start": "2023-01-24",
  "sale_end": "2021-12-07"
}, {
  "name": "Turkey - Ground. Lean",
  "description": "Release Right Posterior Tibial Artery, Open Approach",
  "price": 86697,
  "sale_start": "2023-01-25",
  "sale_end": "2022-11-17"
}, {
  "name": "Vinegar - Sherry",
  "description": "Bypass Intracran Vein to Up Vein w Synth Sub, Open",
  "price": 84104,
  "sale_start": "2022-11-26",
  "sale_end": "2022-06-25"
}, {
  "name": "Soho Lychee Liqueur",
  "description": "Removal of Extralum Dev from Uterus & Cervix, Via Opening",
  "price": 95043,
  "sale_start": "2022-06-10",
  "sale_end": "2022-05-25"
}, {
  "name": "Versatainer Nc - 888",
  "description": "Introduction of Oth Anti-infect into Mouth/Phar, Via Opening",
  "price": 25498,
  "sale_start": "2023-01-05",
  "sale_end": "2022-12-24"
}]
def insert_data():
    for datum in data:
        product = Product(**datum)
        product.save()
        print(f"Saved {product}")

if __name__ == "__main__":
    insert_data()