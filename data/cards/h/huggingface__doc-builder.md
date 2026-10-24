# huggingface/doc-builder

⭐ 144 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/huggingface/doc-builder) · 组织维护

**构建 Hugging Face 各仓库文档的工具包**

Hugging Face 用于构建旗下仓库文档的 Python 包：读取 Markdown/notebook 源文件与库的 docstring，生成 MDX 或 HTML 文档，支持本地预览、版本指定、页级 HTML 构建缓存、notebook 转换与反向转换。可在不安装 torch 等重依赖的情况下 mock 导入构建文档（在 accelerate 上验证 46/48 页与真实构建字节一致）。还提供 docstring 代码风格化命令与 pre-commit 钩子，以及 GitHub Actions 工作流模板。通过 pip 安装，面向 HF 库维护者与文档贡献者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成 MDX/HTML 文档并支持本地 preview
- mock 重依赖（如 torch）以轻量方式构建文档
- 页级 HTML 构建缓存，仅重渲染内容变更页
- 提供 docstring 风格化命令与 pre-commit 钩子、GitHub Actions 模板

## 适用场景

- 为 Hugging Face 库构建与预览文档
- 在 CI 中随 PR 自动构建文档
- 将教程转换为 notebook 或将 notebook 转为 mdx
- 统一团队的 docstring 与代码示例格式

## 场景标签

 · 领域:软件开发/文档构建

## 证据(README 行号)

> L3: This is the package we use to build the documentation of our Hugging Face repos.
> L43: doc-builder build {package_name} {path_to_docs} --build_dir {build_dir}

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/doc-builder 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 143 --> 146
    line [145, 144, 144]
```

2026-10-18 145 → 2026-10-24 144（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `55fb98c818e4` · [字段定义](../../DATASET.md)*
