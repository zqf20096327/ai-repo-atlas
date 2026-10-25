# isaacus-dev/mleb

⭐ 39 · Python · MIT · 推送 2026-02-24 · [GitHub](https://github.com/isaacus-dev/mleb) · [官网](https://isaacus.com/mleb) · 组织维护

**法律文本嵌入模型评测基准 MLEB 的评测代码与结果集**

Isaacus 发布的 Massive Legal Embedding Benchmark（MLEB）配套仓库：包含在 MLEB 上评测法律文本嵌入模型的脚本（scripts 目录），以及已评测模型的完整结果（results 目录，mteb 格式）。基准含 10 个数据集，覆盖多种文档类型、司法辖区、法律领域与任务。安装走 git clone 源码 + uv 虚拟环境，API key 通过 .env 文件配置各嵌入模型提供商；可在 MODEL_CONFIGS 中新增模型配置，结果可导出为 JSONL 供基准网站展示。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供在 MLEB（10 个法律数据集）上评测嵌入模型的脚本
- results 目录含已评测模型的完整结果（mteb 格式）
- 可通过添加 MLEBEvaluationModelConfig 实例扩展新模型
- export.py 可打包全部结果为 JSONL 供网站动态展示

## 适用场景

- 评测自家法律文本嵌入模型在 MLEB 上的表现
- 查看各嵌入模型在法律领域基准上的结果
- 扩展自定义模型配置进行对比评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L4: This repository contains the code used to evaluate embedding models on MLEB (available in the `scripts` directory), 
> L36: To evaluate embedding models on MLEB, you can simply run the `scripts/mleb.py` script, like so:

## 星数曲线

```mermaid
xychart-beta
    title "isaacus-dev/mleb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0dfb446dcc00` · [字段定义](../../DATASET.md)*
