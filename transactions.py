def save_transaction(price,credit_card,description):
    file = open('./data/transactions.txt','a+')
    file.write('%07ds%16s%16s\n'%(price*100,credit_card,description))
    file.close()
