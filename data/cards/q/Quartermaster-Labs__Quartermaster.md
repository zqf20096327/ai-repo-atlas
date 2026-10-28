# Quartermaster-Labs/Quartermaster

⭐ 33 · Go · MIT · 推送 2026-10-24 · [GitHub](https://github.com/Quartermaster-Labs/Quartermaster) · [官网](https://quartermaster-labs.github.io/Quartermaster/) · 组织维护

**单机本地推理编排平台：按 VRAM 自动配置并热切换多后端模型**

用 Go 编写的单二进制本地推理编排器，自身不运行模型，而是调度 llama-server、stable-diffusion.cpp、whisper.cpp、vLLM、TabbyAPI 等 HTTP 推理服务。核心机制是读取 GGUF 头信息、采样实际空闲 VRAM，按架构逐模型计算上下文长度、GPU offload、MoE 分层与 KV-cache 大小，生成可编辑的启动参数，并按请求热切换模型，对外暴露 OpenAI 与 Anthropic 兼容 API。附带带登录的聊天应用，支持图像生成、语音、联网搜索与 Hugging Face 模型下载。限制：需要用户已有或由其安装推理后端。

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

- 读取 GGUF 头并按实际空闲 VRAM 逐模型计算启动参数
- 在单一 OpenAI/Anthropic 兼容 API 后按请求热切换模型
- 编排 llama-server/vLLM/stable-diffusion.cpp/whisper.cpp 等任意 HTTP 推理后端
- KV-cache 驱逐前快照到磁盘、多端口共享调度器、Prometheus 指标

## 适用场景

- 在一台家用 GPU 机器上统一运行聊天、图像与语音模型
- 让多个本地模型按需加载、自动避让显存
- 给家庭内多台设备提供带登录的私有聊天前端

## 场景标签

`推理引擎` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L21: It is a single Go binary and one YAML file. It does not run models itself: it orchestrates the
> L22: inference servers you already trust (llama-server, stable-diffusion.cpp, whisper.cpp, vLLM, TabbyAPI
> L30: - OpenAI + Anthropic API

## 星数曲线

```mermaid
xychart-beta
    title "Quartermaster-Labs/Quartermaster 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24", "2026-10-28"]
    y-axis "stars" 31 --> 34
    line [33, 32, 33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `27408986e144` · [字段定义](../../DATASET.md)*
