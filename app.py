from flask import Flask, render_template,jsonify,request
import re
import os
import shutil
import jieba.analyse
from pypinyin import lazy_pinyin


app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # 获取请求参数
    print(request.form)
    title = request.form['title']
    description = request.form['description']
    initials = ''.join([word[0][0] for word in lazy_pinyin(title)])
    result = initials[:9]
    keywords=jieba.analyse.extract_tags(description, topK=8, withWeight=False, allowPOS=())
    keywords=",".join(keywords)

    # 返回响应
    response = {'name': result,
                'html': update_html(title=title, keywords=keywords, description=description),
                'banner': update_banner(title=title,description=description)
                }
    return jsonify(response)

def update_html(title, keywords, description):
    file_content="""
    <title>【专题】#</title>
    <meta name="keywords" content="$" />
    <meta name="description" content="^" />
"""
    file_content = file_content.replace("#", title)
    file_content = file_content.replace("$", keywords)
    file_content = file_content.replace("^", description)
    return file_content


def update_banner(title,description):
    content ="""
    banner: {
    img: "img/banner.jpg",
    title: ["#", ""],
    text: "$",
},"""
    content = content.replace("#", title)
    content = content.replace("$", description)
    return content

@app.route('/generate', methods=['POST'])
def submit1():
    # 获取请求参数
    input = request.form['nav']

    if(input.find("（")>-1):
        input=remove_brackets(input)

    if(input.find("、")>-1):
        input = input.replace("、"," ")
    names = split_sentence(input," ")

    response ={
        "nav": generate_items(names)
    }
    return jsonify(response)


def split_sentence(sentence, delimiter):
    return sentence.split(delimiter)

def generate_items(names):
    items = []
    for name in names:
        item = {
            "value": name,
            "label": name,
        }
        items.append(item)
    return items

def remove_brackets(text):
    return re.sub(r'\（([^（）]+)\）', '、', text)

@app.route('/New_folder', methods=['POST'])
def submit2():
    name = request.form['Folder_name']
    # 生成路径
    path = r'D:\Tencent Files\1352566613\FileRecv\py\Flask\Generate'
    try:
        os.makedirs(os.path.join(path, name))
        # 模板文件路径
        source_file = r'D:\Tencent Files\1352566613\FileRecv\py\Flask\tmp\index.html'
        shutil.copy2(source_file, os.path.join(path, name, os.path.basename(source_file)))  # 更新复制操作
        os.mkdir(os.path.join(path, name, "img"))  # 创建子文件夹
        return "文件夹创建成功"
    except FileExistsError:
        return "文件夹已存在"

if __name__ == '__main__':
    app.run()

