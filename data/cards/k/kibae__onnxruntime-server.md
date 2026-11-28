# kibae/onnxruntime-server

⭐ 200 · C++ · MIT · 推送 2026-11-26 · [GitHub](https://github.com/kibae/onnxruntime-server) · 个人维护

**把 ONNX 模型目录发布为 TCP/HTTP 推理 API 的服务器**

面向已导出为 ONNX 格式模型的开发者：将模型文件按目录结构放置即可通过 API 提供推理，无需额外编写代码。服务器提供 TCP 与 HTTP/HTTPS REST 两种后端，每个会话可选择 CPU 或 CUDA 执行，自动分析模型输入/输出类型与形状，内置 Swagger 文档供协作者测试模型。支持 onnxruntime-extensions 自定义算子与会话级 SessionOptions 转发。安装方式包括 CMake 源码编译、Docker 镜像（CPU/CUDA12/CUDA13）与 Arch Linux AUR 包；运行需 ONNX Runtime 与 Boost 等依赖。

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

- 放置 ONNX 文件到目录结构即可提供推理 API，无需写代码
- TCP 与 HTTP/HTTPS REST 双后端，按会话选择 CPU 或 CUDA
- 内置 Swagger API 文档，并分析模型输入/输出类型与形状
- 提供 Docker 镜像（CPU/CUDA）与 AUR 包

## 适用场景

- 把训练导出的 ONNX 模型快速部署为团队可调用的推理 API
- 向协作者提供带 Swagger 文档的模型测试入口
- 在 NVIDIA GPU 环境用 CUDA 后端部署 ONNX 模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L11: - **The ONNX Runtime Server is a server that provides TCP and HTTP/HTTPS REST APIs for ONNX inference.**
> L13:  - If you have exported ML models trained in various environments as ONNX files, you can provide inference APIs
> L107: - **You need to enable one of the following backends: TCP, HTTP, or HTTPS.**

## 星数曲线

```mermaid
xychart-beta
    title "kibae/onnxruntime-server 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-11-10", "2026-11-28"]
    y-axis "stars" 198 --> 201
    line [199, 200, 200]
```

2026-10-26 199 → 2026-11-28 200（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `2f9ce01ec8c7` · [字段定义](../../DATASET.md)*
