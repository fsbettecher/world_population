<h1>Repositório direcionado para manipulação de um DataFrame a partir de um dataset do repositório Kaggle</h1><br>
<p align="center">
<img loading="lazy" src="https://img.shields.io/badge/STATUS-FINALIZADO-badge"/>
</p>
<br>

<h2>Primeiramente, é necessário possuir uma conta no site Kaggle</h2>

• Acesse [www.kaggle.com](https://www.kaggle.com/)<br>
• Crie uma conta clicando em "Register" no canto superior direito, conforme a imagem abaixo:
![Registro no Kaggle](https://github.com/fsbettecher/world_population/assets/62480910/72e77922-67f0-4bf3-88eb-54dedd943ddb)<br>

• Após criar a conta, será necessário criar um token para acessar os datasets via API
![Baixando o Token](https://github.com/fsbettecher/world_population/assets/62480910/5e49ab5f-ce7d-49f5-ac82-95a2db4dba08)<br>

• Seguindo os passos acima, será feito o download do token no formato json para o seu computador.

• Em seguida, abra o Git Bash e execute o comando abaixo:

```
cd C:/users/nome_do_usuario/.kaggle
cp diretorio/onde/está/o/arquivo/kaggle.json .
```
<br>

• Dessa forma, o arquivo token baixado será copiado para a pasta .kaggle na pasta do usuário. Essa etapa é importante para a autenticação da API no código.

<h2>🎉 Pronto! Agora você está pronto para rodar o código e utilizar a API do Kaggle! 🎉</h2>
