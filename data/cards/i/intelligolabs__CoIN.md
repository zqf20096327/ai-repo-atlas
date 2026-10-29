# intelligolabs/CoIN

⭐ 33 · Python · NOASSERTION · 推送 2026-04-01 · [GitHub](https://github.com/intelligolabs/CoIN) · [官网](https://intelligolabs.github.io/CoIN/) · 组织维护

**ICCV 25 论文官方库：协作实例导航任务与不确定性感知方法 AIUTA**

ICCV 2025 论文 'Collaborative Instance Object Navigation' 的官方代码库，作者来自意大利多所机构的团队。提出 CoIN 任务：具身导航中 agent 通过自然、开放式对话主动向用户提问以消除目标实例的不确定性；对应方法 AIUTA 结合 VLM 感知与 LLM 对话，含 Self-Questioner 自对话模块、不确定性估计与 Interaction Trigger 决定提问/继续/停止。基于 VLFM 代码库构建，使用 HM3D 数据集，提供 CoIN-Bench 基准（HuggingFace 下载）与可选的 IDKVQA 数据集复现，LLM 需设置 OpenAI 或 Groq 等 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Self-Questioner 自对话获取完整观测描述，不确定性估计缓解 VLM 感知偏差
- Interaction Trigger 决定何时向用户提问，减少用户输入
- CoIN-Bench 基准支持真实与模拟人类用户评估
- 提供多模态不确定性估计的 notebook 示例

## 适用场景

- 复现论文中的 CoIN 任务与 AIUTA 方法
- 在 HM3D 数据集上运行实例目标导航评测
- 使用 CoIN-Bench 或 IDKVQA 数据集做人机协作导航/VQA 研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L1: Collaborative Instance Object Navigation: Leveraging Uncertainty-Awareness to Minimize Human-Agent Dialogues [ICCV 2
> L13: Existing embodied instance goal navigation tasks, driven by natural language, assume human users to provide complet

## 星数曲线

```mermaid
xychart-beta
    title "intelligolabs/CoIN 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-29 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `857828beb459` · [字段定义](../../DATASET.md)*
