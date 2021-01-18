import csv

from _globals import _package_data
new_ids = {}

ENTSOE_new_ids = ['34WETL-KOSTA---J',
                '49W000000000078J', '18WHFIBGES-123-H', '47W000000000243N', '48WSTN00000STVEO', '48WSTN00000HUNBV',
                 '12W-0000000033-I', '48WSTN00000GYARR', '48WSTN00000GRUBR', '26WIMPI-S09NPMVB', '48WSTN00000PETEV',
                 '34WETL-KOSTB---E', '48WSTN00000LAGA3', '47W000000000231U', '48WSTN000ABTHGTK', '48WSTN00000BRYPC',
                 '47W000000000240T', '18WTFSEDAE-123-Q', '48WSTN0000EGGPS5', '11WATKAUN2HRWEAB', '18WPGR3-12345-0L',
                 '18WTFDETIC-123-Y', '18WHFGASN-1234-B', '18WEBRACC1-123-Y', '11WD7RHAU5G-3--3', '12W-0000000011-W',
                 '48WSTN0000RYHPSI', '34WEHP-DJE-1---R', '46WPU0000000023X', '26WIMPI-0417217K', '48WSTN00000EECLC',
                 '26WIMPI-S09RSLCK', '48WSTN00000ROCKK', '12W-0000000031-O', '48WSTN0000BARKBL', '48WSTN0000WBUPSE',
                 '26WIMPI-0155970W', '49W000000000072V', '48WSTN00000ROOS5', '26WIMPI-S03T1CNB', '48WSTN00000MRWDO',
                 '48WSTN00000PEHEU', '26WIMYI-S12CESLB', '32W001100100233F', '48WSTN00000SHOSS', '48WSTN00000DNGBQ',
                 '16WRTG---------V', '48WSTN1000COTPSQ', '18WSLTB-12345-05', '48WSTN0000CACON2', '26WIMPI-01477335',
                 '11WD43VIWXHOILLM', '18W18WSRI4--123V', '18WSILB-12345-0I', '27W-PU-EPC1----Y', '11WD4GKM-2CD4--J',
                 '18WSLTG-12345-0T', '18WMLTB-12345-09', '26WIMPI-S08TEMP6', '18WUFMI-12345-0L', '48WSTN10000DINOQ',
                 '12W-0000000013-Q', '47W000000000153O', '26WIMPI-S07VTDR2', '17W100P100P03493', '26WIMYI-0157750B',
                 '48WSTN00000MARKJ', '47W000000000155K', '34WEHP-BBASH---V', '26WIMZI-S10TERN0', '26WIMPI-01113115',
                 '18WACE3-12345-00', '18WPGR4-12345-0B', '49W000000000074R', '48WSTN000KEADGT6', '18WESCCC1-123-0T', '48WSTN00000STAYA', '26WIMPI-S09TFRMO', '26WIMPI-01128175', '26WIMPI-0157973G', '18WEBRFEN-123-0T', '34WETL-KOSOA---C', '18WSIL-123456-0G', '47W000000000242P', '26WIMPI-S03ATSMM', '27W-PU-EECK----8', '18WHFEGED-1234-V', '26WIMPI-C20TLRA7', '34WETG-NOSAD---Z', '27W-PU-ETEM----A', '34WETL-KOLUA---P', '18WCCO3-12345-0C', '12W-0000000026-D', '34WETL-TENTA---G', '27W-PU-EDET----M', '26WIMPI-0166990F', '49W000000000090T', '26WIMPI-0605986C', '48WSTN00000KEAD4', '27W-PU-ECHV----Y', '26WIMPI-S03PTRMO', '48WSTN0000RUGPS5', '48WSTN00000DEEP3', '18WDUER-12345-0N', '18WHFERRAT-123-C', '34WEHA-BISTR---W', '26WIMPI-S08FCTVE', '12W-0000000105-J', '18WALG3-12345--K', '27W-PU-EME3----W', '12W-0000000021-S', '27W-PU-EPR2----Y', '18WUFGC--1234-00', '48WSTN0000RUGGTU', '48WSTN00000GRMOP', '49W000000000096H', '36W-TE-UGLJEVIKN', '17W100P100P0353C', '48WSTN00000FELLH', '26WIMPI-S03SRCOL', '26WIMPI-S19EPRGR', '18WGDLQ-12345-0A', '18WPGR5-123456-J', '18WAMBIETA-12-0S', '26WIMPI-S09IPNT0', '26WIMPI-S13CTTM2', '48WSTN00000LBARK', '34WEHR-BBASR---X', '47W000000000244L', '27W-PU-EPC2----S', '26WIMPI-0122141U', '27W-PU-ETU2----I', '18WENDPRB-123-0T', '34WETG-ZRENJ---4', '26WIMPI-00524433', '36W-HE-VISEGRADJ', '48WSTN00000BAGE8', '34WETL-TENTB---B', '18WTFIBGES-123-9', '18WPBCN1-12345-D', '48WSTN0000ABTHBN', '18WDUEB-12345-0Z', '48WSTN0000CAKILT', '18WEBRACC2-123-R', '48WSTN0000CAGARK', '12W-0000000925-8', '18WHCHI-12345-0M', '36W-HE-DUBROV--K', '33W--TEC-TE-TO-B', '26WIMPI-S04CTNT7', '26WIMPI-0601951E', '48WSTN0000SHBABF', '18WFFNEXU-1234-4', '18WTAPOWER-12-0V', '26WIMPI-S03BBSR5', '18WESCCC3-123-0D', '48WSTN0000WBURB5', '48WSTN00000DAMCL', '50WP00000000733T', '12W-0000000035-C', '18WJUCA-12345-0Q', '48WSTN000FIDL-GA', '19W0000000002337', '26WIMPI-S09CSPLS', '48WSTN00000STCRI', '48WSTN0000CABEUM', '48WSTN0000CNQPSG', '18WMLTG-12345-0X', '48WSTN00000SIZBP', '26WIMPI-S20CWFTT', '18WGDNA-12345-00', '48WSTN00000RATS9', '48WSTN000DRAXXGK', '18WVIES-12345-0Y', '48WSTN00000DERWO', '18WEBRA-12345-06', '18WESCCC2-123-0L', '18WBAHIAB-123-0X', '27W-PU-EDUK----1', '47W000000000154M', '12W-0000000016-H', '18WTJEG-12345-0K', '18WSBEU-12345-0Q', '26WIMPI-S03UETNE', '26WIMPI-S12TRRLD', '48WSTN00000SHBAT', '36W-TE-KAKANJ--S', '18WTERE-12345-0V', '18WPBCN2-12345-4', '48WSTN00000LOCGL', '48WSTN00000SFILV', '48WSTN000LBAR-G1', '48WSTN0000IRNPS9', '48WSTN0000CAMORS', '26WIMPI-S19APGPP', '48WSTN0000WBUGT2', '26WIMPI-S03NCDCG', '48WSTN00000PEMBL', '18WSPSAETI-123-T', '27W-PU-ELED----H', '26WIMPI-0073522R', '26WIMPI-0138765U', '26WIMPI-S14ENRGS', '47W000000000156I', '11WD72VIA2H-KW-0', '48WSTN0000KILNSJ', '48WSTN00000SCCLO', '48WSTN0000CACLUY', '34WETL-MORAV---H', '18WTARRAG-123-03', '15WALPIQ-----PPY', '27W-PU-ETI1----Y', '48WSTN000FERR-GE', '34WEHP-DJE-2---M', '50WP000000001491', '36W-TE-TUZLA---K', '26WIMPI-0092784R', '48WSTN00000LAIGM', '26WIMPI-S07SMNC8', '47W000000000241R', '48WSTN0000LNMTHP', '26WIMPI-S12MCBL8', '26WIMPI-S12MCNTU', '36W-TE-GACKO---O', '36W-TE-STANARI-V', '18WSFWMARK-123-N', '18WPGR1-12345-04', '48WSTN000RATSGTB', '48WSTN00000FERRO', '11WD2KUET000160J', '48WSTN00000LOAND', '18WTEES-12345-0Y', '36W-HECAPLJINA-1', '18WPGR2-12345-0V', '26WIMPI-S04MTDRS', '34WETL-KOSOB---7', '18WTJEB-12345-0X']

