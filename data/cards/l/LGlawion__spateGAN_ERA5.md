# LGlawion/spateGAN_ERA5

⭐ 46 · Python · MIT · 推送 2026-01-23 · [GitHub](https://github.com/LGlawion/spateGAN_ERA5) · [官网](https://www.nature.com/articles/s41612-025-01103-y) · 个人维护

**深度学习框架：将 ERA5 降水降尺度至 2km/10分钟**

基于概率条件生成对抗网络（cGAN）的时空降尺度框架，读取 ERA5 再分析降水数据（需含对流降水与大尺度降水变量，最小范围 672km×672km、最少 16 小时序列），将 24km/1小时分辨率提升至 2km/10分钟，输出 UTM 与经纬度两种投影的降水场。支持自定义区域与时段的配置驱动推理，可通过修改 seed/slide 参数生成概率集合（不确定性量化）。模型在德国雨量计校准雷达数据上训练，在美国、澳大利亚等地验证。提供 conda 与 uv 两种安装方式和评估示例 notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- cGAN 将 ERA5 降水从 24km/1小时降尺度至 2km/10分钟
- 概率集合生成实现不确定性量化
- 配置驱动（config.yaml）的自定义区域/时段推理
- 训练与评估数据集在 Zenodo 公开（DOI 可查）

## 适用场景

- 洪水与水文风险评估需要高分辨率降水场
- 对任意区域的 ERA5 降水做时空降尺度
- 生成多样化降水集合用于不确定性分析

## 场景标签

 · 领域:气候科学/深度学习

## 证据(README 行号)

> L3: **spateGAN-ERA5** is a deep learning framework designed for the spatio-temporal downscaling of ERA5 precipitation da
> L11:  Converts coarse ERA5 precipitation data into 2 km × 10 min fields, essential for flood and hydrological risk asses

## 星数曲线

```mermaid
xychart-beta
    title "LGlawion/spateGAN_ERA5 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-30 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e3dcaa0bad30` · [字段定义](../../DATASET.md)*
