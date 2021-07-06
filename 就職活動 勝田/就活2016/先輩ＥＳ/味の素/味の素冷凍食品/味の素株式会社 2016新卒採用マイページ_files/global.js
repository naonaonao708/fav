mac=(navigator.appVersion.indexOf('Mac')!=-1)?true:false;
ie=(navigator.appName.charAt(0) == "M")?true:false;
document.write("<STYLE TYPE='text/css'><!--")
if(mac){
	document.write(".size10{font-size:10px; line-height:16px;}")
	document.write(".size12{font-size:12px; line-height:20px;}")
	document.write(".size10n{font-size:10px;}")
	document.write(".size12n{font-size:12px;}")
	document.write("A:link {COLOR:#3366FF; TEXT-DECORATION: underline}")
	document.write("A:hover {COLOR:#FFCC00; TEXT-DECORATION: underline}")
	document.write("A:visited {COLOR:#3366FF; TEXT-DECORATION: underline}")
}
else{
	if(ie){
		document.write(".size10{font-size:10px; line-height:16px;}")
		document.write(".size12{font-size:12px; line-height:20px;}")
		document.write(".size10n{font-size:10px;}")
		document.write(".size12n{font-size:12px;}")
		document.write("A:link {COLOR:#3366FF; TEXT-DECORATION: underline}")
		document.write("A:hover {COLOR:#FFCC00; TEXT-DECORATION: underline}")
		document.write("A:visited {COLOR:#3366FF; TEXT-DECORATION: underline}")
	}
	else{
		document.write(".size10{font-size:11px; line-height:16px;}")
		document.write(".size12{font-size:12px; line-height:20px;}")
		document.write(".size10n{font-size:11px;}")
		document.write(".size12n{font-size:12px;}")
		document.write("A:link {COLOR:#3366FF; TEXT-DECORATION: underline}")
		document.write("A:hover {COLOR:#FFCC00; TEXT-DECORATION: underline}")
		document.write("A:visited {COLOR:#3366FF; TEXT-DECORATION: underline}")
	}
}
//20060914 kousaka add Start
//アンケート項目のスタイルシートを書き出します
document.write("table.matrixComboTable{border: solid 1px #000000; border-collapse: collapse;}");
document.write("td.matrixCombo{font-size: 12px; border: solid 1px #000000; border-collapse: collapse;}");
document.write("td.matrixCombo1{border:none}");
//20060914 kousaka add End
document.write("//--></STYLE>");

function newImage(arg) {
	if (document.images) {
		rslt = new Image();
		rslt.src = arg;
		return rslt;
	}
}

function changeImages() {
	if (document.images && (preloadFlag == true)) {
		for (var i=0; i<changeImages.arguments.length; i+=2) {
			document[changeImages.arguments[i]].src = changeImages.arguments[i+1];
		}
	}
}

var preloadFlag = false;
function preloadImages() {
	if (document.images) {
		preloadFlag = true;
	}
}
//20060914 kousaka add Start
/**
 * テキストエリアの文字数をカウントします。<br>
 * @param str テキストエリアの入力値
 * @param flg 改行チェックフラグ（trueの場合は、改行をエスケープした文字数をカウントします。）
 * @return 文字数
 */
function textAreaCnt( str, flg ){
//◆2010/06/21 Mod Start - [常駐対応] 12PKG改善 No.75 文字数カウント改行コード対応
	var rep = "  ";	//半角スペース２つ

	if( flg ){
		rep = "";	//ブランク
	}

	//改行コードによる文字数の違いを統一
	str = str.replace(/\r\n|\r|\n/g, rep);
	var len = str.length;

	alert("現在の文字数は" + len + "文字です。");
//◆2010/06/21 Mod End
}

/**
 * ラジオボタンの選択を解除します。<br>
 * @param form    対象フォーム
 * @param nameVal 対象オブジェクトID
 * @param num     マトリックス個数（N4時に使用）
 */
