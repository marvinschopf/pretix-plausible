"""
pretix-plausible
Copyright (C) 2021 Marvin Schopf

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from django.dispatch import receiver
from django.http import HttpRequest
from pretix.presale.signals import global_html_head


@receiver(global_html_head, dispatch_uid="plausible_global_html_head")
def frontend_html_head(sender, request: HttpRequest, **kwargs):
    return '<script async defer data-domain="{domain}" src="https://{plausible_host}/js/plausible.js"></script>'.format(
        domain=request.get_host(), plausible_host="plausible.io"
    )
