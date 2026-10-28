# StevePny/DataAssimBench

⭐ 32 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/StevePny/DataAssimBench) · 组织维护

**为数据同化的 AI/ML 方法生成训练集与基准工具的 Python 库**

面向将机器学习应用于数据同化（DA）的研究者：提供 Lorenz63/Lorenz96/SQGTurb 等数值模型数据生成器、ENSOIDX/GCP ERA5 等数据下载器，以及灵活的 Observer 类从生成数据中采样带噪声观测（可指定或随机时空位置、平稳/非平稳）。数据以 Xarray Dataset 输出，参数可通过 kwargs 字典定制。代码源自多篇 Journal of Advances in Modeling Earth Systems 论文，README 要求使用时引用。安装推荐虚拟环境内 pip 可编辑安装，完整安装支持云端数据访问与 qgs 等包接口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 Lorenz63/Lorenz96/SQGTurb 等数值模型数据生成器
- Observer 类支持随机或指定时空位置观测采样
- GCP ERA5 等真实数据下载器（可选变量/时段/范围）
- 数据生成与下载参数均可通过 kwargs 定制

## 适用场景

- 为 DA + ML 研究生成可控的模拟数据与合成观测
- 下载并裁剪 ERA5 等再分析数据用于训练
- 复现论文中的 Lorenz/准地转湍流实验设置

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: This work follows the effort initiated by Rasp et al. in the WeatherBench <https://github.com/pangeo-data/WeatherBen
> L73: l96_obj = dab.data.Lorenz96() # Create data generator object

## 星数曲线

```mermaid
xychart-beta
    title "StevePny/DataAssimBench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e7a4caf60e7e` · [字段定义](../../DATASET.md)*
