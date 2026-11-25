# Interactive-Active-AI/NextTransformer

⭐ 493 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/Interactive-Active-AI/NextTransformer) · [官网](https://interactive-active-ai.github.io/NextTransformer/) · 组织维护 · 中文 README

**面向研究者的下一代 Transformer 架构训练评测框架与自动化研究平台**

统一框架下训练与评测多种 Transformer 变体（线性/稀疏注意力、循环深度、残差流、MoE 等）：所有方法在相同数据（49.152B tokens）、相同训练 FLOPs（±1% 审计）与相同检查点下对比，结果为可审计的文件化记录。提供排行榜、学习曲线、模型卡与浏览器端 observatory；Arena v2 支持让任意 LLM agent 通过 MCP 工具在相同协议下提交新架构。安装要求 Linux、NVIDIA GPU 与 uv，数据集约 600 GB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多架构插件接入同一 trainer、数据管线与评估（GQA/NSA/MoBA/GDN/KDA 等）
- 算力对齐的公平协议：±1% 准入审计、统一数据与评估检查点
- Arena v2 agent 原生研究通道：MCP 工具、计量算力与研究轨迹
- MoE track 与 2K 扩展研究（16 组 T3 配置、固定 10²⁰ FLOPs）

## 适用场景

- 在相同算力预算下对比不同 Transformer 架构的训练效率与验证 BPB
- 把自己的新架构以插件形式提交到统一基准排行榜
- 让 LLM agent 在相同协议下自主搜索并提交新架构
- 在浏览器中查看各次训练运行的学习曲线与模型卡

## 场景标签

`模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3:  The comprehensive, cutting-edge open-source framework, benchmark and auto-research platform for next-generation Tra
> L38: Many architectures, one framework: attention, sparse, linear, looped, residual and hybrid models such as GQA, NSA, 
> L186: Any LLM, with or without a research framework, can already enter an architecture today: it is trained under the sa

## 星数曲线

```mermaid
xychart-beta
    title "Interactive-Active-AI/NextTransformer 星数(近 17 点)"
    x-axis ["2026-11-01", "2026-11-02", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 0 --> 540
    line [16, 87, 393, 402, 404, 408, 411, 412, 421, 457, 476, 481, 483, 487, 489, 492, 493]
```

2026-11-01 16 → 2026-11-25 493（+477）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `fcb9c354bb2b` · [字段定义](../../DATASET.md)*
