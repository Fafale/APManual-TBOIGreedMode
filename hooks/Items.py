from ..Data import characters_list, generic_char_items

def before_item_table_processed(item_table: list) -> list:
    for char_name in characters_list:
        item = {}
        item["name"] = f"Unlock {char_name}"
        item["category"] = ["Characters"]
        item["progression"] = True
        item_table.append(item)

        for idx in range(0, len(generic_char_items)):
            itemName = generic_char_items[idx][0].replace("CHAR", char_name)
            itemCount = generic_char_items[idx][1]
            itemValue = generic_char_items[idx][2]
            itemProg = generic_char_items[idx][3]

            item = {}
            item["name"] = itemName
            item["category"] = ["Items - " + char_name]
            item["count"] = itemCount
            item["progression"] = itemProg
            if (int(itemValue) > 0):
                item["value"] = {f"{char_name.lower()} items":itemValue}
            item_table.append(item)

    return item_table
