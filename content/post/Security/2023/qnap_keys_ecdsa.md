---
title: "Qnap con certificado ECDSA"
description: Actualmente, Let's Encrypt genera los certificados usando el algoritmo ECDSA (Elliptic Curve Digital Signature Algorithm), en vez de usar RSA (Rivest, Shamir y Adleman).
date: 2023-04-06T17:23:26+02:00
lastmod: 2023-04-06T17:23:26+02:00
slug: "Qnap_keys_ecdsa"
image: covers/linux.jpg
hidden: false
draft: false
tags:
  - letsencrypt
  - ssl
  - https
  - qnap
  - ansible
  - ecdsa
categories:
  - Security
---


## Introducción


Actualmente, Let's Encrypt genera los certificados usando el algoritmo ECDSA (Elliptic Curve Digital Signature Algorithm), en vez de usar RSA (Rivest, Shamir y Adleman).

Esto genera un problema, ya que la interfaz web de QNAP (pruebas realizadas en la versión de firmware: QTS 5.0.1.2346) no soporta ni ECDSA, ni RSA con una clave superior a 2048 bits, pero su servidor web sí que tiene la capacidad de utilizarlos.


## Ansible

Por lo que para poder usar nuestro certificado generado por Let's Encrypt, tendremos que cargarlos manualmente, para realizar esta acción y que sea relativamente automática usaremos Ansible.


Fichero `inventory`:

```
[all:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
ansible_ssh_private_key_file=/Users/pablojoserocamora/.ssh/id_ed25519

[test]
qnap.procamora.com
```

Fichero `main.yml`:

```yaml
---
# ansible-playbook -i inventory main.yml -v -K
- name: Playbook QNAP SSL
  hosts: all
  become: false
  become_method: sudo
  become_user: admin
  gather_facts: false
  vars:
    ansible_user: procamora
    ansible_python_interpreter: /share/CACHEDEV1_DATA/.qpkg/Python3/python3/bin/python3

  pre_tasks:
    - name: set custom home
      ansible.builtin.set_fact:
        MY_HOME: "{{ lookup('env', 'HOME') }}/procamora.com/letsencrypt/live/procamora.com"

  tasks:
    # 1) SSH into your NAS and go to /etc/stunnel/
    # 2) replace the backup.cert with your own certificate (PEM format, no human readable content)
    # 3) replace backup.key with your own private key (PEM format, no human readable content)
    # 5) replace uca.pem with your certificate chain (PEM format, no human readable content)
    - name: Copy files
      ansible.builtin.copy:
        src: "{{ MY_HOME }}/{{ item.src }}"
        dest: "/etc/stunnel/{{ item.dest }}"
        mode: 0600
        owner: admin
        group: administrators
        backup: true
      become: true
      loop:
        - { src: cert.pem, dest: backup.cert }
        - { src: privkey.pem, dest: backup.key }
        - { src: chain.pem, dest: uca.pem }

    # 4) replace stunnel.pem with your private key+certificate (PEM format, no human readable content)
    - name: create stunnel.pem (key+certificate)
      ansible.builtin.copy:
        content: "{{ lookup('file', '{{ MY_HOME }}/privkey.pem') }}\n{{ lookup('file', '{{ MY_HOME }}/cert.pem') }}"
        dest: /etc/stunnel/stunnel.pem
        mode: 0600
        owner: admin
        group: administrators
        backup: true
      become: true

    # 6) execute /etc/init.d/thttpd.sh restart
    # 7) execute /etc/init.d/stunnel.sh restart
    # 8) execute /etc/init.d/Qthttpd.sh restart
    - name: restart services
      ansible.builtin.shell: "/etc/init.d/{{ item }} restart"
      become: true
      loop:
        - thttpd.sh
        - stunnel.sh
        - Qthttpd.sh
```

Podemos ejecuta el playbook con el siguiente comando (-K lo usamos para indicar la contraseña de escalado a admin)

```bash
ansible-playbook -i inventory main.yml -v -K
```

Los valores que pueden cambiar del playbook son:

 - `ansible_user: procamora. Que es nuestro usuario de qnap.
 - `ansible_python_interpreter: /share/CACHEDEV1_DATA/.qpkg/Python3/python3/bin/python3`. Ruta del binario de python3 que necesita ansible.
 - `MY_HOME: "{{ lookup('env', 'HOME') }}/procamora.com/letsencrypt/live/procamora.com"`. Ruta donde letsencrypt ha generado el certificado.


## Verificación


Una vez ejecutado podemos acceder con el navegador y ver que tanto el navegador confia en el certificado como que QNAP nos reconoce nuestro certificado generado con wilcard


![qnap_ecdsa](/images/2023/qnap_ecdsa.png)



Fuentes: [0][fuente0]
[fuente0]: https://forum.qnap.com/viewtopic.php?t=110557