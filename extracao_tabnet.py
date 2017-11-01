
#!/bin/bash

if [ $# -ne 1 ]
then
 echo "Sintaxe: $0 <indicador>"
 echo "Indicadores: qrbr qabr aturgbr equipebr"
 exit 1
fi
ind="$1"

# parametrizar de acordo com indicador especificado
case "$ind" in
"qrbr")
 nom="Internações Hospitalares pelo SUS"
 col="num_inter_hospi_sus"
 sis="sih"
 ;;
"qabr")
 nom="Consultas Médicas pelo SUS"
 col="num_consu_medic_sus"
 sis="sia"
 ;;
"aturgbr")
 nom="Estabelecimentos com Atendimento de Urgência SUS"
 col="num_estab_urgen_sus"
 sis="cnes"
 ;;
"equipebr")
 nom="Equipes de Saúde da Família"
 col="num_equip_saude_famil"
 sis="cnes"
 ;;
*)
 echo "Índice desconhecido: $ind"
 exit 2
esac

url="http://tabnet.datasus.gov.br/cgi/tabcgi.exe?$sis/cnv/$ind.def"
tmp="$ind.tmp"
res="$ind.res"
csv="$ind.csv"

echo "Indicador: $nom ($ind)"

# buscar último período disponível
echo "Buscando último período..."
curl -s $url > $tmp
arq=$(awk 'BEGIN{FS="\""}/dbf" SELECTED/{print$2}' $tmp)
mes=$(echo $arq | sed 's/^.*\([0-9]\{2\}\)\.dbf/\1/')
ano=$(echo $arq | sed 's/^.*\([0-9]\{2\}\)[0-9]\{2\}\.dbf/20\1/')
rm -f $tmp
echo "Último período disponível: $mes/$ano (arquivo $arq)"

# definir parâmetros da requisição
case "$ind" in
"qrbr")
 par="Linha=Munic%EDpio&Coluna=--N%E3o-Ativa--&Incremento=Interna%E7%F5es&Arquivos=$arq&SMicrorregi%E3o=TODAS_AS_CATEGORIAS__&SReg.Metropolitana=TODAS_AS_CATEGORIAS__&SAglomerado_urbano=TODAS_AS_CATEGORIAS__&SCapital=TODAS_AS_CATEGORIAS__&SUnidade_Federa%E7%E3o=TODAS_AS_CATEGORIAS__&SProcedimento=TODAS_AS_CATEGORIAS__&SGrupo_procedimento=TODAS_AS_CATEGORIAS__&SSubgrupo_proced.=TODAS_AS_CATEGORIAS__&SForma_organiza%E7%E3o=TODAS_AS_CATEGORIAS__&SComplexidade=TODAS_AS_CATEGORIAS__&SFinanciamento=TODAS_AS_CATEGORIAS__&SRubrica_FAEC=TODAS_AS_CATEGORIAS__&SRegra_contratual=TODAS_AS_CATEGORIAS__&SNatureza=TODAS_AS_CATEGORIAS__&SRegime=TODAS_AS_CATEGORIAS__&SNatureza_jur%EDdica=TODAS_AS_CATEGORIAS__&SEsfera_jur%EDd%EDca=TODAS_AS_CATEGORIAS__&SGest%E3o=TODAS_AS_CATEGORIAS__&zeradas=exibirlz&formato=prn&mostre=Mostra"
 ;;
