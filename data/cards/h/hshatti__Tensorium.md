# hshatti/Tensorium

⭐ 14 · Pascal · MIT · 推送 2026-01-10 · [GitHub](https://github.com/hshatti/Tensorium) · 个人维护

**Pascal 编写的跨平台张量运算库，附神经网络示例**

以 FreePascal/Delphi 编写的通用张量操作库：提供泛型 TTensor<T> 记录类型，堆分配随变量作用域自动管理，无需手工内存管理；方法覆盖创建、resize/reshape、print、plot 等操作，在可能时使用 SIMD 指令，可被其他语言导入。神经网络部分通过 examples/fpc 目录的 make 编译提供 MNIST、CIFAR10、YOLO3 推理、RNN 莎士比亚文本生成示例，并支持 OpenCL 开关做 GPU 计算。面向 Pascal 生态的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 泛型 TTensor<T> 记录类型，栈上生命周期自动管理内存
- 支持在可能时使用 SIMD 指令
- 神经网络示例：MNIST/CIFAR10 训练、YOLO3 推理、RNN 文本生成
- OpenCL 开关（USE_OPENCL=1）支持 GPU 计算

## 适用场景

- 在 FreePascal/Delphi 项目中做张量与线性代数运算
- 用 Pascal 训练 MNIST/CIFAR10 或运行 YOLO3 推理示例
- 需要跨平台且可被其他语言导入的张量后端

## 场景标签

 · 领域:机器学习库/数值计算

## 证据(README 行号)

> L2: A platform agnostic fast tensor manipulation library using SIMD instructions when possible, written in pascal and ca
> L54: ## Neural networks

## 星数曲线

```mermaid
xychart-beta
    title "hshatti/Tensorium 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d59fb239cc29` · [字段定义](../../DATASET.md)*
