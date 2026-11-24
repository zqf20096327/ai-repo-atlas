# qqbot-hub/qqbot-plugins

⭐ 6 · JavaScript · MIT · 推送 2026-10-31 · [GitHub](https://github.com/qqbot-hub/qqbot-plugins) · 个人维护 · 中文 README

**给 AI QQ 机器人补上可调用的 MCP 插件市场（51 插件/87 工具）**

面向按抖音教程部署的「SnowLuma + qq-bridge + DSH（大肥鱼）+ DeepSeek」QQ 机器人链路，提供插件市场层：网页一键安装插件后以 MCP stdio 服务器形式（mcp__qqbot__*）注册进 DSH，让 AI 能调用群管理、签到、记账、长期记忆、语音合成、文生图、识图/OCR 等工具。插件零依赖、跑在 Node 子进程沙箱中，危险操作要求 confirm=true，密钥 AES-256-GCM 加密存储。另聚合 NoneBot/AstrBot/Koishi 三家生态共 1368 个真实插件条目。

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

- 51 个插件 / 87 个工具，网页一键安装后变为 MCP 工具
- 长期记忆、语音合成、文生图、识图/OCR、视频理解等进阶能力
- 群管理带白名单与二次确认护栏，插件跑在 Node 权限沙箱
- 聚合 NoneBot/AstrBot/Koishi 三生态 1368 个插件目录

## 适用场景

- 让 QQ 群机器人真的执行禁言、记账、查天气等操作
- 给聊天机器人加长期记忆和语音/画画能力
- 统一管理多个 QQ 机器人框架生态的插件安装与更新

## 场景标签

`聊天机器人` `Agent 记忆` `图像生成` `语音合成` · 领域:Agent 开发

## 证据(README 行号)

> L10: 这个市场就是它的人生补丁：**51 个插件 / 87 项能力**，网页上点一下安装，
> L240: 2. 本项目用**同一配置文件、同一格式**追加一个自己的条目 `mcp-qqbot`（serverName `qqbot`），指向本仓库的 `mcp-server.mjs`（stdio JSON-RPC）；

## 星数曲线

```mermaid
xychart-beta
    title "qqbot-hub/qqbot-plugins 星数(近 3 点)"
    x-axis ["2026-11-01", "2026-11-16", "2026-11-24"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-11-01 5 → 2026-11-24 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `b0941ab25467` · [字段定义](../../DATASET.md)*
