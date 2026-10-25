# NeoVertex1/SuperPrompt

⭐ 6,424 · 推送 2026-04-26 · [GitHub](https://github.com/NeoVertex1/SuperPrompt) · 个人维护

**引导 LLM 深度推理的提示词模板，配 Claude 使用**

一个开源的 XML 结构化提示词（meta-prompt）工程：通过 <prompt_metadata> 元数据与 <think> 标签等记号引导模型（首选 Claude，作为项目知识中的自定义指令，也可用于其他 LLM）在 tree-of-thought 中探索、自适应生成任务级元数据，以求产生新颖视角的输出；作者称其作用类似“软越狱”，Claude 有时会拒绝执行，输出也可能包含幻觉。项目自述处于 forever beta 阶段。给从事提示词工程与研究 AI agent 行为的用户使用，使用方式为复制提示词文本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- XML 标签 + prompt_metadata 元数据驱动模型自适应生成任务级元数据
- <think> 标签约定 ?(...) → !(...) 推理记号
- 首选 Claude 作为自定义指令使用，兼容其他 LLM

## 适用场景

- 把提示词放入 Claude 项目知识中引导模型深度推理
- 探索模型非常规视角与新想法
- 研究提示词工程与 agent 思维链方法

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L6: >This is a project that I decided to open source because I think it might help others understand AI agents. This pro
> L9: SuperPrompt is a canonical holographic metadata. It uses notations and other methods to turn logical statements into

## 星数曲线

```mermaid
xychart-beta
    title "NeoVertex1/SuperPrompt 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 6422 --> 6426
    line [6423, 6425, 6424]
```

2026-10-18 6,423 → 2026-10-25 6,424（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 high · 依据 README sha `9fab332d76c2` · [字段定义](../../DATASET.md)*
