# InternScience/SpectrumLab

⭐ 38 · Python · 推送 2026-08-08 · [GitHub](https://github.com/InternScience/SpectrumLab) · [官网](https://migo-chem.intern-ai.org.cn/spectrumlab/) · 组织维护

**光谱学深度学习研究的统一评测平台**

面向光谱学深度学习研究者的统一平台：提供 Python API 与 CLI 两种方式运行评测，内置 benchmark 模块（SpectrumBench v1.0，数据托管于 Hugging Face）、模型接口（如 GPT4o）与 evaluator 评测器；支持按级别（如 perception）评测模型。安装采用 git clone 源码方式，配合 conda 与 uv 管理环境，需在 .env 中配置 API key。配套论文为 SpectrumWorld: Artificial Intelligence Foundation for Spectroscopy。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Python API 与 CLI 双入口运行评测
- SpectrumBench v1.0 基准数据（Hugging Face 分发）
- 内置模型接口（GPT4o）与评测器模块
- 配套 ACM 论文可引用

## 适用场景

- 在光谱学基准上评测 LLM 的感知与推理能力
- 用 Python API 将评测集成到研究流程
- 复现论文实验结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L39: from spectrumlab.benchmark import get_benchmark_group
> L47: The CLI provides a simple way to run evaluations:
> L65: @inproceedings{10.1145/3770855.3818936,

## 星数曲线

```mermaid
xychart-beta
    title "InternScience/SpectrumLab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-26 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `02821b785536` · [字段定义](../../DATASET.md)*
