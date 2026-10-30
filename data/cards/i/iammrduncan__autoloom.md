# iammrduncan/autoloom

⭐ 15 · Python · MIT · 推送 2026-04-18 · [GitHub](https://github.com/iammrduncan/autoloom) · [官网](https://thresher.sh) · 个人维护

**基于 tinyloom 的自学习自主 agent 运行器，带心跳调度与 TUI**

构建在 tinyloom 之上的自主 agent 封装：核心运行时约 225 行，整个核心库约 900 行，含插件约 1500 行。状态以纯文件形式存于 ~/.autoloom（会话/任务/记忆/技能），通过 cron 管理 heartbeat 周期运行，自带 Textual TUI 与本地 webhook 服务器，支持插件与知识图谱自学习。继承 tinyloom 的 shell 执行与文件编辑能力，本身非沙箱，README 明确警告应在容器或 microVM 中隔离运行；提供 Docker/Podman/microsandbox/Kata 等沙箱指南。尚未发布首个 PyPI 版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 纯文件状态存储（~/.autoloom）与 cron 心跳自主运行
- Textual TUI、headless JSONL 会话与本地 webhook 服务器
- 插件体系与知识图谱自学习机制
- 非沙箱设计，提供多种容器/microVM 隔离指南

## 适用场景

- 在 VPS 上定时心跳运行，自主研究并开发/测试插件
- 通过自然语言指令执行持久化任务会话
- 以本地 webhook 触发 agent 工作

## 场景标签

`编码 Agent` `AI 助手` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Autoloom is a tiny self-learning autonomous agent wrapper built on top of `tinyloom`.
> L76: - `autoloom setup` walks an interactive setup that configures agent identity, model provider/credentials/tuning, sa

## 星数曲线

```mermaid
xychart-beta
    title "iammrduncan/autoloom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4efb0dbe44c8` · [字段定义](../../DATASET.md)*
