#!/bin/bash
#
env  ansible-playbook \
  ./read-address-books.yml \
  --extra-vars "@/home/ivan.dean/ansible/junos-fw01.yml" \
   --extra-vars "{config_output: /tmp}" \
   --extra-vars "{debug_enabled: True}" \
   --extra-vars "{output_path: .}" \
  --inventory ~/dev/ansible/inventory.yml \
  --limit junos-fw01

