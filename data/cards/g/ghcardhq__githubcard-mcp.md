# ghcardhq/githubcard-mcp

⭐ 15 · MIT · 推送 2026-10-31 · [GitHub](https://github.com/ghcardhq/githubcard-mcp) · [官网](https://githubcard.com) · 组织维护

**让 AI 助手生成 GitHub 个人/仓库卡片的 MCP 服务器**

提供托管（Streamable HTTP）与本地（npx stdio）两种接入方式的 MCP server，使 Claude、Cursor、VS Code、Windsurf、Codex CLI 等 AI 客户端能够调用 create_card 等 10 个工具，基于实时 GitHub 数据生成个人主页与仓库卡片（SVG/PNG 链接及 Markdown/HTML 嵌入片段）。生成卡片需免费 API key，无 key 时仅可列出模板、配色与组件。本地模式加 --allow-file-writes 后可直接编辑磁盘上的 README。免费档每日 100 张，含水印；卡片展示实时 GitHub 数据且 create_card 幂等。

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

- 托管与本地（npx stdio）双接入方式，本地模式可直接更新 README 文件
- 10 个 MCP 工具：建卡、模板/配色/组件查询、卡片管理与用量查询
- create_card 幂等，卡片图片始终展示当前 GitHub 数据
- 错误返回稳定 code、retryable 标志与提示模型下一步的 hint

## 适用场景

- 让 Claude/Cursor 等 AI 客户端直接为我的 README 生成并插入 GitHub 卡片
- 为仓库生成可用作链接预览或社交帖子的卡片图片
- 在注册前先让 AI 列出模板与配色试用能力

## 场景标签

 · 领域:开发者工具/MCP 服务

## 证据(README 行号)

> L1: # GitHubCard MCP server
> L7: - **Hosted:** `https://githubcard.com/mcp` (Streamable HTTP). Nothing to install.
> L113: |Tool|Key|What it does|


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ea29c4598ae4` · [字段定义](../../DATASET.md)*
