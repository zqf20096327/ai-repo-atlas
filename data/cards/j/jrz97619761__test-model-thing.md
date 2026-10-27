# jrz97619761/test-model-thing

⭐ 326 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/jrz97619761/test-model-thing) · 个人维护

**概念验证型小型语言模型：潜空间预测+循环轨迹单元+字节级输出**

个人开发者的实验性语言模型架构（非 LLM），基于 MLX 构建，融合潜空间预测、内部状态与循环轨迹单元（RTUs）、逐字节输入输出、连续数据流与测试时训练。已训练 4.5M 参数模型约 12 小时，输出存在拼写错误但能闭合引号/括号。不提供模型权重，需自行安装 MLX 并运行 main.py 训练。明确声明为未完成作品。支持 Apple Silicon 与 Linux（社区测试），Windows 仅 WSL 可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 潜空间预测与循环轨迹单元（RTUs）内部状态
- 逐字节输入输出与连续数据流
- 测试时训练，训练中断可保存含内部记忆的权重
- 基于 MLX，4.5M 参数概念验证模型

## 适用场景

- 研究非 token 化的逐字节语言模型架构
- 在 Apple Silicon 上实验潜空间预测与测试时训练
- fork 训练与基准代码做扩展实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: This is a small proof-of-concept language model (not an LLM) that aims to incorporate the following (and some smalle
> L14: The model is built with MLX, so it should run fine on all Apple Silicon devices. MLX on Linux has been tested by co

## 星数曲线

```mermaid
xychart-beta
    title "jrz97619761/test-model-thing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 325 --> 327
    line [326, 326]
```

2026-10-18 326 → 2026-10-27 326（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e235547dc2a6` · [字段定义](../../DATASET.md)*
