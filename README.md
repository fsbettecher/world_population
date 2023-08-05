<h1 align="center">Manipulação de um dataset do repositório Kaggle</h1><br>
<p align="center">
<img loading="lazy" src="https://img.shields.io/badge/STATUS-FINALIZADO-badge"/>
</p>

<hr></hr>

<h4 align="justify">🔹 O código consiste no download do dataset através da API do Kaggle e da criação de um DataFrame pandas através do arquivo csv baixado.<br></br>
🔹 Uma vez que o dataset está em inglês, as colunas foram renomeadas para facilitar a manipulação dos dados no código e nas ferramentas de visualização,
porém essa é uma etapa opcional e que pode ser alterada no código.<br></br>
🔹 Por fim, as colunas com os dados populacionais de cada ano são transformadas em linhas. Dessa forma, o DataFrame passou de uma informação por país para
uma informação por país e ano, ou seja, é possível utilizar os dados para uma análise de série temporal, por exemplo. Sendo possíveis análises de crescimento ou diminuição populacional ao longo dos anos.
</h4>

<hr></hr><br>

<h2>Primeiramente, é necessário possuir uma conta no site Kaggle</h2>

• Acesse [www.kaggle.com](https://www.kaggle.com/)<br></br>
• Crie uma conta clicando em "Register" no canto superior direito, conforme a imagem abaixo:<br></br>
![Registro no Kaggle](https://github.com/fsbettecher/world_population/assets/62480910/72e77922-67f0-4bf3-88eb-54dedd943ddb)<br>
<br></br>

• Após criar a conta, será necessário criar um token para acessar os datasets via API<br></br>
![Baixando o Token](https://github.com/fsbettecher/world_population/assets/62480910/5e49ab5f-ce7d-49f5-ac82-95a2db4dba08)
<br></br>

• Seguindo os passos acima, será feito o download do token no formato json para o seu computador.

• Em seguida, abra o Git Bash e execute o comando abaixo:

```
cd C:/users/nome_do_usuario
mkdir .kaggle
cd .kaggle
cp diretorio/onde/está/o/arquivo/kaggle.json .
```
<br>

• Dessa forma, o arquivo token baixado será copiado para a pasta .kaggle criada na pasta do usuário. Essa etapa é importante para a autenticação da API no código e não deve ser pulada.

<h2>🎉 Pronto! Agora sua configuração está preparada para rodar o código e utilizar a API do Kaggle! 🎉</h2>