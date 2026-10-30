# yogeshhk/MidcurveNN

⭐ 44 · TeX · MIT · 推送 2026-08-15 · [GitHub](https://github.com/yogeshhk/MidcurveNN) · 个人维护

**用神经网络计算 2D 闭合多边形中曲线的研究项目**

面向 CAD 几何简化的研究项目：输入简单闭合多边形（点集/线段），输出其中曲线（折线，可开放或分叉）。采用三种平行方法：图像编码-解码（7 种变体，含 Simple/Dense/CNN/Denoising AE 与 UNet）、图几何方法（DGL 图卷积编码-解码，已休眠）、LLM 文本方法（Ludwig/Hugging Face 微调 Nemotron-Mini-4B）。README 声明 2026 年 8 月起活跃开发暂停、寻求协作者，Phase III 作为 MS/PhD 研究课题开放；并披露所有准确率数字存在训练/测试泄漏问题。供科研人员与研究生使用，需 conda 环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三种平行方法：图像、图几何、LLM 文本
- Phase I 提供 7 种编码-解码变体（AE/CNN AE/UNet 等）
- Nemotron-Mini-4B 管线（HF SFTTrainer、Unsloth、few-shot）
- viXra/CAD 会议/IEEE 等多项论文与报告记录

## 适用场景

- 研究 2D 形状中曲线（几何降维）的神经网络求解
- 作为 MS/PhD 研究课题接续 Phase III 图几何方向
- 参考编码-解码与 LLM 处理几何表示的实验设计

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: MidcurveNN is a project aimed at solving the challenging problem of finding the midcurve of a 2D closed shape using 
> L111: 	- Phase I: Image to Image transformation learning
> L120: 	- Phase II: Using Large Language Models (LLMs)

## 星数曲线

```mermaid
xychart-beta
    title "yogeshhk/MidcurveNN 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-30 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5fbe1f8ccd1b` · [字段定义](../../DATASET.md)*
