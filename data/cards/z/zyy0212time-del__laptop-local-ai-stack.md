# zyy0212time-del/laptop-local-ai-stack

⭐ 10 · MIT · 推送 2026-11-27 · [GitHub](https://github.com/zyy0212time-del/laptop-local-ai-stack) · 个人维护

**消费级笔记本本地 AI 全栈调优工程案例：运行时+量化+推理策略+评测**

一份以案例研究形式发布的工程记录：在 RTX 5060 Laptop（8 GB VRAM）上围绕 llama.cpp 调优运行时配置（MoE 专家移至 CPU 后 4.15→43.31 t/s），报告并修补 FreeToken 推理引擎的两个 bug（提交 OSS PR），并执行 6 模型 × 32 题 × 2 条件的盲评（Reasoning Budget Arena，384 条响应），最终给出按角色分工的部署栈（默认/难任务/备选）。仓库还引用由此衍生的 Local AI Deploy 部署项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一 GGUF 下运行时配置调优：MoE 专家移至 CPU，4.15→43.31 t/s
- 发现并修补 FreeToken GGUF 加载器与 MoE CUDA 网格两个 bug，提交 PR
- Reasoning Budget Arena：6 模型 × 32 题 × 2 条件盲评，384 条响应
- 最终栈按角色路由：Ornith（默认）/Nex（难任务）/Gemma（备选）

## 适用场景

- 在 8 GB VRAM 笔记本上复现本地 MoE 模型的运行时调优方案
- 参考推理预算（reasoning budget）对交付质量影响的评测协议
- 了解跨推理引擎调试 GGUF 模型的过程与补丁细节

## 场景标签

`模型评测` `推理引擎` `模型量化` · 领域:评测与运维

## 证据(README 行号)

> L1: # The Fastest, Strongest Local AI Stack I Could Build on My Laptop
> L18: > **The best local model turned out not to be a model at all — it was a stack.**
> L172: The evaluation behind this story is the published **Reasoning Budget Arena** —


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `3e68b8c845f9` · [字段定义](../../DATASET.md)*
