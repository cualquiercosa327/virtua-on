def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 256
    dictionary = {"{:02x}".format(i): i for i in range(dict_size)}

    w = ""
    result = []
    for i in range(0,len(uncompressed),2):
        c = uncompressed[i:i+2]
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result

def requiredBits(value):
    bits = 1
    while(value > 0):
        bits+=1
        value = value >> 1
    return bits

data ="68cc78b478f4780578157885683b684b7835686b7845688b689b786578757895181fc3681868386848685868686878688868c868d868e868f868096819682968398496859686968796889689968b968c968d968e968f9680a681a682a683a684a685a686a687a688a689a68aa68ba68ca68da68ea681b683b684b685b686b687b68868ab68bb789578a578b578c56867687768d768e768f76808182fa16838686868786888689868a868b868f868796889689968a968e568b668c668d668676877688789768a768b768c768e768f76808183f6068b868d668f468a968c768e5184f3068d668e568f4186f3048cd48fc48fb187f70482a484c485c48fc480b48cd48fb1881248694879489948a948b9482a483a484a485a486a487a488a489a48aa48ca48da480b481b482b483b484b485b486b487b488b489b48ab48bb48fb483c484c485c8fc189fa2483848484858486848784888489848a848b848c84849485948694879488948c948d948e948f9480a481a484a485a489a48aa48ba48ca48da48ea48fa41b48bb48d448f4480648464856486648c748d748e748f718af7248584878488848c848e848f84809481948294839480a481a48d448e448f44805483548454855485480648464856486648c648d648e648f6480748174827483748474857486748774887489748a718bfa04886489648a648b648e4480548154825489748a708eea29a198b198d198f198d298e298f298039813983398539863987398b398d398e398f398049814982498349844985498649874988498c498d498e498f4980598159825835984598559865987598169836985698762030e0c0d141200431046630351491040914b61491040914590475040914550474040914ba14c50455348a14c5047e24814c50423244814c50423348ae34a0423348ae34a04232448e34a047e2448e34a0455348af3a90400f3b5f3a904f8f3ea046604f80425046604f8f3eaf3a9f3173ea0466f317042504660400f3b50466f317f3eaf3a9f317042504660400045af3a90400045af3a904f80425f30804cce3cbf34d14a7e389040804cce3cb04d404e04db040004843409e32b043ae36904a80412044314e4043ae369e3ed045bf3491422045bf349e3ed0412f349f36704120443f3f904ed044304e11429f398f36804df398041604ed0443f32e1429f39804a7045df39804c214a7e389f33b04ed04db14220412f34904660400f3b5046604f8f3eaf3a904f80425f3a904f8f3ea0466f17f3eaf3a9f3170425f3a90400f3b5f3a9f317f3ea0466f3170425f3a90400045a04660400045a046604f80425e3d1040004bd143e040004bde3d104002452143e400245204d4042504e9f3680494f3d804a70494f3d8f33b042504e9e37e040914b6e37e04091459f39a04091455f39b040914ba0400f33df36ff38df3aef3bff3804610450040004d204a00482046104500482f3aef3bf0400f3cdf38ff30ef3eef3cff30e042104400400044204800402042104400402f3eef3cf040004ce040c040042504e981305020103040301150607080301190a0b0c00011c225d100770222820077e1915200775212e12000d2f1822220001252423220664252c2d1206662a72922066d1c182f13011a2c1e30400770282b120776292a1b22066b2b1a262206691a19272307770a090803005a3b3d3c33011c272f3142055143525c230503424454001125c1d12055c12535e33030d1112214e704091408a02055f2e283930408040004002050f21343e204000404f319205503734313f30804000400205583e22630408040004002055e24353230400f30cf319205533534373f308040004002050235333630400f30804002055633373830400f30c04f6205083730393040004044f62055930313f204000408040030711122e32804091408a02055e08171d0f308040004002050e0d0310104000404f3192055f0013161040804000400205571511d0f308040004002055d01141310400f30cf3192055216131410408040004002050115121410400f30804002055517161210400f30c04f620507181f061040004044f6205581e001f004000408040020e122040004ab048a6030007464c4d4040004b1f338300064b415c4040004b1f3383000a494f405040004b1f33830008474d4e040004b1f3383000b4a40515040004b1f33830009484e4f4040004b1f3383714c50455348a14c5047e244814c50423244814c50423348ae34a0423348ae34a0423448e34a047e2448e34a0455348a044e04eac309044e0409b3ea044e14fcb3ea044e14fcc309f3c114fcb3ea046e047ec309f3a1047ec309f3a11459b3ea046e145b3ea046e1459c309f3a11459c309f3c114fcc309f3c10409b3eaf3c104eac309046e047eb3eaf3a1047eb3eaf3a90400f3b5f3a904f8f3ea046604f804250466048f3eaf3a9f317f3ea0466f317042504660400f3b50466f317f3eaf3a9f317042504660400045af3a90400045af3a904f80425f30804cce3cbf34d14a7e38904080cce3cb04d404ed04db040004843409e32b043ae36904a804120443040b0412d343f3050412d34314e4043ae369e3ed045bf34904c70426c360f3000429d38914e4412e3c8e32b0412e3c81422045bf349e3ed0412f349f36704120443f3f904ed044304e11429f398f368045df398f3fa041ad343f3000412d338f3480426c3601400429d389041604ed04430415041ad343f32e1429f39804a7045df39804001423d3c604c214a7e389f33b04ed04db14220412f349040004b9b30f14000412d3380460400f3b5046604f8f3eaf3a904f80425f3a904f8f3ea0466f317f3eaf3a9f3170425f3a90400f3b5f3a9f317f3ea0466f3170425f3a90400045a04660400045a06604f80425f3a90400f3b5f3a904f8f3ea046604f80425046604f8f3eaf3a9f317f3ea0466f317042504660400f3b50466f317f3eaf3a9f317042504660400045a3a90400045af3a904f8042504660400f3b5046604f8f3eaf3a904f80425f3a904f8f3ea0466f317f3eaf3a9f3170425f3a90400f3b5f3a9f317f3ea0466f317042f3a90400045a04660400045a046604f80425e3d10400b3bd143e0400b3bde3d10400d352143e0400d352e3d1040004bd143e040004bde3d104002452143e0400242c2301110203040301150607080308890a0b0c0308841d051613082e07181f03077011121310066f3723400114482920077e243e30077a252730082c364a300880c2f32066e2d374232066235443e22066a2f25333206633b313a200610364c32077a213a352007773f2a2200054b2e3432000f27363532066637344922000831493420669282e3b22088a313b3d20082f364030088a3d2c32055c3d2c2032088c274d3f32055931482440077e2e372207772f3d3e2006652a362008224a364008264f242077830462340088346224206634721483008824f33420665262049300882462a33077306050403005c6d6f6e6300507173727403071d122e3280409c308a020555f5e545f3080400040020505545a57504000404f31920556575a5d50408040004002055e5c58545f3080400040020554585b5a50400f30cf319205595d5a5b500804000400205085c595b50400f30804002055c5e5d5950400f30c04f62050e5f565d50400040404f62055f555756504000408040030d1112214e704091408a020594842535040804000400205094b4e48404000404f3192055a415e4b4f3080400040020552584c405040804000400205584e4f4c40400f30cf3192055d4f4e415f08040004002050c4f4d4050400f3080400205505d415250400f30c04f620502515a4350400040404f6205535a4b49404000408040030711122e32804091408a0205a1423291f308040004002050a191f1c104000404f3192055b1c1f12204080400040020553212d191f30804000400205591d102f10400f30cf3192055e122f102008040004002050d112e1020400f30804002055123222e10400f30c04f620503242b1220400040404f6205542a1c1b104000408040030d1d12214e70409c308a02051606a6b604080400040020501636660604000404f319205526966636f308040004002055a60646860408040004002055066676460400f30cf319205556766696f08040004002050467656860400f30804002055865696a60400f30c04f62050a69626b60400040404f62055b626361604000408040055e3d1f33fb3bd143ef33fb3de3d1f33fd352143ef33fd352e3d1f33f04bd143ef33f04bde3d1f33f2452143ef33f245214c50422348a14c5047d244814c504222448e34a0422348ae34a0422248e34a047d2448044e04e9c309044e0408b3ea044e14ebb3ea044e14ebc309f3c114ebb3ea046e046dc309f3a1046dc309f3a11448b3ea046e1448b3ea046e1448309f3a11448c309f3c114ebc309f3c10408b3eaf3c104e9c309046e046db3eaf3a1046db3eaf3a90400f3b5f3a904f80400046604f80400f3a9f31704000466f31040004660400f3b504660400045af3a90400045af368045cf39804001428f39804a7045cf39804d404ec04db040004833409e3ed044af34904a804010443040b041d343f3050401d3431422044af349040004b8b30ff3000428d38914220401f349e3ed0401f349f36704010443f3f904ec0443f3fa0409d343f3000401d3381400028d389041604ec044304150409d343f33b04ec04db14000401d33804660400f3b5046604f80400f3a904f804000466f3170400f3a9f3170400f3a90400f3b5f3a9400045a04660400045af3a90400f3b5f3a904f80400046604f80400f3a9f31704000466f317040004660400f3b504660400045af3a90400045a04660400f3b504604f80400f3a904f804000466f3170400f3a9f3170400f3a90400f3b5f3a90400045a04660400045ae1300510204030300550608070101190a0b01011c0d0e0308800111213088a131b1c1308241d1e1513077617181910066b392820011c3a2b20077c27263008813e2b320660393d3332066438323c22077c2237372200033d2a302000c263534320665363c3b200008292722066b2a2a3d22088732383f2008873f2132088e2d393b320557292a2c3007703a392207792b393030066727382008282313008213b3823077b0d0c090403071d122e3280408c308203055c4b464d40400f30804003055a484749404000400f30830d1112214e7040814082030554434e350400040804003055042414f304000400f30830711122e328040814082030555242f1620400f308040030553212022204000400f30830d1d12214e70408c308203054535e4550400040804003055052515f404000400f30860e0c0d110c0414120043104662015e3d1f33fb3bd143ef33fb3bde3d1f33fd352143ef33fd352e3d1f3304bd143ef33f04bde3d1f33f2452143ef33f245214c50422348a14c5047d244814c504222448e34a0422348ae34a04222448e34a047d2448044e04e9c309044e048b3ea044e14ebb3ea044e14ebc309f3c114ebb3eaf3a11448b3ea046e1448b3ea046e1448c309f3a11448c309f3c114ebc309f3c10408b3eaf3c104e9c309e3c1000f3b5e3c104f80400e37e04f80400e3c1f3170400e37ef3170400e37e0400f3b5e37e0400045ae3c10400045af368045cf39804001428f39804a7045cf39804d44ec04db040004833409e3ed044af34904a804010443040b0401d343f3050401d3431422044af349040004b8b30ff3000428d38914220401f349e3ed0401f349f3604010443f3f904ec0443f3fa0409d343f3000401d33814000428d389041604ec044304150409d343f33b04ec04db14000401d338144e0400f3b5144e04f8040014104f80400144ef31704001491f317040014910400f3b514910400045a144e0400045ae3c10400f3b5e3c104f80400e37e04f80400e3c1f3170400e37ef3170400e7e0400f3b5e37e0400045ae3c10400045a144e0400f3b5144e04f80400149104f80400144ef31704001491f317040014910400f3b514910400045a144e0400045a1300510204030300550608070003390a0b00033c0d0e02033f00111212033813191a120bb4151617100bb73524200bb83627200338232230033d2a2732066c2539f220660343e282203382e233322000f29263c22000822313032066132383720066425232206672626392203333e243b20055d2b2a2003333b2d22033a2935373205325262830033c263522033527353c200bb32334200bb4233d200bbd2734220bbb0d0c0902020d12204000408c308c0205534945424f30804000400205544746480408040004002055b4a4d41504080400040020503424744404000416f3ca2055c405e4f4f308040004002055245464740400f3f9f3ca2050549484640400f3f90452055943444840400041604452050b4c4f4a404000416f3ca2055a4f4e4d40400f3f9f3ca2050d4e405150400f3f9044520551505c4b404000416044520112204004081408c02050c1b102d104000416f3ca2055b1e1f1020400f3f9f3ca2050e12212f10400f3f90445205522c1d1120400041604452055c304e3f3f30804000400050b3c3f3a304000416f3ca2055d102f1120408040004002055a3f3e3d30400f3f9f3ca2050d3e304140400f3f9044520551404c3b30400041604452055b3a3d310408040004002055c122e1b1f308040004002414c50422348a14c504222448e34a0422348ae34a04222448044e04e9c309044e0408b3ea044e14ebb3ea044e14eb309f3c114ebb3eaf3a11448b3ea046e1448b3ea046e1448c309f3a11448c309f3c114ebc309f3c10408b3eaf3c104e9c309e3c1040804bde3c114f01408e37e14f1408e3c1f31f1408e37ef31f1408e37e040804bde37e04082452e3c1040824520400045cf39804001428f398041604ec0443040004833409e3ed044af34904a80410443040b0401d343f3050401d3431422044af349040004b8b30ff3000428d38914220401f349e3ed0401f349f36704010443f3f904ec0443f3000401d3381400028d38914000401d338144e040804bd144e14f01408149114f01408144ef31f14081491f31f14081491040804bd149104082452144e04082452e3c10408b3bde3c14f0c308e37e14f0c308e3c1f31fc308e37ef31fc308e37e0408b3bde37e0408d352e3c10408d352144e0408b3bd144e14f0c308149114f0c308144ef31fc308149f31fc30814910408b3bd14910408d352144e0408d352c12033506070802033e090f00120bba0b0c0d0300003b2231330008333a39300bb72b1c10033d191722066292a2422066528232d12033d1322291200042e1b1122000d172625200666272c10066c1b1e120332232820200552202f12033f1a29222005591b172003312b1912339122921200bb9122a120bb204030103000d3c3e3f33000611181713000d2c2e2f2300031214151300053436373300004b324140000000000000000000000000000000000"

lzw = compress(data)
upper = max(lzw)
bits = requiredBits(upper)
print("orig size:{} bytes -> {} bytes using: {} bits".format(len(data)/2,len(lzw)*bits/8,bits))