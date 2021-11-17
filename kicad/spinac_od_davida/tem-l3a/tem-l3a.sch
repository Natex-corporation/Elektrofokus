EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Timer:LM555xM U1
U 1 1 618B7B92
P 6100 3800
F 0 "U1" H 6100 4381 50  0000 C CNN
F 1 "LM555xM" H 6100 4290 50  0000 C CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 6950 3400 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm555.pdf" H 6950 3400 50  0001 C CNN
	1    6100 3800
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW2
U 1 1 618B8F0E
P 4750 4450
F 0 "SW2" H 4750 4735 50  0000 C CNN
F 1 "SW_Push" H 4750 4644 50  0000 C CNN
F 2 "" H 4750 4650 50  0001 C CNN
F 3 "~" H 4750 4650 50  0001 C CNN
	1    4750 4450
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_Small R1
U 1 1 618B98AB
P 4750 3200
F 0 "R1" H 4809 3246 50  0000 L CNN
F 1 "R_Small" H 4809 3155 50  0000 L CNN
F 2 "" H 4750 3200 50  0001 C CNN
F 3 "~" H 4750 3200 50  0001 C CNN
	1    4750 3200
	1    0    0    -1  
$EndComp
$Comp
L Device:CP C1
U 1 1 618BA883
P 6950 4450
F 0 "C1" H 7068 4496 50  0000 L CNN
F 1 "CP" H 7068 4405 50  0000 L CNN
F 2 "" H 6988 4300 50  0001 C CNN
F 3 "~" H 6950 4450 50  0001 C CNN
	1    6950 4450
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D1
U 1 1 618BAE08
P 8300 4450
F 0 "D1" H 8293 4667 50  0000 C CNN
F 1 "LED" H 8293 4576 50  0000 C CNN
F 2 "" H 8300 4450 50  0001 C CNN
F 3 "~" H 8300 4450 50  0001 C CNN
	1    8300 4450
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_Small R3
U 1 1 618BD2C7
P 8300 3950
F 0 "R3" H 8359 3996 50  0000 L CNN
F 1 "R_Small" H 8359 3905 50  0000 L CNN
F 2 "" H 8300 3950 50  0001 C CNN
F 3 "~" H 8300 3950 50  0001 C CNN
	1    8300 3950
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW1
U 1 1 618BDABF
P 7800 4450
F 0 "SW1" H 7800 4735 50  0000 C CNN
F 1 "SW_Push" H 7800 4644 50  0000 C CNN
F 2 "" H 7800 4650 50  0001 C CNN
F 3 "~" H 7800 4650 50  0001 C CNN
	1    7800 4450
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_POT RV1
U 1 1 618BE14C
P 6950 2800
F 0 "RV1" H 6881 2846 50  0000 R CNN
F 1 "R_POT" H 6881 2755 50  0000 R CNN
F 2 "" H 6950 2800 50  0001 C CNN
F 3 "~" H 6950 2800 50  0001 C CNN
	1    6950 2800
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 618BF49D
P 5150 4300
F 0 "C?" H 5265 4346 50  0000 L CNN
F 1 "C" H 5265 4255 50  0000 L CNN
F 2 "" H 5188 4150 50  0001 C CNN
F 3 "~" H 5150 4300 50  0001 C CNN
	1    5150 4300
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 3800 5150 3800
Wire Wire Line
	5150 3800 5150 4150
Wire Wire Line
	5150 4450 5150 4750
Wire Wire Line
	5150 4750 6100 4750
Wire Wire Line
	6100 4750 6100 4200
Wire Wire Line
	5600 4000 5600 4250
Wire Wire Line
	5600 4250 7800 4250
Wire Wire Line
	7800 4650 7800 4750
Wire Wire Line
	7800 4750 6950 4750
Connection ~ 6100 4750
Wire Wire Line
	6950 4600 6950 4750
