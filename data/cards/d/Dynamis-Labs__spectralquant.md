# Dynamis-Labs/spectralquant

⭐ 204 · Python · MIT · 推送 2026-05-15 · [GitHub](https://github.com/Dynamis-Labs/spectralquant) · [官网](https://arxiv.org/abs/XXXX.XXXXX) · 组织维护

**LLM 推理 KV 缓存压缩方法的研究论文代码（NeurIPS 2026 投稿）**

面向大语言模型推理场景的 KV cache 压缩方法及配套论文工件：通过一次约 15 秒的特征谱校准识别 key 向量中承载信号的头维度（跨 6 个模型 4 类架构约占 3–4%），对剩余维度停用误差修正，实现校准式压缩与按维度注水的比特分配。仓库提供 9 个模块的核心库、10 个实验脚本、结果 JSON 及论文 LaTeX 源，逐条声明论文数字到脚本与结果文件的映射。实验需 Python 3.10+、PyTorch 2.2+ 与 CUDA GPU（实验在 NVIDIA B200 上运行），MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 校准式特征谱分析识别 key 向量低秩维度（d_eff/head_dim≈3–4%）
- 论文声明→脚本→结果文件的逐条可追溯映射表
- 10 个实验脚本覆盖多模型、多种子 CI、延迟与消融
- 对比基线 TurboQuant，报告余弦相似度/压缩率/延迟等指标

## 适用场景

- 复现论文中的 KV cache 压缩实验与统计检验
- 研究不同模型架构下 KV 缓存的谱结构
- 作为 LLM 推理压缩研究的代码与数据工件来源

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L34: SpectralQuant is a KV cache compression method for large language model inference. It improves on TurboQuant (Zandi
> L78: - Python ≥ 3.10

## 星数曲线

```mermaid
xychart-beta
    title "Dynamis-Labs/spectralquant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 203 --> 205
    line [204, 204]
```

2026-10-18 204 → 2026-10-26 204（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `d3d221fbc603` · [字段定义](../../DATASET.md)*
