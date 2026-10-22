# mgonzs13/llama_ros

⭐ 268 · C++ · MIT · 推送 2026-10-17 · [GitHub](https://github.com/mgonzs13/llama_ros) · [官网](https://mgonzs13.github.io/llama_ros/) · 个人维护

**将 llama.cpp 集成进 ROS 2 的包集合，运行 GGUF 模型**

一组 ROS 2 包，把 llama.cpp 的推理能力接入 ROS 2：支持运行 GGUF 格式的 LLM、VLM、audio-language、embedding 与 reranking 模型，提供 OpenAI 兼容的 chat completions 接口（含工具调用、推理、流式输出）、投机解码（draft 模型与 ngram 自投机）以及 GBNF 语法和实时 LoRA 修改。通过 launch 文件/YAML 配置模型，可从 HuggingFace 下载模型，支持 CUDA 编译与 Docker 镜像。面向在机器人系统中使用本地模型的 ROS 2 开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 运行 GGUF 格式的 LLM/VLM/audio-language/embedding/reranking 模型
- OpenAI 兼容 chat completions 接口，支持工具调用、reasoning 与流式输出
- 投机解码（draft-eagle3/draft-mtp/ngram 等多种方法）
- GBNF 语法与实时 LoRA 修改

## 适用场景

- 在机器人 ROS 2 项目中本地运行 LLM/VLM 生成回答
- 用 ros2 llama 命令行快速测试 GGUF 模型
- 在 ROS 2 节点中生成 embedding 或做 reranking

## 场景标签

 · 领域:机器人/LLM 基础设施

## 证据(README 行号)

> L3: This repository provides a set of ROS 2 packages to integrate llama.cpp into ROS 2. Using the llama_ros packages, yo
> L24: To run llama_ros with CUDA, first, you must install the CUDA Toolkit. Then, you can compile llama_ros with `--cmake
> L67: ros2 llama launch ~/ros2_ws/src/llama_ros/llama_bringup/models/StableLM-Zephyr.yaml

## 星数曲线

```mermaid
xychart-beta
    title "mgonzs13/llama_ros 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 267 --> 269
    line [268, 268]
```

2026-10-18 268 → 2026-10-22 268（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2706230f5682` · [字段定义](../../DATASET.md)*
