#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'wrap_xml': self.wrap_rendered_xml
        }

    def wrap_rendered_xml(self, xml_config):
        """
          This wraps the XML config with some other elements to make it
          valid for loading into a junipernetworks.junos module to parse it
          into JSON.

        """
        rpc_reply_start = ('<rpc-reply '
                           'message-id='
                           '"urn:uuid:0cadb4e8-3defa-47f4-986e-72906996007f">')
        rpc_reply_end = '</rpc-reply>'

        config_start = ('<configuration changed-seconds="1590139550" '
                        'changed-localtime="2020-05-22 09:25:50 UTC">')
        config_end = '</configuration>'

        wrapped_xml = (rpc_reply_start +
                       config_start +
                       xml_config +
                       config_end +
                       rpc_reply_end)

        wrapped_xml = wrapped_xml.replace("nc:", "")
        return wrapped_xml
