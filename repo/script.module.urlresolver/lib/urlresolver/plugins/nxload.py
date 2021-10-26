"""
    Plugin for URLResolver
    #2020-08-08 ka

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from urlresolver.plugins.lib import helpers
from urlresolver.plugins.__generic_resolver__ import GenericResolver

import re
from urlresolver import common
from urlresolver.plugins.lib import jsunpack

class NxloadResolver(GenericResolver):
    name = "nxload"
    domains = ["nxload.com"]
    pattern = r'(?://|\.)(nxload\.com)/(?:v/|embed[-/])?([0-9a-zA-Z]+)'

    def get_media_url(self, host, media_id):
        # return helpers.get_media_url(self.get_url(host, media_id), patterns=[r"src:\s*'(?P<url>[^']+)"])

        web_url = self.get_url(host, media_id)
        headers = {'User-Agent': common.RAND_UA}
        html = self.net.http_GET(web_url, headers=headers).content
        try:
            r = re.search('(eval\(function\(p,a,c,k,e,d\).+)\s+?player', html)
            r = jsunpack.unpack(r.group(1))
            #r = re.search('src:\\\'([^"]+?)\'', r.replace('\\', ''))
            #pattern = r'src:\\.(http.*?[^,\\]+).*?(/[^\\]+)'
            pattern = r"src:.*?'(http.*?)'"
            r = re.search(pattern, r)
            url = r.group(1) #+ r.group(2)
            return url
        except:
            return

    def get_url(self, host, media_id):
        return self._default_get_url(host, media_id, template='https://{host}/embed-{media_id}.html')
