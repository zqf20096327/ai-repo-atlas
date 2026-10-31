# pytraveler/LlamaServerLauncherAvalonia

⭐ 80 · C# · MIT · 推送 2026-10-28 · [GitHub](https://github.com/pytraveler/LlamaServerLauncherAvalonia) · 个人维护 · 中文 README

**跨平台桌面应用：启动并管理 llama.cpp llama-server 实例**

基于 Avalonia UI 与 .NET 8 的跨平台桌面应用（Windows/Linux/macOS），用于配置、启动和管理多个 llama-server 实例：以启动配置文件组织参数（上下文、GPU 层数、采样、投机解码等），支持从应用内下载 llama.cpp 构建与 Hugging Face 模型（.gguf，含分片识别与断点续传），从 GGUF 张量表读取数据做 VRAM 占用预估与“能否放下”判定，并提供基准测试、Prompt 运行记录、硬件监控与 MCP 服务器挂载。限制：MCP 与工具调用依赖支持 --mcp-servers-config 的 llama.cpp 构建及 Jinja 模板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 GGUF 张量表逐块读取并预估 VRAM 占用，给出“能否放下”三色判定与可点击建议
- 多实例管理：每实例启停、/health 与 /slots 轮询、推理速率与托盘控制
- Hugging Face 下载器：搜索、分片合并显示、断点续传、Gated/私有仓库 token
- 基准测试与对比：捕获 /metrics 与 tokens/s，保存运行并可导出 Markdown 报告

## 适用场景

- 用图形界面配置并运行多个本地 llama.cpp 服务实例
- 下载 GGUF 模型并事先判断是否放得进当前显存
- 对不同参数组合跑基准测试并对比结果
- 为模型挂载 MCP 工具服务器

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L14: A cross-platform desktop application for launching and managing llama.cpp server instances with an intuitive graphi
> L25: - **Executable Path** — Select the `llama-server` binary, or download llama.cpp directly from the app

## 星数曲线

```mermaid
xychart-beta
    title "pytraveler/LlamaServerLauncherAvalonia 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 78 --> 81
    line [79, 80, 80]
```

2026-10-18 79 → 2026-10-31 80（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0cd002a62d19` · [字段定义](../../DATASET.md)*
