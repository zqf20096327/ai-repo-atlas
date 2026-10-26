# Dicklesworthstone/jeffreysprompts.com

⭐ 118 · TypeScript · NOASSERTION · 推送 2026-10-14 · [GitHub](https://github.com/Dicklesworthstone/jeffreysprompts.com) · [官网](https://jeffreyspromptscom.vercel.app) · 个人维护

**面向 AI 编程 agent 的提示词策展平台，提供浏览/复制/导出与 CLI**

由 Jeffrey Emanuel 维护的 agentic coding 提示词集合及配套平台：Web 应用支持浏览、搜索、评分、分享与 markdown 批量导出；`jfp` CLI 提供 JSON 输出、模糊搜索与 MCP server 模式（`jfp serve`），单二进制编译、无运行时依赖、跨 Linux/macOS/Windows。仓库为 monorepo：Next.js 应用、TypeScript 共享核心包、进行中的 Rust 移植。免费命令覆盖公共注册表；云同步、collections 等功能需 $10/月 Pro 订阅。提示词以 TypeScript 对象而非 markdown 定义。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Web 应用 + `jfp` CLI + MCP server 模式（`jfp serve`）
- Bun 编译单二进制、跨 Linux/macOS/Windows、全命令支持 --json
- 提示词以 TypeScript 对象定义，编译期类型检查
- 支持导出为 .md 或 Claude Code SKILL.md bundle

## 适用场景

- 查找并复制经过实际使用检验的 AI 编程提示词
- 让 AI agent 通过 MCP 或 JSON 输出检索提示词
- 批量导出提示词集合并分享给团队

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: **A curated collection of battle-tested prompts for agentic coding**
> L20: JeffreysPrompts.com is a platform for discovering, copying, exporting, and operationalizing curated prompts for AI 
> L126: |**MCP Server Mode**|`jfp serve` exposes prompts as MCP resources and tools|

## 星数曲线

```mermaid
xychart-beta
    title "Dicklesworthstone/jeffreysprompts.com 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 117 --> 119
    line [118, 118]
```

2026-10-18 118 → 2026-10-26 118（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1623d3e0d422` · [字段定义](../../DATASET.md)*
