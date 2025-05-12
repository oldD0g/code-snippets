# Three deep Ansible loops

Ansible only provides loops that handle two levels of nesting.  This is typically with_subelements, that is now deprecated in favour of the 

```
loop: top_level|subelements('next_level')
```

construct.

Address sets for SRX devices, as intuitively coded into YML, are three levels deep.  Typically they look like:

```
address_books:
    - name: first-book-of-addresses
        zone: prod
        address_sets:
        - name: address-set-1-prod
            addresses:
            - name: web1.prod.com
            - name: web2.prod.com
        -name: address-set-2-prod
            addresses:
            - name: db1.prod.com
            - name: db2.prod.com
    - name: second-book-of-addresses
    etc...

```
  * The first level is the list of address books.
  * The second level is the list of address sets in that address book
  * The third level is the list of addresses in the address set

There are a range of different solutions to this discussed on StackOverflow and other sites. Some of them are a bit messy, involving the inclusion of other playbook files into the top level file.

The solution I worked with successfuly is from: https://stackoverflow.com/questions/49772057/ansible-with-subelements-nested-levels

This solution uses the approach of looping through the data initially using a subelements loop to create a new value, that can then be processed by a subelements loop.  The data is altered in the first run to make it possible to process all the values in the second run.

The playbook task that performs the transformation magic looks like this:

```
- set_fact:
        address_set_list: >
          {{ address_set_list|d([])
             + [ {'address_book_name': item.0.name} | combine(item[0]) | combine(item[1]) ]
          }}
      with_subelements:
        - "{{ address_books }}"
        - address_sets

```

This loop builds up a new list, where every entry is a dictionary containing the values we need to
create the address book.  But the entire data structure is now only two levels deep:

  * a list of address book + address set combinations
  * inside each entry is a list of addresses for that address set.

Basically we are eliminating the middle part of the hierarchy, to produce data like this:

```
address_set_list =
    [
        {
            'address_book_name': 'first-book-of-addresses', 
            'name': 'address-set-1-prod', 
            'zone': 'prod', 
            'addresses': [
                {'name': 'web1.prod.com'},
                {'name': 'web2.prod.com'}
                ]
        }, 
        {
            'address_book_name': 'first-book-of-addresses', 
            'name': 'address-set-2-prod', 
            'zone': 'prod', 
            'addresses': [
                {'name': 'db1.prod.com'},
                {'name': 'db2.prod.com'}
                ]
        }, 
    ]
```

This means we can now loop over this structure with an Ansible loop like:

```
    loop: "{{ lookup('subelements', address_set_list, 'addresses', {'skip_missing': True} )}}"
```

It is important to use the lookup syntax, so "skip_missing" can be included, because
not all address books will have address sets.  Without skip_missing, the playbook
will fail with an error.
