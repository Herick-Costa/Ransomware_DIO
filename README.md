# Criptografador de Arquivos em Python

Este projeto contém um script Python que criptografa arquivos e pastas em um sistema Linux usando criptografia AES em modo CTR. O script gera uma chave aleatória para criptografar os arquivos e salva essa chave em um arquivo separado chamado `salvo.txt`, o qual pode ser utilizado para descriptografar os arquivos posteriormente.

## 🚨 Aviso Importante

Este script é destinado exclusivamente para fins educativos e **não deve ser utilizado para fins maliciosos ou ilegais**. O uso deste código para criptografar arquivos sem permissão, especialmente em sistemas de outras pessoas, é **ilegal** e pode resultar em consequências legais graves.

## 📋 Funcionalidades

- Criptografa todos os arquivos e subpastas de um diretório especificado.
- Salva a chave de criptografia no arquivo `salvo.txt` para posterior descriptografia.
- Substitui os arquivos originais com os arquivos criptografados (extensão `.ransomwaretroll`).
- Utiliza AES no modo CTR para criptografar os arquivos.

## Resultado:

Os arquivos no diretório serão criptografados e terão a extensão .ransomwaretroll.
O arquivo salvo.txt conterá a chave de criptografia necessária para descriptografar os arquivos.

## ⚠️ Atenção
Este código é fornecido apenas para fins educativos. O uso para criptografar arquivos de terceiros sem permissão é estritamente ilegal.
Não use esse script em sistemas de produção ou em redes de clientes sem autorização.
Mantenha a chave de criptografia segura. Sem ela, não será possível descriptografar os arquivos.
