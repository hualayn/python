# import os

# dir_ = os.listdir('D:\迅雷下载\php模板\静态')
#
# def write_content(content):
#     lines = '<a href="/' + content + '">' + content + '</a><br>'
#     return lines
#
# content = ''
# for foo in dir_:
#     content = content + write_content(foo)
#
# with open("index.html", "w") as f:
#     f.write(content)
#
# f.close()

def write_content(file_path, write_to_file, file_format='html'):
    import os
    content = ''
    file_name_list = os.listdir(file_path)
    for file_name in file_name_list:
        if file_format == 'html':
            lines = '<a href="/' + file_name + '">' + file_name + '</a><br>\n'
        else:
            lines = file_name + '\n'
        content = content + lines
    with open(write_to_file + '.' + file_format,'w') as f:
        f.write(content)


