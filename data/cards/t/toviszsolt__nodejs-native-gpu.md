# toviszsolt/nodejs-native-gpu

⭐ 14 · JavaScript · 推送 2026-02-23 · [GitHub](https://github.com/toviszsolt/nodejs-native-gpu) · 个人维护

**在 Node.js 中运行 GPU 计算的原生插件（已无限期暂停）**

个人开发者构建的 Node.js 原生 GPU 计算插件：通过原生插件直接访问 GPU，支持 Windows/Linux/macOS 与 Vulkan、DirectX、Metal、OpenGL、WebGL 后端，提供异步操作。已实现张量创建与运算、线性代数（matmul/SVD/QR 等）、神经网络激活函数、Autograd、Dense 层、SGD/Adam 优化器及完整训练管线，API 先按 TensorFlow.js 兼容设计后转向 PyTorch 兼容。仓库含 proof-of-concept 代码。项目已于 2026 年 2 月宣布无限期暂停开发，仅作概念验证保留。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 原生插件使 Node.js 直接访问 GPU，覆盖 Vulkan/DirectX/Metal/OpenGL/WebGL 后端
- 已实现张量运算、线性代数、激活函数与损失函数等 GPU 算子
- 实现 Autograd、Dense 层、SGD/Adam 优化器与完整训练管线
- proof-of-concept 目录提供概念验证代码

## 适用场景

- 在 Node.js 环境中进行 GPU 张量运算与神经网络训练
- 不依赖 Python 在 JavaScript 中做 GPU 加速计算实验
- 参考其概念验证代码了解 Node.js 原生 GPU 插件实现方式

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L40: I have solved the creation of a native GPU addon that enables computational tasks to run on the GPU in Node.js.
> L44: - Native addon for Node.js that allows direct GPU access
> L46: - GPU backend support (Vulkan, DirectX, Metal, OpenGL, WebGL)
> L121: - Complete neural network training pipeline: learning and inference on GPU

## 星数曲线

```mermaid
xychart-beta
    title "toviszsolt/nodejs-native-gpu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `659a124d2555` · [字段定义](../../DATASET.md)*
