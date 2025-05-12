#!/bin/bash
ansible-playbook \
  --extra-vars "@nxos_interfaces.yml" \
  --extra-vars "{config_output: ~/dev/}" \
  --extra-vars "{output_path: ~/tmp/}" \
  --inventory inventory.yml \
  --limit dev-nxos-sw01 \
  --tags update,update_interfaces \
  update_interfaces_playbook.yml

