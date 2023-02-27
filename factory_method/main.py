from factories import MessageBoxCreator

WARNING_MESSAGE = "this is a sample warning message"
INFO_MESSAGE = "this is a sample info message"

creator = MessageBoxCreator()

box = creator.create_success_message()
box.show()


box = creator.create_warning_message(body=WARNING_MESSAGE)
box.show()


box = creator.create_error_message()
box.show()


box = creator.create_info_message(body=INFO_MESSAGE)
box.show()
