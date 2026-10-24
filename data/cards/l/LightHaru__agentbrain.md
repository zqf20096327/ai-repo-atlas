# LightHaru/agentbrain

⭐ 107 · TypeScript · 推送 2026-08-13 · [GitHub](https://github.com/LightHaru/agentbrain) · [官网](https://openclaw.ai) · 个人维护

**为 OpenClaw AI agent 提供持久记忆与人格/情绪演化的插件**

运行于 OpenClaw 平台的脑启发认知架构插件：提供三类持久记忆（情景/语义/程序性）、6 项可演化人格特质、基于多巴胺/血清素/皮质醇/催产素建模的情绪系统、从用户纠正中学习教训并注入提示、基于行为模式的主动建议。每次对话自动注入约 200 token 认知上下文。状态存储于单个 SQLite 文件，语义召回使用本地 all-MiniLM-L6-v2 嵌入模型（3 级回退到 TF-IDF），全部本地运行。要求 OpenClaw 2026.3.24+ 与 Node.js 22+，磁盘约 50MB、内存约 100MB，无需 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三类记忆持久存储于单文件 SQLite，内容哈希去重
- 3 级语义召回回退：本地嵌入模型 → OpenClaw 嵌入缓存 → TF-IDF
- 多巴胺/血清素/皮质醇/催产素神经化学建模驱动情绪
- 自动检测用户纠正语句并按置信度注入提示

## 适用场景

- 让长期使用的 agent 记住用户偏好与历史纠正
- 为对话型 agent 添加随交互演化的人格与情绪
- 基于行为模式获得主动操作建议

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L1: AgentBrain — Brain-Inspired Cognitive Architecture for AI Agents
> L50: openclaw plugins install @lightharu/agentbrain
> L439: - **OpenClaw:** 2026.3.24 or later

## 星数曲线

```mermaid
xychart-beta
    title "LightHaru/agentbrain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-24 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f4ae85f2e1e2` · [字段定义](../../DATASET.md)*
