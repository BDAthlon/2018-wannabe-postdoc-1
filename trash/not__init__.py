2018-wannabe-postdoc-1			# Top-level package
	__init__.py					# Initial this package
	utilities/					# Subpackage for utilities package
		configuration_manager.py
		configuration_manager_tester.py
		date_time_processing.py
		date_time_processing_tester.py
		file_io.py
		file_io_tester.py
		generate_results_filename.py
		generate_results_filename_tester.py
		miscellaneous.py
		miscellaneous_tester.py
		queue_ip_arguments.py
		queue_ip_arguments_tester.py
		custom_exceptions/		# Subsubpackage for custom exceptions
			graph_error.py
			graph_error_tester.py
	statistics/					# Subpackage for statistics
		test_statistics.py
		test_statistics_tester.py
	parsers/					# Subpackage for parsers
		json_object.py
		json_object_tester.py
		config_file_parser.py
		config_file_parser_tester.py
	data_structures/			# Subpackage for data structures
		vertex.py
		vertex_tester.py
		graph.py
		graph_tester.py
		directed_graph/
			graph_dg.py
			graph_tester_dg.py
			vertex_dg.py
			vertex_tester_dg.py
		undirected_graph/
			vertex_tester_ug.py
			graph_tester_ug.py
			graph_ug.py
			vertex_ug.py
