# jonathanpeppers/inclusive-code-reviews-ml

⭐ 18 · C# · MIT · 推送 2026-09-01 · [GitHub](https://github.com/jonathanpeppers/inclusive-code-reviews-ml) · 个人维护

**分类代码评审评论句子的 ML 模型（ML.NET/ONNX 格式）**

Inclusive Code Comments 浏览器扩展的配套机器学习项目：训练一个二分类模型，将代码评审中的单句评论判定为 OK 或 BAD（如针对个人的攻击性语句）。模型以 ML.NET 的 MLModel.zip 与 ONNX 的 model.onnx 两种格式产出，可在其他项目免费使用；提供 C# 与 TypeScript/JavaScript 调用示例。仓库含标注数据 CSV、用于人工分类数据的 Maui 桌面应用（Windows/Mac 构建可从 CI 产物下载，Mac 包未签名）。README 详细说明输入预处理规则：需按句切分、GitHub 用户名替换为 @github、代码块/URL 替换为占位符等。构建模型需 .NET 9.0 SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 句子级二分类模型，同时产出 ML.NET 与 ONNX 两种格式
- 提供 C# 与 TypeScript/JavaScript（onnxruntime-web）调用示例
- CSV 格式的代码评审评论数据集与 MLTrainer 数据标注桌面应用
- README 规定输入预处理：按句切分、@github/#code/#url 替换规则

## 适用场景

- 在代码评审工具或扩展中检测不恰当的评论句子
- 复用 MLModel.zip 或 model.onnx 做自定义评审文本分类
- 用 MLTrainer 应用人工标注新的评审评论数据

## 场景标签

 · 领域:开发工具/文本分类

## 证据(README 行号)

> L6: The goal of this project is to produce a machine learning model for
> L7: classifying sentences for code reviews.
> L19: * `MLModel.zip` - model in ML.NET format

## 星数曲线

```mermaid
xychart-beta
    title "jonathanpeppers/inclusive-code-reviews-ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `b7c1f4a7fcf3` · [字段定义](../../DATASET.md)*
