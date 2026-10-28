# onnx/tensorflow-onnx

⭐ 2,558 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-07 · [GitHub](https://github.com/onnx/tensorflow-onnx) · 组织维护

**将 TensorFlow/Keras/tf.js/TFLite 模型转换为 ONNX 的工具**

tf2onnx 通过命令行或 Python API 将 TensorFlow 2.x、Keras、TensorFlow.js 和 TFLite 模型转换为 ONNX 格式。支持 saved model、checkpoint、graphdef 等输入格式，默认生成 opset-15（支持 14-18），可指定 --opset。转换过程包含 protobuf 格式转换、类型映射、子图重写、NHWC/NCHW 转置插入与图优化。提供自定义算子映射扩展机制，要求 Python 3.10-3.12、TensorFlow 2.13+、onnx 1.9+。项目当前在招募新维护者，tensorflow.js 支持为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 saved model/checkpoint/graphdef/tflite/tfjs 五种输入格式
- CLI 与 Python API（from_keras/from_function/from_graph_def/from_tflite）两种使用方式
- 支持 opset 14-18，可通过 _OPS_MAPPING 与图重写扩展自定义算子
- 带预训练模型验证工具，可对比 TensorFlow 与 ONNX runtime 输出及推理耗时

## 适用场景

- 把训练好的 TensorFlow/Keras 模型导出为 ONNX 以在其他推理运行时部署
- 将移动端 TFLite 模型迁移到 ONNX 生态
- 对比转换前后模型在 onnxruntime 上的输出与性能

## 场景标签

 · 领域:深度学习工具链/模型转换

## 证据(README 行号)

> L3: tf2onnx converts TensorFlow (tf-2.x), keras, tensorflow.js and tflite models to ONNX via command
> L244: ## How tf2onnx works

## 星数曲线

```mermaid
xychart-beta
    title "onnx/tensorflow-onnx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 2556 --> 2559
    line [2557, 2558]
```

2026-10-18 2,557 → 2026-10-28 2,558（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ccbc4f156653` · [字段定义](../../DATASET.md)*
