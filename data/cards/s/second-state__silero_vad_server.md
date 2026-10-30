# second-state/silero_vad_server

⭐ 18 · Rust · GPL-3.0 · 推送 2025-12-06 · [GitHub](https://github.com/second-state/silero_vad_server) · [官网](https://echokit.dev/) · 组织维护

**Rust 编写的 Silero VAD 语音活动检测 API 服务**

以 Rust 实现的语音活动检测（VAD）API 服务器，加载 Silero VAD 模型，为 EchoKit 服务器的 ASR 管道提供 /v1/audio/vad 接口，可与任意 ASR API 搭配使用。安装需先下载 LibTorch 依赖（支持 Linux x86 CPU/CUDA/ROCm 与 Apple Silicon macOS），再从源码 cargo build 编译，通过环境变量 VAD_LISTEN 监听端口运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 HTTP API 形式的 VAD 服务（/v1/audio/vad）
- 以 Rust 实现，依赖 LibTorch 运行 Silero VAD 模型
- 支持 Linux x86（CPU/CUDA/ROCm）与 Apple Silicon macOS

## 适用场景

- 为 EchoKit 的 ASR 配置提供语音活动检测
- 在语音转写管道中过滤静音与噪声片段

## 场景标签

 · 领域:语音处理/服务端

## 证据(README 行号)

> L1: # An API server for AI VAD
> L3: This is the VAD server that is designed to work with the EchoKit server.

## 星数曲线

```mermaid
xychart-beta
    title "second-state/silero_vad_server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8f3030d62d12` · [字段定义](../../DATASET.md)*
