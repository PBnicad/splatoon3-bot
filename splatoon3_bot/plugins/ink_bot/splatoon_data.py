#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#sys.setdefaultencoding('utf-8')

#friend_list = [424374030,2763844098,645642]
friend_list = [645642,1050725160, 641569063,731015337,291611226,624006585,1792404681,1530669363,741853137,87606250,913228762,1025943438,1723364,469862870,526674852,657437047,864829711,891997651,1374157631]

game_types={
'蛤蜊':'24px-Mode_Icon_Clam_Blitz.png',
'鱼':'24px-Mode_Icon_Rainmaker.png',
'区域':'24px-Mode_Icon_Splat_Zones.png',
'塔':'24px-Mode_Icon_Tower_Control.png'
}

stage = {"0":{"image":"stage/300px-S2_Stage_The_Reef.png","name":"寿司街"},
"1":{"image":"stage/300px-S2_Stage_Musselforge_Fitness.png","name":"健身房"},
"2":{"image":"stage/300px-S2_Stage_Starfish_Mainstage.png","name":"音乐堂"},
"4":{"image":"stage/300px-S2_Stage_Inkblot_Art_Academy.png","name":"美術大学"},
"3":{"image":"stage/300px-S2_Stage_Sturgeon_Shipyard.png","name":"造船厂"},
"5":{"image":"stage/300px-S2_Stage_Humpback_Pump_Track.png","name":"赛道"},
"6":{"image":"stage/300px-S2_Stage_Manta_Maria.png","name":"玛丽号"},
"7":{"image":"stage/300px-S2_Stage_Port_Mackerel.png","name":"码头"},
"8":{"image":"stage/300px-S2_Stage_Moray_Towers.png","name":"停车场"},
"9":{"image":"stage/300px-S2_Stage_Snapper_Canal.png","name":"河川"},
"10":{"image":"stage/300px-S2_Stage_Kelp_Dome.png","name":"农园"},
"11":{"image":"stage/300px-S2_Stage_Blackbelly_Skatepark.png","name":"滑板公园"},
"12":{"image":"stage/300px-S2_Stage_Shellendorf_Institute.png","name":"海洋館"},
"13":{"image":"stage/300px-S2_Stage_MakoMart.png","name":"超市"},
"14":{"image":"stage/300px-S2_Stage_Walleye_Warehouse.png","name":"倉庫"},
"15":{"image":"stage/300px-S2_Stage_Arowana_Mall.png","name":"购物街"},
"16":{"image":"stage/300px-S2_Stage_Camp_Triggerfish.png","name":"露营地"},
"17":{"image":"stage/300px-S2_Stage_Piranha_Pit.png","name":"矿山"},
"18":{"image":"stage/300px-S2_Stage_Goby_Arena.png","name":"篮球场"},
"19":{"image":"stage/300px-S2_Stage_New_Albacore_Hotel.png","name":"酒店"},	
"20":{"image":"stage/300px-S2_Stage_Wahoo_World.png","name":"游乐园"},
"21":{"image":"stage/300px-S2_Stage_Ancho-V_Games.png","name":"游戏房"},
"22":{"image":"stage/300px-S2_Stage_Skipper_Pavilion.png","name":"针鱼楼"},
"Salmonid Smokeyard":{"image":"stage/run/200px-S2_Stage_Salmonid_Smokeyard.png","name":"工房"},
"Spawning Grounds":{"image":"stage/run/200px-S2_Stage_Spawning_Grounds.png","name":"大坝"},
"Marooner's Bay":{"image":"stage/run/200px-S2_Stage_Marooner's_Bay.png","name":"破船"},
"Lost Outpost":{"image":"stage/run/200px-S2_Stage_Lost_Outpost.png","name":"集落"},
"Ruins of Ark Polaris":{"image":"stage/run/200px-S2_Ruins_of_Ark_Polaris_Promo_Image1.jpg","name":"方舟"}
}


stage3 ={"1":{"image":"stage/3/300px-Scorch_Gorge_Promo.jpg","name":"Scorch Gorge","cname":"温泉花大峡谷"},
"2":{"image":"stage/3/300px-S3_promo_screenshot_Eeltail_Alley_00.jpg","name":"Eeltail Alley","cname":"鳗鲶区"},
"3":{"image":"stage/3/300px-S3HagglefishMarketIcon.webp.png","name":"Hagglefish Market","cname":"煙管魚市場"},
"4":{"image":"stage/3/300px-S3UndertowSpillwayIcon.webp.png","name":"Undertow Spillway","cname":"竹蛏疏洪道"},
"6":{"image":"stage/3/300px-S3MincemeatMetalworksIcon.webp.png","name":"Mincemeat Metalworks","cname":"鱼肉碎金属"},
"7":{"image":"stage/3/300px-S3_Brinewater_Springs.png","name":"Brinewater Springs","cname":"臭鱼干温泉"},
"9":{"image":"stage/3/300px-S3_Stage_Flounder_Heights.png","name":"Flounder Heights","cname":"比目鱼住宅区"},
"10":{"image":"stage/3/300px-S3HammerheadBridgeIcon.jpeg","name":"Hammerhead Bridge","cname":"真鯖跨海大橋"},
"11":{"image":"stage/3/300px-S3_Stage_Museum_d'Alfonsino_Promo_1.jpg","name":"Museum d'Alfonsino","cname":"金眼鲷美术馆"},
"12":{"image":"stage/3/300px-S3MahiMahiResortIcon.jpeg","name":"Mahi-Mahi Resort","cname":"鬼头刀SPA度假区"},
"13":{"image":"stage/3/300px-S3_Inkblot_Art_Academy.jpeg","name":"Inkblot Art Academy","cname":"海女美術大學"},
"14":{"image":"stage/3/300px-S3_Sturgeon_Shipyard.jpg","name":"Sturgeon Shipyard","cname":"鲟鱼造船厂"},
"15":{"image":"stage/3/300px-S3_Mako_Mart.jpg","name":"MakoMart","cname":"座頭購物中心"},
"16":{"image":"stage/3/300px-S3_Wahoo_World.jpg","name":"Wahoo World","cname":"醋飯海洋世界"},
"5":{"image":"stage/3/300px-S3_Stage_Um'ami_Ruins.png","name":"Um'ami Ruins","cname":"鱼露遗迹"},
"18":{"image":"stage/3/300px-S3_Stage_Manta_Maria.png","name":"Manta Maria","cname":"鬼蝠鲼玛利亚号"},
'Sockeye Station':{"image":"stage/3/Sockeye Station.jpg","name":'新卷堡'},
'Gone Fission Hydroplant':{"image":"stage/3/Gone Fission Hydroplant.jpg","name":'麦年海洋发电所'},
"Marooner's Bay":{"image":"stage/3/200px-S3_Stage_Marooner's_Bay.png","name":'漂浮落难船'},
'Spawning Grounds':{"image":"stage/3/Spawning Grounds.jpg","name":'鲑坝'}}

