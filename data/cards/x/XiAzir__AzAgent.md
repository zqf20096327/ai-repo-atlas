# XiAzir/AzAgent

⭐ 4 · TypeScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/XiAzir/AzAgent) · 个人维护 · 中文 README

**面向 DeepSeek Harness 的自主编码助手，覆盖 GitHub/Web/飞书/QQ**

由 XiAzir 独立维护的自主编码助手，以 DeepSeek Harness 扩展形式运行，支持 Windows 与 Linux。功能包括仓库模式与个人模式、Web 任务收件箱、通过 OneBot v11 接入 QQ（支持文件与视觉媒体输入、语义任务路由）、飞书与 GitHub 集成、不可变任务工件、Router 状态回复与外部 Watchdog。设计原则强调尽量少占用人类注意力，仅在规则允许时行动。安装步骤较多，README 提供由编码 agent 陪同逐步执行的 SETUP.md 流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 DeepSeek Harness 扩展形式运行，支持 Windows 与 Linux
- 通过 OneBot v11（NapCat 或 WebSocket）接入 QQ，支持文件与视觉媒体输入
- 提供个人模式、任务房间、结果验证与独立 Watchdog 机制
- SETUP.md 引导编码 agent 逐步完成安装配置

## 适用场景

- 让 agent 自主处理 GitHub 仓库任务并产出可验证结果
- 通过 QQ/飞书提交任务并接收路由与状态回复
- 部署带 Watchdog 监督与外部恢复机制的个人助理

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L3: AZAGENT is an autonomous coding assistant maintained by XiAzir. It handles
> L5: an extension for DeepSeek Harness
> L10: AZAGENT supports repository mode and personal mode, including a Web task inbox,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `c752f7d2f368` · [字段定义](../../DATASET.md)*
