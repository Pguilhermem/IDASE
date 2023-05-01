from flask import Flask, make_response, jsonify, send_file
import csv
import json
from PIL import Image
import qrcode

app = Flask(__name__)

# Rota 1 - Vendas de um produto


@app.route('/vendas')
def gerar_vendas():
    response = make_response(json.dumps(vendas))
    response.headers['Content-Disposition'] = 'attachment; filename=vendas.json'
    response.headers['Content-Type'] = 'application/json'
    return response


# Rota 2 - Informações sobre um produto
@app.route('/prod/info/<nome_produto>')
def informacoes_produto(nome_produto):
    produto = produtos.get(nome_produto)
    if produto:
        return jsonify(produto)
    else:
        return jsonify({'mensagem': 'Produto não encontrado.'}), 404


# Rota 3 - QR code de um produto
@app.route('/prod/qrcode/<nome_produto>')
def gerar_qrcode(nome_produto):
    produto = produtos.get(nome_produto)
    if produto:
        descricao = produto.get('descricao', '')
        fabricante = produto.get('fabricante', '')
        modelo = produto.get('modelo', '')
        link_datasheet = produto.get('link_datasheet', '')
        texto_qr = f'{descricao}\n{fabricante}\n{modelo}\n{link_datasheet}'
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        qr.add_data(texto_qr)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"qrcode_{nome_produto}.png")
        return send_file(f'qrcode_{nome_produto}.png', mimetype='image/png')
    else:
        return jsonify({'mensagem': 'Produto não encontrado.'}), 404


if name == 'main':
    app.run(debug=True)
