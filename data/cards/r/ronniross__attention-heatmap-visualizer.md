# ronniross/attention-heatmap-visualizer

⭐ 16 · Jupyter Notebook · 推送 2026-04-19 · [GitHub](https://github.com/ronniross/attention-heatmap-visualizer) · 个人维护

**生成 Transformer 模型逐层逐头注意力热图的 Python 脚本集**

一组 Python 脚本与 Jupyter notebook，用于为基于 Transformer 的语言模型（如 uncased BERT、Qwen 3.5）生成全量 attention-head 热图，展示模型推理时对各 token 的注意力权重分布，覆盖所有层与头。README 说明需在脚本中调整层数/头数等超参数与模型配置以适配目标架构，代码定位为模板。面向研究者用于调试偏差、改进提示工程与设计模型架构。依赖 Python 3.8+ 与 transformers、torch、matplotlib、seaborn。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成覆盖所有层与头的完整注意力热图
- 提供静态热图与动画（animator）两类 notebook
- 需在脚本内调整超参数与模型配置，作为适配其他模型的模板
- 包含 BERT 与 Qwen 3.5 示例

## 适用场景

- 研究模型推理时对哪些 token 分配更高注意力
- 调试模型偏差与改进提示工程
- 对比不同层/头的注意力模式以理解模型行为

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A Python scripts to generate **full attention-head heat-maps** for transformer-based Language Models. They show "whe
> L5: By analyzing these heatmaps across all layers and heads you can gain insights into how the model processes informati

## 星数曲线

```mermaid
xychart-beta
    title "ronniross/attention-heatmap-visualizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2e7a6a8cdf79` · [字段定义](../../DATASET.md)*
