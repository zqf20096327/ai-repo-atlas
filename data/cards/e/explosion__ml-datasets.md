# explosion/ml-datasets

⭐ 47 · Python · MIT · 推送 2026-03-26 · [GitHub](https://github.com/explosion/ml-datasets) · 组织维护

**供测试与示例脚本使用的机器学习数据集加载器库**

Explosion 维护的 Python 库，为测试和示例脚本提供常用机器学习数据集的加载器，前身为 thinc.extra.datasets。覆盖 IMDB、DBPedia、CMU、Quora、SNLI、Reuters、UD POS 标注、WikiNER 等 NLP 数据集及 MNIST 图像数据集；加载器可直接导入或通过 loaders 注册表按字符串名称获取，支持用装饰器注册自定义加载器。README 附各数据集的实例数、标签分布与下载 URL 等统计信息。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 个 NLP 数据集与 MNIST 的加载器，含任务类型与来源 URL
- 加载器支持直接导入或经 loaders 注册表按名称获取
- 可用装饰器注册自定义数据集加载器
- 提供各数据集的实例数、标签分布等统计详情

## 适用场景

- 为 NLP/ML 实验脚本快速加载标准数据集
- 通过命令行参数按名称指定数据集加载器
- 查阅常用数据集的规模与标签分布信息

## 场景标签

 · 领域:机器学习/数据集工具

## 证据(README 行号)

> L1: # Machine learning dataset loaders for testing and examples
> L3: Loaders for various machine learning datasets for testing and example scripts.

## 星数曲线

```mermaid
xychart-beta
    title "explosion/ml-datasets 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-30 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `00131ad31012` · [字段定义](../../DATASET.md)*
