# Mozilla-Data-Collective/datacollective-python

⭐ 30 · Python · MPL-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/Mozilla-Data-Collective/datacollective-python) · [官网](https://mozilla-data-collective.github.io/datacollective-python/) · 组织维护

**访问 Mozilla Data Collective 数据集平台的官方 Python SDK**

Mozilla Data Collective 平台的官方 Python 客户端库，面向数据使用方与上传方：支持断点续传下载数据集或其样本、加载为 pandas DataFrame 或 HuggingFace Dataset 对象（含惰性音频解码）、免 API key 浏览检索公开目录；上传方可通过单次调用创建提交、设置元数据、并发分片可续传上传并送审。下载需先在平台阅读并同意数据集条款，上传需先申请获批。SDK 处于 0.X.X 版本，官方声明存在破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 数据集下载支持中断后自动续传，可先下载样本评估
- 加载为 pandas DataFrame 或 HuggingFace Dataset（可选 hf extra）
- 免 API key 浏览与搜索公开数据集目录
- 程序化提交上传：并发分片、可续传、单次调用完成送审

## 适用场景

- 在 Python 中下载并加载 MDC 数据集用于训练或分析
- 先检索目录再决定获取哪个数据集
- 通过脚本把自有数据集上传到 MDC 平台送审

## 场景标签

 · 领域:数据集/开放数据平台

## 证据(README 行号)

> L9: The official Python SDK for accessing and contributing to the Mozilla Data Collective platform.
> L17: - **Download datasets** to local storage with automatic resume after an interruption, or just a dataset's **sample*
> L18: - **Load datasets into pandas DataFrames or HuggingFace `Dataset` objects**, with optional lazy audio decoding.

## 星数曲线

```mermaid
xychart-beta
    title "Mozilla-Data-Collective/datacollective-python 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 27 --> 31
    line [28, 30, 30]
```

2026-10-18 28 → 2026-10-28 30（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9330a6955882` · [字段定义](../../DATASET.md)*
