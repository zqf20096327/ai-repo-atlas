# mimo-x/Code-Review-GPT-Gitlab

⭐ 816 · Python · MIT · 推送 2025-12-05 · [GitHub](https://github.com/mimo-x/Code-Review-GPT-Gitlab) · [官网](https://mimo-x.github.io/Code-Review-GPT-Gitlab/) · 组织维护 · 中文 README

**面向 Gitlab 的 LLM 辅助 Code Review 工具**

利用大模型（GPT、DeepSeek 等）对 Gitlab 的 Merge Request 进行代码评审，通过 Webhook 触发，提供 Prompt 提示词配置、消息通知与评审结果展示。针对 Gitlab 定制（计划支持 Github、Gitee、Bitbucket 等），支持接入多种大模型与私有化 LLM，正开发多 Agent 协同评审插件。提供 Docker Compose 一键部署与源码运行（前后端分离）两种方式，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 针对 Gitlab 定制，通过 Webhook 触发 MR 评审
- 支持对接多种大模型及私有化 LLM
- 可配置 Prompt 提示词与消息通知
- 开发中的 Multi-Agent 多 Agent 协同评审插件

## 适用场景

- 团队在 Gitlab MR 流程中加入 LLM 自动 Code Review
- 接入私有化 LLM 处理代码安全相关的评审
- 通过 Web 界面配置提示词并接收评审通知

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L13: > 一个利用大模型帮助我们在 Gitlab 上进行 Code Review 提升研发效能的项目 💪🏻 (( 包括但不限于 GPT 、DeepSeek 等🎁))
> L19: 🤖 我们正在开发 ** Multi-Agent ** 的插件，多个 ** Agent ** 协同工作，共同完成评审
> L21: 🐱 结合了 ** 多种大模型对接 ** 的能力 🚀

## 星数曲线

```mermaid
xychart-beta
    title "mimo-x/Code-Review-GPT-Gitlab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 815 --> 817
    line [816, 816]
```

2026-10-18 816 → 2026-10-25 816（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `60b05b50ca38` · [字段定义](../../DATASET.md)*
