# brcampidelli/chimera-agent

⭐ 29 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/brcampidelli/chimera-agent) · 个人维护

**多模型融合、可自我治理的自托管 AI agent**

开源（Apache-2.0）自主 agent，Python 3.11-3.13，处于 alpha 阶段。核心机制：对难题同时询问多个模型，由一个模型比较答案、合成器合并输出；可跨会话存储用户告知的事实并沉淀为可复用技能；高风险动作经过安全检查，不可信代码可在断网容器中运行（容器隔离为可选项）。支持作为消息应用 bot 部署、7×24 服务器运行，通过单一接口接入托管或本地模型。README 明确声明：累积学习未显示出可测量的任务提升，七次预注册实验无显著效应并撤回过一次阳性结果；安全层为启发式污点追踪而非真实数据流。附预注册基准测试（SWE-bench 局部切片等），并公示失败与撤回记录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多模型并发作答＋模型比较＋合成器合并的融合机制
- 事实跨会话存储与重复任务转为可复用技能（学习效果无显著证据，项目自行声明）
- 风险动作安全检查、破坏性操作需确认、可选断网容器沙箱
- 以真实 diff 与 A/B 结果为门控的自我进化步骤，附预注册基准与撤回记录

## 适用场景

- 自托管一个可接入多种托管/本地模型的自主 agent
- 让它代为执行目标：拆解任务、编辑文件、跑测试，仅保留通过的改动
- 作为消息应用 bot 或 7×24 服务器服务运行
- 查看带置信区间的诚实基准与撤回记录以评估项目成熟度

## 场景标签

`多智能体` `聊天机器人` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L23: For hard questions, Chimera asks **several** AI models at once; a model compares their answers,
> L43: - 🧠 **Several models, one answer.** For tough questions, Chimera asks several models the same thing, lets one model
> L44: - 🚀 **It does the work, not just talk.** Give it a goal. It breaks it down, uses tools, edits files, runs the tests

## 星数曲线

```mermaid
xychart-beta
    title "brcampidelli/chimera-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b62d02cb6393` · [字段定义](../../DATASET.md)*
