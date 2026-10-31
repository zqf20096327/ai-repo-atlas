# GeneralSubhra/variant-analysis-evo2

⭐ 22 · TypeScript · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/GeneralSubhra/variant-analysis-evo2) · 个人维护

**用 Evo2 基因组大模型预测 DNA 变异致病性的全栈 Web 应用**

应用型 AI 研究原型：接收基因变异或目标基因，通过 Evo2 基因组基础模型做序列分析预测 SNV 致病性，同时检索 NCBI ClinVar 临床分类与 UCSC 基因组参考上下文，以 Next.js 交互式 Web 界面呈现结果。后端为 Python 3.12 + FastAPI，经 Modal 部署到无服务器 GPU 做加速推理。README 明确声明非临床诊断工具，不做任何临床性能声明，并给出防数据泄露、基线对比等评估规范。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Evo2 模型推断预测单核苷酸变异致病性
- 与 ClinVar 临床分类对比并展示模型置信信息
- Modal 无服务器 GPU 部署，支持 GPU 加速推理
- 检索 UCSC Genome Browser API 获取参考基因组上下文

## 适用场景

- 探索 DNA 变异与基因的致病性预测结果
- 将模型预测与 ClinVar 临床证据并排查看
- 作为基因组基础模型应用化研究原型学习与复现

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L14: 2. Run model-based sequence analysis with **Evo2**.
> L30: - 🧬 DNA variant analysis with Evo2
> L35: - ⚡ GPU-accelerated inference

## 星数曲线

```mermaid
xychart-beta
    title "GeneralSubhra/variant-analysis-evo2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `cdaae4b939d3` · [字段定义](../../DATASET.md)*
