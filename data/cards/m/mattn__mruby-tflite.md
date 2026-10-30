# mattn/mruby-tflite

⭐ 15 · C · 推送 2026-09-28 · [GitHub](https://github.com/mattn/mruby-tflite) · 个人维护

**在 mruby 中加载运行 TensorFlow Lite 模型的绑定库**

为 mruby 提供 TensorFlow Lite C API 绑定：可从文件加载 .tflite 模型、创建解释器、分配张量并执行推理。附示例脚本，覆盖 XOR、FizzBuzz、张量布局导出、多线程数基准测试及 MobileNet 图像分类。若系统已安装 TensorFlow Lite C 库则直接使用（默认搜索 /usr/local、/usr、/opt/homebrew 等前缀，可用 TFLITE_PREFIX 指定），否则回退到克隆 TensorFlow 源码并用 bazel 构建，耗时较长。需自行编译集成到 mruby。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 TfLite::Model / Interpreter 等 mruby 接口加载并运行 .tflite 模型
- 若本机已有 TensorFlow Lite C 库则直接复用，可用 TFLITE_PREFIX 指定前缀
- 示例含 MobileNet 图像分类与多线程基准测试
- 无预编译产物，需自行构建集成 mruby

## 适用场景

- 在嵌入式或 mruby 环境中运行已训练的 TFLite 模型
- 测量模型在不同线程数下的推理耗时
- 导出查看模型的张量布局

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: interface to TensorFlow Lite for mruby
> L8: model = TfLite::Model.from_file "xor_model.tflite"

## 星数曲线

```mermaid
xychart-beta
    title "mattn/mruby-tflite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `66ed719b1062` · [字段定义](../../DATASET.md)*
