# chroma-core/package-search

⭐ 54 · 推送 2026-05-14 · [GitHub](https://github.com/chroma-core/package-search) · [官网](https://trychroma.com/package-search) · 组织维护

**Chroma 索引的公开代码包策展清单，供 MCP 代码检索**

由 Chroma 团队维护的公开代码包收录仓库：当前索引 3K+ 包，覆盖 NPM、PyPI、crates.io、Golang Proxy、GitHub Releases 等注册表。每个包以 config.json 声明标识符、tag 格式、文件 glob、版本采样等索引配置，社区可通过 PR 或 issue 申请收录，经 Chroma 团队审核后进入每日索引任务。检索入口为远程 MCP 服务器（需 trychroma.com API key），README 提供 Cursor、VS Code、Windsurf、Warp、Codex、Claude Code、OpenAI/Anthropic/Gemini SDK、Ollama 等客户端的接入配置示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 当前索引 3K+ 公开代码包，覆盖 NPM/PyPI/crates.io/Golang/GitHub Releases 等 7 种注册表
- 每包以 config.json 声明索引配置（tag 格式、glob、版本采样）
- 远程 MCP 服务器检索，支持十余种客户端接入配置
- PR/issue 两种收录方式，Chroma 团队审核

## 适用场景

- 申请将自己的开源包纳入 Chroma 代码检索索引
- 在 Cursor/Claude Code 等客户端中通过 MCP 搜索公开包源码
- 了解当前已被索引的包与注册表覆盖范围

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains a curated list of public code packages that Chroma keeps indexed into Chroma collections. T
> L149: This repository serves as the authoritative source of truth for packages that Chroma indexes for code search and r

## 星数曲线

```mermaid
xychart-beta
    title "chroma-core/package-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-25 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `2dac31428d85` · [字段定义](../../DATASET.md)*
