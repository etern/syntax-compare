# 语法对比学习

一个用于 side-by-side 对比学习多种编程语言语法的静态网站。

## 功能特性

- 支持 Python、JavaScript、C++、Go、Rust 五种语言对比
- 按照语法名称（如 str、list、dict、for_loop 等）进行对应
- 简约亮色风格界面
- 代码语法高亮
- 响应式设计，支持移动端
- 自动部署到 GitHub Pages

## 本地开发

### 环境要求

- Python 3.11+

### 安装依赖

```bash
pip install -e .
```

### 生成静态网站

```bash
python src/generator.py
```

生成的文件位于 `docs/index.html`，可以直接在浏览器中打开。

### 本地预览

使用任意 HTTP 服务器预览：

```bash
cd docs
python -m http.server 8000
```

然后访问 http://localhost:8000

## 项目结构

```
syntax-compare/
├── yaml/                    # 语法示例 YAML 文件
│   ├── python.yaml          # Python（基准语言）
│   ├── javascript.yaml      # JavaScript
│   ├── cpp.yaml             # C++
│   ├── go.yaml              # Go
│   └── rust.yaml            # Rust
├── src/                     # 网页生成脚本
│   ├── generator.py         # 主生成脚本
│   └── template.html        # Jinja2 模板
├── docs/                    # 生成的静态网页
│   └── index.html
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions 自动部署
├── pyproject.toml           # 依赖配置
└── README.md
```

## 添加新语言

1. 在 `yaml/` 目录下创建新的 YAML 文件
2. 确保 `name` 字段与 `python.yaml` 中的语法项名称一致
3. 重新生成网站

```bash
python src/generator.py
```

## 部署到 GitHub Pages

项目使用 GitHub Actions 自动部署：

1. Fork 或 clone 本仓库
2. 推送代码到 `main` 分支
3. GitHub Actions 会自动构建并部署到 GitHub Pages

首次部署需要在仓库设置中启用 GitHub Pages：

1. 进入仓库 Settings → Pages
2. Source 选择 GitHub Actions
3. 保存设置

## YAML 文件格式

每个语言的 YAML 文件格式如下：

```yaml
items:
  - name: str              # 语法项名称（与 python.yaml 对应）
    description: "字符串定义"
    code: |
      const name = "World";
      console.log(`Hello, ${name}!`);
    output: "Hello, World!"
    comment: "字符串使用单引号、双引号或反引号"
```

## 技术栈

- **生成脚本**: Python + PyYAML + Jinja2
- **代码高亮**: Prism.js
- **样式**: 原生 CSS
- **部署**: GitHub Pages + GitHub Actions

## License

MIT
