"""
    Plugin for URLResolver
    Copyright (C) 2020 Anis3

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
import re
from urlresolver.plugins.lib import helpers
from urlresolver import common
from urlresolver.resolver import UrlResolver, ResolverError

class MegaLoadResolver(UrlResolver):
    name = "megaload"
    domains = ['megaload.to']
    pattern = r'(?://|\.)(megaload\.to)/(.*?.html)'

    def get_media_url(self, host, media_id):
        web_url = self.get_url(host, media_id)
        headers = {'User-Agent': common.FF_USER_AGENT}
        html = self.net.http_GET(web_url, headers=headers).content
        match = re.search(r'''id"[^>]value="([^"]+).*?fname"[^>]value="([^"]+)''', html, re.DOTALL)
        if match:
            ID = match.group(1)
            name = match.group(2)
            headers = {'User-Agent': common.FF_USER_AGENT, 'Referer': web_url}
            data = {'op': 'download1', 'usr_login': '', 'id': ID, 'fname': name, 'referer': web_url, 'method_free': 'Kostenloser+Download'}
            html = self.net.http_POST(web_url,data ,headers=headers).content
            r = re.search(r'''source src="([^"]+)''', html, re.DOTALL)
            if r:
                return r.group(1) + helpers.append_headers(headers)
        raise ResolverError('Video Link Not Found')

    def get_url(self, host, media_id):
        return self._default_get_url(host, media_id, template='https://megaload.to/{media_id}')
