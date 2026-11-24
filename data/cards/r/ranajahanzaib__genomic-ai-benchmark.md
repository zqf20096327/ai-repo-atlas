# ranajahanzaib/genomic-ai-benchmark

⭐ 3 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/ranajahanzaib/genomic-ai-benchmark) · 个人维护

**基因组基础模型可复现评测与数据泄漏审计工具**

本地运行的研究型评测框架：通过留一物种交叉验证检验生物泛化能力，扫描训练/评估划分间的精确匹配、反向互补与子串包含泄漏，并提供 3-mer 最近质心序列基线校准预期。结果持久化到 SQLite，每次运行生成含 SHA-256 校验和的可复现 manifest。以 Next.js 前端 + FastAPI 后端提供 Web 工作台，全部流程亦可经 CLI 执行。内置数据为合成启动子序列演示数据，Evo 2 适配器本地推理需 Linux + CUDA 及验证权重。

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

- 留一物种交叉验证评测与准确率/宏 F1 等指标计算
- 跨划分泄漏检测（精确匹配/反向互补/子串包含）
- 每次运行生成带 SHA-256 的确定性可复现 manifest
- Web 观测台与 CLI 双入口，结果本地 SQLite 持久化

## 适用场景

- 基准测试前验证数据集划分是否存在序列泄漏
- 用物种级留出评估基因组模型的跨物种泛化
- 导入 FASTA 或 NCBI 登录号建立本地序列数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: **Genomic AI Benchmark** provides a local research observatory and evaluation harness designed to:
> L21: > **Demonstration Notice:** The included local observatory is a research demo initialized with synthetic promoter s


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `3bbd86e662ef` · [字段定义](../../DATASET.md)*
