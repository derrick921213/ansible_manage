import yaml,random,string
passwd = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(20))
with open('vars/DB_user.yml','r') as f:
    data = yaml.load(f,Loader = yaml.FullLoader)
    with open('vars/DB_user.yml','w') as w_f:
        data['db_pass'] = passwd
        yaml.dump(data,w_f)
