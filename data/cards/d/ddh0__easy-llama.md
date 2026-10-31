# ddh0/easy-llama

⭐ 106 · Python · MIT · 推送 2026-04-02 · [GitHub](https://github.com/ddh0/easy-llama) · 个人维护

**封装 llama.cpp C API 的本地 LLM 推理 Python 库**

Python 包，通过 ctypes 接口封装 llama.cpp 的 C/C++ API（libllama），供在本地设备上加载 GGUF 模型做文本补全与对话，支持 GPU 层卸载（n_gpu_layers）与逐 token 评测。给需要直接调用 llama.cpp 但不写 C 代码的开发者使用。需自行编译或下载 libllama 共享库，并通过 LIBLLAMA 环境变量指定路径；README 声明项目长期未维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 llama.cpp 的 libllama C/C++ API，加载 GGUF 模型推理
- 通过 LIBLLAMA 环境变量定位共享库（.so/.dylib/.dll）
- 支持 n_gpu_layers 控制 CPU→GPU 层卸载
- 提供单 token 评测、文本补全、对话等示例

## 适用场景

- 在 Python 脚本中本地运行 GGUF 模型做补全或聊天
- 把模型逐层卸载到 GPU 提升吞吐
- 直接读取模型 logits 做底层实验

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: This repository provides **easy-llama**, a Python package which serves as a wrapper over the C/C++ API (`libllama`) 
> L31: To use easy-llama, you will need Python (any version 3.9 – 3.12[^1]) and a compiled `libllama` shared library file.
> L72: easy-llama needs to know where your compiled `libllama` shared library is located in order to interface with the C/

## 星数曲线

```mermaid
xychart-beta
    title "ddh0/easy-llama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-31 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1fdbad09ab7c` · [字段定义](../../DATASET.md)*
