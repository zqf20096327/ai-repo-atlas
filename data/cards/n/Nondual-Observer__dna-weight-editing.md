# Nondual-Observer/dna-weight-editing

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/Nondual-Observer/dna-weight-editing) · [官网](https://huggingface.co/Nondual-Observer/Qwen3.5-0.8B-SGNE-CC) · 个人维护

**对 Qwen3.5-0.8B 两种免训练权重编辑的几何审计与基准研究**

针对 Qwen3.5-0.8B 的权重空间研究项目：审计 MIT-p50c 权重编辑的几何性质，并与之对比 SGNE-CC（球面范数保持编辑，3.13 MiB 补丁，无需梯度重训练）。提供补丁文件、FP64 验证脚本、5 个基准 × 2 种解码设置 × 3 个模型的完整逐条 JSONL 生成轨迹、CPU 核验器与 McNemar 配对检验。面向研究权重编辑机制的读者；结果限于该单一 0.8B 模型与 32,768 token 生成长度设定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SGNE-CC 为 3.13 MiB 免训练补丁，保持列范数（BF16 舍入后最大偏差约 0.16%）
- 5 个基准 × 贪婪/模型卡两种解码 × 3 模型的完整逐条轨迹与配对显著性检验
- FP64 补丁几何验证脚本与 BF16/T4-FP16 数值一致性检查
- 30 组完整推理运行，每模型每设置覆盖 1,128 个任务

## 适用场景

- 复现并核验 Qwen3.5-0.8B 权重补丁的几何性质
- 研究循环层与注意力层编辑对推理截断行为的影响
- 获取可审计的基准评测轨迹用于二次分析

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # Weight-Space Audit of MIT-p50c and DNA Weight Editing (SGNE-CC) at a 32,768-Token Generation Limit
> L7: This study audits the weight geometry of MIT-p50c and compares it with **SGNE-CC** (*Spherical Gated Norm-preserving
> L44: All ten benchmark slices (5 datasets × 2 regimes) across all three models (Qwen3.5-0.8B, MIT-p50c, SGNE-CC) include

## 星数曲线

```mermaid
xychart-beta
    title "Nondual-Observer/dna-weight-editing 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-19 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `d5dec1eb96a3` · [字段定义](../../DATASET.md)*
