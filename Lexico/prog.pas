program teste;
var entrada, aux, te1 : integer;
te, ti : integer;
procedure umprocedimento(argproc1, argproc2 : integer; argproc3, argproc4 : integer);
        var procvar, pvar : integer;
        intprocvar, ppvar : integer;
        procedure outroproc;
            var x : integer;
            begin
                v := 1;
                procvar := +(intprocvar,v);
            end;
        procedure maisumproc;
            var x : integer;
            begin
                v := 1;
            end;    
    begin
        procvar := 1;
        intprocvar := 34;
        ppvar := +(intprocvar,2);
        outroproc ();
        maisumproc ();
    end;
function umafuncao(funcvar : integer) : integer;
    begin
        funcvar := 1;
    end;
begin;
    entrada := *(15,2);
    if (> ( entrada , 15 )) then
    begin
        aux := 5;
    end;
    umprocedimento ();
end

