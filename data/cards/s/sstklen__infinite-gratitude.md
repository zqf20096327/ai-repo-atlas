# sstklen/infinite-gratitude

⭐ 31 · MIT · 推送 2026-03-15 · [GitHub](https://github.com/sstklen/infinite-gratitude) · [官网](https://washinmura.jp) · 个人维护 · 中文 README

**Claude Code 技能：并行调度最多 10 个 AI 研究代理产出报告**

一个以 SKILL.md 形式安装到 Claude Code 的多代理研究技能：通过 /infinite-gratitude 命令按主题并行派出最多 10 个研究代理，各自调研不同角度后汇总为多份研究报告，支持 quick/normal/deep 三档深度、代理数（1-10）与迭代波次（默认 3）参数。README 记录了一次宠物 AI 识别调研实例：10 个并行代理、30 分钟产出 9 份报告。一条 curl 命令完成安装，需在 Claude Code 环境中使用；MIT 许可。

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

- 最多 10 个代理并行调研，可配深度/代理数/迭代波次
- 以 Claude Code 技能文件形式安装，单条 curl 命令部署
- README 记录实例：30 分钟产出 9 份研究报告

## 适用场景

- 并行对比多个工具或库做技术调研
- 每个代理各分析一个竞争对手做竞品研究
- 多代理并行读论文做文献综述

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L9: > **Dispatch 10 parallel research agents** — like having a team of researchers working for you simultaneously
> L26: **Solution:** Dispatch multiple AI agents in parallel. Each agent researches a different angle, then brings finding

## 星数曲线

```mermaid
xychart-beta
    title "sstklen/infinite-gratitude 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `516cb8afdd31` · [字段定义](../../DATASET.md)*
