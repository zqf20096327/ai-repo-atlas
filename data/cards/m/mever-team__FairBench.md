# mever-team/FairBench

⭐ 23 · Jupyter Notebook · NOASSERTION · 推送 2026-08-28 · [GitHub](https://github.com/mever-team/FairBench) · 个人维护

**Python AI 公平性评测库：300+ 指标计算与报告生成**

MAI-BIAS 生态下的低代码公平性分析工具包的 Python 库组件：为模型预测提供 300 余个公平性指标的标准计算、多维度多属性分析（多种族、性别等），覆盖表格、图像、文本、图数据模态，并支持 LLM 偏差评估（示例用 Ollama 加载模型）。计算可回溯中间量，输出可在终端/浏览器查看的报告与 stamps，附带社会学家提炼的注意事项与建议。兼容 numpy/pandas/torch/tensorflow/jax 等栈，Python 3.9+（详测 3.11-3.14）。面向 ML 工程师、研究者、审计与合规团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 300+ 公平性指标的标准计算与组织化报告
- 多维度多属性、跨模态（表格/图像/文本/图）分析
- 计算可回溯中间量，报告附注意事项与建议
- 兼容 numpy/pandas/torch/tensorflow/jax/transformers/ollama

## 适用场景

- 在 Python 项目中评估模型的多维度公平性
- 生成可追溯的公平性报告供审计与合规使用
- 检测 LLM 输出中的偏差
- 随时间跟踪部署系统各项公平性指标

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L32: FairBench can be imported in Python AI projects to
> L34: fairness metrics. It also produces reports that organize
> L141: model = fb.bench.text.Ollama("llama3.2:latest")

## 星数曲线

```mermaid
xychart-beta
    title "mever-team/FairBench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-26 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `f5db3f0f0f29` · [字段定义](../../DATASET.md)*
