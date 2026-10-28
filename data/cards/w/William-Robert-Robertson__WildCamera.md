# William-Robert-Robertson/WildCamera

⭐ 25 · HTML · AGPL-3.0 · 推送 2026-08-31 · [GitHub](https://github.com/William-Robert-Robertson/WildCamera) · [官网](https://new-homes-for-old-friends.cairnwater.com/wildcamera/) · 个人维护

**开源野生动物相机硬件项目：面向生态学家的可定制相机系统（规划阶段）**

面向生态学家与动物学家的开源野外相机设计文档，目前处于规划阶段，尚未提供代码或成品。内容覆盖需求分析、关键技术、硬件选型与可选扩展模块：支持多种图像传感器与处理器（含 Linux/libcamera 方案与低功耗 MCU 方案）、PIR/AIR 触发、太阳能供电、Wi-Fi 数据下载，以及 RFID 读卡、热成像、LTE、卫星通信等约 30 种扩展模块。AI 以可选模块形式出现：处理器端 NPU 运行神经网络做图像/声音识别与动物计数，或采用带板载神经网络的 IMX500 传感器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 模块化硬件设计：相机、PIR、处理器、电池、太阳能板可分体部署
- 两类处理器路线：Linux（libcamera/v4l2）高画质与 MCU 低功耗方案
- 约 30 种可选扩展模块（RFID、热成像、LTE、卫星通信、蝙蝠超声检测等）
- AI 为可选模块：NPU 运行 CNN 做图像识别、声音识别与动物计数

## 适用场景

- 生态研究者野外长期自动拍摄记录野生动物
- 为小型哺乳动物、爬行类等商用相机难以可靠捕捉的物种做监测
- 按研究需求自行组合传感器与供电方案的定制化野外观测

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: ## Planning phase
> L160: - **AI on Camera** Camera module with onboard neural network processing - e.g. Sony IMX500 Intelligent Vision Sens
> L161: - **AI on Processor** NPU, TPU, GPU or other AI accelerators on processor to run neural networks e.g. CNNs (Convol

## 星数曲线

```mermaid
xychart-beta
    title "William-Robert-Robertson/WildCamera 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 26
    line [24, 25]
```

2026-10-18 24 → 2026-10-28 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `ae68793b7de3` · [字段定义](../../DATASET.md)*
