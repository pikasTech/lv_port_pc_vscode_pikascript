import re
module_prefix = 'pika_obj'
lv_method_pattern = re.compile(
    '^{prefix}_[^_]+_(.+)'.format(prefix=module_prefix), re.IGNORECASE)


def method_name_from_func_name(func_name):
    res = lv_method_pattern.match(func_name).group(1)
    return res if res != "del" else "delete"  # del is a resrved name, don't use it
