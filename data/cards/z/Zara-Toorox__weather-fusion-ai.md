# Zara-Toorox/weather-fusion-ai

⭐ 41 · Python · NOASSERTION · 推送 2026-06-21 · [GitHub](https://github.com/Zara-Toorox/weather-fusion-ai) · 个人维护

**Home Assistant 本地多源天气融合预报集成，从自有传感器学习**

Home Assistant 自定义集成，将 Open-Meteo(GFS)、Bright Sky(ICON)、wttr.in(ECMWF)、Pirate Weather 四个天气源作为独立专家，按 6 种云型分别维护学习权重进行融合，再用 5 层修正管线结合本地传感器数据修正，输出 7 天逐小时预报。学习采用 EMA 权重优化与 11 种位置模式检测，全部在本地运行，不调用 LLM、无遥测。部分源代码经 PyArmor 加密保护。通过 HACS 或手动复制 custom_components 安装，需 Home Assistant 2026.3.0+，支持 x86_64/ARM/树莓派 4/5。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个独立天气源按 6 种云型做专家融合
- 5 层修正管线（逐时/云型/组合/季节/模式）
- EMA 权重优化与 11 种本地天气模式检测，全部本地运行
- 无 LLM 调用、无遥测，仅需约 20 MB 磁盘

## 适用场景

- 让家用气象站获得适配本地微气候的 7 天预报
- 多个天气源预报差异大时获得融合结果
- 在 Home Assistant 中运行不联网上传数据的天气学习系统

## 场景标签

 · 领域:智能家居/天气预报

## 证据(README 行号)

> L10: Your location. Your data. Your AI. Weather Fusion AI combines multiple independent weather sources into an intellig
> L43: Four independent weather experts feed into an intelligent blender that produces a robust fused forecast. This raw f
> L192: - Home Assistant 2026.3.0+

## 星数曲线

```mermaid
xychart-beta
    title "Zara-Toorox/weather-fusion-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-29 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0e1ffd6f7c7e` · [字段定义](../../DATASET.md)*
