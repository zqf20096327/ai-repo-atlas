# orthoseg/orthoseg

⭐ 51 · Python · GPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/orthoseg/orthoseg) · [官网](https://orthoseg.readthedocs.io/) · 组织维护

**训练自有神经网络对正射影像做地物分割的 Python 包**

Python 包，用于训练神经网络并对正射影像（卫星、航空、无人机影像、历史地图、山体阴影等地理配准图像）做分割。典型流程为：在 QGIS 中制作训练数据集、训练网络、对大区域运行分割并矢量化结果、再做 dissolve/simplify 等后处理。全程通过配置文件管理，无需编程；依赖开源软件 QGIS 与 TensorFlow。安装与用法见项目文档，README 展示了航空影像树木检测的输出示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持任意地理配准图像（卫星/航空/无人机/地图/山体阴影）
- 训练数据制作→训练→分割+矢量化→后处理的完整流程
- 全部通过配置文件管理，无需编程

## 适用场景

- 对航拍影像做树木等地物检测并矢量化
- 训练自定义分割模型应用于大范围测绘区域
- 基于卫星或无人机影像做地物提取

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L8: A python package that makes it (relatively) easy to segment orthophotos. Any type of
> L16: 2. train a neural network to segment orthophotos

## 星数曲线

```mermaid
xychart-beta
    title "orthoseg/orthoseg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-30 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `117d33ee4f2c` · [字段定义](../../DATASET.md)*
