from shared.utilities.csv_config_manager import CSVConfig

csv_config = CSVConfig.get_instance()

addr_prefix_28_list = []
for key in csv_config.id_components:
    addr_prefix_28_list.append(csv_config.id_components[key]['mac'])
    addr_prefix_28_list.append(csv_config.master_mac)

print(addr_prefix_28_list)