rank_mode = {"clam_blitz":"蛤蜊","rainmaker" :"抢鱼","tower_control": "推塔","splat_zones": "区域"}
fest_ranks = {
	'0': '粉丝',
	'1': '着迷',
	'2': '守护者',
	'3': '冠军',
	'4': '王者'
}

weapons={"0":{"en":"Sploosh-o-matic","cn":"喇叭枪","image":"weapons/Wst_Shooter_Short_00.png","sub_name":"冰壶","speical_name":"捶地"},
"1":{"en":"Neo Sploosh-o-matic","cn":"喇叭枪(贴牌)","image":"weapons/Wst_Shooter_Short_01.png","sub_name":"跳点","speical_name":"导弹"},
"2":{"en":"Sploosh-o-matic 7","cn":"喇叭枪(贴牌)","image":"weapons/Shooter_Short_02.png","sub_name":"三角雷","speical_name":"大锤"},
"10":{"en":"Splattershot Jr.","cn":"新叶","image":"weapons/Wst_Shooter_First_00.png","sub_name":"三角雷","speical_name":"墨甲"},
"11":{"en":"Custom Splattershot Jr.","cn":"枫叶","image":"weapons/Wst_Shooter_First_01.png","sub_name":"小鸡","speical_name":"雨"},
"12":{"en":"Kensa Splattershot Jr.","cn":"新叶(它牌)","image":"weapons/Wst_Shooter_First_02.png","sub_name":"鱼雷","speical_name":"泡泡"},
"20":{"en":"Splash-o-matic","cn":"针管","image":"weapons/Wst_Shooter_Precision_00.png","sub_name":"毒雾","speical_name":"飞机"},
"21":{"en":"Neo Splash-o-matic","cn":"针管(贴牌)","image":"weapons/Wst_Shooter_Precision_01.png","sub_name":"水球","speical_name":"粘弹rush"},
"30":{"en":"Aerospray MG","cn":"银喷","image":"weapons/Wst_Shooter_Blaze_00.png","sub_name":"粘弹","speical_name":"冰壶rush"},
"31":{"en":"Aerospray RG","cn":"金喷","image":"weapons/Wst_Shooter_Blaze_01.png","sub_name":"花洒","speical_name":"仓鼠球"},
"32":{"en":"Aerospray PG","cn":"铜喷","image":"weapons/Shooter_Blaze_02.png","sub_name":"水球","speical_name":"nice弹"},
"40":{"en":"Splattershot","cn":"小绿","image":"weapons/Wst_Shooter_Normal_00.png","sub_name":"水球","speical_name":"捶地"},
"41":{"en":"Tentatek Splattershot","cn":"小绿(贴牌)","image":"weapons/Wst_Shooter_Normal_01.png","sub_name":"三角雷","speical_name":"飞机"},
"42":{"en":"Kensa Splattershot","cn":"小绿(它牌)","image":"weapons/Wst_Shooter_Normal_02.png","sub_name":"粘弹","speical_name":"导弹"},
"45":{"en":"Hero Shot Replica","cn":"P90","image":"weapons/Wst_Shooter_Normal_H.png","sub_name":"水球","speical_name":"捶地"},
"46":{"en":"Octo Shot Replica","cn":"小黑(章鱼)","image":"weapons/Wst_Shooter_Normal_Oct.png","sub_name":"三角雷","speical_name":"飞机"},
"50":{"en":".52 Gal","cn":"52","image":"weapons/Wst_Shooter_Gravity_00.png","sub_name":"追踪器","speical_name":"仓鼠球"},
"51":{"en":".52 Gal Deco","cn":"52(贴牌)","image":"weapons/Wst_Shooter_Gravity_01.png","sub_name":"冰壶","speical_name":"水枪"},
"52":{"en":"Kensa .52 Gal","cn":"52(它牌)","image":"weapons/Wst_Shooter_Gravity_02.png","sub_name":"雨帘","speical_name":"nice弹"},
"60":{"en":"N-ZAP '85","cn":"85","image":"weapons/Wst_Shooter_QuickMiddle_00.png","sub_name":"粘弹","speical_name":"墨甲"},
"61":{"en":"N-ZAP '89","cn":"89","image":"weapons/Wst_Shooter_QuickMiddle_01.png","sub_name":"小鸡","speical_name":"导弹"},
"62":{"en":"N-ZAP '83","cn":"83","image":"weapons/Shooter_QuickMiddle_02.png","sub_name":"花洒","speical_name":"雨"},
"70":{"en":"Splattershot Pro","cn":"精英枪","image":"weapons/Wst_Shooter_Expert_00.png","sub_name":"追踪器","speical_name":"雨"},
"71":{"en":"Forge Splattershot Pro","cn":"精英枪(贴牌)","image":"weapons/Wst_Shooter_Expert_01.png","sub_name":"粘弹","speical_name":"泡泡"},
"72":{"en":"Kensa Splattershot Pro","cn":"精英枪(它牌)","image":"weapons/Wst_Shooter_Expert_02.png","sub_name":"三角雷","speical_name":"nice弹"},
"80":{"en":".96 Gal","cn":"96","image":"weapons/Wst_Shooter_Heavy_00.png","sub_name":"花洒","speical_name":"墨甲"},
"81":{"en":".96 Gal Deco","cn":"96(贴牌)","image":"weapons/Wst_Shooter_Heavy_01.png","sub_name":"雨帘","speical_name":"捶地"},
"90":{"en":"Jet Squelcher","cn":"蓝管","image":"weapons/Wst_Shooter_Long_00.png","sub_name":"毒雾","speical_name":"导弹"},
"91":{"en":"Custom Jet Squelcher","cn":"蓝管(贴牌)","image":"weapons/Wst_Shooter_Long_01.png","sub_name":"水球","speical_name":"水枪"},
"200":{"en":"Luna Blaster","cn":"露娜泡","image":"weapons/Wst_Shooter_BlasterShort_00.png","sub_name":"三角雷","speical_name":"仓鼠球"},
"201":{"en":"Luna Blaster Neo","cn":"露娜泡(贴牌)","image":"weapons/Wst_Shooter_BlasterShort_01.png","sub_name":"陷阱","speical_name":"粘弹rush"},
"202":{"en":"Kensa Luna Blaster","cn":"露娜泡(它牌)","image":"weapons/Wst_Shooter_BlasterShort_02.png","sub_name":"碳酸弹","speical_name":"雨"},
"210":{"en":"Blaster","cn":"热泡","image":"weapons/Wst_Shooter_BlasterMiddle_00.png","sub_name":"毒雾","speical_name":"捶地"},
"211":{"en":"Custom Blaster","cn":"热泡(贴牌)","image":"weapons/Wst_Shooter_BlasterMiddle_01.png","sub_name":"小鸡","speical_name":"飞机"},
"215":{"en":"Hero Blaster Replica","cn":"英雄泡","image":"weapons/Wst_Shooter_BlasterMiddle_H.png","sub_name":"毒雾","speical_name":"捶地"},
"220":{"en":"Range Blaster","cn":"长热泡枪","image":"weapons/Wst_Shooter_BlasterLong_00.png","sub_name":"粘弹","speical_name":"雨"},
"221":{"en":"Custom Range Blaster","cn":"长热泡(贴牌)","image":"weapons/Wst_Shooter_BlasterLong_01.png","sub_name":"冰壶","speical_name":"泡泡"},
"222":{"en":"Grim Range Blaster","cn":"长热泡(贴牌)","image":"weapons/Shooter_BlasterLong_02.png","sub_name":"水球","speical_name":"导弹"},
"230":{"en":"Clash Blaster","cn":"蜡笔泡","image":"weapons/Wst_Shooter_BlasterLightShort_00.png","sub_name":"三角雷","speical_name":"水枪"},
"231":{"en":"Clash Blaster Neo","cn":"蜡笔泡(贴牌)","image":"weapons/Wst_Shooter_BlasterLightShort_01.png","sub_name":"冰壶","speical_name":"导弹"},
"240":{"en":"Rapid Blaster","cn":"红泡","image":"weapons/Wst_Shooter_BlasterLight_00.png","sub_name":"陷阱","speical_name":"三角雷rush"},
"241":{"en":"Rapid Blaster Deco","cn":"红泡(贴牌)","image":"weapons/Wst_Shooter_BlasterLight_01.png","sub_name":"粘弹","speical_name":"飞机"},
"242":{"en":"Kensa Rapid Blaster","cn":"红泡(它牌)","image":"weapons/Wst_Shooter_BlasterLight_02.png","sub_name":"鱼雷","speical_name":"仓鼠球"},
"250":{"en":"Rapid Blaster Pro","cn":"长红泡","image":"weapons/Wst_Shooter_BlasterLightLong_00.png","sub_name":"毒雾","speical_name":"雨"},
"251":{"en":"Rapid Blaster Pro Deco","cn":"长红泡(贴牌)","image":"weapons/Wst_Shooter_BlasterLightLong_01.png","sub_name":"雨帘","speical_name":"墨甲"},
"300":{"en":"L-3 Nozzlenose","cn":"L3","image":"weapons/Wst_Shooter_TripleQuick_00.png","sub_name":"冰壶","speical_name":"仓鼠球"},
"301":{"en":"L-3 Nozzlenose D","cn":"L3(贴牌)","image":"weapons/Wst_Shooter_TripleQuick_01.png","sub_name":"水球","speical_name":"飞机"},
"302":{"en":"Kensa L-3 Nozzlenose","cn":"L3(它牌)","image":"weapons/Wst_Shooter_TripleQuick_02.png","sub_name":"雨帘","speical_name":"大锤"},
"310":{"en":"H-3 Nozzlenose","cn":"H3","image":"weapons/Wst_Shooter_TripleMiddle_00.png","sub_name":"追踪器","speical_name":"导弹"},
"311":{"en":"H-3 Nozzlenose D","cn":"H3(贴牌)","image":"weapons/Wst_Shooter_TripleMiddle_01.png","sub_name":"粘弹","speical_name":"墨甲"},
"312":{"en":"Cherry H-3 Nozzlenose","cn":"H3(贴牌)","image":"weapons/Shooter_TripleMiddle_02.png","sub_name":"雨帘","speical_name":"泡泡"},
"400":{"en":"Squeezer","cn":"香槟枪","image":"weapons/Wst_Shooter_Flash_00.png","sub_name":"雨帘","speical_name":"水枪"},
"401":{"en":"Foil Squeezer","cn":"香槟枪(贴牌)","image":"weapons/Wst_Shooter_Flash_01.png","sub_name":"三角雷","speical_name":"泡泡"},
"1000":{"en":"Carbon Roller","cn":"碳刷","image":"weapons/Wst_Roller_Compact_00.png","sub_name":"小鸡","speical_name":"雨"},
"1001":{"en":"Carbon Roller Deco","cn":"碳刷(贴牌)","image":"weapons/Wst_Roller_Compact_01.png","sub_name":"水球","speical_name":"小鸡rush"},
"1010":{"en":"Splat Roller","cn":"中刷","image":"weapons/Wst_Roller_Normal_00.png","sub_name":"冰壶","speical_name":"捶地"},
"1011":{"en":"Krak-On Splat Roller","cn":"中刷(贴牌)","image":"weapons/Wst_Roller_Normal_01.png","sub_name":"跳点","speical_name":"仓鼠球"},
"1012":{"en":"Kensa Splat Roller","cn":"中刷(贴牌)","image":"weapons/Wst_Roller_Normal_02.png","sub_name":"三角雷","speical_name":"泡泡"},
"1015":{"en":"Hero Roller Replica","cn":"英雄中刷","image":"weapons/Wst_Roller_Normal_H.png","sub_name":"冰壶","speical_name":"捶地"},
"1020":{"en":"Dynamo Roller","cn":"重刷","image":"weapons/Wst_Roller_Heavy_00.png","sub_name":"陷阱","speical_name":"水枪"},
"1021":{"en":"Gold Dynamo Roller","cn":"重刷(贴牌)","image":"weapons/Wst_Roller_Heavy_01.png","sub_name":"三角雷","speical_name":"墨甲"},
"1022":{"en":"Kensa Dynamo Roller","cn":"重刷(它牌)","image":"weapons/Wst_Roller_Heavy_02.png","sub_name":"花洒","speical_name":"nice弹"},
"1030":{"en":"Flingza Roller","cn":"钢笔刷","image":"weapons/Wst_Roller_Hunter_00.png","sub_name":"雨帘","speical_name":"三角雷rush"},
"1031":{"en":"Foil Flingza Roller","cn":"钢笔刷(贴牌)","image":"weapons/Wst_Roller_Hunter_01.png","sub_name":"粘弹","speical_name":"导弹"},
"1100":{"en":"Inkbrush","cn":"笔刷","image":"weapons/Wst_Roller_BrushMini_00.png","sub_name":"三角雷","speical_name":"捶地"},
"1101":{"en":"Inkbrush Nouveau","cn":"笔刷(贴牌)","image":"weapons/Wst_Roller_BrushMini_01.png","sub_name":"陷阱","speical_name":"仓鼠球"},
"1102":{"en":"Permanent Inkbrush","cn":"笔刷(贴牌)","image":"weapons/Roller_BrushMini_02.png","sub_name":"花洒","speical_name":"墨甲"},
"1110":{"en":"Octobrush","cn":"北斋","image":"weapons/Wst_Roller_BrushNormal_00.png","sub_name":"小鸡","speical_name":"飞机"},
"1111":{"en":"Octobrush Nouveau","cn":"北斋(贴牌)","image":"weapons/Wst_Roller_BrushNormal_01.png","sub_name":"跳点","speical_name":"导弹"},
"1112":{"en":"Kensa Octobrush","cn":"北斋(它牌)","image":"weapons/Wst_Roller_BrushNormal_02.png","sub_name":"粘弹","speical_name":"大锤"},
"1115":{"en":"Herobrush Replica","cn":"英雄北斋","image":"weapons/Wst_Roller_BrushNormal_H.png","sub_name":"小鸡","speical_name":"飞机"},
"2000":{"en":"Classic Squiffer","cn":"洗洁精","image":"weapons/Wst_Charger_Quick_00.png","sub_name":"追踪器","speical_name":"墨甲"},
"2001":{"en":"New Squiffer","cn":"洗洁精(贴牌)","image":"weapons/Wst_Charger_Quick_01.png","sub_name":"小鸡","speical_name":"仓鼠球"},
"2002":{"en":"Fresh Squiffer","cn":"洗洁精(贴牌)","image":"weapons/Charger_Quick_02.png","sub_name":"粘弹","speical_name":"飞机"},
"2010":{"en":"Splat Charger","cn":"短狙","image":"weapons/Wst_Charger_Normal_00.png","sub_name":"三角雷","speical_name":"水枪"},
"2011":{"en":"Firefin Splat Charger","cn":"短狙(贴牌)","image":"weapons/Wst_Charger_Normal_01.png","sub_name":"雨帘","speical_name":"粘弹rush"},
"2012":{"en":"Kensa Charger","cn":"短狙(它牌)","image":"weapons/Wst_Charger_Normal_02.png","sub_name":"花洒","speical_name":"仓鼠球"},
"2015":{"en":"Hero Charger Replica","cn":"英雄狙","image":"weapons/Wst_Charger_Normal_H.png","sub_name":"三角雷","speical_name":"水枪"},
"2020":{"en":"Splatterscope","cn":"有镜短狙","image":"weapons/Wst_Charger_NormalScope_00.png","sub_name":"三角雷","speical_name":"水枪"},
"2021":{"en":"Firefin Splatterscope","cn":"有镜短狙(贴牌)","image":"weapons/Wst_Charger_NormalScope_01.png","sub_name":"雨帘","speical_name":"粘弹rush"},
"2022":{"en":"Kensa Splatterscope","cn":"有镜短狙(它牌)","image":"weapons/Wst_Charger_NormalScope_01.png","sub_name":"花洒","speical_name":"仓鼠球"},
"2030":{"en":"E-liter 4K","cn":"4K","image":"weapons/Wst_Charger_Long_00.png","sub_name":"陷阱","speical_name":"雨"},
"2031":{"en":"Custom E-liter 4K","cn":"4k(贴牌)","image":"weapons/Wst_Charger_Long_01.png","sub_name":"跳点","speical_name":"泡泡"},
"2040":{"en":"E-liter 4K Scope","cn":"有镜4K","image":"weapons/Wst_Charger_LongScope_00.png","sub_name":"陷阱","speical_name":"雨"},
"2041":{"en":"Custom E-liter 4K Scope","cn":"有镜4K(贴牌)","image":"weapons/Wst_Charger_LongScope_01.png","sub_name":"跳点","speical_name":"泡泡"},
"2050":{"en":"Bamboozler 14 Mk I","cn":"竹狙","image":"weapons/Wst_Charger_Light_00.png","sub_name":"冰壶","speical_name":"导弹"},
"2051":{"en":"Bamboozler 14 Mk II","cn":"竹狙(贴牌)","image":"weapons/Wst_Charger_Light_01.png","sub_name":"毒雾","speical_name":"水球rush"},
"2052":{"en":"Bamboozler 14 Mk III","cn":"竹狙(贴牌)","image":"weapons/Charger_Light_02.png","sub_name":"碳酸弹","speical_name":"泡泡"},
"2060":{"en":"Goo Tuber","cn":"水管狙","image":"weapons/Wst_Charger_Keeper_00.png","sub_name":"粘弹","speical_name":"捶地"},
"2061":{"en":"Custom Goo Tuber","cn":"水管狙(贴牌)","image":"weapons/Wst_Charger_Keeper_01.png","sub_name":"冰壶","speical_name":"飞机"},
"3000":{"en":"Slosher","cn":"红桶","image":"weapons/Wst_Slosher_Strong_00.png","sub_name":"粘弹","speical_name":"导弹"},
"3001":{"en":"Slosher Deco","cn":"红桶(贴牌)","image":"weapons/Wst_Slosher_Strong_01.png","sub_name":"花洒","speical_name":"仓鼠球"},
"3002":{"en":"Soda Slosher","cn":"苏打桶","image":"weapons/Slosher_Strong_02.png","sub_name":"三角雷","speical_name":"水球rush"},
"3005":{"en":"Hero Slosher Replica","cn":"英雄桶","image":"weapons/Wst_Slosher_Strong_H.png","sub_name":"粘弹","speical_name":"导弹"},
"3010":{"en":"Tri-Slosher","cn":"绿桶(贴牌）","image":"weapons/Wst_Slosher_Diffusion_00.png","sub_name":"水球","speical_name":"墨甲"},
"3011":{"en":"Tri-Slosher Nouveau","cn":"绿桶(贴牌）","image":"weapons/Wst_Slosher_Diffusion_01.png","sub_name":"三角雷","speical_name":"雨"},
"3020":{"en":"Sloshing Machine","cn":"洗衣机","image":"weapons/Wst_Slosher_Launcher_00.png","sub_name":"小鸡","speical_name":"水枪"},
"3021":{"en":"Sloshing Machine Neo","cn":"洗衣机(贴牌)","image":"weapons/Wst_Slosher_Launcher_01.png","sub_name":"追踪器","speical_name":"三角雷rush"},
"3022":{"en":"Kensa Sloshing Machine","cn":"洗衣机(它牌)","image":"weapons/Wst_Slosher_Launcher_02.png","sub_name":"碳酸弹","speical_name":"捶地"},
"3030":{"en":"Bloblobber","cn":"浴缸","image":"weapons/Wst_Slosher_Bathtub_00.png","sub_name":"雨帘","speical_name":"雨"},
"3031":{"en":"Bloblobber Deco","cn":"浴缸(贴牌)","image":"weapons/Wst_Slosher_Bathtub_01.png","sub_name":"花洒","speical_name":"粘弹rush"},
"3040":{"en":"Explosher","cn":"重桶","image":"weapons/Wst_Slosher_Washtub_00.png","sub_name":"花洒","speical_name":"泡泡"},
"3041":{"en":"Custom Explosher","cn":"重桶(贴牌)","image":"weapons/Wst_Slosher_Washtub_01.png","sub_name":"追踪器","speical_name":"仓鼠球"},
"4000":{"en":"Mini Splatling","cn":"轻加","image":"weapons/Wst_Spinner_Quick_00.png","sub_name":"水球","speical_name":"导弹"},
"4001":{"en":"Zink Mini Splatling","cn":"轻加(贴牌)","image":"weapons/Wst_Spinner_Quick_01.png","sub_name":"冰壶","speical_name":"雨"},
"4002":{"en":"Kensa Mini Splatling","cn":"轻加(它牌)","image":"weapons/Wst_Spinner_Quick_02.png","sub_name":"毒雾","speical_name":"大锤"},
"4010":{"en":"Heavy Splatling","cn":"中加","image":"weapons/Wst_Spinner_Standard_00.png","sub_name":"花洒","speical_name":"水枪"},
"4011":{"en":"Heavy Splatling Deco","cn":"中加(贴牌)","image":"weapons/Wst_Spinner_Standard_01.png","sub_name":"雨帘","speical_name":"泡泡"},
"4012":{"en":"Heavy Splatling Remix","cn":"中加(贴牌)","image":"weapons/Spinner_Standard_02.png","sub_name":"追踪器","speical_name":"nice弹"},
"4015":{"en":"Hero Splatling Replica","cn":"英雄中加","image":"weapons/Wst_Spinner_Standard_H.png","sub_name":"花洒","speical_name":"水枪"},
"4020":{"en":"Hydra Splatling","cn":"消防栓","image":"weapons/Wst_Spinner_Hyper_00.png","sub_name":"小鸡","speical_name":"捶地"},
"4021":{"en":"Custom Hydra Splatling","cn":"消防栓(贴牌)","image":"weapons/Wst_Spinner_Hyper_01.png","sub_name":"陷阱","speical_name":"墨甲"},
"4030":{"en":"Ballpoint Splatling","cn":"圆珠笔","image":"weapons/Wst_Spinner_Downpour_00.png","sub_name":"毒雾","speical_name":"飞机"},
"4031":{"en":"Ballpoint Splatling Nouveau","cn":"圆珠笔(贴牌)","image":"weapons/Wst_Spinner_Downpour_01.png","sub_name":"跳点","speical_name":"雨"},
"4040":{"en":"Nautilus 47","cn":"鹦鹉螺","image":"weapons/Wst_Spinner_Serein_00.png","sub_name":"追踪器","speical_name":"仓鼠球"},
"4041":{"en":"Nautilus 79","cn":"鹦鹉螺(贴牌)","image":"weapons/Wst_Spinner_Serein_01.png","sub_name":"粘弹","speical_name":"飞机"},
"5000":{"en":"Dapple Dualies","cn":"红牙刷","image":"weapons/Wst_Twins_Short_00.png","sub_name":"跳点","speical_name":"粘弹rush"},
"5001":{"en":"Dapple Dualies Nouveau","cn":"蓝牙刷","image":"weapons/Wst_Twins_Short_01.png","sub_name":"毒雾","speical_name":"雨"},
"5002":{"en":"Clear Dapple Dualies","cn":"白牙刷","image":"weapons/Twins_Short_02.png","sub_name":"鱼雷","speical_name":"捶地"},
"5010":{"en":"Splat Dualies","cn":"绿双","image":"weapons/Wst_Twins_Normal_00.png","sub_name":"水球","speical_name":"导弹"},
"5011":{"en":"Enperry Splat Dualies","cn":"金双","image":"weapons/Wst_Twins_Normal_01.png","sub_name":"冰壶","speical_name":"飞机"},
"5012":{"en":"Kensa Splat Dualies","cn":"黑双(它牌)","image":"weapons/Wst_Twins_Normal_02.png","sub_name":"粘弹","speical_name":"仓鼠球"},
"5015":{"en":"Hero Dualie Replicas","cn":"英雄双枪","image":"weapons/Wst_Twins_Normal_H.png","sub_name":"水球","speical_name":"导弹"},
"5020":{"en":"Glooga Dualies","cn":"525","image":"weapons/Wst_Twins_Gallon_00.png","sub_name":"陷阱","speical_name":"飞机"},
"5021":{"en":"Glooga Dualies Deco","cn":"525(贴牌)","image":"weapons/Wst_Twins_Gallon_01.png","sub_name":"雨帘","speical_name":"仓鼠球"},
"5022":{"en":"Kensa Glooga Dualies","cn":"525(它牌)","image":"weapons/Wst_Twins_Gallon_02.png","sub_name":"碳酸弹","speical_name":"墨甲"},
"5030":{"en":"Dualie Squelchers","cn":"红双(贴牌)","image":"weapons/Wst_Twins_Dual_00.png","sub_name":"追踪器","speical_name":"导弹"},
"5031":{"en":"Custom Dualie Squelchers","cn":"红双(贴牌)","image":"weapons/Wst_Twins_Dual_01.png","sub_name":"三角雷","speical_name":"雨"},
"5040":{"en":"Dark Tetra Dualies","cn":"气垫","image":"weapons/Wst_Twins_Stepper_00.png","sub_name":"小鸡","speical_name":"捶地"},
"5041":{"en":"Light Tetra Dualies","cn":"气垫(贴牌)","image":"weapons/Wst_Twins_Stepper_01.png","sub_name":"花洒","speical_name":"小鸡rush"},
"6000":{"en":"Splat Brella","cn":"伞","image":"weapons/Wst_Umbrella_Normal_00.png","sub_name":"花洒","speical_name":"雨"},
"6001":{"en":"Sorella Brella","cn":"银伞","image":"weapons/Wst_Umbrella_Normal_01.png","sub_name":"小鸡","speical_name":"三角雷rush"},
"6005":{"en":"Hero Brella Replica","cn":"英雄伞","image":"weapons/Wst_Umbrella_Normal_H.png","sub_name":"花洒","speical_name":"雨"},
"6010":{"en":"Tenta Brella","cn":"重伞","image":"weapons/Wst_Umbrella_Wide_00.png","sub_name":"跳点","speical_name":"泡泡"},
"6011":{"en":"Tenta Sorella Brella","cn":"重伞(贴牌)","image":"weapons/Wst_Umbrella_Wide_01.png","sub_name":"雨帘","speical_name":"冰壶rush"},
"6012":{"en":"Tenta Camo Brella","cn":"重伞(贴牌)","image":"weapons/Umbrella_Wide_02.png","sub_name":"陷阱","speical_name":"大锤"},
"6020":{"en":"Undercover Brella","cn":"间谍伞","image":"weapons/Wst_Umbrella_Compact_00.png","sub_name":"陷阱","speical_name":"捶地"},
"6021":{"en":"Undercover Sorella Brella","cn":"间谍伞(贴牌)","image":"weapons/Wst_Umbrella_Compact_01.png","sub_name":"三角雷","speical_name":"仓鼠球"},
"6022":{"en":"Kensa Undercover Brella","cn":"间谍伞(贴牌)","image":"weapons/Wst_Umbrella_Compact_02.png","sub_name":"鱼雷","speical_name":"墨甲"},
"-1":{"en":"random","cn":"随机","image":"weapons/run/S2_Weapon_Main_Random.png"},
"-2":{"en":"random","cn":"随机","image":"weapons/run/S2_Weapon_Main_Random_2.png"},
"-3":{"en":"random","cn":"随机熊武器","image":"weapons/run/S2_Weapon_Main_Random_2.png"},
"-4":{"en":"random","cn":"熊伞","image":"weapons/run/64px-S2_Weapon_Main_Grizzco_Brella.png"},
"-5":{"en":"random","cn":"熊泡","image":"weapons/run/64px-S2_Weapon_Main_Grizzco_Blaster.png"},
"-6":{"en":"random","cn":"熊狙","image":"weapons/run/64px-S2_Weapon_Main_Grizzco_Charger.png"},
"-3":{"en":"random","cn":"熊桶","image":"weapons/run/64px-S2_Weapon_Main_Grizzco_Slosher.png"}
}							

