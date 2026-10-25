# mattn/go-tflite

⭐ 322 · Jupyter Notebook · MIT · 推送 2026-09-21 · [GitHub](https://github.com/mattn/go-tflite) · 个人维护

**TensorFlow Lite 的 Go 语言绑定库，供 Go 加载运行 tflite 模型**

Go binding，封装 TensorFlow Lite C API（libtensorflowlite_c.so），供 Go 程序从文件加载 .tflite 模型并用 Interpreter 执行推理；面向希望在 Go 项目中运行 TensorFlow Lite 模型的开发者。链接仅需 C API 库而非完整 TensorFlow，提供预编译 buildkit（含 XNNPACK delegate 库，覆盖 Linux/macOS/Windows 多平台）、bazel/cmake/Makefile 构建路径及 Edge TPU delegate 支持方式，通过 cgo 环境变量配置头文件与库路径。CI 针对 TensorFlow v2.17.1 测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从文件加载 .tflite 模型并通过 Interpreter 执行推理
- 仅需链接 TensorFlow Lite C API，无需构建完整 TensorFlow
- release 提供多平台预编译 buildkit（linux/darwin/windows，含 XNNPACK）
- 支持 Edge TPU delegate 与 xnnpack_builtin 构建标签

## 适用场景

- 在 Go 服务中加载并运行 TensorFlow Lite 模型做推理
- 在边缘设备上以 Go 部署轻量模型（含 Edge TPU 加速）
- 通过 Jupyter/Binder 在浏览器中试用库并训练示例分类器

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Go binding for TensorFlow Lite
> L17: model := tflite.NewModelFromFile("sin_model.tflite")
> L27: * TensorFlow Lite C API (`libtensorflowlite_c.so`). CI builds and tests

## 星数曲线

```mermaid
xychart-beta
    title "mattn/go-tflite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 321 --> 323
    line [322, 322]
```

2026-10-18 322 → 2026-10-25 322（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `7c1cd0025216` · [字段定义](../../DATASET.md)*
