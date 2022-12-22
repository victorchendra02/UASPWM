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

    clerk_idnya = data[-1][0]
    print("SEPP")
    print()
    print(clerk_idnya)
    print()
    data.pop()

    # 1. Create Invoice
    new_invoice = Invoice(clerk_idnya, datetime.now())
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
    
    return "AAA"


@app.route('/report', methods=['GET'])
def get_report():
    sql = text(f"SELECT invoice.id_invoice, clerk.username, invoice.date, SUM(invoice_detail.sub_total) as total \
               FROM invoice \
               INNER JOIN clerk ON invoice.id_clerk = clerk.id_clerk \
               INNER JOIN invoice_detail ON invoice.id_invoice = invoice_detail.id_invoice \
               GROUP BY invoice.id_invoice ")
    results = db.engine.execute(sql)
    
    collect = []
    for result in results:
        collect.append(
            {
                "id_invoice": result[0],
                "username": result[1],
                "date": result[2],
                "total": result[3],
            }
        )
    
    return collect
