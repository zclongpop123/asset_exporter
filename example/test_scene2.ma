//Maya ASCII 2018ff09 scene
//Name: test_scene2.ma
//Last modified: Mon, Jan 24, 2022 11:19:27 AM
//Codeset: 936
file -rdi 1 -ns "rig" -rfn "rigRN" -op "v=0;" -typ "mayaAscii" "D:/work/asset_exporter/example/ball.ma";
file -rdi 1 -ns "rig1" -rfn "rigRN1" -op "v=0;" -typ "mayaAscii" "D:/work/asset_exporter/example/ball.ma";
file -r -ns "rig" -dr 1 -rfn "rigRN" -op "v=0;" -typ "mayaAscii" "D:/work/asset_exporter/example/ball.ma";
file -r -ns "rig1" -dr 1 -rfn "rigRN1" -op "v=0;" -typ "mayaAscii" "D:/work/asset_exporter/example/ball.ma";
requires maya "2018ff09";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201903222215-65bada0e52";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -n "cameras";
	rename -uid "EF0EE5B9-4678-CEAD-A90E-3C8FB94A1066";
createNode transform -n "camera1" -p "cameras";
	rename -uid "D71F92F7-482C-0076-1302-C997D4D79417";
createNode camera -n "cameraShape1" -p "camera1";
	rename -uid "1204ACEF-4C9C-F098-BD13-AFACAB14B9D4";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".cap" -type "double2" 1.41732 0.94488 ;
	setAttr ".ff" 0;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "camera1";
	setAttr ".den" -type "string" "camera1_depth";
	setAttr ".man" -type "string" "camera1_mask";
createNode transform -n "camera2" -p "cameras";
	rename -uid "C1EFDC6C-45F5-13EE-2B59-9F8902F08CA9";
	setAttr ".t" -type "double3" 4 0 0 ;
createNode camera -n "cameraShape2" -p "camera2";
	rename -uid "DA8C2C0E-464E-0085-CA3B-8DACCF27DBA2";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".cap" -type "double2" 1.41732 0.94488 ;
	setAttr ".ff" 0;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "camera2";
	setAttr ".den" -type "string" "camera2_depth";
	setAttr ".man" -type "string" "camera2_mask";
createNode reference -n "rigRN";
	rename -uid "7C76EECB-4FDB-3DDF-2E63-F99C2086C373";
	setAttr ".ed" -type "dataReferenceEdits" 
		"rigRN"
		"rigRN" 0;
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode reference -n "rigRN1";
	rename -uid "DA32B07F-4329-282F-5B4A-649F9D80423F";
	setAttr ".ed" -type "dataReferenceEdits" 
		"rigRN1"
		"rigRN1" 0;
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -s 10 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
// End of test_scene2.ma
