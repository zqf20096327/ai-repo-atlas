# atpuxiner/docsloader

⭐ 52 · Python · MIT · 推送 2025-12-16 · [GitHub](https://github.com/atpuxiner/docsloader) · 个人维护 · 中文 README

**Python 异步文档加载库：多格式解析供 RAG 使用**

docsloader 是一个 Python 包，提供多种文件后缀的异步文档加载器：覆盖 txt、csv、md、html、excel、ppt、word、pdf 与图片等格式，各格式有专属 Loader 类，另有 AutoLoader 按后缀自动选择加载器。所有 Loader 实现异步 load 方法。安装方式为 pip install docsloader（要求 Python>=3.11），可按文件类型选装依赖（如 docsloader[pdf]），主题标签表明其定位为 RAG 文档解析与知识库构建的输入环节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 类文件后缀的专属 Loader 与按后缀自动选择的 AutoLoader
- 全部 Loader 实现异步 load 方法
- pip 按格式选装可选依赖（txt/csv/md/xlsx/pptx/docx/pdf/img/auto）

## 适用场景

- RAG 知识库构建时统一解析多种格式的文档
- 批量异步加载并解析本地文件内容
- 按需安装特定格式的解析依赖

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L28: The `docsloader` package provides asynchronous document loaders for various file suffixes. It includes dedicated lo
> L29: for specific file types and an `AutoLoader` that automatically selects the appropriate loader based on file suffix.

## 星数曲线

```mermaid
xychart-beta
    title "atpuxiner/docsloader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-25 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `4bcc9dff917a` · [字段定义](../../DATASET.md)*
