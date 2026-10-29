# perminder-klair/locca

⭐ 32 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/perminder-klair/locca) · [官网](https://locca.klair.co) · 个人维护

**管理本地 GGUF 模型与 llama.cpp 服务器的终端 TUI 工具**

基于 llama.cpp 的终端界面：安装向导检测硬件与 llama-server 环境，按显存/内存推荐模型并显示下载体积与上下文长度；支持启动/停止 llama-server（前台守护、无头模式、空闲卸载释放 VRAM）、独立嵌入服务器、原子可续传的 GGUF 下载（HuggingFace sha256 校验、HF_TOKEN 支持）、llama-bench 基准测试渲染，并可启动 pi 编码代理对接本地服务器。默认参数面向 iGPU 级硬件调优，Linux/macOS 可用，提供 Docker 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 管理 llama-server 生命周期：无头模式、前台守护、--idle-timeout 空闲卸载释放 VRAM
- 按检测硬件推荐模型与自动上下文分层（4k–256k），下载显示体积/RAM/上下文提示
- 原子可续传 GGUF 下载，HuggingFace sha256 校验与 gated repo 支持
- 独立嵌入服务器 sidecar 与 llama-bench 结果渲染

## 适用场景

- 在本机跑本地 GGUF 模型并获得 OpenAI 兼容接口
- 让 pi 编码代理连接自己的本地 llama.cpp 服务器
- 给手机或局域网其他设备指向同一本地推理服务
- 对比不同本地模型的生成与提示词处理速度

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: A TUI around llama.cpp for running,
> L55: locca serve [model] [opts]     # start llama-server — interactive, head-less, -f foreground, or --idle-timeout
> L171: The repo ships a `Dockerfile` and `docker-compose.yml` that run llama.cpp's

## 星数曲线

```mermaid
xychart-beta
    title "perminder-klair/locca 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-29 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cd3ad7e84715` · [字段定义](../../DATASET.md)*
