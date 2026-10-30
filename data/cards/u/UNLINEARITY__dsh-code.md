# UNLINEARITY/dsh-code

⭐ 43 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/UNLINEARITY/dsh-code) · 个人维护 · 中文 README

**DeepSeek Harness 的终端编码界面（TUI 插件）**

构建于官方 @deepseek-ai/dsh-base 之上的 out-of-tree 插件包，以终端 TUI 形式提供 DeepSeek Harness 的 Agent、模型、工具、会话与插件服务。功能覆盖会话管理与恢复、每会话 Agent Preset、模型与供应商/API key/OAuth 管理、图像附件、/diff 与 /review 代码审查、排队的与插话的消息、模型切换动画。需 Node ^22.19 || >=24 与 preview 版 dsh CLI（0.2.0-rc.2），依赖精确锁版；上游处于开发者预览阶段，可能引入破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 在终端复用 DSH 的 Agent/会话/工具/权限/沙箱/插件服务
- 每会话独立 Agent Preset 与模型/供应商管理（/model、/mode）
- 排队消息与插话（steer）消息两种运行中发送方式
- 图像附件、/diff 文件级变更查看与 /review 只读代码审查

## 适用场景

- 在终端中用 DeepSeek 模型完成编码任务与代码审查
- 跨会话恢复历史上下文并追踪 token/缓存用量
- 在任务运行中排队或即时纠偏指令

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L17: **DSH-Code is a terminal coding interface for DeepSeek Harness (`dsh`).** It is composed as an out-of-tree bundle o
> L19: DeepSeek Harness registers models, tools, storage, policies, and interfaces as plugins through Cordis. Durable sess

## 星数曲线

```mermaid
xychart-beta
    title "UNLINEARITY/dsh-code 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-30 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2b86a14efe87` · [字段定义](../../DATASET.md)*