weapons3 = {
'Sploosh-o-matic':{'wimg':'3/Path_Wst_Shooter_Short_00.png','subname':'Curling Bomb','subimg':'Wsb_Bomb_Curling00.png','spename':'Ultra Stamp','speimg':'Wsp_SpUltraStamp00.png'},
'Splattershot Jr.':{'wimg':'3/Path_Wst_Shooter_First_00.png','subname':'Splat Bomb','subimg':'Wsb_Bomb_Splash00.png','spename':'Big Bubbler','speimg':'Wsp_SpGreatBarrier00.png'},
'Splash-o-matic':{'wimg':'3/Path_Wst_Shooter_Precision_00.png','subname':'Burst Bomb','subimg':'Wsb_Bomb_Quick00.png','spename':'Crab Tank','speimg':'Wsp_SpChariot00.png'},
'Aerospray MG':{'wimg':'3/Path_Wst_Shooter_Blaze_00.png','subname':'Fizzy Bomb','subimg':'Wsb_Bomb_Fizzy00.png','spename':'Reefslider','speimg':'Wsp_SpSkewer00.png'},
'Splattershot':{'wimg':'3/Path_Wst_Shooter_Normal_00.png','subname':'Suction Bomb','subimg':'Wsb_Bomb_Suction00.png','spename':'Trizooka','speimg':'Wsp_SpUltraShot00.png'},
'Hero Shot Replica':{'wimg':'3/Path_Wst_Shooter_Normal_H.png','subname':'Suction Bomb','subimg':'Wsb_Bomb_Suction00.png','spename':'Trizooka','speimg':'Wsp_SpUltraShot00.png'},
'.52 Gal':{'wimg':'3/Path_Wst_Shooter_Gravity_00.png','subname':'Splash Wall','subimg':'Wsb_Shield00.png','spename':'Killer Wail 5.1','speimg':'Wsp_SpMicroLaser00.png'},
'N-ZAP \'85':{'wimg':'3/Path_Wst_Shooter_QuickMiddle_00.png','subname':'Suction Bomb','subimg':'Wsb_Bomb_Suction00.png','spename':'Tacticooler','speimg':'Wsp_SpEnergyStand00.png'},
'Splattershot Pro':{'wimg':'3/Path_Wst_Shooter_Expert_00.png','subname':'Angle Shooter','subimg':'Wsb_LineMarker00.png','spename':'Crab Tank','speimg':'Wsp_SpChariot00.png'},
'.96 Gal':{'wimg':'3/Path_Wst_Shooter_Heavy_00.png','subname':'Sprinkler','subimg':'Wsb_Sprinkler00.png','spename':'Ink Vac','speimg':'Wsp_SpBlower00.png'},
'Jet Squelcher':{'wimg':'3/Path_Wst_Shooter_Long_00.png','subname':'Angle Shooter','subimg':'Wsb_LineMarker00.png','spename':'Ink Vac','speimg':'Wsp_SpBlower00.png'},
'Luna Blaster':{'wimg':'3/Path_Wst_Blaster_Short_00.png','subname':'Splat Bomb','subimg':'Wsb_Bomb_Splash00.png','spename':'Zipcaster','speimg':'Wsp_SpSuperHook00.png'},
'Blaster':{'wimg':'3/Path_Wst_Blaster_Middle_00.png','subname':'Autobomb','subimg':'Wsb_Bomb_Robot00.png','spename':'Big Bubbler','speimg':'Wsp_SpGreatBarrier00.png'},
'Range Blaster':{'wimg':'3/Path_Wst_Blaster_Long_00.png','subname':'Suction Bomb','subimg':'Wsb_Bomb_Suction00.png','spename':'Wave Breaker','speimg':'Wsp_SpShockSonar00.png'},
'Clash Blaster':{'wimg':'3/Path_Wst_Blaster_LightShort_00.png','subname':'Splat Bomb','subimg':'Wsb_Bomb_Splash00.png','spename':'Trizooka','speimg':'Wsp_SpUltraShot00.png'},
'Rapid Blaster':{'wimg':'3/Path_Wst_Blaster_Light_00.png','subname':'Ink Mine','subimg':'Wsb_Trap00.png','spename':'Triple Inkstrike','speimg':'Wsp_SpTripleTornado00.png'},
'Rapid Blaster Pro':{'wimg':'3/Path_Wst_Blaster_LightLong_00.png','subname':'Toxic Mist','subimg':'Wsb_PoisonMist00.png','spename':'Ink Vac','speimg':'Wsp_SpBlower00.png'},
'L-3 Nozzlenose':{'wimg':'3/Path_Wst_Shooter_TripleQuick_00.png','subname':'Curling Bomb','subimg':'Wsb_Bomb_Curling00.png','spename':'Crab Tank','speimg':'Wsp_SpChariot00.png'},
'H-3 Nozzlenose':{'wimg':'3/Path_Wst_Shooter_TripleMiddle_00.png','subname':'Point Sensor','subimg':'Wsb_PointSensor00.png','spename':'Tacticooler','speimg':'Wsp_SpEnergyStand00.png'},
'Squeezer':{'wimg':'3/Path_Wst_Shooter_Flash_00.png','subname':'Splash Wall','subimg':'Wsb_Shield00.png','spename':'Trizooka','speimg':'Wsp_SpUltraShot00.png'},
'Carbon Roller':{'wimg':'3/Path_Wst_Roller_Compact_00.png','subname':'Autobomb','subimg':'Wsb_Bomb_Robot00.png','spename':'Zipcaster','speimg':'Wsp_SpSuperHook00.png'},
'Splat Roller':{'wimg':'3/Path_Wst_Roller_Normal_00.png','subname':'Curling Bomb','subimg':'Wsb_Bomb_Curling00.png','spename':'Big Bubbler','speimg':'Wsp_SpGreatBarrier00.png'},
'Dynamo Roller':{'wimg':'3/Path_Wst_Roller_Heavy_00.png','subname':'Sprinkler','subimg':'Wsb_Sprinkler00.png','spename':'Tacticooler','speimg':'Wsp_SpEnergyStand00.png'},
'Flingza Roller':{'wimg':'3/Path_Wst_Roller_Hunter_00.png','subname':'Ink Mine','subimg':'Wsb_Trap00.png','spename':'Tenta Missiles','speimg':'Wsp_SpMultiMissile00.png'},
'Inkbrush':{'wimg':'3/Path_Wst_Brush_Mini_00.png','subname':'Splat Bomb','subimg':'Wsb_Bomb_Splash00.png','spename':'Killer Wail 5.1','speimg':'Wsp_SpMicroLaser00.png'},
'Octobrush':{'wimg':'3/Path_Wst_Brush_Normal_00.png','subname':'Suction Bomb','subimg':'Wsb_Bomb_Suction00.png','spename':'Zipcaster','speimg':'Wsp_SpSuperHook00.png'},
'Classic Squiffer':{'wimg':'3/Path_Wst_Charger_Quick_00.png','subname':'Point Sensor','subimg':'Wsb_PointSensor00.png','spename':'Big Bubbler','speimg':'Wsp_SpGreatBarrier00.png'},
'Splat Charger':{'wimg':'3/Path_Wst_Charger_Normal_00.png','subname':'Splat Bomb','subimg':'Wsb_Bomb_Splash00.png','spename':'Ink Vac','speimg':'Wsp_SpBlower00.png'},
'Splatterscope':{'wimg':'3/Path_Wst_Charger_NormalScope_00.png','subname':'Splat Bomb','subimg':'Wsb_Bomb_Splash00.png','spename':'Ink Vac','speimg':'Wsp_SpBlower00.png'},
'E-liter 4K':{'wimg':'3/Path_Wst_Charger_Long_00.png','subname':'Ink Mine','subimg':'Wsb_Trap00.png','spename':'Wave Breaker','speimg':'Wsp_SpShockSonar00.png'},
'E-liter 4K Scope':{'wimg':'3/Path_Wst_Charger_LongScope_00.png','subname':'Ink Mine','subimg':'Wsb_Trap00.png','spename':'Wave Breaker','speimg':'Wsp_SpShockSonar00.png'},
'Bamboozler 14 Mk I':{'wimg':'3/Path_Wst_Charger_Light_00.png','subname':'Autobomb','subimg':'Wsb_Bomb_Robot00.png','spename':'Killer Wail 5.1','speimg':'Wsp_SpMicroLaser00.png'},
'Goo Tuber':{'wimg':'3/Path_Wst_Charger_Keeper_00.png','subname':'Torpedo','subimg':'Wsb_Bomb_Torpedo00.png','spename':'Tenta Missiles','speimg':'Wsp_SpMultiMissile00.png'},
'Slosher':{'wimg':'3/Path_Wst_Slosher_Strong_00.png','subname':'Splat Bomb','subimg':'Wsb_Bomb_Splash00.png','spename':'Triple Inkstrike','speimg':'Wsp_SpTripleTornado00.png'},
'Tri-Slosher':{'wimg':'3/Path_Wst_Slosher_Diffusion_00.png','subname':'Toxic Mist','subimg':'Wsb_PoisonMist00.png','spename':'Inkjet','speimg':'Wsp_SpJetpack00.png'},
'Sloshing Machine':{'wimg':'3/Path_Wst_Slosher_Launcher_00.png','subname':'Fizzy Bomb','subimg':'Wsb_Bomb_Fizzy00.png','spename':'Booyah Bomb','speimg':'Wsp_SpNiceBall00.png'},
'Bloblobber':{'wimg':'3/Path_Wst_Slosher_Bathtub_00.png','subname':'Sprinkler','subimg':'Wsb_Sprinkler00.png','spename':'Ink Storm','speimg':'Wsp_SpInkStorm00.png'},
'Explosher':{'wimg':'3/Path_Wst_Slosher_Washtub_00.png','subname':'Point Sensor','subimg':'Wsb_PointSensor00.png','spename':'Ink Storm','speimg':'Wsp_SpInkStorm00.png'},
'Mini Splatling':{'wimg':'3/Path_Wst_Spinner_Quick_00.png','subname':'Burst Bomb','subimg':'Wsb_Bomb_Quick00.png','spename':'Ultra Stamp','speimg':'Wsp_SpUltraStamp00.png'},
'Heavy Splatling':{'wimg':'3/Path_Wst_Spinner_Standard_00.png','subname':'Sprinkler','subimg':'Wsb_Sprinkler00.png','spename':'Wave Breaker','speimg':'Wsp_SpShockSonar00.png'},
'Hydra Splatling':{'wimg':'3/Path_Wst_Spinner_Hyper_00.png','subname':'Autobomb','subimg':'Wsb_Bomb_Robot00.png','spename':'Booyah Bomb','speimg':'Wsp_SpNiceBall00.png'},
'Ballpoint Splatling':{'wimg':'3/Path_Wst_Spinner_Downpour_00.png','subname':'Fizzy Bomb','subimg':'Wsb_Bomb_Fizzy00.png','spename':'Inkjet','speimg':'Wsp_SpJetpack00.png'},
'Nautilus 47':{'wimg':'3/Path_Wst_Spinner_Serein_00.png','subname':'Point Sensor','subimg':'Wsb_PointSensor00.png','spename':'Ink Storm','speimg':'Wsp_SpInkStorm00.png'},
'Dapple Dualies':{'wimg':'3/Path_Wst_Maneuver_Short_00.png','subname':'Squid Beakon','subimg':'Wsb_Beacon00.png','spename':'Tacticooler','speimg':'Wsp_SpEnergyStand00.png'},
'Splat Dualies':{'wimg':'3/Path_Wst_Maneuver_Normal_00.png','subname':'Suction Bomb','subimg':'Wsb_Bomb_Suction00.png','spename':'Crab Tank','speimg':'Wsp_SpChariot00.png'},
'Glooga Dualies':{'wimg':'3/Path_Wst_Maneuver_Gallon_00.png','subname':'Splash Wall','subimg':'Wsb_Shield00.png','spename':'Booyah Bomb','speimg':'Wsp_SpNiceBall00.png'},
'Dualie Squelchers':{'wimg':'3/Path_Wst_Maneuver_Dual_00.png','subname':'Splat Bomb','subimg':'Wsb_Bomb_Splash00.png','spename':'Wave Breaker','speimg':'Wsp_SpShockSonar00.png'},
'Dark Tetra Dualies':{'wimg':'3/Path_Wst_Maneuver_Stepper_00.png','subname':'Autobomb','subimg':'Wsb_Bomb_Robot00.png','spename':'Reefslider','speimg':'Wsp_SpSkewer00.png'},
'Splat Brella':{'wimg':'3/Path_Wst_Shelter_Normal_00.png','subname':'Sprinkler','subimg':'Wsb_Sprinkler00.png','spename':'Triple Inkstrike','speimg':'Wsp_SpTripleTornado00.png'},
'Tenta Brella':{'wimg':'3/Path_Wst_Shelter_Wide_00.png','subname':'Squid Beakon','subimg':'Wsb_Beacon00.png','spename':'Ink Vac','speimg':'Wsp_SpBlower00.png'},
'Undercover Brella':{'wimg':'3/Path_Wst_Shelter_Compact_00.png','subname':'Ink Mine','subimg':'Wsb_Trap00.png','spename':'Reefslider','speimg':'Wsp_SpSkewer00.png'},
'Tri-Stringer':{'wimg':'3/Path_Wst_Stringer_Normal_00.png','subname':'Toxic Mist','subimg':'Wsb_PoisonMist00.png','spename':'Killer Wail 5.1','speimg':'Wsp_SpMicroLaser00.png'},
'REEF-LUX 450':{'wimg':'3/Path_Wst_Stringer_Short_00.png','subname':'Curling Bomb','subimg':'Wsb_Bomb_Curling00.png','spename':'Tenta Missiles','speimg':'Wsp_SpMultiMissile00.png'},
'Splatana Stamper':{'wimg':'3/Path_Wst_Saber_Normal_00.png','subname':'Burst Bomb','subimg':'Wsb_Bomb_Quick00.png','spename':'Zipcaster','speimg':'Wsp_SpSuperHook00.png'},
'Splatana Wiper':{'wimg':'3/Path_Wst_Saber_Lite_00.png','subname':'Torpedo','subimg':'Wsb_Bomb_Torpedo00.png','spename':'Ultra Stamp','speimg':'Wsp_SpUltraStamp00.png'},
'Big Swig Roller':{'wimg':'3/256px-S3_Weapon_Main_Big_Swig_Roller.png','subname':'Splash Wall','subimg':'Wsb_Shield00.png','spename':'Ink Vac','speimg':'Wsp_SpBlower00.png'},
'Snipewriter 5H':{'wimg':'3/256px-S3_Weapon_Main_Snipewriter_5H.png','subname':'Sprinkler','subimg':'Wsb_Sprinkler00.png','spename':'Tacticooler','speimg':'Wsp_SpEnergyStand00.png'},
'Splattershot Nova':{'wimg':'3/256px-S3_Weapon_Main_Splattershot_Nova.png','subname':'Point Sensor','subimg':'Wsb_PointSensor00.png','spename':'Killer Wail 5.1','speimg':'Wsp_SpMicroLaser00.png'},
'Random':{'wimg':'3/random.png','subname':'Random','subimg':'Random.png','spename':'Random','speimg':'random.png'},
}


