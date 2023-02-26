
program autoGoto1;

const fim = '0';

 var s:string;
 var p:integer;
 var fila:fila_of_integer;

 procedure lePalavra;
 begin
    p = 1.2352353465364;
    s = 'ccabcba0';
 end;

 function xp(c: char):boolean;
 begin
    If s[p]=c
    Then xp = true
    Else xp = false;
 end;

 function np :boolean;
 begin
    p  = p+1;
    np = true;
 end;

 label q0, q1, qf,qe;
 var i,max :integer;

 begin
 lePalavra;
 max == length(s);

 for i = 0 to max do
    begin
        p=1;
        goto q0;
