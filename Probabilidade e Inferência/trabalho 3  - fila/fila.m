%% gerando um vetor com P(T<t) , para t entre 2 e 4
clear all

vec=zeros(1000,1);


for k=1:1000; vec(k)= quad(@espera,2,2+0.002*k); end


%% fazendo 10000 sorteios entre 0 e 1 e, para cada sorteio, atribuindo um
% tempo entre 2 e 4, de acordo com vec.

sorteios=rand(10000,1);
tempo2=zeros(10000,1);
for k=1:10000; tempo2(k)=2+0.002*find(vec >sorteios(k),1); end

%% vetor de chegadas

chegadas=poissrnd(10,10000,1);

%% vetor de exps

tempo1=exprnd(7,10000,1);

%% escolhendo entre tempo1 e tempo2

tempo=zeros(10000,1);
for k=1:10000; 
    if randi(10)<5;
        tempo(k)=tempo2(k);
    else
        tempo(k)=tempo1(k);
    end
end

%%
fila=zeros(10000,1);

for k=2:10000; 
     fila(k)=max(tempo(k-1)-chegadas(k)+fila(k-1),0);
end


%% calcula media de fila

mean(fila); %nesse caso, deu 2.879

%% calcula prob de espera > 3

length(find(fila>3))/10000

%% refaz tudo , com 2 atendentes...

%usando os vetores "chegadas" , "tempo"


fila2=zeros(10000,2);
fila2(1,1)=tempo(1);
tespera=zeros(10000,1);
for k=2:10000;

    %subtraindo o tempo de chegada do prox cliente.
     fila2(k,1)=max(fila2(k-1,1)-chegadas(k),0);
     fila2(k,2)=max(fila2(k-1,2)-chegadas(k),0);
     
     [tmin,guiche]=min(fila2(k,:));
     fila2(k,guiche)=tmin+tempo(k);
     
     tespera(k)=tmin;
end

mean(tespera); %nada mal, aprox 3 segundos.