function resetRadio( form, nameVal, num){
	var element = form.elements[nameVal];
	var undefinedFlg = true;
	
	if( element != null ){
		for( i = 0; i < element.length; i++ ){
			if( element[i].checked ){
				element[i].checked = false;
			}
			undefinedFlg = false;
		}
	}
	//選択肢が一つの場合のチェックを解除
	if( undefinedFlg ){
		element = null;
		if( document.getElementById ){
			element = document.getElementById(nameVal);
			element.checked = false;
		}else{
			if( num == 0 ){
				element = form.elements[nameVal];
				element.checked = false;
			}else{
				for( i = 1; i < num; i++ ){
					var strNameVal = nameVal + "_" + i;
					element = form.elements[strNameVal];
					
					if( element != null ){
						for( j = 0; j < element.length; j++ ){
							if( element[j].checked ){
								element[j].checked = false;
							}
						}
					}
				}
			}
		}
	}
}

/**
 * 郵便番号を入力内容から検索します<br>
 * @param yubin1	郵便番号１エレメント
 * @param yubin2	郵便番号２エレメント
 * @param form		フォームオブジェクト
 * @param ken 		県エレメント名称
 * @param address 住所エレメント名称
 */
function jsSearchAddress( yubin1, yubin2, form, ken, address ){
	var fname = form.name;
	var ybnno= yubin1.value + yubin2.value;
	if( ybnno.length == 7 && escape(ybnno).length == 7 ){
		var WinF01=window.open ("", "WinF01name", "height=200,width=400,scrollbars=yes,status=yes,toolbar=no,menubar=no,location=no,top=0,left=0");
		WinF01.opener = self;

		var form = document.createElement('form');
		document.body.appendChild(form);
		var input = document.createElement('input');
		input.setAttribute('type','hidden');
		input.setAttribute('name','ybnno');
		input.setAttribute('value', ybnno);
		var input2 = document.createElement('input');
		input2.setAttribute('type','hidden');
		input2.setAttribute('name','fname');
		input2.setAttribute('value',fname);
		var input3 = document.createElement('input');
		input3.setAttribute('type','hidden');
		input3.setAttribute('name','ken');
		input3.setAttribute('value',ken);
		var input4 = document.createElement('input');
		input4.setAttribute('type','hidden');
		input4.setAttribute('name','address');
		input4.setAttribute('value',address);
		form.appendChild(input);
		form.appendChild(input2);
		form.appendChild(input3);
		form.appendChild(input4);
		form.setAttribute('action','../ybnk/ysearch.php');
		form.setAttribute('target','WinF01name');
		form.setAttribute('method','post');
		form.submit();

	}else{
		alert("半角数値7文字で入力してください。");
		return false;
	}
}

/**
 * 郵便番号を住所から検索します<br>
 * @param yubin1Name	郵便番号１エレメント名称
 * @param yubin2Name	郵便番号２エレメント名称
 * @param kenName 		県エレメント名称
 * @param addressName 住所エレメント名称
 */
function jsSearchZip( yubin1Name, yubin2Name, kenName, addressName ){
	var formLength = document.forms.length;
	var formName = "";
	for( i = 0; i < formLength; i++ ){
		if( document.forms[i].elements[yubin1Name] ){
			if( document.forms[i].elements[yubin1Name].type == "text" ){
				formName = document.forms[i].elements[yubin1Name].form.name;
			}
		}
	}
	
	var url = "../ybnk/ybnk010.php?fname=" + formName + "&ybnz1=" + yubin1Name + "&ybnz2=" + yubin2Name + "&ken=" + kenName + "&address=" + addressName;
	var WinF01=window.open (url, "WinF01name", "height=400,width=500,scrollbars=yes,status=yes,toolbar=no,menubar=no,location=no,top=0,left=0");
	WinF01.opener = self;
}
//20060914 kousaka add End
