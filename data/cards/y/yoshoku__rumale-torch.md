# yoshoku/rumale-torch

⭐ 18 · Ruby · BSD-3-Clause · 推送 2026-09-17 · [GitHub](https://github.com/yoshoku/rumale-torch) · 个人维护

**Ruby gem：用 Rumale 接口训练/推理 torch.rb 神经网络**

Rumale 的扩展 gem，让用 torch.rb 定义的神经网络以与 Rumale 相同的接口进行学习与推理，并可结合 Rumale 做交叉验证等流程。运行时依赖 torch.rb，后者要求预先安装 LibTorch（如 macOS 下 brew install libtorch，并需 automake 编译 rice gem）。面向 Ruby 生态的机器学习开发者，示例演示了 pendigits 分类训练与 housing 回归 5 折交叉验证。以 BSD-3-Clause 许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Rumale 同一套接口驱动 torch.rb 定义的网络进行训练与推理
- 支持与 Rumale 的交叉验证等既有流程结合
- 以 Ruby gem 形式分发（gem install rumale-torch）

## 适用场景

- 在 Ruby 项目中用 Rumale 接口训练 PyTorch（LibTorch）后端网络
- 复用 Rumale 的评估/交叉验证工具处理神经网络模型
- 已有 Rumale 工作流中引入神经网络模型

## 场景标签

`模型训练` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L8: Rumale::Torch provides the learning and inference by the neural network defined in torch.rb
> L12: torch.rb is a runtime dependent gem of Rumale::Torch. It requires to install LibTorch:

## 星数曲线

```mermaid
xychart-beta
    title "yoshoku/rumale-torch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `40c9568c1afb` · [字段定义](../../DATASET.md)*
