# 使用ansible部署服務器
## 目錄結構
```
./
|- j2/
|- play_books/
    |- functions/
    |- handlers/
|- vars/
|- ansible.cfg
|- hosts.ini
## 目錄用途
1. j2資料夾內是放template的檔案
2. play_books內是放主要的playbook
3. play_books/functions 放的是各個功能的tasks
4. play_books/handlers 放的是所需要執行的handlers
```

## 使用方法
在play_books下寫一個main.yml的playbooks,在使用import_task/include_task去呼叫play_books/functions下的tasks
### 舉例
#### 以下playbook為安裝LAMP
```
---
- name: Install LAMP
  hosts: hosted_web
  vars_files:
    - ../vars/DB_user.yml
    - ../vars/Domain_name.yml
  tasks:
    - import_tasks: "functions/update_upgrade.yml"

    - import_tasks: "functions/Install_apache2.yml"
      vars: 
        Dname:
          "{{Domain_name}}"

    - import_tasks: "functions/Install_php.yml"
      vars: 
        Dname:
          "{{Domain_name}}"

    - import_tasks: "functions/Install_mysql.yml"
      vars: 
        db:
          "{{db_name}}"
        db_u:
          "{{db_user}}"
        db_p:
          "{{db_pass}}"

    - import_tasks: "functions/Service.yml"
      vars: 
        Service_name:
          - mysql
          - apache2
    
    - name: Check that a page returns a status 200 and fail if the word AWESOME is not in the page contents
      uri:
        url: "http://192.168.2.32"
        return_content: yes

  handlers:
    - import_tasks: "handlers/restart_apache2.yml"
```