GEO_new_ids = ['GEO40107', 'GEO39868', 'GEO44115', 'GEO42685', 'GEO44001', 'GEO44768', 'GEO39894', 'GEO39834',
                 'GEO40002', 'GEO2429', 'GEO39977', 'GEO39978', 'GEO40010', 'GEO39869', 'GEO42778', 'GEO39881',
                 'GEO4776', 'GEO42691', 'GEO44129', 'GEO44809', 'GEO42690', 'GEO40605', 'GEO39844', 'GEO44770',
                 'GEO6032', 'GEO43778', 'GEO5165', 'GEO44805', 'GEO4107', 'GEO39887', 'GEO42694', 'GEO44124', 'GEO40055',
                 'GEO2643', 'GEO43938', 'GEO45687', 'GEO39953', 'GEO39941', 'GEO44455', 'GEO44108', 'GEO3170', 'GEO42369',
                 'GEO40094', 'GEO44771', 'GEO39877', 'GEO39891', 'GEO42159', 'GEO44004', 'GEO44232', 'GEO41958', 'GEO42780',
                 'GEO39981', 'GEO44123', 'GEO40084', 'GEO39842', 'GEO42666', 'GEO44766', 'GEO39836', 'GEO2401', 'GEO39870', 'GEO45688',
                 'GEO39875', 'GEO46117', 'GEO39866', 'GEO43569', 'GEO40109', 'GEO44258', 'GEO44113', 'GEO39841', 'GEO42688', 'GEO42693',
                 'GEO39999', 'GEO3863', 'GEO40053', 'GEO40031', 'GEO42681', 'GEO44118', 'GEO40100', 'GEO42118', 'GEO39964', 'GEO42692',
                 'GEO41994', 'GEO3177', 'GEO45399', 'GEO44007', 'GEO44117', 'GEO45689', 'GEO39835', 'GEO42327', 'GEO42696', 'GEO44122',
                 'GEO41995', 'GEO44764', 'GEO39826', 'GEO40040', 'GEO2928', 'GEO40046', 'GEO42177', 'GEO39973', 'GEO40078', 'GEO42357',
                 'GEO44767', 'GEO39886', 'GEO42686', 'GEO42779', 'GEO44811', 'GEO44791', 'GEO39871', 'GEO2905', 'GEO2248', 'GEO44120',
                 'GEO41983', 'GEO46223', 'GEO41988', 'GEO39863', 'GEO39872', 'GEO39909', 'GEO3389', 'GEO43787', 'GEO42171', 'GEO39853',
                 'GEO41955', 'GEO41145', 'GEO40000', 'GEO44229', 'GEO44112', 'GEO5180', 'GEO41960', 'GEO40072', 'GEO39951', 'GEO44806',
                 'GEO40088', 'GEO43567', 'GEO39993', 'GEO42008', 'GEO40075', 'GEO40062', 'GEO3687', 'GEO40106', 'GEO44119', 'GEO40065',
                 'GEO44116', 'GEO44126', 'GEO42682', 'GEO42768', 'GEO39940', 'GEO45686', 'GEO44773', 'GEO40020', 'GEO44813', 'GEO40032',
                 'GEO44522', 'GEO40972', 'GEO42695', 'GEO39970', 'GEO44324', 'GEO39876', 'GEO40073', 'GEO5387', 'GEO39932', 'GEO45622',
                 'GEO5726', 'GEO40093', 'GEO44240', 'GEO40005', 'GEO43786', 'GEO42168', 'GEO44130', 'GEO40009', 'GEO42714', 'GEO40054',
                 'GEO44114', 'GEO39906', 'GEO41134', 'GEO39917', 'GEO39914', 'GEO44125', 'GEO41992', 'GEO39907', 'GEO40008', 'GEO39967', 'GEO39986', 'GEO42167', 'GEO45435', 'GEO44526', 'GEO40007', 'GEO39926', 'GEO39852', 'GEO40102', 'GEO40603', 'GEO45436', 'GEO40070', 'GEO43836', 'GEO39889', 'GEO41963', 'GEO42179', 'GEO43579', 'GEO39989', 'GEO42664', 'GEO39857', 'GEO46186', 'GEO44474', 'GEO42170', 'GEO40098', 'GEO41987', 'GEO40015', 'GEO2711', 'GEO41999', 'GEO43816', 'GEO40039', 'GEO39758', 'GEO41961', 'GEO42169', 'GEO39898', 'GEO39976', 'GEO45718', 'GEO40051', 'GEO43937', 'GEO40030', 'GEO44228', 'GEO40096', 'GEO43838', 'GEO3211', 'GEO44824', 'GEO40019', 'GEO39998', 'GEO40016', 'GEO39918', 'GEO43800', 'GEO3753', 'GEO44808', 'GEO42639', 'GEO42689', 'GEO41989', 'GEO41980', 'GEO39883', 'GEO40108', 'GEO44230', 'GEO3631', 'GEO43833', 'GEO3157', 'GEO2068', 'GEO46119', 'GEO3203', 'GEO39828', 'GEO39846', 'GEO2201', 'GEO2791', 'GEO45871', 'GEO39982', 'GEO39921', 'GEO43790', 'GEO39864', 'GEO4071', 'GEO41979', 'GEO5676', 'GEO39969', 'GEO39873', 'GEO44794', 'GEO44111', 'GEO4766', 'GEO39851', 'GEO40063', 'GEO42178', 'GEO44322', 'GEO40606', 'GEO42687', 'GEO40077', 'GEO44772', 'GEO39840', 'GEO39925', 'GEO43987', 'GEO4963', 'GEO43980', 'GEO40103', 'GEO43701', 'GEO40034', 'GEO5229', 'GEO4000', 'GEO44233', 'GEO39832', 'GEO41993', 'GEO39902', 'GEO44008', 'GEO39838', 'GEO43931', 'GEO45655', 'GEO41957', 'GEO39827', 'GEO40056', 'GEO40069', 'GEO39991', 'GEO44009', 'GEO43568', 'GEO41136', 'GEO40071', 'GEO40049', 'GEO39980', 'GEO40068', 'GEO41981', 'GEO40064', 'GEO39983', 'GEO46118', 'GEO43936', 'GEO40080', 'GEO2453', 'GEO44818', 'GEO40074', 'GEO45209', 'GEO5302', 'GEO45424', 'GEO42697', 'GEO39996', 'GEO44521', 'GEO39974', 'GEO5075', 'GEO40041', 'GEO40105', 'GEO43563', 'GEO40012', 'GEO4604', 'GEO39936', 'GEO40067', 'GEO39862', 'GEO39829', 'GEO44127', 'GEO41954', 'GEO40091', 'GEO40023', 'GEO40057', 'GEO41991', 'GEO44538', 'GEO40033', 'GEO44128', 'GEO44792', 'GEO44765', 'GEO39912', 'GEO41135', 'GEO44121', 'GEO40104', 'GEO45769', 'GEO40101', 'GEO40045', 'GEO44793']

new_ids['ENTSOE'] = ENTSOE_new_ids
new_ids['GEO'] = GEO_new_ids

new_ids_list = []
for ds_name, id_list in new_ids.items():

    for id in id_list:
        new_ids_list.append( (ds_name, id))

new_id_spec = _package_data("new_ids.csv")
with open(new_id_spec, 'w', newline="") as fh: 
    
    write = csv.writer(fh)  

    header = ["DataSet", "projectID"]
    write.writerow(header)
    write.writerows(new_ids_list)








