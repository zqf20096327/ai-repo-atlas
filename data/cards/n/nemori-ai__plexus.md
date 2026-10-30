# nemori-ai/plexus

⭐ 15 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/nemori-ai/plexus) · [官网](https://plexus.vibecoding.icu/) · 组织维护

**给开发者：本地 AI agent 能力网关，受控暴露本机软件**

用户自行安装的本地开源网关，基于 Bun + TypeScript、macOS 优先。通过单一自描述端点让 AI agent 按发现→理解→授权→调用四步使用本机软件能力：内置 Obsidian、Apple 日历/提醒/备忘录/邮件/通讯录/照片、Shortcuts、浏览器、Claude Code、Codex 等数据源。信任机制：默认拒绝、按能力作用域授权、写/执行需人工批准、可撤销、留有审计日志；双凭证（connection-key 与每 agent PAT）分离管理与调用身份。限制：第一方数据源未做真实 macOS TCC E2E 验证，桌面应用为未签名开发版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一自描述端点供任意 agent 发现并调用本机能力
- 默认拒绝 + 按能力作用域授权 + 信任窗口 + 可撤销 + 审计日志
- Obsidian、Apple 套件、浏览器、Claude Code、Codex 等第一方数据源
- manifest 方式编写扩展并预览其安全面

## 适用场景

- 让 Claude Code 等 agent 在受授权范围内读取我的 Obsidian 库或 Apple 数据
- 通过管理 UI 逐项批准 agent 的写/执行请求并随时撤销
- 把本机软件封装为 agent 可发现的能力并保留审计记录

## 场景标签

 · 领域:AI agent 基础设施/安全

## 证据(README 行号)

> L3: > **A local capability gateway for AI agents.** Plexus is a user-installed,
> L4: > open-source gateway that exposes **one** AI-native **self-describe** endpoint, so
> L5: > any AI agent can **DISCOVER → UNDERSTAND → be GRANTED → CALL** the capabilities of

## 星数曲线

```mermaid
xychart-beta
    title "nemori-ai/plexus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `60f9435f6a80` · [字段定义](../../DATASET.md)*
