class SRXConfig():

    @property
    def repr(self):
        
        return "SRX Configuration"

    @property
    def address_books(self):

        return ["book1", "book2"]

    @property
    def applications(self):
        """
        Returns all the applications in the config in a dictionary that contains lists of 
        dictionaries.  There are two keys at the top level, "application" and "application-set"

        Each is a list of dictionaries.  The "application" list looks like:

            [
            {
                "name": "kpasswd-udp-464",
                "protocol": "udp",
                "source-port": "1024-65535",
                "destination-port": "464"
            },
            ...
            ]


        The application-set list looks like:

        [
            {
            "name": "syslog-services-gp",
            "application": [
                {
                    "name": "junos-syslog"
                },
                {
                    "name": "rsyslog-tcp-6514"
                },
                {
                    "name": "rsyslog-tls-tcp-10514"
                }
            ]
        ]

        If the device has no applications installed, return an empty dictionary.
        """

        _this_config = self.config.get('configuration')
        if _this_config:
            _this_applications = _this_config.get('applications')
            if _this_applications:
                return _this_applications
            
        return {}


    @property
    def addresses(self):
        """
        Returns a list of dictionaries, each dictionary is
        a zone and its address book, e.g. an element of the list might
        look like:

        {
            "name": "zone1",
            "addresses": [
                {
                "name": "zone1-test1",
                "ip-prefix": "10.10.10.1/32"
                },
                {
                "name": "zone1-test2",
                "ip-prefix": "10.10.10.2/32"
                }
            ]
        }

        The 'addresses' entry is just a copy of the address entry list from the JSON config, e.g. the list from:

          config['configuration']['security']['zones']['security-zone'][1]['address-book']['address']

        NOTE: The more modern way to set up addresses is to create address books at the global level,
        and attach them to zones.  They then appear in a different part of the config, i.e.

        config['configuration']['security']['address-book']

        """

        """
        all_addresses = []

        for zone in self.config['configuration']['security']['zones']['security-zone']:
            a_entry = {}
            zone_ab = zone.get('address-book')
            zone_name = zone.get('name')
            a_entry['name'] = zone_name
            if zone_ab:
                a_entry['addresses'] = zone_ab.copy()
            else:
                a_entry['addresses'] = []
                    
            all_addresses.append(a_entry)

        #print(".addresses returning list: ")
        #print(all_addresses)

        return all_addresses
        """

        _my_config = self.config.get('configuration')
        if _my_config:
            _my_security = _my_config.get('security')
            if _my_security:
                _my_address_book = _my_security.get('address-book')
                if _my_address_book:
                    return _my_address_book
                
        return []

    @property
    def zones(self):
        """
        Returns all the zones in the config in a list.
        The list of zones is typically found in:

        config['configuration']['security']['zones']['security-zone']

        """

        return self.config['configuration']['security']['zones']['security-zone']

    @property
    def filename(self):

        return self.name

    def __init__(self, filename, configuration_json):

        self.name = filename
        self.config = configuration_json

