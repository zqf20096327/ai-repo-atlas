# Flame-Code-VLM/Flame-Code-VLM

⭐ 563 · Python · Apache-2.0 · 推送 2026-02-11 · [GitHub](https://github.com/Flame-Code-VLM/Flame-Code-VLM) · 组织维护 · 中文 README

**将 UI 设计图转为 React 代码的视觉-语言模型及训练评测框架**

面向前端代码生成研究者的完整框架：数据合成管线（演化式、瀑布模型式、增量开发式三种方法）、模型训练流程（SigLIP 视觉编码器 + DeepSeek-Coder 经 2 层 MLP 连接，三阶段训练）与评测套件（Flame-React-Eval 基准、pass@k 指标、基于渲染余弦相似度的视觉一致性评估）。数据构建中使用 DeepSeek V2/V3 API。当前针对 React 优化，方法可扩展至 Vue/Angular。已开源数据集与 7B 模型权重，安装采用 git clone + conda 环境 + npm 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种数据合成方法生成图像-代码多模态数据集
- SigLIP + DeepSeek-Coder 三阶段训练流程
- Flame-React-Eval 评测套件与 pass@k 指标
- 支持多图像输入实现迭代式 UI 优化

## 适用场景

- 复现或扩展设计图转 React 代码的模型研究
- 构建前端代码生成的合成训练数据
- 评测图像转代码模型的语法、功能与视觉一致性

## 场景标签

`代码生成` `模型评测` `多模态` · 领域:编码与开发

## 证据(README 行号)

> L17: To overcome these limitations, we introduce a comprehensive framework that includes a data synthesis pipeline, mode
> L19: One of the primary challenges in developing a robust large-scale VLM for front-end development is the lack of high-
> L39: - Evaluation Pipeline for React Code Generation: The repository provides:

## 星数曲线

```mermaid
xychart-beta
    title "Flame-Code-VLM/Flame-Code-VLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 562 --> 564
    line [563, 563]
```

2026-10-18 563 → 2026-10-27 563（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `fa5369ba081a` · [字段定义](../../DATASET.md)*
