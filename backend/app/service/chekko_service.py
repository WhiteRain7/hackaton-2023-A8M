import httpx
from lxml import html


class ChekkoService:
    async def parse_contacts_competitors(self, ogrn: str) -> dict:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"https://checko.ru/company/{ogrn}/")
            content = r.text

            tree = html.fromstring(content)

            competitors = []

            competitor_rows = tree.xpath(
                '//section[@id="competitors"]//table[contains(@class, "data-table")]/tbody/tr'
            )
            for row in competitor_rows:
                columns = row.xpath("td")
                if len(columns) >= 2:
                    competitor_name = columns[0].xpath(
                        'normalize-space(.//a[@class="link"])'
                    )
                    competitor_location = columns[0].xpath(
                        "normalize-space(.//br/following-sibling::text())"
                    )
                    competitor_info = columns[1].xpath("normalize-space(.)")

                    if competitor_info:
                        if "Выручка" in competitor_info:
                            competitor_info = [
                                "Выручка",
                                competitor_info.replace("Выручка", ""),
                            ]
                        elif "Активы" in competitor_info:
                            competitor_info = [
                                "Активы",
                                competitor_info.replace("Активы", ""),
                            ]
                    else:
                        competitor_info = []

                    competitor_data = {
                        "name": competitor_name,
                        "location": competitor_location,
                        "info": competitor_info,
                    }
                    competitors.append(competitor_data)

            # Извлекаем информацию
            contacts_section = tree.xpath('//section[@id="contacts"]')[0]

            phone = contacts_section.xpath(
                    './/strong[text()="Телефон"]/following-sibling::a/text()'
                )
            if not phone:
                phone = contacts_section.xpath(
                    './/strong[text()="Телефоны"]/following-sibling::a/text()'
                )

            contacts_data = {
                "Адрес": contacts_section.xpath(
                    './/div[@class="uk-text-bold"]/following-sibling::div[1]/text()'
                )[0].strip(),
                "Телефон": phone[0].strip(),
                "Электронная почта": contacts_section.xpath(
                    './/div[@class="uk-text-bold"][text()="Электронная почта"]/following-sibling::a/text()'
                )[0].strip(),
                "Веб-сайт": contacts_section.xpath(
                    './/div[@class="uk-text-bold"][text()="Веб-сайт"]/following-sibling::a/@href'
                )[0].strip()
                if contacts_section.xpath(
                    './/div[@class="uk-text-bold"][text()="Веб-сайт"]/following-sibling::a/@href'
                )
                else "",
                "Cоциальные сети": contacts_section.xpath(
                    './/div[@class="uk-text-bold mb-2"][text()="Cоциальные сети"]/following-sibling::div[1]/text()'
                )[0].strip(),
            }
            return {"competitors": competitors, "contacts": contacts_data}

    async def get_dop_info(self, ogrn):
        data = await self.parse_contacts_competitors(ogrn)
        return data


# import asyncio


# b = ChekkoService()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(b.get_dop_info())
