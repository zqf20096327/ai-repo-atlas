# torrentclaw/torrentclaw-mcp

⭐ 16 · TypeScript · MIT · 推送 2026-09-07 · [GitHub](https://github.com/torrentclaw/torrentclaw-mcp) · 组织维护

**让 AI 助手搜索影视资源与流媒体信息的 MCP 服务器**

TorrentClaw 官方维护的 Model Context Protocol 服务器，把 TorrentClaw API 封装为 MCP 标准，供 Claude Desktop、Claude Code 等 MCP 兼容 AI 助手调用。提供 10 个工具：影视搜索（含磁力链接、画质/语言等过滤）、自动补全、热门与最新内容、按国家的流媒体可用性查询、演职员表、.torrent 下载 URL、交互跟踪，以及通过 TrueSpec 提交与查询种子音视频质量分析。无需 API key 即可运行（可选 key 提升速率限制）。以 npx 直接运行或 git clone 源码构建。

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

- 10 个 MCP 工具：影视搜索返回种子、磁力链接与流媒体信息
- 按国家查询流媒体观看渠道（Netflix、Disney+ 等）
- TrueSpec 种子音视频质量分析提交与状态查询
- 无需 API key 即可运行（可选 key 提升速率限制）

## 适用场景

- 在 Claude 等 AI 助手中用自然语言查找影视种子与磁力链接
- 查询某部影片在哪些流媒体平台可看
- 对种子提交质量分析并跟踪扫描结果

## 场景标签

 · 领域:媒体搜索/MCP 工具

## 证据(README 行号)

> L8: Model Context Protocol server for TorrentClaw — giving AI assistants the ability to search movies and TV shows, find
> L10: torrentclaw-mcp is developed by TorrentClaw as part of its open-source ecosystem. It wraps the TorrentClaw API into

## 星数曲线

```mermaid
xychart-beta
    title "torrentclaw/torrentclaw-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `08a92e866fc7` · [字段定义](../../DATASET.md)*
