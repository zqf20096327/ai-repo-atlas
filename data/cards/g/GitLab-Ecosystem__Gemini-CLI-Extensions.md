# GitLab-Ecosystem/Gemini-CLI-Extensions

⭐ 15 · TypeScript · 推送 2026-04-16 · [GitHub](https://github.com/GitLab-Ecosystem/Gemini-CLI-Extensions) · [官网](https://about.gitlab.com) · 组织维护

**为 Gemini CLI 接入 GitLab MCP 工具的扩展**

Gemini CLI 扩展：将 CLI 连接到 GitLab 官方托管的 MCP 服务器（gitlab.com/api/v4/mcp），通过 npx mcp-remote 桥接，无需本地 Ruby 运行时。以 commands/*.toml 定义斜杠命令，映射 issue、MR、pipeline、work item 与搜索等 MCP 工具，首次运行需浏览器 OAuth 授权。要求 GitLab SaaS 账号开启 mcp_server 等功能开关、Gemini CLI v0.8.0+ 与 Node.js 20+，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 连接 GitLab 托管 MCP 服务器，无需本地 Ruby 运行时
- 提供 issue/MR/pipeline/搜索等约 12 个斜杠命令
- 支持 gemini extensions install 一键安装或本地 link 开发

## 适用场景

- 在 Gemini CLI 中直接查看和创建 GitLab issue 与 MR
- 通过命令查询 pipeline 状态与作业
- 在 CLI 内执行 GitLab 项目搜索与语义搜索

## 场景标签

 · 领域:开发者工具/GitLab 集成

## 证据(README 行号)

> L3: Connects Gemini CLI to the GitLab-hosted Model Context Protocol (MCP) server (`https://gitlab.com/api/v4/mcp`). Expo
> L36: - **Manifest**: `gemini-extension.json` (defines `npx mcp-remote`).

## 星数曲线

```mermaid
xychart-beta
    title "GitLab-Ecosystem/Gemini-CLI-Extensions 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `ac23d7f1ef74` · [字段定义](../../DATASET.md)*
