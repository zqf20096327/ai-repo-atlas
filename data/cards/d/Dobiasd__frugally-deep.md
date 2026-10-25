# Dobiasd/frugally-deep

⭐ 1,128 · C++ · MIT · 推送 2026-05-06 · [GitHub](https://github.com/Dobiasd/frugally-deep) · 个人维护

**C++ 头文件库：在 C++ 中运行 Keras 模型推理**

用 Python/Keras 训练模型后，经 convert_model.py 转换为专有 JSON 格式，即可在 C++ 中以 fdeep::load_model 加载并调用 model.predict 执行前向推理，无需链接 TensorFlow。仅依赖 FunctionalPlus、Eigen、json 三个头文件库，支持序贯模型与函数式 API 计算图、多输入输出、嵌套模型等；不支持 Lambda、Hashing、StringLookup、有状态 RNN 等。仅用单个 CPU 核做每次预测（可并行多预测），不使用 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 头文件库，依赖仅 FunctionalPlus/Eigen/json，无需链接 TensorFlow
- 转换时自动生成测试用例，加载时核验与 Keras 结果一致
- 支持函数式 API 计算图、多输入输出、嵌套模型、自定义层
- 每次预测用单 CPU 核，可并行运行多个预测提升吞吐

## 适用场景

- 在 C++ 应用中部署 Keras 训练的模型做推理
- 边缘/嵌入式场景避免链接庞大的 TensorFlow
- 多线程并行跑多个模型预测提高吞吐

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L16: Would you like to build/train a model using Keras/Python? And would you like to run the prediction (forward pass) o
> L23: * supports inference (`model.predict`) not only for sequential models but also for computational graphs with a more

## 星数曲线

```mermaid
xychart-beta
    title "Dobiasd/frugally-deep 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 1127 --> 1129
    line [1128, 1128]
```

2026-10-18 1,128 → 2026-10-25 1,128（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5b44568f628c` · [字段定义](../../DATASET.md)*
