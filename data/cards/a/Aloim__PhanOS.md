# Aloim/PhanOS

⭐ 37 · 推送 2026-10-22 · [GitHub](https://github.com/Aloim/PhanOS) · 个人维护

**面向 AI 的自动化项目操作系统：让 AI 在 PC 上执行项目工作**

PhanOS 是一个自动化项目操作系统项目，由编排器 Phanes、文档与上下文底座 Cyphor（待发布）及未公开的 Blueprompt 组成。其首个应用 PhanOS Builder 是 Windows/Linux 上的项目操作系统：内置编排器规划工作、并行分派多个 AI agent、校验结果并记录每步；项目上下文归属项目本身而非会话，各工作有唯一属主以支持并行。模型可为本地自带的微调模型或托管模型。README 自述项目处于建设早期，Builder 应用接近完成、Beta 访问需在 phanos.eu 申请，无安装说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 内置编排器：规划工作、并行分派多个 AI agent 并校验结果
- 项目上下文、决策与进度归属于项目而非单个会话
- 支持本地自带微调模型或外部托管模型，可调自主程度
- 安全设计：AI 产出签名、密钥隔离、程序仅获得狭窄临时权限

## 适用场景

- 让 AI 在本地机器上以项目为单位持续推进工作
- 多个 agent 并行处理项目任务且互不覆盖
- 编码工作流插件（首个插件）

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3:  The engine your AI plugs into, to get real work done on your PC.
> L12: The PhanOS Builder app takes that idea a step further. Instead of a suite of applications that you operate, it is a
> L29: A built-in orchestrator plans the work, hands pieces to several AI agents at once, checks what comes back and keeps

## 星数曲线

```mermaid
xychart-beta
    title "Aloim/PhanOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `cd8b8f56ce7f` · [字段定义](../../DATASET.md)*
