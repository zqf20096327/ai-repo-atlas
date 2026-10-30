# manu12121999/GIMP-Selection-Refiner

⭐ 32 · Python · 推送 2026-02-01 · [GitHub](https://github.com/manu12121999/GIMP-Selection-Refiner) · 个人维护

**GIMP 插件：用 SAM2 神经网络细化粗略选区**

面向 GIMP 3.0 用户（Linux/Windows）的插件：用户先粗略框选目标物体，插件调用 segment-anything2 神经网络将选区细化为贴合物体边缘的精确选区，通过菜单 Select -> Refine Selection using SAM 触发。setup 脚本安装依赖并从 fbaipublicfiles 下载模型权重；提供 tiny/small/base/large 四种模型档位，默认 base，可改脚本与源码常量切换。需本机已安装 Python。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 segment-anything2 的选区细化
- 支持 Linux 与 Windows，setup 脚本下载模型权重
- 可选 tiny/small/base/large 四种模型档位（默认 base）

## 适用场景

- 在 GIMP 中把粗略框选细化为精确物体选区
- 抠图前获得贴合边缘的选区
- 按速度/质量偏好切换 SAM2 模型档位

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L2: GIMP Plugin to refine a selection using the neural network segment-anything2
> L6: ## Made for Gimp 3.0.

## 星数曲线

```mermaid
xychart-beta
    title "manu12121999/GIMP-Selection-Refiner 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 31 --> 34
    line [33, 32, 32]
```

2026-10-18 33 → 2026-10-30 32（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `78c2d9927844` · [字段定义](../../DATASET.md)*