Connection ~ 6950 4750
Wire Wire Line
	6950 4750 6100 4750
Wire Wire Line
	6950 4300 6950 4000
Wire Wire Line
	6950 4000 6600 4000
Wire Wire Line
	6950 4000 6950 3800
Wire Wire Line
	6950 3800 6600 3800
Connection ~ 6950 4000
Wire Wire Line
	7800 4750 8300 4750
Wire Wire Line
	8300 4750 8300 4600
Connection ~ 7800 4750
Wire Wire Line
	8300 4300 8300 4050
Wire Wire Line
	8300 3850 8300 3600
Wire Wire Line
	8300 3600 6600 3600
$Comp
L Device:R_Small R2
U 1 1 618BD1DF
P 7800 3250
F 0 "R2" H 7859 3296 50  0000 L CNN
F 1 "R_Small" H 7859 3205 50  0000 L CNN
F 2 "" H 7800 3250 50  0001 C CNN
F 3 "~" H 7800 3250 50  0001 C CNN
	1    7800 3250
	1    0    0    -1  
$EndComp
Wire Wire Line
	7800 4250 7800 3350
Connection ~ 7800 4250
$Comp
L Device:R_Small R?
U 1 1 618CC1EB
P 6950 3200
F 0 "R?" H 7009 3246 50  0000 L CNN
F 1 "R_Small" H 7009 3155 50  0000 L CNN
F 2 "" H 6950 3200 50  0001 C CNN
F 3 "~" H 6950 3200 50  0001 C CNN
	1    6950 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	6950 3800 6950 3300
Connection ~ 6950 3800
Wire Wire Line
	6950 3100 6950 3000
Wire Wire Line
	6950 3000 7100 3000
Wire Wire Line
	7100 3000 7100 2800
Connection ~ 6950 3000
Wire Wire Line
	6950 3000 6950 2950
Wire Wire Line
	5600 3600 4750 3600
Wire Wire Line
	4750 3600 4750 4250
Wire Wire Line
	4750 4650 4750 4750
Wire Wire Line
	4750 4750 5150 4750
Connection ~ 5150 4750
Wire Wire Line
	4750 3600 4750 3300
Connection ~ 4750 3600
Wire Wire Line
	7800 3150 7800 2500
Wire Wire Line
	7800 2500 6950 2500
Wire Wire Line
	6950 2500 6950 2650
Wire Wire Line
	6950 2500 6100 2500
Wire Wire Line
	6100 2500 6100 3400
Connection ~ 6950 2500
Wire Wire Line
	6100 2500 4750 2500
Wire Wire Line
	4750 2500 4750 3100
Connection ~ 6100 2500
$Comp
L power:PWR_FLAG #FLG?
U 1 1 618D1DE5
P 3400 3950
F 0 "#FLG?" H 3400 4025 50  0001 C CNN
F 1 "PWR_FLAG" H 3400 4123 50  0000 C CNN
F 2 "" H 3400 3950 50  0001 C CNN
F 3 "~" H 3400 3950 50  0001 C CNN
	1    3400 3950
	1    0    0    -1  
$EndComp
$Comp
L power:PWR_FLAG #FLG?
U 1 1 618D20CC
P 3400 4250
F 0 "#FLG?" H 3400 4325 50  0001 C CNN
F 1 "PWR_FLAG" H 3400 4423 50  0000 C CNN
F 2 "" H 3400 4250 50  0001 C CNN
F 3 "~" H 3400 4250 50  0001 C CNN
	1    3400 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4750 2500 4000 2500
Wire Wire Line
	4000 2500 4000 3950
Wire Wire Line
	4000 3950 3400 3950
Connection ~ 4750 2500
Wire Wire Line
	3400 4250 4000 4250
Wire Wire Line
	4000 4250 4000 4750
Wire Wire Line
	4000 4750 4750 4750
Connection ~ 4750 4750
$EndSCHEMATC
