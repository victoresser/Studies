function Cadastrar() {
    var sh = SpreadsheetApp.getActive();
    var nm = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet().getName();
    var form = sh.getSheetByName(nm);
    var base = sh.getSheetByName('Base');
  
    sh.setActiveSheet(form, true);
  
    var data = sh.getRange('C4').getValue();
    var usuario = sh.getRange('C6').getValue();
  
    if (data === ''){
      Browser.msgBox('Data não informada!');
    } else if (usuario === ''){
      Browser.msgBox('Usuário não informado!');
    } else {
      var itens = sh.getRange('B9:B38').getValues();
      var qtdes = sh.getRange('C9:C38').getValues();
      var vunits = sh.getRange('D9:D38').getValues();
      var descontos = sh.getRange('E9:E38').getValues();
      var vtotais = sh.getRange('F9:F38').getValues();
      var obs = sh.getRange('G9:G38').getValues();
      var descAplicado = sh.getRange('H9:H38').getValues();
      var formPag = sh.getRange('I9:I38').getValues();
      var x = base.getLastRow()+1;
  
      for (var i in itens) {
        var item = itens[i][0]
        var qtde = qtdes[i][0]
        var vunit = vunits[i][0]
        var desconto = descontos[i][0]
        var vtotal = vtotais[i][0]
        var observ = obs[i][0]
        var descAplic = descAplicado[i][0]
        var pag = formPag[i][0]

        if (nm == "Controle Caixa") {
            if (item !== '') {
                if (qtde !== '') {
                  base.getRange(x,1).setValue(data);
                  base.getRange(x,2).setValue(item);
                  base.getRange(x,3).setValue(qtde);
                  base.getRange(x,4).setValue(vunit);
                  base.getRange(x,5).setValue(desconto);
                  base.getRange(x,6).setValue(vtotal);
                  base.getRange(x,7).setValue(usuario);
                  base.getRange(x,8).setValue('Saída');
                  base.getRange(x,9).setValue(observ);
                  base.getRange(x,10).setValue(descAplic);
                  base.getRange(x,11).setValue(pag);
                  x+=1
                } else {
                  msg = 'Não foi informado a quantidade para o item '+ item +'! O mesmo não foi cadastrado.'
                  Browser.msgBox(msg);
                }
            }
        }

        if (nm == "Controle Estoque") {
            if (item !== '') {
                if (qtde !== '') {
                  base.getRange(x,1).setValue(data);
                  base.getRange(x,2).setValue(item);
                  base.getRange(x,3).setValue(qtde);
                  base.getRange(x,4).setValue(vunit);
                  base.getRange(x,5).setValue(desconto);
                  base.getRange(x,6).setValue(vtotal);
                  base.getRange(x,7).setValue(usuario);
                  base.getRange(x,8).setValue(observ === "%Entrada%" ? 'Entrada' : 'Baixa');
                  base.getRange(x,9).setValue(observ);
                  base.getRange(x,10).setValue(descAplic);
                  base.getRange(x,11).setValue(pag);
                  x+=1
                } else {
                  msg = 'Não foi informado a quantidade para o item '+ item +'! O mesmo não foi cadastrado.'
                  Browser.msgBox(msg);
                }
            }
        }
      }
      form.getRange('B9:C38').clearContent();
      // Browser.msgBox('Limpei B9');
      form.getRange('G9:G38').clearContent();
      // Browser.msgBox('Limpei G9');
      form.getRange('C4:E4').clearContent();
      // Browser.msgBox('Limpei C4');
      form.getRange('C6:E6').clearContent();
      // Browser.msgBox('Limpei C6');
      form.getRange('C9:C38').clearContent();
      // Browser.msgBox('Limpei C9');
      Browser.msgBox('Dados salvos com sucesso!');
    }
  }
  