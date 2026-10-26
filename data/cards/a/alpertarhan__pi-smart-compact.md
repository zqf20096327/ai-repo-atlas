# alpertarhan/pi-smart-compact

⭐ 36 · TypeScript · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/alpertarhan/pi-smart-compact) · [官网](https://www.npmjs.com/package/pi-smart-compact) · 个人维护

**Pi Coding Agent 的上下文治理与会话延续扩展**

以 npm 包 pi-smart-compact 分发的 Pi Coding Agent 扩展：对长会话的工具输出做可恢复的归档清理，提供检查点与回退、命名锚点、跨会话只读检索、无模型调用的新会话 handoff，以及基于 Extract→Explore→Synthesize→Verify 流程的压缩并附带确定性校验。记忆后端（本地图/Mnemopi/Hindsight）为可选。需要 Pi 0.87.1+ 与 Node.js 22.19+；回退不撤销文件改动，校验不保证语义正确性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可恢复的工具输出归档与上下文清理
- EESV 流程的压缩并带确定性校验
- 命名锚点、跨会话只读检索与分支返回
- 无模型调用的新会话 handoff 种子

## 适用场景

- 长会话中降低旧工具输出噪音、保留证据可回查
- 研究绕路后保留报告并保留回到证据的路径
- 在新会话中延续目标、约束与未完成工作

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: Pi Continuity helps long-running Pi Coding Agent
> L10: this extension adds context hygiene and continuity policies around it.

## 星数曲线

```mermaid
xychart-beta
    title "alpertarhan/pi-smart-compact 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-26 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0dd3128a263b` · [字段定义](../../DATASET.md)*