subweapon_path ="subspe/"
subweapons={
"小鸡":"Wsb_Bomb_Robo.png",
"水球":"Wsb_Bomb_Quick.png",
"冰壶":"Wsb_Bomb_Curling.png",
"碳酸弹":"Wsb_Bomb_Piyo.png",
"陷阱": "Wsb_TimerTrap.png",
"追踪器": "Wsb_PointSensor.png",
"雨帘": "Wsb_Shield.png",
"三角雷": "Wsb_Bomb_Splash.png",
"花洒":"Wsb_Sprinkler.png",
"跳点": "Wsb_Flag.png",
"粘弹": "Wsb_Bomb_Suction.png",
"鱼雷": "Wsb_Bomb_Tako.png",
"毒雾": "Wsb_PoisonFog.png"
}

specials={
"导弹": "Wsp_SuperMissile.png",
"仓鼠球": "Wsp_AquaBall.png",
"捶地": "Wsp_SuperLanding.png",
"泡泡": "Wsp_SuperBubble.png",
"墨甲": "Wsp_SuperArmor.png",
"飞机": "Wsp_Jetpack.png",
"水枪": "Wsp_WaterCutter.png",
"雨": "Wsp_RainCloud.png",
"粘弹rush": "Wsp_LauncherSuction.png",
"小鸡rush": "Wsp_LauncherRobo.png",
"三角雷rush": "Wsp_LauncherSplash.png",
"水球rush": "Wsp_LauncherQuick.png",
"冰壶rush": "Wsp_LauncherCurling.png",
"nice弹": "Wsp_BooyahBomb.png",
"大锤": "Wsp_Ultra_Stamp.png"}

 
