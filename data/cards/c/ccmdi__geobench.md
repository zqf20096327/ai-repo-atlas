# ccmdi/geobench

⭐ 66 · Python · MIT · 推送 2026-09-21 · [GitHub](https://github.com/ccmdi/geobench) · [官网](https://geobench.org) · 个人维护

**评估大语言模型图像地理定位能力的 GeoGuessr 基准**

在 GeoGuessr 场景下测试大语言模型能否对图像进行地理定位与空间推理的基准项目。用户通过脚本从 GeoGuessr 地图生成数据集，配置 .env 中的各模型 API key（如 Anthropic），按 models.py 中的类名指定模型运行测试，并可用浏览器脚本可视化各位置的模型猜测结果。项目自称检验模型能否在主训练模态之外泛化。安装方式为 git clone 源码并安装依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 GeoGuessr 地图 ID 生成自定义测试数据集
- 支持按类名指定多种模型（如 Claude 3.5 Haiku）进行地理定位测试
- 浏览器可视化展示各位置的模型猜测

## 适用场景

- 评测大语言模型的图像地理定位能力
- 对比不同模型在空间推理任务上的表现
- 研究模型在主训练模态之外的泛化能力

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: GeoBench is a benchmark for evaluating how well large language models can geolocate images, through the context of G
> L23: python geobench.py --dataset <test name> --model <model name>

## 星数曲线

```mermaid
xychart-beta
    title "ccmdi/geobench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 64 --> 67
    line [65, 66, 66]
```

2026-10-18 65 → 2026-10-26 66（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `c24460f42f48` · [字段定义](../../DATASET.md)*
