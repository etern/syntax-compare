import yaml
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def load_yaml_files(yaml_dir):
    """加载所有 YAML 文件"""
    languages = {}
    for file in yaml_dir.glob('*.yaml'):
        lang_name = file.stem
        with open(file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            languages[lang_name] = {item['name']: item for item in data['items']}
    return languages


def get_ordered_names(languages, base_lang='python'):
    """从基准语言获取 items 顺序"""
    base_data = languages.get(base_lang)
    if not base_data:
        return []
    return list(base_data.keys())


def generate_data_json(languages, ordered_names, output_path):
    """生成数据 JSON 文件"""
    data = {
        'languages': languages,
        'orderedNames': ordered_names
    }
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def generate_html(lang_names, template_path, output_path):
    """生成 HTML 文件"""
    env = Environment(loader=FileSystemLoader(str(template_path.parent)))
    template = env.get_template(template_path.name)
    
    html = template.render(
        lang_names=lang_names,
        default_left='python',
        default_right='javascript'
    )
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)


def main():
    yaml_dir = Path(__file__).parent.parent / 'yaml'
    template_path = Path(__file__).parent / 'template.html'
    docs_dir = Path(__file__).parent.parent / 'docs'
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    html_path = docs_dir / 'index.html'
    data_path = docs_dir / 'data.json'

    languages = load_yaml_files(yaml_dir)
    ordered_names = get_ordered_names(languages, base_lang='python')
    
    generate_data_json(languages, ordered_names, data_path)
    generate_html(list(languages.keys()), template_path, html_path)
    
    print(f"Generated {html_path}")
    print(f"Generated {data_path}")


if __name__ == '__main__':
    main()
