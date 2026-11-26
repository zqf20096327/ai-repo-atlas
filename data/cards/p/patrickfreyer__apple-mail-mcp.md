# patrickfreyer/apple-mail-mcp

⭐ 267 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/patrickfreyer/apple-mail-mcp) · 个人维护

**让 AI 助手通过 MCP 读写、搜索、整理 Apple Mail**

基于 FastMCP 的 macOS MCP server，通过 AppleScript 操作 Mail.app，提供 28 个工具：邮件读取与跨账户搜索、邮箱整理（移动/标记/删除并带 dry-run）、撰写/回复/转发/草稿、附件处理，以及待回复识别、高频发件人分析、统计导出。支持 --read-only 只读模式、批量操作默认上限、写入与附件路径的拒绝清单与可选白名单；本机运行、不自行发起网络请求。安装方式覆盖 Claude Code 插件、uvx/pip、MCPB 与源码。

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

- 28 个 MCP 工具覆盖读取、搜索、整理、撰写、附件、统计与导出
- 只读模式与批量操作默认上限（如 move_email 默认 1 封）
- 写入/附件路径拒绝清单（shell 启动文件、SSH/GPG/AWS 凭据等）与可选目录白名单
- 附带 Claude Code 邮件管理技能（Inbox Zero、日常分诊等工作流）

## 适用场景

- 用自然语言让 Claude 搜索、总结和回复 Apple Mail 邮件
- 批量整理收件箱：按条件移动、归档、标记邮件
- 统计近 30 天邮件量与高频发件人并导出为 TXT/HTML
- 只读接入让助手分析邮件而不允许发送

## 场景标签

 · 领域:效率工具/邮件自动化

## 证据(README 行号)

> L1: # Apple Mail MCP Server
> L78: ## Tools (28)
> L231: - Claude Desktop or any MCP-compatible client

## 星数曲线

```mermaid
xychart-beta
    title "patrickfreyer/apple-mail-mcp 星数(近 19 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-18", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-26"]
    y-axis "stars" 231 --> 270
    line [234, 235, 236, 237, 240, 241, 243, 245, 246, 235, 250, 252, 255, 256, 257, 261, 262, 264, 267]
```

2026-10-24 234 → 2026-11-26 267（+33）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `e0d4ab2dafe3` · [字段定义](../../DATASET.md)*
