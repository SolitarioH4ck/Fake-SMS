dr='\033[1;34m'
rd='\033[1;30m'
nv='\033[1;39m'

echo -e "${dr}Instalando Dependencias...{nv}"
pkg install openssl

echo -e ${dr}"Instalando requests..${nv}"
pip install requests
python sms.py
