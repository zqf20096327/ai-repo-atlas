# uTensor/utensor_cgen

⭐ 53 · Python · Apache-2.0 · 推送 2025-12-13 · [GitHub](https://github.com/uTensor/utensor_cgen) · 组织维护

**为 uTensor 生成 C++ 代码的工具：把训练模型转成嵌入式可编译源码**

uTensor 生态的 Python 命令行工具：读取 TensorFlow pb 文件或 Keras 训练产物，通过 utensor-cli convert 生成面向 uTensor 运行时的 C/C++ 源码与权重文件，供微控制器等边缘设备编译部署。附带子图同构匹配器库，可用于节点融合（conv-relu-pooling）与 dropout 层删除等推理优化，并提供离线张量内存分配规划。支持 setup.py、pip 安装，pipenv 供开发者模式使用。限制：pb 文件方式已标注弃用，推荐改用 TensorFlow 2.x/Keras 流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- utensor-cli 将 pb 模型转换为 C/C++ 源码与权重文件
- uTensorGraphMatcher 子图同构匹配，支持节点融合与 dropout 删除
- tensor_alloc 离线张量内存分配规划
- toml 配置文件可通过 generate-config 生成

## 适用场景

- 把训练好的神经网络模型部署到微控制器上运行
- 对 CNN 模型做节点融合以压缩体积与推理时间
- 为 uTensor 运行时准备可编译的模型源码

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L84:  $ utensor-cli convert <model.pb> \
> L261:  $ utensor-cli convert --output-nodes=pred graph.pb

## 星数曲线

```mermaid
xychart-beta
    title "uTensor/utensor_cgen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-24 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a507b09bcd30` · [字段定义](../../DATASET.md)*
