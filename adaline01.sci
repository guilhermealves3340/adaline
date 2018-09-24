// implementação do Adaline para função lógica AND bipolar
// data: 18/09/2018
// autor: Keiji
// versão: 01

// entradas
x=[ 1  1
   -1  1
    1 -1
   -1 -1];

// target
t=[1 -1 -1 -1];

// inicialização dos parâmetros
alfa=0.12; // taxa de aprendizagem

// critérios de parada
erroquadraticoadmissivel=0.01;
ciclomaximo=100;
tolerancia=0.0001;// ajuste máximo admissivel dos pesos

// inicialização dos pesos entre -0.5 e +0.5
wanterior=rand(1,2)-0.5;
banterior=rand()-0.5;
wnovo=wanterior;
bnovo=banterior;
ylabel("Erroquadraticototal");
xlabel("Ciclos");
// treinamento da rede neural
disp('Treinando a rede neural....')
ciclos=0;
while ciclos< ciclomaximo
    ciclos=ciclos+1;
    erroquadraticototal=0;
    // inserir padroes de treinamento
    for padrao=1:4
        yin= banterior+ x(padrao,1)*wanterior(1)+x(padrao,2)*wanterior(2);
        erroquadraticototal=erroquadraticototal+0.5*(t(padrao)-yin)^2;
        // atualizacao dos pesos
        bnovo=banterior+alfa*(t(padrao)-yin);
        for k=1:2
        wnovo(k)=wanterior(k)+alfa*x(padrao,k)*(t(padrao)-yin);
        end
        wanterior=wnovo;
        banterior=bnovo;
    end

    plot(ciclos, erroquadraticototal,'r*');// plota com asterico vermelho
end
disp('----fim do treinamento-----');
disp('Pesos finais');

mprintf('wnovo(1): %2.4f  wnovo(2): %2.4f\n',wnovo(1),wnovo(2));
mprintf('bnovo: %2.4f\n',bnovo);
mprintf('Ciclos: %2.0d\n',ciclos);
mprintf('Erroquadraticototal: %2.4f\n',erroquadraticototal)

// teste da rede neural com todos os padrões de treinamento
// usando função de ativação degrau
disp("Teste da rede neural")
disp("entrada      saida y");
    for padrao=1:4
        yin= banterior+ x(padrao,1)*wanterior(1)+x(padrao,2)*wanterior(2);
        if yin>=0
            y=1;
        else
            y=-1;
        end        
        mprintf('[%2.0d  %2.0d]',x(padrao,1), x(padrao,2));
        mprintf('       %2.0d\n',y);
    end
    
    
    
    






