# OBA-Research/VAAS

⭐ 27 · Python · MIT · 推送 2026-03-30 · [GitHub](https://github.com/OBA-Research/VAAS) · [官网](https://github.com/OBA-Research/VAAS) · 组织维护

**图像完整性分析库：ViT 注意力+块级一致性做篡改检测与定位**

面向研究人员与工程师的推理优先图像取证库，检测图像篡改与不一致区域并做细粒度定位。双模块架构：Fx 用 Vision Transformer 捕捉全局注意力异常，Px 用 SegFormer 做块级一致性分析，v2 版通过交叉注意力融合全局特征，输出全局保真分 S_F、块级合理度 S_P 与连续混合异常分 S_H 及异常热图。提供 pip/uv 安装，需自行安装 PyTorch 与 torchvision，模型托管于 Hugging Face，附 Colab notebook 与论文（FSIDI / DFRWS EU 2026）。S_H 反映相对异常强度而非二值判定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Fx 全局注意力 + Px 块级一致性双模块，交叉注意力融合
- 输出 S_F/S_P/S_H 三个连续分数与异常定位热图
- v1/v2 各 base/medium/large 三档模型变体托管于 Hugging Face
- 提供可视化解释（热图叠加、注意力图、分数仪表图）

## 适用场景

- 检测图像拼接、身份篡改、文字编辑等完整性违规并定位区域
- 数字取证研究中的图像篡改检测推理与可视化
- 在 Colab notebook 中复现实验或试用模型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L16: VAAS is an inference-first, research-driven dual-module vision library for image integrity analysis. It integrates 
> L31: * **Fx — Global Attention Module**
> L34: * **Px — Patch Consistency Module**

## 星数曲线

```mermaid
xychart-beta
    title "OBA-Research/VAAS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `45529d4f628d` · [字段定义](../../DATASET.md)*
