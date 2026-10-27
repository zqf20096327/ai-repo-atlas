# socialfoundations/folktexts

⭐ 30 · Jupyter Notebook · MIT · 推送 2026-07-07 · [GitHub](https://github.com/socialfoundations/folktexts) · [官网](https://socialfoundations.github.io/folktexts/) · 组织维护

**基于真实调查数据的 LLM 不确定性/校准/公平性评测工具**

Python 工具箱，将美国社区调查(ACS)等表格数据转化为自然语言问答预测任务，用 LLM 生成风险分数并与真实结果对比，计算不确定性、校准、准确率与公平性等统计指标。预定义 folktables 各任务，数据集托管于 Hugging Face，支持自定义目标特征、提示模板与风险分数提取方式。推理后端含 vLLM(默认，需 CUDA GPU)、HuggingFace transformers 与 litellm 兼容的 Web API；另支持思维链提示、数值风险提示、少样本与二值化阈值拟合。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ACS 调查数据派生的表格预测任务转为自然语言 Q&A 基准
- 从 LLM 输出提取风险分数并计算校准/不确定性/公平性指标
- 三种推理后端：vLLM(默认)/transformers/Web API(litellm)，一行切换
- PromptConfig/FewShotConfig 可组合提示配置与 --variation 变体实验

## 适用场景

- 用 ACS 真实调查数据基准测试我的 LLM 的预测与校准表现
- 比较不同提示方式（多选Q&A/数值风险/思维链）下的风险分数质量
- 研究 LLM 在个体结果预测任务上的群体公平性
- 直接下载预渲染的提示/标签数据集做离线分析

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: Folktexts provides a suite of Q&A datasets for evaluating **uncertainty**, **calibration**, **accuracy** and **fair
> L13: **Use folktexts to benchmark your LLM:**

## 星数曲线

```mermaid
xychart-beta
    title "socialfoundations/folktexts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `67243d549e33` · [字段定义](../../DATASET.md)*