"qabr")
 par="Linha=Munic%EDpio&Coluna=--N%E3o-Ativa--&Incremento=Qtd.apresentada&Arquivos=$arq&SMicrorregi%E3o=TODAS_AS_CATEGORIAS__&SReg.Metropolitana=TODAS_AS_CATEGORIAS__&SAglomerado_urbano=TODAS_AS_CATEGORIAS__&SCapital=TODAS_AS_CATEGORIAS__&SUnidade_Federa%E7%E3o=TODAS_AS_CATEGORIAS__&SProcedimento=1075&SProcedimento=1076&SProcedimento=1077&SProcedimento=1078&SProcedimento=1079&SProcedimento=1080&SProcedimento=1081&SProcedimento=1082&SProcedimento=1083&SProcedimento=1084&SProcedimento=1085&SProcedimento=1086&SProcedimento=1087&SProcedimento=1088&SProcedimento=1089&SProcedimento=1090&SProcedimento=1091&SProcedimento=1092&SProcedimento=1093&SProcedimento=1094&SProcedimento=1114&SProcedimento=1115&SProcedimento=1117&SProcedimento=1125&SProcedimento=1126&SProcedimento=1127&SProcedimento=1128&SProcedimento=1129&SProcedimento=1130&SProcedimento=1131&SProcedimento=1132&SProcedimento=1133&SProcedimento=1134&SProcedimento=1135&SProcedimento=1136&SProcedimento=1137&SProcedimento=1138&SProcedimento=1139&SProcedimento=1140&SProcedimento=1141&SProcedimento=1142&SProcedimento=1143&SProcedimento=1144&SProcedimento=1145&SProcedimento=1146&SProcedimento=1147&SProcedimento=1148&SProcedimento=1149&SProcedimento=1150&SProcedimento=1169&SProcedimento=1170&SProcedimento=1189&SProcedimento=1190&SProcedimento=1191&SProcedimento=1192&SProcedimento=1193&SProcedimento=1194&SProcedimento=1195&SProcedimento=1196&SProcedimento=1197&SGrupo_procedimento=TODAS_AS_CATEGORIAS__&SSubgrupo_proced.=TODAS_AS_CATEGORIAS__&SForma_organiza%E7%E3o=TODAS_AS_CATEGORIAS__&SComplexidade=TODAS_AS_CATEGORIAS__&SFinanciamento=TODAS_AS_CATEGORIAS__&SSubtp_Financiament=TODAS_AS_CATEGORIAS__&SRegra_contratual=TODAS_AS_CATEGORIAS__&SCar%E1ter_Atendiment=TODAS_AS_CATEGORIAS__&SGest%E3o=TODAS_AS_CATEGORIAS__&SDocumento_registro=TODAS_AS_CATEGORIAS__&SEsfera_administrat=TODAS_AS_CATEGORIAS__&STipo_de_prestador=TODAS_AS_CATEGORIAS__&SAprova%E7%E3o_produ%E7%E3o=TODAS_AS_CATEGORIAS__&zeradas=exibirlz&formato=prn&mostre=Mostra"
 ;;
"aturgbr")
 par="Linha=Munic%EDpio&Coluna=--N%E3o-Ativa--&Incremento=SUS&Arquivos=$arq&SRegi%E3o=TODAS_AS_CATEGORIAS__&SUnidade_Federa%E7%E3o=TODAS_AS_CATEGORIAS__&SCapital=TODAS_AS_CATEGORIAS__&SMicrorregi%E3o=TODAS_AS_CATEGORIAS__&SReg.Metropolitana=TODAS_AS_CATEGORIAS__&SAglomerado_urbano=TODAS_AS_CATEGORIAS__&SEnsino%2FPesquisa=TODAS_AS_CATEGORIAS__&SEsfera_Administrativa=TODAS_AS_CATEGORIAS__&SNatureza=TODAS_AS_CATEGORIAS__&STipo_de_Estabelecimento=TODAS_AS_CATEGORIAS__&STipo_de_Gest%E3o=TODAS_AS_CATEGORIAS__&STipo_de_Prestador=TODAS_AS_CATEGORIAS__&zeradas=exibirlz&formato=prn&mostre=Mostra"
 ;;
"equipebr")
 par="Linha=Munic%EDpio&Coluna=--N%E3o-Ativa--&Incremento=Quantidade&Arquivos=$arq&SRegi%E3o=TODAS_AS_CATEGORIAS__&SUnidade_Federa%E7%E3o=TODAS_AS_CATEGORIAS__&SCapital=TODAS_AS_CATEGORIAS__&SMicrorregi%E3o=TODAS_AS_CATEGORIAS__&SReg.Metropolitana=TODAS_AS_CATEGORIAS__&SAglomerado_urbano=TODAS_AS_CATEGORIAS__&SEnsino%2FPesquisa=TODAS_AS_CATEGORIAS__&SEsfera_Administrativa=TODAS_AS_CATEGORIAS__&SNatureza=TODAS_AS_CATEGORIAS__&STipo_de_Estabelecimento=TODAS_AS_CATEGORIAS__&STipo_de_Gest%E3o=TODAS_AS_CATEGORIAS__&STipo_de_Prestador=TODAS_AS_CATEGORIAS__&STipo_da_Equipe=1&STipo_da_Equipe=2&STipo_da_Equipe=3&zeradas=exibirlz&formato=prn&mostre=Mostra"
 ;;
esac

# obter dados via requisição HTTP POST
echo "Buscando dados do servidor..."
curl -s -d $par $url > $res

# extrair trecho e converter em formato CSV
sed -n '/<PRE>/,/PRE>/p' $res | tr -d '\r' | sed \
 -e '/^"[0-9]/!d' -e 's/^"\([0-9]\+\).*;/\1;/' \
 -e '/^000000/d' -e 's/;-$/;0/' > $csv

# manipulações no banco de dados
export PGDATABASE="banco"
export PGHOST="servidor"
export PGUSER="usuario"

# popular tabela de entrada
echo "Populando tabela de entrada..."

cat $csv > $ano$mes$col