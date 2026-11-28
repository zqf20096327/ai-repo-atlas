# mukhanov/mlx-stack

⭐ 3 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/mukhanov/mlx-stack) · 个人维护

**macOS 菜单栏应用：把本地 MLX/llama.cpp 模型服务给编码 agent**

原生 macOS 菜单栏应用，在 Apple Silicon Mac 上通过 MLX 或 llama.cpp 运行本地模型，以 OpenAI 与 Anthropic 兼容端点经 localhost 代理提供给 pi、omp、opencode、Claude Code、dsh 等编码 agent。含模型管理器（Hugging Face 搜索、内存适配评分、后台下载续传）与每秒刷新的监控（解码速率、上下文、CPU/RAM/swap）。加载模型时自动写入 agent 配置并生成时间戳备份，支持回滚；所有服务仅绑定 127.0.0.1。要求 macOS 14+，Python 后端与 uv 内置于应用。

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

- OpenAI 与 Anthropic 双协议本地代理，Anthropic 请求转译为 chat completions（含流式与工具调用）
- 模型管理器：硬件适配评分、RAM 预算预测、后台下载可暂停/续传/取消
- 每秒刷新的 Monitor：解码速率、上下文占用、CPU/RAM/swap
- 自动写入并备份 agent 配置文件，写入失败自动恢复

## 适用场景

- 在 Apple Silicon Mac 上为 Claude Code 等编码 agent 提供本地模型
- 集中管理本地 MLX/GGUF 模型的搜索、下载与加载
- 监控本地推理速度、上下文与内存占用

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Turn an Apple Silicon Mac into a local AI coding server. MLX Stack is a native macOS menu-bar app that runs models t
> L106: Loading a model writes the supported harness configuration and points the agents at the client proxy on `127.0.0.1
> L126: The proxy speaks both APIs:


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `ea1350815603` · [字段定义](../../DATASET.md)*
