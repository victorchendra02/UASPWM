from db import *

@app.route('/clerks', methods=['GET'])
def get_clerks():
    clerks = Clerk.query.all()
    clerks_list = []

    for clerk in clerks:
        clerks_list.append(
            {
                "id_clerk": clerk.id_clerk,
                "username": clerk.username,
                "password": clerk.password
            }
        )

    return jsonify(clerks_list)


@app.route('/category', methods=['GET'])
def get_products_category_uniquely():
    sql = text("SELECT DISTINCT category FROM product")
    result = db.engine.execute(sql)  # return [(cat1), (cat2), ...]
    
    result = [res[0] for res in result]
    print(result)
    
    return jsonify(result)


@app.route('/spec_prod/<cate>', methods=['GET', 'POST'])
def get_specific_product_based_category(cate):
    sql = text(f"SELECT * FROM product WHERE category='{cate}'")
    result = db.engine.execute(sql)  # return [(cat1), (cat2), ...]

    collect = []
    for x in result:
        collect.append(
            {
                "id_product": x[0],
                "product_name": x[1],
                "price": x[2],
                "category": x[3],
                "img_path": x[4]
            }
        )
    
    return jsonify(collect)


# get images path
@app.route('/static/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],filename)


def get_last_recorded_id_invoice():
    sql = text(f"SELECT id_invoice FROM invoice ORDER BY id_invoice DESC LIMIT 1;")
    result = db.engine.execute(sql)
    return result  # make to list() first 


@app.route('/submit', methods=['GET', 'POST'])
def entry_payment_to_database():
    data = request.json  # it's a list

    # 1. Create Invoice
    new_invoice = Invoice(1, date.today())
    db.session.add(new_invoice)
    db.session.commit()
    
    # 2. Get last recorded invoice id
    last_id_invoice = get_last_recorded_id_invoice()
    last_id_invoice = list(last_id_invoice)[0][0]
    
    # 3. Loop each dictionary data 
    #    data is a list filled with dictionary like this:
    #    data = [
    #       {id: 1, name: "Jacob"}, 
    #       {id:2, name: "Victor"}, 
    #       {...}, ...
    #    ]
    for item in data:
        new_invoicedetail = InvoiceDetail(last_id_invoice, item["id_product"], item["qty"], item["sub_total"])
        db.session.add(new_invoicedetail)
        db.session.commit()
