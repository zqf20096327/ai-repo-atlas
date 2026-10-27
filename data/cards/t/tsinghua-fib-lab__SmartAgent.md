# tsinghua-fib-lab/SmartAgent

⭐ 28 · Python · MIT · 推送 2026-07-27 · [GitHub](https://github.com/tsinghua-fib-lab/SmartAgent) · 组织维护 · 中文 README

**AAAI 2026 论文官方库：网络世界具身个性化 Agent 与 SmartSpot 基准**

清华大学 FIB 实验室论文 "SmartAgent: Chain-of-User-Thought for Embodied Personalized Agent in Cyber World" 的官方代码仓库。提出 COUT（Chain-of-User-Thought）三阶段推理范式：Thought #1 中 Agent 执行 GUI 动作搜索候选物品池，Thought #2 基于动作推断指令背后的隐含需求，Thought #3 在池内向用户推荐物品。附带 SmartSpot 基准数据集（Google Drive 提供图像与中英文标注），提供数据预处理、训练、评测与 LoRA 检查点转换脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- COUT 三阶段推理范式：GUI 搜索→隐含需求推断→池内推荐
- SmartSpot 基准数据集（图像数据与中/英标注）
- 提供预处理、训练、评测、LoRA 检查点转换完整脚本

## 适用场景

- 复现论文中的具身个性化 Agent 训练与评测流程
- 基于 SmartSpot 基准做个性化推荐 Agent 研究
- 在 GUI 环境中训练执行搜索与推荐的 LLM Agent

## 场景标签

`模型评测` `微调` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L1: # [AAAI 2026] SmartAgent: Chain-of-User-Thought for Embodied Personalized Agent in Cyber World
> L10: # Chain-of-User-Thought (COUT) Reasoning Paradigm
> L11: We formulate COUT to achieve embodied personalized agent training in terms of three stages of thought. In Thought #

## 星数曲线

```mermaid
xychart-beta
    title "tsinghua-fib-lab/SmartAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-27 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `03646b672e98` · [字段定义](../../DATASET.md)*
