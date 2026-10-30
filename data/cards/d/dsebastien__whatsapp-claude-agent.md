# dsebastien/whatsapp-claude-agent

⭐ 42 · TypeScript · MIT · 推送 2026-02-09 · [GitHub](https://github.com/dsebastien/whatsapp-claude-agent) · 个人维护

**把 WhatsApp 消息接入 Claude Code，远程操作本机文件**

以独立二进制形式运行的桥接程序：通过 WhatsApp 收发消息，调用 Claude Agent SDK 在指定工作目录下执行任务，使用户能用手机远程与本地文件和代码交互。支持五种 SDK 权限模式切换、会话持久化/恢复/分叉、模型切换（opus/sonnet/haiku 等速记名）、自定义系统提示词与 CLAUDE.md 加载、群组模式定向触发，以及手机号白名单安全限制。提供 curl 安装脚本下载多平台二进制，内置自更新命令，配置可经 JSON 文件管理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Claude Agent SDK 的 WhatsApp 消息桥接，含会话持久化、恢复与分叉
- 五种权限模式可经 WhatsApp 命令切换（default/acceptEdits/bypass/plan/dontAsk）
- 模型速记切换、系统提示词与 CLAUDE.md 来源配置
- 手机号白名单安全限制与群组模式定向触发

## 适用场景

- 出门在外用 WhatsApp 远程让 Claude 处理本机项目文件
- 在 WhatsApp 群里 @agent 让其执行任务并回复权限确认
- 通过 /fork 从同一会话分叉探索不同方案

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L3: Bridge WhatsApp with Claude Code - interact with your files via WhatsApp messages.
> L7: - **Claude Agent SDK integration**: Direct integration with Claude Agent SDK
> L300: These align with the Claude Agent SDK permission modes:

## 星数曲线

```mermaid
xychart-beta
    title "dsebastien/whatsapp-claude-agent 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25", "2026-10-30"]
    y-axis "stars" 39 --> 43
    line [40, 41, 42, 42]
```

2026-10-18 40 → 2026-10-30 42（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `32bfd1555246` · [字段定义](../../DATASET.md)*
