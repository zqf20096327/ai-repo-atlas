# MIKOTOKAWAII25/local-ai-code-assistant

⭐ 122 · HTML · 推送 2026-10-23 · [GitHub](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant) · 个人维护

**离线多模型桌面编程助手：本地编排多个开源模型辅助编码**

面向开发者的跨平台桌面应用：在一个工作区内并发运行至多五个本地模型会话（经 llama.cpp、ExLlama、MLX 后端推理），支持为不同任务分配不同规模模型、在模型线程间传递与合并上下文、导入 Hugging Face/Ollama/GGUF/GPTQ 模型并按显存自动选择量化方案。全程离线运行，无遥测与账号，支持局域网多人协作会话与 Lua 编写模型交互脚本。安装方式为下载发布页可执行文件，最低 16 GB 内存、6 GB VRAM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 最多 5 个并发模型会话，各线程独立上下文与参数
- 本地后端推理（llama.cpp/ExLlama/MLX），全程离线
- 从 Hugging Face/Ollama/本地 GGUF/GPTQ 导入模型并自动匹配量化
- 索引项目目录（最多 10 万 token）并分发给各模型线程

## 适用场景

- 离线环境中用多个本地模型辅助编写与审查代码
- 为补全、调试、架构设计分别指定不同规模的模型
- 内网团队通过局域网共享模型会话进行协作编程

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L18: - **Chain commands** across models: one suggests code, another reviews it, a third refractors it.
> L26: Spin up to five concurrent model sessions in one workspace. Each thread maintains its own context window, conversat
> L31: ### 3. Privacy-First Offline Mesh 🔒

## 星数曲线

```mermaid
xychart-beta
    title "MIKOTOKAWAII25/local-ai-code-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 121 --> 123
    line [122, 122]
```

2026-10-18 122 → 2026-10-24 122（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `331d29477ef2` · [字段定义](../../DATASET.md)*
