# tegridydev/auto-md

⭐ 167 · Python · MIT · 推送 2026-08-30 · [GitHub](https://github.com/tegridydev/auto-md) · 个人维护

**把代码库/文档/GitHub 仓库转为 Markdown 与 RAG 就绪数据包的本地网页应用**

以私有本地 Web 应用形式运行的转换工具：读取本地文件、文件夹、公共 GitHub 仓库、网页、压缩包及 PDF/DOCX/图像等，输出单一 Markdown 文档（含出处、锚点、目录）或 RAG 数据包（chunks.jsonl、manifest.json）。分块遵循标题、段落、代码等边界，提供确定性 token 估算。服务器仅绑定回环地址，出站请求仅限用户显式添加的 URL，默认限制单任务 512 MiB。通过 uv 运行 Python 脚本启动，不需要 Docker、Node.js、API key 或云服务。

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

- 输出含稳定 ID 与来源元数据的 chunks.jsonl RAG 数据包
- 支持 GitHub 仓库、网页、压缩包、PDF/DOCX/图像与本地 OCR
- 遵守 .gitignore/.automdignore 的智能过滤
- 仅绑定 127.0.0.1，不使用分析、CDN 或 AI API

## 适用场景

- 把整个代码仓库整理成一份 Markdown 交给 LLM 阅读
- 为 RAG 管道生成分块与元数据齐全的语料包
- 在不上传文件的前提下本地转换 PDF 与扫描件

## 场景标签

`文档解析` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L3: Auto-MD turns codebases and documents into one clean Markdown file or a RAG-ready bundle. It runs as a private local
> L41: RAG bundle produces a ZIP containing:

## 星数曲线

```mermaid
xychart-beta
    title "tegridydev/auto-md 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 166 --> 168
    line [167, 167]
```

2026-10-18 167 → 2026-10-30 167（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `1a81d8cc95ea` · [字段定义](../../DATASET.md)*
