# josepha-mayo/model-unfetter

⭐ 53 · Python · Apache-2.0 · 推送 2026-06-28 · [GitHub](https://github.com/josepha-mayo/model-unfetter) · [官网](https://github.com/HOLYKEYZ/model-unfetter) · 个人维护

**移除 LLM 拒绝行为的安全研究工具（方向消融引擎）**

面向 AI 安全研究与红队的 LLM 去对齐引擎：通过计算拒绝向量并对权重矩阵做方向消融（含激进斥力正交化），去除模型的拒绝行为。支持 CPU、单/多 GPU、流式（1T 参数级）与 GGUF 直编后端，自动检测 20+ 模型架构；适用于 0.5B-3B 等小模型。提供 Python API 与 CLI，附带消融后验证与基准测试脚本，可导出 GGUF 配合 Ollama/LM Studio 部署。仅限安全研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 列式投影数学与激进斥力（强度 1.5+）消融方法
- CPU/单GPU/多GPU/流式/GGUF 直编五类后端与硬件自动检测
- SVD 范数保持与 LoRA 恢复微调以减少能力损失
- Optuna 超参搜索与消融后验证/基准测试脚本

## 适用场景

- 安全研究中分析并移除模型的拒绝方向
- 在小模型或低配 CPU 上做消融实验
- 消融后导出 GGUF 在本地运行时部署验证

## 场景标签

 · 领域:LLM 安全研究/模型修改

## 证据(README 行号)

> L14: Model Unfetter is a production-grade engine for removing refusal behaviors from Large Language Models. While inspir
> L33: |`ablation.py`|**Standard directional ablation** — Projects refusal direction out of weight matrices. Supports `dir

## 星数曲线

```mermaid
xychart-beta
    title "josepha-mayo/model-unfetter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-25 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1d255ad79187` · [字段定义](../../DATASET.md)*
