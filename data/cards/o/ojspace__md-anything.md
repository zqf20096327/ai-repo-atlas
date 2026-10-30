# ojspace/md-anything

⭐ 49 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/ojspace/md-anything) · 个人维护

**本地优先的文件转 Markdown CLI + MCP 服务器，供 agent 摄取文档**

提供两个使用面：CLI `mda` 与 stdio MCP 服务器 `md-anything-mcp`，将文件、URL、媒体转换为 Markdown 或机器可读 JSON。支持 txt/html/pdf 等强格式，图片 OCR、EPUB/MOBI、音视频转录为 best-effort/optional，需 tesseract、Calibre、whisper-cpp 等可选工具或 OpenRouter 远程回退（需 API key，默认关闭）。一条命令接入 Claude Desktop/Cursor/VS Code 等 MCP 客户端，内置工作区路径与私网 URL 安全限制。默认安装不捆绑模型，核心流程无需云端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI 与 MCP 服务器共享同一转换管道，输出 Markdown 或稳定 JSON 信封
- 三级支持级别（strong/best-effort/optional）明确标注各格式能力与所需工具
- `mda mcp install` 一条命令接入 Claude Desktop/Cursor/VS Code 等客户端
- MCP 安全规则：路径限定工作区内，默认阻断私网/localhost URL

## 适用场景

- 为 RAG 或 agent 管线批量把 PDF/网页等文档转为 Markdown
- 让 Claude/Cursor 等 MCP 客户端直接读取和转换工作区文档
- 本地离线完成文档摄取，不依赖云服务

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L7: - a local-first CLI: `mda`
> L215: The goal is for md-anything to become the default open-source layer for document ingestion in agent pipelines — lo
> L223: - **Agent-ready**: CLI JSON output, chunk/provenance metadata, and an MCP server all share the same core pipeline

## 星数曲线

```mermaid
xychart-beta
    title "ojspace/md-anything 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-30 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `7369a6b1a1a5` · [字段定义](../../DATASET.md)*
